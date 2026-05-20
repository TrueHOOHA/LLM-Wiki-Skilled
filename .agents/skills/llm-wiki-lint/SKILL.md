# LLM Wiki Lint Skill

## Purpose
Run a structural and logical health check of the wiki, then coordinate and apply agreed fixes.

## Preconditions (must pass before lint)
1. The wiki tree is accessible (`wiki/` with index and pages).
2. Operator requested linting or accepted a lint pass.

## Guardrails
- **Scope control:** Lint checks apply across wiki pages; do not modify `raw/`.
- **Discussion before fixes:** Do not apply non-trivial fixes until operator reviews report and confirms priorities.
- **Append-only logging:** After applying agreed fixes, append one lint entry to `wiki/log.md`.

## Required Checks
1. Contradictions
2. Stale Claims
3. Orphan Pages
4. Missing Pages
5. Broken Links
6. Data Gaps

## Required Step Order (exact)
1. **Scan all pages** for the required checks.
2. **Produce lint report** (inline or temporary synthesis page).
3. **Discuss fixes with operator.**
4. **Apply agreed fixes.**
5. **Append entry to `wiki/log.md`.**

## Lint Report Format (mandatory)
For each issue, include:
- `id`: stable issue id (e.g., `ORPHAN-003`)
- `severity`: `critical | high | medium | low`
- `check_type`: one of required checks
- `location`: file path(s)
- `evidence`: short excerpt/description
- `impact`: why it matters
- `proposed_fix`: explicit patch plan
- `operator_decision`: `pending | accepted | rejected`

### Fix Proposal Structure (explicit)
- **Target files:** exact paths
- **Change type:** add | update | remove link | merge | split
- **Patch intent:** 1-2 sentences
- **Risk level:** low/medium/high
- **Validation:** how to verify issue resolved

## Operator Interaction Prompts
- After report (minimal):
  - "Which issue IDs should I fix first?"
  - "Do you approve the proposed fixes for accepted IDs as written, or should I revise scope?"

## Path Handling Rules
- Scan scope: `wiki/index.md`, `wiki/log.md`, `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/syntheses/`.
- Optional report file: `wiki/syntheses/YYYY-MM-DD--lint-report-<slug>.md`.
- Required post-fix logging: append to `wiki/log.md`.

## Done Criteria
- Lint report lists all found issues with severity.
- Agreed fixes are applied.
- `wiki/log.md` has a newly appended lint entry.
