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
- **Single source of truth:** The schema is defined in `AGENTS.md`. This skill enforces it; it never re-defines page types, frontmatter, or sections inline.

## Required Step Order (exact)
1. **Read `wiki/index.md`** to discover relevant pages.
2. **Read relevant pages** across entities, concepts, sources, and syntheses.
3. **Synthesize answer with citations** using wikilinks to pages used.
4. **Present answer to operator.**
5. **If reusable/new synthesis:** file it in `wiki/syntheses/` following `AGENTS.md` § Synthesis Pages (frontmatter + sections), then **rebuild `wiki/index.md`** per the Canonical rebuild procedure in `AGENTS.md` § Update Rules for Special Files, and **append to `wiki/log.md`** a single new entry (header: `## [YYYY-MM-DD] query | <question>`, bullets: `Action`, `Pages touched`, `Notes`, `Open questions`).

## Operator Interaction Prompts
- Before filing (minimal):
  - "Should I file this answer as a reusable synthesis page in `wiki/syntheses/`?"
  - "If yes, what exact question/title should the synthesis preserve?"

## Done Gate (verify before reporting done)
- [ ] Delivered answer cites wiki pages via wikilinks for every claim.
- [ ] **If filed:** the synthesis page complies with its type contract in `AGENTS.md` § Synthesis Pages (all required frontmatter keys + sections), every `[[wikilink]]` in the filed page resolves to a page on disk, `wiki/index.md` is rebuilt per the Canonical rebuild procedure and lists the new page, and `wiki/log.md` has a newly appended query entry.

## Path Handling Rules
- Discovery entrypoint: `wiki/index.md`.
- Evidence pages: `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/syntheses/`.
- Optional filing target: `wiki/syntheses/YYYY-MM-DD--<slug>.md`.
- Required bookkeeping on filing: `wiki/index.md`, `wiki/log.md`.
