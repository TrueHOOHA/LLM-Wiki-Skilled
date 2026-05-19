---
name: llm-wiki-ingest
description: Ingest a new raw source into the LLM Wiki knowledge base. Use when the operator wants to add a new source (article, paper, transcript) to the wiki by dropping it into raw/sources/ and requesting ingestion. The agent reads the source, creates a summary page, updates entity and concept pages, and maintains the index and log. Trigger keywords: "ingest", "add source", "import article", "process source", "integrate source".
---

# Skill: Ingest

## When to Use

Use this skill when the operator wants to add a new source to the wiki.

## Inputs

- Path to raw source file (e.g., `raw/sources/2026-05-15--article-title.md`)
- Optional: operator's initial observations or focus areas

## Preconditions

- Source file exists in `raw/sources/` or `raw/assets/`.
- Source has not already been ingested (check `wiki/sources/` for existing pages).

## Step-by-Step Process

1. **Read the raw source**.
   - If the source references images, read them separately after reading the text.

2. **Discuss key takeaways with the operator**.
   - Summarize the main points in your own words.
   - Ask what to emphasize, what connections to draw, what to prioritize.
   - This is a conversation, not a report — the operator's judgment shapes what gets extracted and how it's framed.
   - Prefer one source at a time with active operator involvement, but support batch ingestion if requested.

3. **Create a source summary page** in `wiki/sources/`.
   - Filename: `YYYY-MM-DD--source-title-slug.md`
   - Follow the template in `wiki/templates/source.md`.
   - Include frontmatter with `type: source`, `source_path`, `title`, `author`, `date`, `tags`, `created`.
   - Write `## Summary`, `## Key Claims`, `## Notable Quotes`, `## Entities Mentioned`, `## Concepts Mentioned`, `## Follow-ups`.

4. **Update or create entity pages** in `wiki/entities/`.
   - For each concrete thing mentioned in the source, ensure an entity page exists.
   - Update `source_count`, `updated`, and `tags` in frontmatter.
   - Add evidence from the new source to `## Evidence`.
   - Add or update `## Related` links.

5. **Update or create concept pages** in `wiki/concepts/`.
   - For each abstract idea mentioned in the source, ensure a concept page exists.
   - Update `source_count`, `updated`, and `tags` in frontmatter.
   - Add evidence from the new source to `## Evidence`.
   - Add or update `## Related` links.

6. **Rebuild `wiki/index.md`**.
   - Run `python3 scripts/rebuild_index.py` to deterministically regenerate all four index tables.
   - The script recomputes statistics (total pages, total sources, last updated).

7. **Append an entry to `wiki/log.md`**.
   - Format: `## [YYYY-MM-DD] ingest | Source Title`
   - Include: action type, pages touched, notes, open questions.

## Output Contract

- Raw source remains untouched.
- Source page exists and is complete.
- All entities and concepts mentioned have pages.
- `wiki/index.md` reflects all changes.
- `wiki/log.md` has a new entry.

## Guardrails

- Never edit files in `raw/`.
- Do not remove old citations when adding new ones.
- If a source contradicts existing claims, note the contradiction on the relevant pages and in the log.
- Ask the operator before creating more than 10 new pages in one ingest.

## Verification Checklist

- [ ] Raw source was read.
- [ ] Source page created in `wiki/sources/`.
- [ ] Entity pages updated/created in `wiki/entities/`.
- [ ] Concept pages updated/created in `wiki/concepts/`.
- [ ] `python3 scripts/rebuild_index.py` run and `wiki/index.md` updated.
- [ ] `wiki/log.md` appended.
