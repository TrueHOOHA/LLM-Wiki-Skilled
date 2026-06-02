#!/usr/bin/env python3
"""Restart-safe queue helper for Tolaria Alpha/Beta link backfill.

This script deliberately does not fetch web pages or mutate wiki notes. It only
manages `backlog/ingestion-ledger.jsonl` so a future Hermes cron/agent run can
claim exactly one URL at a time, process it, and mark the result.

Usage examples:
  python scripts/tolaria_backfill_queue.py next --dry-run
  python scripts/tolaria_backfill_queue.py claim --dry-run
  python scripts/tolaria_backfill_queue.py claim
  python scripts/tolaria_backfill_queue.py complete --url <url> --status queued --task-id t_...
  python scripts/tolaria_backfill_queue.py fail --url <url> --reason "fetch failed"
  python scripts/tolaria_backfill_queue.py stale --minutes 60
  python scripts/tolaria_backfill_queue.py stats
"""

from __future__ import annotations

import argparse
import contextlib
import fcntl
import json
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "backlog"
LEDGER = BACKLOG / "ingestion-ledger.jsonl"
LOCK = BACKLOG / ".ingestion-ledger.lock"
CURSOR = BACKLOG / "backfill-cursor.json"
FAILURES = BACKLOG / "failures.jsonl"
ELIGIBLE_STATUSES = {"new"}
RETRYABLE_STATUSES = {"failed"}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@contextlib.contextmanager
def ledger_lock():
    BACKLOG.mkdir(exist_ok=True)
    with LOCK.open("w") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        yield


