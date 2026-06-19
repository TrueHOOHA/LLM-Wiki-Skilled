# LLM Wiki Ingest Skill

## Purpose
Integrate a newly provided raw source into the wiki while preserving raw-source immutability and maintaining index/log bookkeeping.

## Preconditions (must pass before edits)
1. The operator explicitly requested ingestion.
2. The source file exists at `raw/sources/<file>` or `raw/assets/<file>`.
3. The workflow will not modify anything under `raw/`.

## Guardrails
- **Immutable raw files:** Never edit, rename, move, or delete any file under `raw/`.
- **Wiki ownership:** Create/update pages only under `wiki/` (unless operator explicitly overrides).
- **Append-only log:** Only append a new section to `wiki/log.md`; never rewrite or reorder prior entries.
- **Index freshness:** Any wiki page change in this workflow requires corresponding `wiki/index.md` updates before completion.
- **Single source of truth:** The schema is defined in `AGENTS.md`. This skill enforces it; it never re-defines page types, frontmatter, or sections inline.

## Required Step Order (exact)
1. **Read the raw source** from `raw/sources/` or `raw/assets/`.
   - If text references images/assets, read those after the main text.
2. **Discuss key takeaways with operator** before framing final extraction.
   - Minimal prompt:
     - "I summarized the source. What should I emphasize?"
     - "Any specific connections to existing entities/concepts you want prioritized?"
     - "What should be de-emphasized or deferred?"
3. **Write source summary page** in `wiki/sources/` using filename `YYYY-MM-DD--source-title-slug.md`, following `AGENTS.md` § Source Pages (frontmatter + sections).
4. **Update/create entity pages** in `wiki/entities/` for concrete things mentioned, following `AGENTS.md` § Entity Pages. When updating an existing entity page from this source, increment its `source_count` by 1 and bump `updated` to today; when creating a new page, set `source_count: 1`.
5. **Update/create concept pages** in `wiki/concepts/` for abstract ideas mentioned, following `AGENTS.md` § Concept Pages, applying the same `source_count` increment and `updated` bump rule as step 4.
6. **Rebuild `wiki/index.md`** following the Canonical rebuild procedure in `AGENTS.md` § Update Rules for Special Files (`wiki/index.md`): scan every `.md` under `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, and `wiki/syntheses/` (never `wiki/templates/`), read each page's frontmatter, and rewrite the four grouped tables (Entities, Concepts, Sources, Syntheses) with summary + source_count + updated date, plus the `## Statistics` block. The index must list exactly the pages that exist on disk.
7. **Append to `wiki/log.md`** a single new ingest entry — never edit or reorder prior entries.
   - Header: `## [YYYY-MM-DD] ingest | <Source Title>`
   - Bullets: `Action`, `Pages touched`, `Notes`, `Open questions` (see `AGENTS.md` § `wiki/log.md`).

## Done Gate (verify before reporting done)
- [ ] Source page exists in `wiki/sources/` and **complies with its type contract** in `AGENTS.md` § Source Pages (all required frontmatter keys + all required sections present).
- [ ] Every entity/concept page created or updated complies with its type contract in `AGENTS.md` (Entity Pages / Concept Pages).
- [ ] Every `[[wikilink]]` anywhere in created/updated pages resolves to a page that exists on disk.
- [ ] `wiki/index.md` rebuilt per the Canonical rebuild procedure and lists every page touched in this ingest (no phantom rows, no missing rows).
- [ ] `wiki/log.md` has a newly appended ingest entry matching the header/bullet format above.

## Path Handling Rules
- Input source roots: `raw/sources/`, `raw/assets/`.
- Output summary root: `wiki/sources/`.
- Entity updates: `wiki/entities/`.
- Concept updates: `wiki/concepts/`.
- Required global bookkeeping files: `wiki/index.md`, `wiki/log.md`.
