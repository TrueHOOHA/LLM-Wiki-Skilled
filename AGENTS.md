# LLM Wiki Schema

> This is the authoritative schema document. The LLM must follow these conventions when maintaining the wiki. Treat this as the system prompt for wiki operations.

## Mission

Build and maintain a persistent, compounding knowledge base. The wiki is not a dump of raw text—it is a structured, interlinked artifact that grows richer with every source. Cross-references are pre-built. Contradictions are flagged. Synthesis reflects everything read so far.

## OKF Conformance

The `wiki/` tree is an **[Open Knowledge Format (OKF)](SPEC.md)** bundle (v0.1). `wiki/` is the bundle root; every `.md` file under it that is not a reserved filename (`index.md`, `log.md`) is an OKF *concept document*. Files outside `wiki/` (`AGENTS.md`, `README.md`, `SPEC.md`, `raw/**`) are project-level artifacts, not part of the bundle, and are not subject to OKF conformance.

OKF (SPEC.md §9) requires only that every concept document carry a parseable YAML frontmatter block with a non-empty `type` field, and that reserved files follow §6/§7. This document defines the *producer conventions* layered on top of OKF: the four `type` values used (entity, concept, source, synthesis), their recommended sections, the cross-link and citation style, and the index/log contracts. These are permitted OKF extensions (SPEC.md §4.1 Extensions, §4.2 body). Where this document is silent, OKF (SPEC.md) governs.

**Obsidian-first deviation from OKF §5.** OKF §5 recommends standard markdown links for cross-linking. This bundle instead uses **Obsidian wikilinks** (`[[note]]`) for all internal note-to-note links, to provide first-class Obsidian graph-view support. Link format is not an OKF §9 conformance requirement, and OKF's permissive consumption model (§9) tolerates this. External URLs remain standard markdown links (`[text](https://…)`) — wikilinks are for internal notes only.

## Non-negotiables

1. **Raw sources are immutable.** The LLM never edits files in `raw/`. Ever.
2. **The LLM owns the wiki layer.** All markdown files under `wiki/` are created, updated, and maintained by the LLM unless explicitly overridden by the operator.
3. **Every action is logged.** Every ingest, query result filed, and lint pass appends an entry to `wiki/log.md`.
4. **The index is always current.** `wiki/index.md` must reflect the state of the wiki after every operation that touches pages.
5. **Cross-references are first-class.** Every page should link to related pages. Orphan pages are bugs.

## Directory Layout

```
LLM-Wiki/
├── AGENTS.md          # This file. Authoritative schema.
├── README.md          # Human quickstart.
├── SPEC.md            # Open Knowledge Format (OKF) v0.1 spec this bundle follows.
├── raw/               # Immutable source documents (outside the OKF bundle).
│   ├── sources/       # Text sources (articles, papers, transcripts).
│   └── assets/        # Downloaded images, data files.
├── wiki/              # OKF bundle root. LLM-generated markdown. LLM owns this tree.
│   ├── index.md       # Bundle-root index (OKF §6). Declares okf_version.
│   ├── log.md         # Update history (OKF §7).
│   ├── entities/      # Concept docs: concrete things (people, places, organizations, products).
│   ├── concepts/      # Concept docs: abstract ideas (theories, frameworks, methodologies).
│   ├── sources/       # Concept docs: one summary page per ingested source.
│   ├── syntheses/     # Concept docs: cross-source analysis, comparisons, answers.
│   └── templates/     # Reusable page templates (not concept docs; excluded from index/lint).
└── .agents/            # Project-level skill definitions (OpenCode autodiscovery).
    └── skills/
        ├── llm-wiki-ingest/   # Ingest workflow skill.
        ├── llm-wiki-query/    # Query workflow skill.
        └── llm-wiki-lint/     # Lint workflow skill.
```

