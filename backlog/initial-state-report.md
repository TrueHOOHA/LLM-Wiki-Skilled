# Initial Tolaria Backfill State Report

Generated: 2026-05-29T00:20:07.654825+00:00

## Structure counts

- raw/sources: 2
- wiki/sources: 1
- wiki/entities: 2
- wiki/concepts: 1
- wiki/syntheses: 2
- wiki/templates: 4

## Backlog scaffolding

Created:
- /home/admin/.hermes/tolaria/backlog/ingestion-ledger.jsonl
- /home/admin/.hermes/tolaria/backlog/failures.jsonl
- /home/admin/.hermes/tolaria/backlog/backfill-cursor.json
- /home/admin/.hermes/tolaria/backlog/README.md

Already existed:

## Profile/model snapshot

- default: openai-codex / gpt-5.5 / dispatch_in_gateway=false
- agent-alpha: openai-codex / gpt-5.4-mini / dispatch_in_gateway=true
- agent-beta: openai-codex / gpt-5.3-codex / dispatch_in_gateway=false

## Git status at start

```text
M wiki/index.md
 M wiki/log.md
?? backlog/
?? legacy/
?? raw/sources/2026-05-28-ibuzovskyi-2059860662658949530.md
?? verification/lint-schema-report.json
?? wiki/concepts/
?? wiki/entities/
?? wiki/sources/
?? wiki/syntheses/
```

## Immediate observations

- LLM-Wiki core structure exists.
- `backlog/` was missing and is now initialized.
- Tolaria already had dirty/untracked changes before this scaffolding; do not treat these as created solely by this run.
- Alpha is the only profile with `kanban.dispatch_in_gateway=true`, matching the one-dispatcher policy.
- Alpha/Beta are not yet on gpt-5.5; profile model change still needs explicit smoke-test/change step.
