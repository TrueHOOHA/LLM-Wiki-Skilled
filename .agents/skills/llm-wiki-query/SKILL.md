---
name: llm-wiki-query
description: "Answer operator questions using the LLM Wiki as the primary source of truth, and optionally file reusable syntheses back into the wiki. Use whenever the operator asks a question about wiki content, queries the knowledge base, requests a synthesis across sources, or wants an answer based on what has been ingested."
---

# LLM Wiki Query Skill

## Purpose
Answer operator questions using the wiki as the primary source of truth, with reusable syntheses optionally filed back into the wiki. The wiki is an OKF v0.1 bundle (see `SPEC.md`); `wiki/` is the bundle root.

## Preconditions (must pass before analysis)
1. An operator question is provided.
2. `wiki/index.md` exists and is readable as the routing map for relevant pages.

## Guardrails
- **Primary-source discipline:** Use wiki pages first (`wiki/index.md`, then linked pages) before external assumptions.
- **Cited answers:** Claims in the answer must cite relevant wiki pages via Obsidian wikilinks (`[[note]]` / `[[note|Display]]`); external sources use standard markdown links.
- **Conditional filing:** Do not file a synthesis page without operator confirmation when framing/reusability is ambiguous.
- **Append-only log when filing:** If a synthesis is filed, append a new date-grouped entry to `wiki/log.md` only; do not edit prior entries (OKF §7).
- **Index freshness when filing:** If a new synthesis page is created, `wiki/index.md` must be rebuilt in the same operation.
- **Single source of truth:** The schema is defined in `AGENTS.md`. This skill enforces it; it never re-defines page types, frontmatter, or sections inline.

## Required Step Order (exact)
1. **Read `wiki/index.md`** to discover relevant pages.
2. **Read relevant pages** across entities, concepts, sources, and syntheses.
3. **Synthesize answer with citations** using Obsidian wikilinks to pages used.
4. **Present answer to operator.**
5. **If reusable/new synthesis:** file it in `wiki/syntheses/` following `AGENTS.md` § Synthesis Pages (frontmatter with non-empty `type` plus `title`/`description`/`question`/`tags`/`timestamp`; H1 sections including `# Citations` with numbered wikilinks for source pages and markdown links for external URLs), then **rebuild `wiki/index.md`** per the Canonical rebuild procedure in `AGENTS.md` § Update Rules for Special Files, and **append to `wiki/log.md`** a single new `## YYYY-MM-DD` entry (OKF §7) with bullets `* **Query**: <question> — <summary>.`, `* **Pages touched**: ...`, `* **Notes**: ...`, `* **Open questions**: ...`.

## Operator Interaction Prompts
- Before filing (minimal):
  - "Should I file this answer as a reusable synthesis page in `wiki/syntheses/`?"
  - "If yes, what exact question/title should the synthesis preserve?"

## Done Gate (verify before reporting done)
- [ ] Delivered answer cites wiki pages via Obsidian wikilinks for every claim.
- [ ] **If filed:** the synthesis page complies with its type contract in `AGENTS.md` § Synthesis Pages (non-empty `type` plus `title`/`description`/`question`/`tags`/`timestamp`; all H1 sections present), uses Obsidian wikilinks for internal links (markdown links only for external URLs), has no legacy `updated`/`source_path` fields, `wiki/index.md` is rebuilt per the Canonical rebuild procedure and lists the new page, and `wiki/log.md` has a newly appended `## YYYY-MM-DD` query entry.

## Path Handling Rules
- Discovery entrypoint: `wiki/index.md`.
- Evidence pages: `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/syntheses/`.
- Optional filing target: `wiki/syntheses/YYYY-MM-DD--<slug>.md`.
- Required bookkeeping on filing: `wiki/index.md`, `wiki/log.md`.