> **Enforcement model.** Workflow rigidity is enforced entirely by the skills under `.agents/skills/` against the schema defined in this file. There are no helper scripts. `AGENTS.md` is the single source of truth for every page type, frontmatter field, section, index format, and log contract. Skills must never re-define the schema inline — they reference and enforce this document.

## Frontmatter Contract

Every concept document (every `.md` under `wiki/` except `index.md` and `log.md`) MUST include a YAML frontmatter block delimited by `---`.

**Required (OKF §4.1):**
- `type` — `entity` | `concept` | `source` | `synthesis`. Non-empty string. This is the only field OKF strictly requires.

**Recommended (OKF §4.1, in priority order):**
- `title` — Human-readable display name. If omitted, consumers may derive it from the filename. Expected on every page.
- `description` — A single sentence summarizing the concept. Used by `index.md` generators, search snippets, and previews. Expected on every page so the index can list it.
- `tags` — YAML list of short strings for cross-cutting categorization.
- `timestamp` — ISO 8601 (date or datetime) of last meaningful change. Replaces the legacy `updated` field.
- `resource` — A URI identifying the underlying asset the concept describes. Used on source pages to point at the raw source file. Absent for abstract concepts.

**Producer extensions (permitted by OKF §4.1 — consumers must tolerate unknown keys):**
- `aliases` — YAML list of alternative names (entity, concept). **Load-bearing for wikilink resolution** — see § Cross-linking.
- `created` — ISO date the page was first created.
- `source_count` — Integer; how many ingested sources mention this entity/concept.
- `question` — The exact question a synthesis page answers.
- `author` / `date` — Source metadata.

The legacy `updated` and `source_path` fields are migrated to `timestamp` and `resource` respectively; do not reintroduce them.

## Page Types & Conventions

The body of every concept document is standard markdown. Per OKF §4.2 there are *no required body sections*; the sections below are this bundle's producer conventions. Section headings use `#` (H1) — the document title lives in frontmatter `title`, not as a body heading (OKF §4.2/§4.3). Producers SHOULD favor structural markdown (headings, lists, tables, fenced code) over freeform prose.

### Entity Pages (`wiki/entities/`)

- Filename: `kebab-case.md`
- Purpose: A concrete thing that appears across multiple sources.
- Frontmatter:
  ```yaml
  ---
  type: entity
  title: Entity Name
  description: One-line summary.
  aliases: ["Alternative Name", "Abbreviation"]
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  timestamp: YYYY-MM-DD
  source_count: 1
  ---
  ```
- Update rule: when creating a page, set `source_count: 1`; when updating from a new source, increment `source_count` by 1 and bump `timestamp` to today.
- Sections (H1):
  - `# Identity` — What it is, one concise paragraph.
  - `# Aliases` — List of known aliases.
  - `# Key Attributes` — Structured facts (table or bullet list).
  - `# Citations` — Numbered wikilinks to source summaries that mention this entity, with brief context. See § Citations.
  - `# Related` — Obsidian wikilinks to related entity and concept pages.
  - `# Open Questions` — Uncertainties or gaps about this entity.

### Concept Pages (`wiki/concepts/`)

- Filename: `kebab-case.md`
- Purpose: An abstract idea, theory, or methodology.
- Frontmatter:
  ```yaml
  ---
  type: concept
  title: Concept Name
  description: One-line summary.
  aliases: ["Synonym", "Related Term"]
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  timestamp: YYYY-MM-DD
  source_count: 1
  ---
  ```
- Update rule: when creating a page, set `source_count: 1`; when updating from a new source, increment `source_count` by 1 and bump `timestamp` to today.
- Sections (H1):
  - `# Definition` — Precise definition in one paragraph.
  - `# Scope` — What this concept covers and what it does not.
  - `# Contrasts` — Differences from related concepts.
  - `# Citations` — Numbered wikilinks with context.
  - `# Related` — Cross-links (wikilinks).
  - `# Open Questions`

### Source Pages (`wiki/sources/`)