def load_rows() -> list[dict[str, Any]]:
    if not LEDGER.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(LEDGER.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSON in {LEDGER}:{line_no}: {exc}") from exc
    return rows


def save_rows(rows: list[dict[str, Any]]) -> None:
    tmp = LEDGER.with_suffix(".jsonl.tmp")
    tmp.write_text("\n".join(json.dumps(r, sort_keys=True) for r in rows) + ("\n" if rows else ""))
    tmp.replace(LEDGER)


def load_cursor() -> dict[str, Any]:
    if CURSOR.exists():
        return json.loads(CURSOR.read_text())
    return {"version": 1, "created_at": now_iso(), "cursor": None, "last_processed_url": None}


def save_cursor(cursor: dict[str, Any]) -> None:
    cursor["updated_at"] = now_iso()
    CURSOR.write_text(json.dumps(cursor, indent=2, sort_keys=True) + "\n")


def pick_next(rows: list[dict[str, Any]]) -> int | None:
    # Oldest first, but skip already queued/processing/archive-only/malformed rows.
    eligible = []
    for idx, row in enumerate(rows):
        status = row.get("processing_status")
        if status in ELIGIBLE_STATUSES:
            eligible.append((row.get("first_seen") or "", row.get("mentions", 1), idx))
    if not eligible:
        return None
    # High mention count can indicate noisy links, so keep chronological order first.
    eligible.sort(key=lambda x: (x[0], -int(x[1] or 1), rows[x[2]].get("url", "")))
    return eligible[0][2]


def cmd_stats(args: argparse.Namespace) -> int:
    rows = load_rows()
    counts = Counter(r.get("processing_status", "unknown") for r in rows)
    print(json.dumps({"ledger_rows": len(rows), "status_counts": dict(sorted(counts.items()))}, indent=2))
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    with ledger_lock():
        rows = load_rows()
        idx = pick_next(rows)
        if idx is None:
            print(json.dumps({"ok": True, "item": None, "message": "no eligible new ledger rows"}))
            return 0
        item = rows[idx]
        print(json.dumps({"ok": True, "item": item}, indent=2, sort_keys=True))
    return 0


def cmd_claim(args: argparse.Namespace) -> int:
    with ledger_lock():
        rows = load_rows()
        idx = pick_next(rows)
        if idx is None:
            print(json.dumps({"ok": True, "claimed": None, "message": "no eligible new ledger rows"}))
            return 0
        if args.dry_run:
            print(json.dumps({"ok": True, "dry_run": True, "would_claim": rows[idx]}, indent=2, sort_keys=True))
            return 0
        rows[idx]["processing_status"] = "processing"
        rows[idx]["processing_started_at"] = now_iso()
        rows[idx]["processing_claim"] = f"{int(time.time())}:{args.claimant}"
        rows[idx]["updated_at"] = now_iso()
        save_rows(rows)
        cursor = load_cursor()
        cursor["cursor"] = rows[idx]["url"]
        cursor["last_claimed_url"] = rows[idx]["url"]
        save_cursor(cursor)
        print(json.dumps({"ok": True, "claimed": rows[idx]}, indent=2, sort_keys=True))
    return 0


def find_row(rows: list[dict[str, Any]], url: str) -> int:
    for idx, row in enumerate(rows):
        if row.get("url") == url:
            return idx
    raise SystemExit(f"URL not found in ledger: {url}")


def cmd_complete(args: argparse.Namespace) -> int:
    allowed = {"queued", "promoted", "archived", "archive_only", "read_later", "weak_hypothesis", "duplicate", "follow_up_required"}
    if args.status not in allowed:
        raise SystemExit(f"Invalid complete status {args.status!r}; allowed: {sorted(allowed)}")
    with ledger_lock():
        rows = load_rows()
        idx = find_row(rows, args.url)
        row = rows[idx]
        row["processing_status"] = args.status
        row["updated_at"] = now_iso()
        row.pop("processing_claim", None)
        row.pop("processing_started_at", None)
        if args.task_id:
            row.setdefault("kanban_task_ids", [])
            if args.task_id not in row["kanban_task_ids"]:
                row["kanban_task_ids"].append(args.task_id)
        if args.path:
            row.setdefault("tolaria_paths", {})
            row["tolaria_paths"][args.path_kind] = args.path
        if args.note:
            row.setdefault("notes", []).append({"at": now_iso(), "note": args.note})
        save_rows(rows)
        cursor = load_cursor()
        cursor["last_processed_url"] = args.url
        save_cursor(cursor)
        print(json.dumps({"ok": True, "row": row}, indent=2, sort_keys=True))
    return 0


def cmd_fail(args: argparse.Namespace) -> int:
    with ledger_lock():
        rows = load_rows()
        idx = find_row(rows, args.url)
        row = rows[idx]
        row["processing_status"] = "failed"
        row["failure_reason"] = args.reason
        row["updated_at"] = now_iso()
        row.pop("processing_claim", None)
        row.pop("processing_started_at", None)
        save_rows(rows)
        entry = {"at": now_iso(), "url": args.url, "reason": args.reason}
        with FAILURES.open("a") as fh:
            fh.write(json.dumps(entry, sort_keys=True) + "\n")
        print(json.dumps({"ok": True, "row": row}, indent=2, sort_keys=True))
    return 0


def cmd_stale(args: argparse.Namespace) -> int:
    cutoff = time.time() - args.minutes * 60
    changed = []
    with ledger_lock():
        rows = load_rows()
        for row in rows:
            if row.get("processing_status") != "processing":
                continue
            started = row.get("processing_started_at")
            try:
                ts = datetime.fromisoformat(started).timestamp() if started else 0
            except Exception:
                ts = 0
            if ts < cutoff:
                row["processing_status"] = "new"
                row.setdefault("notes", []).append({"at": now_iso(), "note": f"stale processing claim reset after {args.minutes} minutes"})
                row.pop("processing_claim", None)
                row.pop("processing_started_at", None)
                row["updated_at"] = now_iso()
                changed.append(row.get("url"))
        if changed:
            save_rows(rows)
    print(json.dumps({"ok": True, "reset": changed}, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("stats")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("next")
    p.add_argument("--dry-run", action="store_true", help="Compatibility flag; next never mutates")
    p.set_defaults(func=cmd_next)

    p = sub.add_parser("claim")
    p.add_argument("--claimant", default="manual", help="Name recorded in processing_claim")
    p.add_argument("--dry-run", action="store_true", help="Show which row would be claimed without mutating ledger/cursor")
    p.set_defaults(func=cmd_claim)

    p = sub.add_parser("complete")
    p.add_argument("--url", required=True)
    p.add_argument("--status", required=True)
    p.add_argument("--task-id")
    p.add_argument("--path")
    p.add_argument("--path-kind", default="source_note")
    p.add_argument("--note")
    p.set_defaults(func=cmd_complete)

    p = sub.add_parser("fail")
    p.add_argument("--url", required=True)
    p.add_argument("--reason", required=True)
    p.set_defaults(func=cmd_fail)

    p = sub.add_parser("stale")
    p.add_argument("--minutes", type=int, default=60)
    p.set_defaults(func=cmd_stale)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
