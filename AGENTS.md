# LLM Wiki Schema

> This is the authoritative schema document. The LLM must follow these conventions when maintaining the wiki. Treat this as the system prompt for wiki operations.

## Mission

Build and maintain a persistent, compounding knowledge base. The wiki is not a dump of raw text—it is a structured, interlinked artifact that grows richer with every source. Cross-references are pre-built. Contradictions are flagged. Synthesis reflects everything read so far.

## Non-negotiables

1. **Raw sources are immutable.** The LLM never edits files in `raw/`. Ever.
2. **The LLM owns the wiki layer.** All markdown files under `wiki/` are created, updated, and maintained by the LLM unless explicitly overridden by the operator.
3. **Every action is logged.** Every ingest, query result filed, and lint pass appends an entry to `wiki/log.md`.
4. **The index is always current.** `wiki/index.md` must reflect the state of the wiki after every operation that touches pages.
5. **Cross-references are first-class.** Every page must link to related pages. Orphan pages are bugs.

## Directory Layout

```
LLM-wiki/
├── AGENTS.md          # This file. Authoritative schema.
├── README.md          # Human quickstart.
├── raw/               # Immutable source documents.
│   ├── sources/       # Text sources (articles, papers, transcripts).
│   └── assets/        # Downloaded images, data files.
├── wiki/              # LLM-generated markdown. LLM owns this tree.
│   ├── index.md       # Content catalog. Always up to date.
│   ├── log.md         # Append-only timeline.
│   ├── entities/      # Concrete things (people, places, organizations, products).
│   ├── concepts/      # Abstract ideas (theories, frameworks, methodologies).
│   ├── sources/       # One summary page per ingested source.
│   ├── syntheses/     # Cross-source analysis, comparisons, answers.
│   └── templates/     # Reusable page templates.
└── .agents/            # Project-level skill definitions (OpenCode autodiscovery).
    └── skills/
        ├── llm-wiki-ingest/   # Ingest workflow skill.
        ├── llm-wiki-query/    # Query workflow skill.
        └── llm-wiki-lint/     # Lint workflow skill.
```

> **Enforcement model.** Workflow rigidity is enforced entirely by the skills under `.agents/skills/` against the schema defined in this file. There are no helper scripts. `AGENTS.md` is the single source of truth for every page type, frontmatter field, section, index format, and log contract. Skills must never re-define the schema inline — they reference and enforce this document.

## Page Types & Conventions

### Entity Pages (`wiki/entities/`)

- Filename: `kebab-case.md`
- Purpose: A concrete thing that appears across multiple sources.
- Frontmatter:
  ```yaml
  ---
  type: entity
  aliases: ["Alternative Name", "Abbreviation"]
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  source_count: 0
  ---
  ```
- Sections:
  - `# Entity Name` — H1 title, exact canonical name.
  - `## Identity` — What it is, one concise paragraph.
  - `## Aliases` — List of known aliases.
  - `## Key Attributes` — Structured facts (table or bullet list).
  - `## Evidence` — Links to source summaries that mention this entity, with brief quote or context per link.
  - `## Related` — Links to related entity and concept pages.
  - `## Open Questions` — Uncertainties or gaps about this entity.

### Concept Pages (`wiki/concepts/`)

- Filename: `kebab-case.md`
- Purpose: An abstract idea, theory, or methodology.
- Frontmatter:
  ```yaml
  ---
  type: concept
  aliases: ["Synonym", "Related Term"]
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  source_count: 0
  ---
  ```
- Sections:
  - `# Concept Name`
  - `## Definition` — Precise definition in one paragraph.
  - `## Scope` — What this concept covers and what it does not.
  - `## Contrasts` — Differences from related concepts.
  - `## Evidence` — Source links with context.
  - `## Related` — Cross-links.
  - `## Open Questions`

### Source Pages (`wiki/sources/`)

- Filename: `YYYY-MM-DD--source-title-slug.md`
- Purpose: Summary and extraction from a single raw source.
- Frontmatter:
  ```yaml
  ---
  type: source
  source_path: raw/sources/original-filename.pdf
  title: "Exact Title of Source"
  author: "Author Name"
  date: YYYY-MM-DD
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  ---
  ```
