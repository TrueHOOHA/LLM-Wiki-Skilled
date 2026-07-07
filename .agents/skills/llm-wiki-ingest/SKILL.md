---
name: llm-wiki-ingest
description: "Ingest a newly provided raw source into the LLM Wiki OKF bundle. Use whenever the operator asks to add a source to the wiki, process a file under raw/sources or raw/assets, summarize and file an article/paper/transcript, or mentions ingestion, importing sources, or updating the wiki from a document."
---

# LLM Wiki Ingest Skill

## Purpose
Integrate a newly provided raw source into the wiki while preserving raw-source immutability and maintaining index/log bookkeeping. The wiki is an OKF v0.1 bundle (see `SPEC.md`); `wiki/` is the bundle root.

## Preconditions (must pass before edits)
1. The operator explicitly requested ingestion.
2. The source file exists at `raw/sources/<file>` or `raw/assets/<file>`.
3. The workflow will not modify anything under `raw/`.

## Guardrails
- **Immutable raw files:** Never edit, rename, move, or delete any file under `raw/`.
- **Wiki ownership:** Create/update pages only under `wiki/` (unless operator explicitly overrides).
- **Append-only log:** Only append a new date-grouped entry to `wiki/log.md`; never rewrite or reorder prior entries.
- **Index freshness:** Any wiki page change in this workflow requires `wiki/index.md` to be rebuilt before completion.
- **OKF conformance:** Created/updated pages must satisfy OKF §9 (parseable frontmatter with non-empty `type`) and the producer conventions in `AGENTS.md` § Page Types & Conventions.
- **Obsidian wikilinks:** Internal note-to-note links use Obsidian wikilinks (`[[note]]` / `[[note|Display]]`), resolving by file basename or frontmatter `aliases`. Standard markdown links are used ONLY for external URLs (`https://…`). See `AGENTS.md` § Cross-linking.
- **Single source of truth:** The schema is defined in `AGENTS.md`. This skill enforces it; it never re-defines page types, frontmatter, or sections inline.

## Required Step Order (exact)
1. **Read the raw source** from `raw/sources/` or `raw/assets/`.
   - If text references images/assets, read those after the main text.
2. **Discuss key takeaways with operator** before framing final extraction.
   - Minimal prompt:
     - "I summarized the source. What should I emphasize?"
     - "Any specific connections to existing entities/concepts you want prioritized?"
     - "What should be de-emphasized or deferred?"
3. **Write source summary page** in `wiki/sources/` using filename `YYYY-MM-DD--source-title-slug.md`, following `AGENTS.md` § Source Pages. Set frontmatter `resource` to the raw source path (e.g. `raw/sources/file.pdf`); set `title`, `description`, `tags`, `created`, `timestamp` (today).
4. **Update/create entity pages** in `wiki/entities/` for concrete things mentioned, following `AGENTS.md` § Entity Pages. Use Obsidian wikilinks (`[[note]]` or `[[note|Display]]`) for cross-links and `# Citations` entries — the link target is the note's basename or one of its `aliases`. When updating an existing entity page from this source, increment its `source_count` by 1 and bump `timestamp` to today; when creating a new page, set `source_count: 1`.
5. **Update/create concept pages** in `wiki/concepts/` for abstract ideas mentioned, following `AGENTS.md` § Concept Pages, applying the same `source_count` increment and `timestamp` bump rule as step 4.
6. **Rebuild `wiki/index.md`** following the Canonical rebuild procedure in `AGENTS.md` § Update Rules for Special Files (`wiki/index.md`): scan every `.md` under `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, and `wiki/syntheses/` (never `wiki/templates/`), read each page's frontmatter, and rewrite the five sections (Entities, Concepts, Sources, Syntheses, Statistics) as bullet lists (`* [[note-name|Title]] - description`), preserving the `okf_version: "0.1"` frontmatter. The index must list exactly the pages that exist on disk.
7. **Append to `wiki/log.md`** a single new date-grouped entry — newest first, never edit or reorder prior entries (OKF §7).
   - Heading: `## YYYY-MM-DD`
   - Bullets: `* **Ingest**: <Source Title> — <one-line summary of what was created/updated>.`, `* **Pages touched**: <list>.`, `* **Notes**: ...`, `* **Open questions**: ...`

## Done Gate (verify before reporting done)
- [ ] Source page exists in `wiki/sources/` and complies with its type contract in `AGENTS.md` § Source Pages (frontmatter has non-empty `type` plus `title`/`description`/`resource`/`tags`/`timestamp`; all H1 sections present).
- [ ] Every entity/concept page created or updated complies with its type contract in `AGENTS.md` (Entity Pages / Concept Pages).
- [ ] No legacy fields reintroduced (`updated`, `source_path`).
- [ ] Internal links are Obsidian wikilinks (`[[…]]`); standard markdown links appear only for external URLs. No bundle-relative `/path` markdown links to internal notes.
- [ ] Every `[[wikilink]]` in created/updated pages resolves to a page on disk (basename or `aliases` match), OR is an intentional not-yet-written reference (OKF §5.3 tolerates the latter; note any such links).
- [ ] `wiki/index.md` rebuilt per the Canonical rebuild procedure and lists every page touched in this ingest (no phantom entries, no missing entries).
- [ ] `wiki/log.md` has a newly appended `## YYYY-MM-DD` ingest entry in the OKF §7 date-grouped format above.

## Path Handling Rules
- Input source roots: `raw/sources/`, `raw/assets/`.
- Output summary root: `wiki/sources/`.
- Entity updates: `wiki/entities/`.
- Concept updates: `wiki/concepts/`.
- Required global bookkeeping files: `wiki/index.md`, `wiki/log.md`.