- Filename: `YYYY-MM-DD--source-title-slug.md`, where the date prefix is the **ingest date** (when the source page is created). The source's own publication date is recorded in the frontmatter `date` field below.
- Purpose: Summary and extraction from a single raw source.
- Frontmatter:
  ```yaml
  ---
  type: source
  title: "Exact Title of Source"
  description: One-line summary.
  resource: raw/sources/original-filename.pdf
  author: "Author Name"
  date: YYYY-MM-DD
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  timestamp: YYYY-MM-DD
  ---
  ```
- Sections (H1):
  - `# Summary` — 3-5 sentence overview.
  - `# Key Claims` — Numbered list of main assertions.
  - `# Notable Quotes` — Direct quotes with page/section references if available.
  - `# Entities Mentioned` — Obsidian wikilinks to entity pages created or updated.
  - `# Concepts Mentioned` — Obsidian wikilinks to concept pages.
  - `# Follow-ups` — Questions or leads from this source.

`resource` holds the path to the immutable raw source, relative to the repo root (e.g. `raw/sources/file.pdf` or `raw/assets/file.png`). It replaces the legacy `source_path`.

### Synthesis Pages (`wiki/syntheses/`)

- Filename: `YYYY-MM-DD--question-slug.md` or `YYYY-MM-DD--topic-slug.md`
- Purpose: Cross-source analysis, answers to questions, comparisons.
- Frontmatter:
  ```yaml
  ---
  type: synthesis
  title: Synthesis Title
  description: One-line summary.
  question: "The exact question this page answers"
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  timestamp: YYYY-MM-DD
  ---
  ```
- Sections (H1):
  - `# Question / Purpose`
  - `# Answer / Analysis`
  - `# Comparison Table` (include only when comparing options side by side; omit otherwise)
  - `# Citations` — Numbered wikilinks to source pages with brief evidence snippets.
  - `# Implications` — Why this matters.
  - `# Follow-up Questions`

## Cross-linking

Concepts link to other concepts using **Obsidian wikilinks** (the `[[…]]` syntax). This is a producer convention that overrides OKF §5's standard-markdown-link recommendation, chosen for first-class Obsidian graph-view support; it does not affect OKF §9 conformance (link format is not a §9 requirement). Two forms:

- `[[note-name]]` — links to the note whose file basename (without `.md`) is `note-name`.
- `[[note-name|Display Text]]` — same, with a human-readable label.

**Resolution:** a wikilink resolves (and passes lint) if `note-name` matches a file's basename OR one of its frontmatter `aliases`. The `aliases` field keeps pages linkable by human-readable names regardless of their kebab-case filename — e.g. `[[My Entity]]` resolves to `my-entity.md` via its alias `"My Entity"`.

A link asserts a *relationship*; the specific kind (references, related-to, depends-on) is conveyed by the surrounding prose. Consumers MUST tolerate broken links — a `[[target]]` whose note does not yet exist represents not-yet-written knowledge, not a malformed document (OKF §5.3 spirit). The lint pass reports unresolved wikilinks at **low** severity for cleanup, never as schema violations.

**External URLs are not wikilinks.** For `https://…` (or other external schemes) use standard markdown links: `[text](https://example.com)`. Wikilinks are for internal notes only. In particular, Obsidian's `[[https://example.com]]` / `[[http://…]]` syntax (an external URL wrapped in wikilink brackets) is PROHIBITED — it is an external link, not an internal note reference; use `[text](https://example.com)` instead.

## Citations

When a concept's body makes claims sourced from other material, list those sources under a `# Citations` heading (OKF §8), numbered:

```markdown
# Citations

[1] [[source-slug|Source Title]] — brief context or quote.
[2] [External announcement](https://example.com/announcement)
```

Rules:
1. Every factual claim in a page SHOULD cite at least one source page or external source.
2. Citation links to internal source pages are **Obsidian wikilinks** (`[[source-slug]]` or `[[source-slug|Title]]`); citation links to external material are standard markdown links (`[text](https://…)`) (OKF §8).
3. In source pages, the raw source is cited via the `resource` frontmatter field, not a body citation.
4. When updating a page from a new source, append the new citation — do not remove earlier ones unless they are factually incorrect.