- Sections:
  - `# Source Title`
  - `## Summary` — 3-5 sentence overview.
  - `## Key Claims` — Numbered list of main assertions.
  - `## Notable Quotes` — Direct quotes with page/section references if available.
  - `## Entities Mentioned` — Links to entity pages created or updated.
  - `## Concepts Mentioned` — Links to concept pages.
  - `## Follow-ups` — Questions or leads from this source.

### Synthesis Pages (`wiki/syntheses/`)

- Filename: `YYYY-MM-DD--question-slug.md` or `YYYY-MM-DD--topic-slug.md`
- Purpose: Cross-source analysis, answers to questions, comparisons.
- Frontmatter:
  ```yaml
  ---
  type: synthesis
  question: "The exact question this page answers"
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  ---
  ```
- Sections:
  - `# Synthesis Title`
  - `## Question / Purpose`
  - `## Answer / Analysis`
  - `## Comparison Table` (if applicable)
  - `## Citations` — Links to source pages with brief evidence snippets.
  - `## Implications` — Why this matters.
  - `## Follow-up Questions`

## Citation Rules

1. Every claim in a wiki page must cite at least one source page or synthesis page.
2. Use Obsidian wikilink syntax: `[[target]]` or `[[target|display text]]`, where `target` is the linked note's name — the file's **basename without extension**. For a page stored as `wiki/entities/my-entity.md`, the note name is `my-entity`, so link to it as `[[my-entity]]` or, for a readable label, `[[my-entity|My Entity]]`.
3. A wikilink resolves (and passes lint) if `target` matches either the file's basename or one of its frontmatter `aliases`. The `aliases` field exists so pages stay linkable by human-readable names (e.g. `[[My Entity]]`) regardless of their kebab-case filename.
4. In source pages, cite the raw source file path in `source_path` frontmatter.
5. When updating a page based on a new source, append the new citation—do not remove old ones unless they are factually incorrect.

## Ingest Workflow

See `.agents/skills/llm-wiki-ingest/SKILL.md`. Procedure is owned by the skill; this document owns only the schema (page types, frontmatter, sections, citation rules, and the index/log update rules below).

## Query Workflow

See `.agents/skills/llm-wiki-query/SKILL.md`.

## Lint Workflow

See `.agents/skills/llm-wiki-lint/SKILL.md`.

## Update Rules for Special Files

### `wiki/index.md`

- Append-only for new pages.
- Modify existing entries when pages are updated (change `updated` date and summary if needed).
- Group by: Entities, Concepts, Sources, Syntheses.
- Each entry: `| [[Page Name]] | One-line summary | Source count | Status | Updated |`

**Canonical rebuild procedure** (the only way to regenerate the index; every workflow that touches pages must run this on completion):

1. Read every `.md` file under `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, and `wiki/syntheses/` (never `wiki/templates/`).
2. For each page, read its YAML frontmatter: `type`, `tags`, `created`, `updated`, `source_count` (and `title` for source pages).
3. Derive a one-line summary from the first content paragraph under the page's first `## ` section.
4. Rewrite `wiki/index.md` wholesale, preserving the fixed structure: H1 `# Wiki Index`, the catalog note, then four tables (Entities, Concepts, Sources, Syntheses) each with the header `| Page | Summary | Sources | Status | Updated |`, followed by a `## Statistics` block listing total pages, total sources, and last-updated date.
5. The index must list exactly the pages that exist on disk — no missing rows, no phantom rows. `updated` dates come from page frontmatter.

### `wiki/log.md`

- Strictly append-only.
- Each entry starts with: `## [YYYY-MM-DD] action-type | Brief description`
- Include: action type (ingest/query/lint), pages touched, notes, open questions.

## Frontmatter Contract

Every wiki page must include YAML frontmatter with at minimum:
- `type`: entity | concept | source | synthesis
- `tags`: list of relevant tags
- `created`: ISO date

Optional but recommended:
- `updated`: ISO date
- `source_count`: integer
- `aliases`: list of alternative names

## Operator Communication Style

- When ingesting, summarize what was done and what pages were touched.
- When querying, cite sources and offer to file reusable answers.
- When linting, present findings with severity and suggested fixes.
- Always ask before making large structural changes.

## Schema Evolution

This document is co-evolved with the operator. If a workflow isn't working, propose a change here before changing behavior.

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting contradictions, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Private, actively curated, with the connections between documents as valuable as the documents themselves. The part Bush couldn't solve was who does the maintenance. The LLM handles that.
