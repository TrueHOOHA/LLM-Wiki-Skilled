# LLM Wiki Lint Skill

## Purpose
Run a structural and logical health check of the wiki, then coordinate and apply agreed fixes.

## When to Use

Use this skill when the operator asks to health-check the wiki, or periodically (e.g., after every 10 ingests or when the wiki feels unwieldy).

## Inputs

- Optional: specific area to focus on (e.g., "check for contradictions in the AI section").

## Single Source of Truth

The page schema (frontmatter keys and required sections per type) is defined **only** in `AGENTS.md` § Page Types & Conventions. When validating, read that section and enforce it — never hardcode or re-derive the schema here.

## Checks

### 1. Schema Compliance (structural)

For every page under `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, and `wiki/syntheses/` (skip `wiki/templates/`), validate against `AGENTS.md` § Page Types & Conventions:

- **Frontmatter:** every key required for the page's `type` is present and correctly typed (`type`, `tags`, `created` always; plus type-specific keys per AGENTS.md).
- **Sections:** every required `## ` heading for the page's `type` is present and spelled exactly as in AGENTS.md.
- **Wikilinks:** every `[[link]]` anywhere in the page resolves to a page that exists on disk.
- **Filenames:** entity and concept pages use `kebab-case.md`; source and synthesis pages use `YYYY-MM-DD--slug.md` (per `AGENTS.md` § Page Types & Conventions).
- **Source pages:** `source_path` frontmatter begins with `raw/sources/` or `raw/assets/`.

Report each violation (code: `schema/*`, severity: **high**).

### 2. Contradictions

- Scan for claims on different pages that conflict.
- Look for: opposite facts, inconsistent dates, contradictory opinions attributed to the same source.
- Report each contradiction with: page A, page B, the conflicting claims, and severity (high/medium/low).

### 3. Stale Claims

- Identify assertions that newer sources have superseded.
- Look for: outdated statistics, deprecated technologies, revised theories.
- Report with: page, claim, why it's stale, and what should replace it.

### 4. Orphan Pages

- Find pages with no inbound wikilinks.
- A page is an orphan if no other page links to it.
- Report with: page name, reason it might be orphaned, and suggested pages to link from.

### 5. Missing Pages

- Identify important concepts or entities mentioned in existing pages but lacking their own dedicated page.
- Report with: where it's mentioned, why it deserves a page, and suggested page type (entity/concept).

### 6. Data Gaps

- Note areas where additional sources or web search could fill holes.
- Report with: topic, why it's important, and suggested sources or searches.

## Step-by-Step Process

1. **Run Check 1 (Schema Compliance)** against `AGENTS.md` § Page Types & Conventions for every content page. This is the mechanical gate — structural violations are high severity and should be fixed first.
2. **Scan all pages** in `wiki/` (excluding templates) for the semantic checks 2–6, documenting findings.
3. **Produce a lint report.**
   - Can be a temporary synthesis page in `wiki/syntheses/` or inline in chat.
   - Group findings by check type.
   - Rate each finding by severity (high/medium/low).
4. **Discuss fixes with the operator.**
   - Present findings.
   - Suggest specific fixes.
   - Ask for confirmation before applying.
5. **Apply agreed fixes.**
6. **Rebuild `wiki/index.md`** following the Canonical rebuild procedure in `AGENTS.md` § Update Rules for Special Files (`wiki/index.md`): scan all content pages, read frontmatter, rewrite the four grouped tables + Statistics block, listing exactly the pages on disk.
7. **Append an entry to `wiki/log.md`** — append-only, never edit prior entries.
   - Header: `## [YYYY-MM-DD] lint | <brief description>`
   - Bullets: `Action`, `Pages touched`, `Notes`, `Open questions` (see `AGENTS.md` § `wiki/log.md`).

## Output Contract

- Report lists all found issues with severity.
- Agreed fixes are applied.
- `wiki/log.md` is updated (append-only).

## Guardrails

- Do not delete pages without operator confirmation.
- Do not fix contradictions by removing older claims; instead, add context about how understanding has evolved.
- Prioritize high-severity issues (schema violations, contradictions, broken links) over cosmetic ones.
- If the wiki is very large, focus on a specific subset or ask the operator for priorities.

## Verification Checklist

- [ ] Check 1 (Schema Compliance) run against `AGENTS.md` for every content page; all `schema/*` findings addressed or triaged.
- [ ] All content pages in `wiki/` scanned for checks 2–6.
- [ ] Lint report produced and grouped by check type with severities.
- [ ] Operator consulted on fixes.
- [ ] Agreed fixes applied.
- [ ] `wiki/index.md` rebuilt per the Canonical rebuild procedure (matches pages on disk).
- [ ] `wiki/log.md` appended with a single lint entry in the required header/bullet format.
