#!/usr/bin/env python3
"""Validate wiki/log.md contract.

Checks:
1) Entry headers follow: ## [YYYY-MM-DD] action-type | Brief description
2) Entry blocks include required bullets:
   - **Action**
   - **Pages touched**
   - **Notes**
   - **Open questions**
3) Dates are valid ISO dates and non-decreasing.
4) Optional append-only check against a git baseline (--baseline).
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

HEADER_RE = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\] ([a-z][a-z-]*) \| (.+)$")
REQUIRED_BULLETS = ["Action", "Pages touched", "Notes", "Open questions"]


@dataclass
class Entry:
    header_line_no: int
    date: dt.date
    action_type: str
    description: str
    block_lines: list[str]


def parse_entries(lines: list[str]) -> tuple[list[Entry], list[str]]:
    errors: list[str] = []
    entries: list[Entry] = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")
        m = HEADER_RE.match(line)
        if not m:
            i += 1
            continue

        date_s, action_type, description = m.groups()
        try:
            date_v = dt.date.fromisoformat(date_s)
        except ValueError:
            errors.append(f"Line {i+1}: invalid ISO date '{date_s}'.")
            i += 1
            continue

        j = i + 1
        block: list[str] = []
        while j < len(lines) and not lines[j].startswith("## "):
            block.append(lines[j].rstrip("\n"))
            j += 1

        entries.append(
            Entry(
                header_line_no=i + 1,
                date=date_v,
                action_type=action_type,
                description=description.strip(),
                block_lines=block,
            )
        )
        i = j

    if not entries:
        errors.append("No log entries found with the required header format.")

    return entries, errors


def validate_entries(entries: list[Entry]) -> list[str]:
    errors: list[str] = []
    prev_date: dt.date | None = None

    for idx, entry in enumerate(entries, start=1):
        if not entry.description:
            errors.append(
                f"Entry #{idx} (line {entry.header_line_no}): description after '|' must not be empty."
            )

        if prev_date and entry.date < prev_date:
            errors.append(
                f"Entry #{idx} (line {entry.header_line_no}): date {entry.date.isoformat()} is earlier than previous entry date {prev_date.isoformat()}."
            )
        prev_date = entry.date

        for label in REQUIRED_BULLETS:
            expected = f"- **{label}**:"
            if not any(l.startswith(expected) for l in entry.block_lines):
                errors.append(
                    f"Entry #{idx} (line {entry.header_line_no}): missing required bullet '{expected}'."
                )

    return errors


def check_append_only(log_path: Path, baseline: str) -> list[str]:
    """Ensure current log equals baseline log plus appended suffix only."""
    errors: list[str] = []

    try:
        baseline_content = subprocess.check_output(
            ["git", "show", f"{baseline}:{log_path.as_posix()}"],
            text=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as exc:
        errors.append(
            "Append-only check failed to read baseline via git show "
            f"({baseline}:{log_path.as_posix()}):\n{exc.output.strip()}"
        )
        return errors

    current_content = log_path.read_text(encoding="utf-8")
    if not current_content.startswith(baseline_content):
        errors.append(
            "Append-only check failed: current wiki/log.md is not a strict append of "
            f"{baseline}:{log_path.as_posix()}."
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate wiki/log.md contract.")
    parser.add_argument(
        "--log",
        default="wiki/log.md",
        help="Path to log file (default: wiki/log.md)",
    )
    parser.add_argument(
        "--baseline",
        help=(
            "Optional git ref for append-only verification. Example: "
            "--baseline origin/main"
        ),
    )
    args = parser.parse_args()

    log_path = Path(args.log)
    if not log_path.exists():
        print(f"ERROR: log file does not exist: {log_path}")
        return 1

    lines = log_path.read_text(encoding="utf-8").splitlines(keepends=True)
    entries, errors = parse_entries(lines)
    errors.extend(validate_entries(entries))

    if args.baseline:
        errors.extend(check_append_only(log_path, args.baseline))

    if errors:
        print("Log contract validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(
        "Log contract validation passed "
        f"({len(entries)} entries, non-decreasing dates, required bullets present)."
    )
    if args.baseline:
        print(f"Append-only check passed against baseline: {args.baseline}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
