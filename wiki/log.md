# Directory Update Log

> Append-only history of all operations (OKF §7). Newest first. Each entry is a date group with prose bullets.

## 2026-07-16

* **Lint**: Audited every produced `wiki/` file for OKF v0.1 §9 conformance and Obsidian-wikilink-only internal linking (4 dimension scouts + 1 completeness critic). All 6 files verified clean; closed 1 file issue and 3 forward-enforcement gaps.
* **Pages touched**: `wiki/templates/synthesis.md`, `.agents/skills/llm-wiki-query/SKILL.md`, `.agents/skills/llm-wiki-lint/SKILL.md`, `AGENTS.md`.
* **Notes**: Verified `wiki/index.md`, `wiki/log.md`, and the 4 templates are OKF-conformant and use wikilinks exclusively for internal links (index↔disk consistent: 0 content pages = 0 index entries). Fixed a prose `[[wikilinks]]` in `wiki/templates/synthesis.md` (would have rendered as a link to a nonexistent note). Closed 3 enforcement gaps so future-produced files stay conformant: (1) query skill Done Gate and (2) lint Check 2 no longer over-require the optional synthesis `# Comparison Table` section; (3) AGENTS.md § Cross-linking and lint Check 3 now explicitly prohibit the Obsidian `[[https://…]]` external-URL-in-wikilink-brackets form. `wiki/index.md` not rebuilt — no content pages changed (verified already consistent).
* **Open questions**: None.

* **Migration**: Synced README documentation to the latest state.
* **Pages touched**: `README.zh-CN.md`.
* **Notes**: The Chinese README's Project Structure block was stale — it used `LLM-wiki/` (wrong case), omitted `LICENSE`, and lacked the `raw/README.md` / `raw/README.en.md` rows that the English README already listed. Brought it into exact parity with the English README's structure block (which was fixed in the earlier Migration entry). The English README needed no further changes. `wiki/index.md` not rebuilt — no content pages changed.
* **Open questions**: None.

* **Migration**: Completed the wiki scaffold and clarified schema conventions.
* **Pages touched**: `wiki/templates/entity.md`, `wiki/templates/concept.md`, `wiki/templates/source.md`, `wiki/templates/synthesis.md`, `wiki/entities/.gitkeep`, `wiki/concepts/.gitkeep`, `wiki/sources/.gitkeep`, `wiki/syntheses/.gitkeep`, `raw/assets/.gitkeep`, `wiki/index.md`, `wiki/log.md`, `AGENTS.md`, `README.md`, `raw/README.en.md`, `.agents/skills/llm-wiki-lint/SKILL.md`.
* **Notes**: Created the four page templates and `.gitkeep` markers so the scaffold matches the layout documented in AGENTS.md/README. Clarified in AGENTS.md that the source-page filename date prefix is the ingest date (source's own date lives in frontmatter `date`) and centralized the `source_count` increment rule into the Entity/Concept page conventions. Enhanced the lint skill with index↔disk consistency (no missing/phantom entries) and source-`resource` file-existence checks. Fixed the README and AGENTS.md project-structure blocks. Added `raw/README.en.md` as the English companion to `raw/README.md` (left untouched per raw immutability).
* **Open questions**: None.

## 2026-06-28

* **Migration**: Reformatted the wiki to conform to the Open Knowledge Format (OKF v0.1, `SPEC.md`). `wiki/` is now the OKF bundle root.
* **Pages touched**: `AGENTS.md`, `wiki/index.md`, `wiki/log.md`, `wiki/templates/{entity,concept,source,synthesis}.md`, `.agents/skills/llm-wiki-{ingest,query,lint}/SKILL.md`, `README.md`, `README.zh-CN.md`.
* **Notes**: Frontmatter migrated to OKF fields (`title`, `description`, `tags`, `timestamp`, `resource`); `updated`→`timestamp`, `source_path`→`resource`. Body sections moved to H1 with title in frontmatter. Internal note-to-note links use Obsidian wikilink syntax (`[[note]]` / `[[note|Display]]`) for first-class Obsidian graph-view support — a producer convention overriding OKF §5's markdown-link recommendation (link format is not an OKF §9 requirement); standard markdown links reserved for external URLs only. `wiki/index.md` rebuilt as OKF §6 bullet lists (wikilink entries) with `okf_version: "0.1"` frontmatter. This log itself follows OKF §7 date-grouped format; the prior `init` entry is preserved below in the new shape.
* **Open questions**: None.

## 2026-05-15

* **Init**: Created the LLM Wiki project scaffold — directory structure, schema (`AGENTS.md`), initial templates, `wiki/index.md`, `wiki/log.md`, `raw/README.md`.
* **Pages touched**: `AGENTS.md`, `README.md`, `raw/README.md`, `wiki/index.md`, `wiki/log.md`.
* **Notes**: Initial layout and schema (pre-OKF format).
* **Open questions**: None.
