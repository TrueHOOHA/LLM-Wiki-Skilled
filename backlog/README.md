# Tolaria Backfill Backlog

This directory tracks the Alpha/Beta historical link re-processing workflow.

- `ingestion-ledger.jsonl` — one canonical URL/source per line, seeded by the Alpha ingress audit.
- `backfill-cursor.json` — restart-safe cursor for the future 10-minute trickle job.
- `failures.jsonl` — durable fetch/parse/archive failures with reasons.
- `initial-state-report.md` — first inspection snapshot.

Progress plan: `/home/admin/.hermes/plans/tolaria-alpha-beta-link-backfill-plan.md`.
