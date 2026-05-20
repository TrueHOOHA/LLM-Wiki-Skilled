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

## Required Step Order (exact)
1. **Read the raw source** from `raw/sources/` or `raw/assets/`.
   - If text references images/assets, read those after the main text.
2. **Discuss key takeaways with operator** before framing final extraction.
   - Minimal prompt:
     - "I summarized the source. What should I emphasize?"
     - "Any specific connections to existing entities/concepts you want prioritized?"
     - "What should be de-emphasized or deferred?"
3. **Write source summary page** in `wiki/sources/` using filename `YYYY-MM-DD--source-title-slug.md`.
4. **Update/create entity pages** in `wiki/entities/` for concrete things mentioned.
5. **Update/create concept pages** in `wiki/concepts/` for abstract ideas mentioned.
6. **Update `wiki/index.md`** to reflect all new/updated pages.
7. **Append to `wiki/log.md`** with an ingest entry.

## Path Handling Rules
- Input source roots: `raw/sources/`, `raw/assets/`.
- Output summary root: `wiki/sources/`.
- Entity updates: `wiki/entities/`.
- Concept updates: `wiki/concepts/`.
- Required global bookkeeping files: `wiki/index.md`, `wiki/log.md`.

## Done Criteria
- Source page exists in `wiki/sources/` and is complete.
- All entities/concepts mentioned in the source have corresponding created/updated pages.
- `wiki/index.md` reflects these changes.
- `wiki/log.md` contains a newly appended ingest entry.
