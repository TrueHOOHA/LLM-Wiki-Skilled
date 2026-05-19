---
name: llm-wiki-lint
description: Health-check the LLM Wiki for structural and logical issues. Use when the operator asks to lint, check, or audit the wiki, or periodically after ingests. The agent scans all pages for contradictions, stale claims, orphan pages, missing cross-references, broken links, and data gaps, then produces a severity-rated report and applies agreed fixes. Trigger keywords: "lint", "health check", "audit wiki", "check wiki", "fix wiki", "clean up wiki".
---

# Skill: Lint

## When to Use

Use this skill when the operator asks to health-check the wiki, or periodically (e.g., after every 10 ingests or when the wiki feels unwieldy).

## Inputs

- Optional: specific area to focus on (e.g., "check for contradictions in the AI section").

## Checks

### 1. Contradictions

- Scan for claims on different pages that conflict.
- Look for: opposite facts, inconsistent dates, contradictory opinions attributed to the same source.
- Report each contradiction with: page A, page B, the conflicting claims, and severity (high/medium/low).

### 2. Stale Claims

- Identify assertions that newer sources have superseded.
- Look for: outdated statistics, deprecated technologies, revised theories.
- Report with: page, claim, why it's stale, and what should replace it.

### 3. Orphan Pages

- Find pages with no inbound wikilinks.
- A page is an orphan if no other page links to it.
- Report with: page name, reason it might be orphaned, and suggested pages to link from.

### 4. Missing Pages

- Identify important concepts or entities mentioned in existing pages but lacking their own dedicated page.
- Report with: where it's mentioned, why it deserves a page, and suggested page type (entity/concept).

### 5. Broken Links

- Find wikilinks pointing to non-existent pages.
- Report with: source page, broken link text, and suggested fix (create page or remove link).

### 6. Data Gaps

- Note areas where additional sources or web search could fill holes.
- Report with: topic, why it's important, and suggested sources or searches.

## Step-by-Step Process

1. **Run schema checker first**: `python scripts/lint_schema.py --wiki-root wiki --json-out verification/lint-schema-report.json --strict` to validate frontmatter, headings, source paths, and `## Related` cross-links.
2. **Scan all pages** in `wiki/` (excluding templates) for semantic lint checks.
3. **Run each check** above, documenting findings.
4. **Produce a lint report**.
   - Can be a temporary synthesis page in `wiki/syntheses/` or inline in chat.
   - Group findings by check type.
   - Rate each finding by severity (high/medium/low).
5. **Discuss fixes with the operator**.
   - Present findings.
   - Suggest specific fixes.
   - Ask for confirmation before applying.
6. **Apply agreed fixes**.
7. **Append an entry to `wiki/log.md`**.
   - Format: `## [YYYY-MM-DD] lint | Wiki health check`
   - Include: checks run, issues found, fixes applied, open questions.

## Output Contract

- Report lists all found issues with severity.
- Agreed fixes are applied.
- `wiki/log.md` is updated.

## Guardrails

- Do not delete pages without operator confirmation.
- Do not fix contradictions by removing older claims; instead, add context about how understanding has evolved.
- Prioritize high-severity issues (contradictions, broken links) over cosmetic ones.
- If the wiki is very large, focus on a specific subset or ask the operator for priorities.

## Verification Checklist

- [ ] `scripts/lint_schema.py` run with machine-readable JSON output captured.
- [ ] All pages in `wiki/` scanned.
- [ ] Six checks completed.
- [ ] Lint report produced.
- [ ] Operator consulted on fixes.
- [ ] Agreed fixes applied.
- [ ] `wiki/log.md` appended.