# Directory Update Log

> Append-only history of all operations (OKF §7). Newest first. Each entry is a date group with prose bullets.

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
