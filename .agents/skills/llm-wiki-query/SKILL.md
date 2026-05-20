# LLM Wiki Query Skill

## Purpose
Answer operator questions using the wiki as the primary source of truth, with reusable syntheses optionally filed back into the wiki.

## Preconditions (must pass before analysis)
1. An operator question is provided.
2. `wiki/index.md` exists and is readable as the routing map for relevant pages.

## Guardrails
- **Primary-source discipline:** Use wiki pages first (`wiki/index.md`, then linked pages) before external assumptions.
- **Cited answers:** Claims in the answer must cite relevant wiki pages via wikilinks.
- **Conditional filing:** Do not file a synthesis page without operator confirmation when framing/reusability is ambiguous.
- **Append-only log when filing:** If a synthesis is filed, append to `wiki/log.md` only; do not edit prior entries.
- **Index freshness when filing:** If a new synthesis page is created, `wiki/index.md` must be updated in the same operation.

## Required Step Order (exact)
1. **Read `wiki/index.md`** to discover relevant pages.
2. **Read relevant pages** across entities, concepts, sources, and syntheses.
3. **Synthesize answer with citations** using wikilinks to pages used.
4. **Present answer to operator.**
5. **If reusable/new synthesis:** file it in `wiki/syntheses/`, then update `wiki/index.md` and append to `wiki/log.md`.

## Operator Interaction Prompts
- Before filing (minimal):
  - "Should I file this answer as a reusable synthesis page in `wiki/syntheses/`?"
  - "If yes, what exact question/title should the synthesis preserve?"

## Path Handling Rules
- Discovery entrypoint: `wiki/index.md`.
- Evidence pages: `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/syntheses/`.
- Optional filing target: `wiki/syntheses/YYYY-MM-DD--<slug>.md`.
- Required bookkeeping on filing: `wiki/index.md`, `wiki/log.md`.

## Done Criteria
- Delivered answer is supported by cited wiki pages.
- If filed: synthesis page exists, is linked in `wiki/index.md`, and is logged in appended `wiki/log.md` entry.
