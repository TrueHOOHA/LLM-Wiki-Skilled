---
name: llm-wiki-lint
description: "Run a structural and logical health check of the LLM Wiki OKF bundle against SPEC.md and AGENTS.md. Use whenever the operator asks to lint the wiki, check for schema violations, contradictions, stale claims, orphan pages, broken wikilinks, or health-check the wiki after ingests."
---

# LLM Wiki Lint Skill

## Purpose
Run a structural and logical health check of the wiki against OKF (SPEC.md) and the producer conventions in `AGENTS.md`, then coordinate and apply agreed fixes.

## When to Use

Use this skill when the operator asks to health-check the wiki, or periodically (e.g., after every 10 ingests or when the wiki feels unwieldy).

## Inputs

- Optional: specific area to focus on (e.g., "check for contradictions in the AI section").

## Single Source of Truth

The page schema (frontmatter fields and recommended sections per type, cross-link and citation rules, index/log formats) is defined **only** in `AGENTS.md` and OKF (SPEC.md). When validating, read `AGENTS.md` § Frontmatter Contract, § Page Types & Conventions, § Cross-linking, § Citations, and § Update Rules for Special Files, plus SPEC.md §4–§9 — never hardcode or re-derive the schema here.

## Scope

The bundle root is `wiki/`. Validate every `.md` under `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, and `wiki/syntheses/` (skip `wiki/templates/`). Also validate the reserved files `wiki/index.md` and `wiki/log.md`. Files outside `wiki/` are not part of the bundle and are not checked.

## Checks

### 1. OKF Conformance (structural, SPEC.md §9)

For every concept document under `wiki/` (excluding `index.md`, `log.md`, `templates/`):

- **Frontmatter present and parseable:** a `---`-delimited YAML block exists at the top (high if missing/malformed).
- **`type` non-empty:** the `type` field is present and non-empty (high if missing).
- **No legacy fields:** `updated` and `source_path` are not used (they migrated to `timestamp` and `resource`) (medium).
- **Recommended fields present:** `title`, `description`, `tags`, `timestamp` (low if absent — these are OKF-recommended, not strictly required).
- **Source pages:** `resource` is present, begins with `raw/sources/` or `raw/assets/`, AND the file at that path exists on disk (high if missing/malformed; high if the referenced file does not exist).

Report each violation (code: `okf/*`, severity as noted).

### 2. Producer-Convention Compliance (AGENTS.md § Page Types & Conventions)

- **Sections:** every recommended `# ` (H1) heading for the page's `type` is present and spelled exactly as in AGENTS.md (medium). Optional sections explicitly marked "omit otherwise" in AGENTS.md (e.g. synthesis `# Comparison Table`) are NOT required — do not flag their absence. The title is NOT a body heading — it lives in frontmatter `title` (medium if a stray `# Title` H1 duplicates the frontmatter title).
- **Filenames:** entity and concept pages use `kebab-case.md`; source and synthesis pages use `YYYY-MM-DD--slug.md` (medium).
- **Citations:** `# Citations` (where present) uses numbered `[n] [[source-slug|Title]]` wikilinks for internal source pages and `[n] [text](https://…)` markdown links for external material (low).
- **Type-specific fields:** synthesis pages have a non-empty `question`; entity/concept pages have an integer `source_count` ≥ 0 (low if absent/malformed).

Report each violation (code: `schema/*`, severity as noted).

### 3. Link Health (Obsidian wikilinks, AGENTS.md § Cross-linking)

- **Internal links are wikilinks:** every internal note-to-note link uses `[[…]]` Obsidian wikilink syntax. A bundle-relative markdown link like `[Title](/entities/x.md)` or `[Title](../entities/x.md)` for an internal note is a deviation (medium) — convert it to `[[x|Title]]`.
- **External links are markdown:** `https://…` (and other external schemes) use standard markdown links `[text](https://…)`, NOT wikilinks (low). This includes the Obsidian `[[https://…]]` / `[[http://…]]` form (an external URL wrapped in wikilink brackets) — flag it as a deviation (low) and convert to `[text](https://…)`.
- **Resolution:** every `[[target]]` (plain or `[[target|Display]]`) resolves to a file whose basename (without `.md`) or one of its frontmatter `aliases` equals `target`. Per OKF §5.3, unresolved wikilinks are **tolerated, not malformed** — report them at **low** severity for cleanup, never as schema violations.

### 4. Reserved-File Structure

- **`wiki/index.md`:** carries only `okf_version: "0.1"` frontmatter (the only frontmatter permitted in a bundle-root index, OKF §11) and OKF §6 bullet-list sections (Entities, Concepts, Sources, Syntheses, Statistics). Entries use Obsidian wikilinks (`[[note-name|Title]]`), not markdown links. No tables (medium).
- **`wiki/index.md` ↔ disk consistency:** every `.md` content page under `wiki/{entities,concepts,sources,syntheses}/` is listed in `index.md`, and every `index.md` entry resolves to a page on disk — no missing entries, no phantom entries (high). Phantom detection overlaps Check 3 wikilink resolution; the missing-entry direction is the one most easily broken by an incomplete rebuild.
- **`wiki/log.md`:** OKF §7 — `## YYYY-MM-DD` date headings, newest first, prose bullets. No `## [YYYY-MM-DD] action | desc` legacy headers (medium).

### 5. Contradictions

- Scan for claims on different pages that conflict.
- Look for: opposite facts, inconsistent dates, contradictory opinions attributed to the same source.
- Report each contradiction with: page A, page B, the conflicting claims, and severity (high/medium/low).

### 6. Stale Claims

- Identify assertions that newer sources have superseded.
- Look for: outdated statistics, deprecated technologies, revised theories.
- Report with: page, claim, why it's stale, and what should replace it.

### 7. Orphan Pages

- Find concept documents with no inbound wikilinks from other pages.
- Report with: page name, reason it might be orphaned, and suggested pages to link from.

### 8. Missing Pages

- Identify important concepts or entities mentioned via `[[target]]` in existing pages but whose target note does not yet exist (unresolved wikilinks). Per OKF §5.3 these are tolerated, but a cluster of unresolved links to the same missing concept suggests it deserves a page.
- Report with: where it's mentioned, why it deserves a page, and suggested page type (entity/concept).

### 9. Data Gaps

- Note areas where additional sources or web search could fill holes.
- Report with: topic, why it's important, and suggested sources or searches.

## Step-by-Step Process

1. **Run Checks 1–4** (the mechanical gate) against `AGENTS.md` and SPEC.md for every content page and the reserved files. Structural violations are high/medium severity and should be fixed first.
2. **Scan all pages** in `wiki/` (excluding templates) for the semantic checks 5–9, documenting findings.
3. **Produce a lint report.**
   - Can be a temporary synthesis page in `wiki/syntheses/` or inline in chat.
   - Group findings by check type.
   - Rate each finding by severity (high/medium/low).
4. **Discuss fixes with the operator.**
   - Present findings.
   - Suggest specific fixes.
   - Ask for confirmation before applying.
5. **Apply agreed fixes.**
6. **Rebuild `wiki/index.md`** following the Canonical rebuild procedure in `AGENTS.md` § Update Rules for Special Files: scan all content pages, read frontmatter, rewrite the five bullet-list sections (`[[note-name|Title]]` entries) + Statistics block, preserving `okf_version: "0.1"`, listing exactly the pages on disk.
7. **Append an entry to `wiki/log.md`** — append-only, newest first, never edit prior entries (OKF §7).
   - Heading: `## YYYY-MM-DD`
   - Bullets: `* **Lint**: <brief description>.`, `* **Pages touched**: ...`, `* **Notes**: ...`, `* **Open questions**: ...`

## Output Contract

- Report lists all found issues with severity.
- Agreed fixes are applied.
- `wiki/log.md` is updated (append-only, OKF §7).

## Guardrails

- Do not delete pages without operator confirmation.
- Do not fix contradictions by removing older claims; instead, add context about how understanding has evolved.
- Prioritize high-severity issues (OKF/§9 conformance, `type` missing, malformed frontmatter, source `resource` wrong, contradictions) over cosmetic ones.
- If the wiki is very large, focus on a specific subset or ask the operator for priorities.

## Verification Checklist

- [ ] Checks 1–4 run against `AGENTS.md` and SPEC.md for every content page and the reserved files; all `okf/*` and high-severity `schema/*` findings addressed or triaged.
- [ ] All content pages in `wiki/` scanned for checks 5–9.
- [ ] Lint report produced and grouped by check type with severities.
- [ ] Operator consulted on fixes.
- [ ] Agreed fixes applied.
- [ ] `wiki/index.md` rebuilt per the Canonical rebuild procedure (matches pages on disk).
- [ ] `wiki/log.md` appended with a single `## YYYY-MM-DD` lint entry in the OKF §7 format.