## Ingest Workflow

See `.agents/skills/llm-wiki-ingest/SKILL.md`. Procedure is owned by the skill; this document owns only the schema (page types, frontmatter, sections, cross-link and citation rules, and the index/log update rules below).

## Query Workflow

See `.agents/skills/llm-wiki-query/SKILL.md`.

## Lint Workflow

See `.agents/skills/llm-wiki-lint/SKILL.md`.

## Update Rules for Special Files

### `wiki/index.md` (bundle-root index, OKF §6)

`wiki/index.md` is the bundle-root index. It is the ONLY `index.md` permitted to carry frontmatter, and only to declare the OKF version (OKF §11):

```yaml
---
okf_version: "0.1"
---
```

The body uses one section per group, each a bullet list of entries. Entries use Obsidian wikilinks (consistent with § Cross-linking) and SHOULD include the linked concept's `description` (OKF §6):

```markdown
# Entities

* [[my-entity|Entity Name]] - one-line summary
* [[another|Another]] - summary

# Concepts

* [[my-concept|Concept Name]] - summary

# Sources

* [[2026-01-01--source-slug|Source Title]] - summary

# Syntheses

* [[2026-01-01--topic-slug|Synthesis Title]] - summary

# Statistics

- Total pages: 0
- Total sources: 0
- Last updated: YYYY-MM-DD
```

**Canonical rebuild procedure** (the only way to regenerate the index; every workflow that touches pages must run this on completion):

1. Read every `.md` file under `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, and `wiki/syntheses/` (never `wiki/templates/`).
2. For each page, read its YAML frontmatter: `type`, `title` (or derive from filename), `description`, `tags`, `created`, `timestamp`, `source_count`, and the file's basename (note name) and `aliases`.
3. Derive the one-line summary from the page's `description` frontmatter; if absent, from the first content paragraph under the page's first `# ` section.
4. Rewrite `wiki/index.md` wholesale: preserve the `okf_version: "0.1"` frontmatter, then the five sections (Entities, Concepts, Sources, Syntheses, Statistics) as bullet lists. Each non-Statistics entry: `* [[note-name|Title]] - description`, where `note-name` is the file's basename without `.md` and `Title` is the frontmatter `title`.
5. The Statistics block lists total pages, total sources (count of `type: source` pages), and the latest `timestamp` across all pages as "Last updated".
6. The index must list exactly the pages that exist on disk — no missing entries, no phantom entries.

### `wiki/log.md` (update history, OKF §7)

- Strictly append-only during routine operations. (A one-time format migration to OKF §7 is the only permitted rewrite.)
- Newest entries first.
- Each entry is a date group: an `## YYYY-MM-DD` heading (ISO 8601 date) followed by one or more bullets. The leading bold word is a convention, not a requirement (OKF §7):

```markdown
## 2026-05-22

* **Ingest**: Added source "Article Title" — created source page, updated 3 entities, 1 concept.
* **Pages touched**: `wiki/sources/2026-05-22--article-title.md`, `wiki/entities/foo.md`, …
* **Notes**: First source on this topic.
* **Open questions**: None.
```

Action types: `Ingest`, `Query`, `Lint`, `Init`, `Migration`.

## Operator Communication Style

- When ingesting, summarize what was done and what pages were touched.
- When querying, cite sources and offer to file reusable answers.
- When linting, present findings with severity and suggested fixes.
- Always ask before making large structural changes.

## Schema Evolution

This document is co-evolved with the operator. If a workflow isn't working, propose a change here before changing behavior. OKF itself evolves per SPEC.md §11; this bundle declares `okf_version: "0.1"`.

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting contradictions, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Private, actively curated, with the connections between documents as valuable as the documents themselves. The part Bush couldn't solve was who does the maintenance. The LLM handles that.
