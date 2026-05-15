# Verification Fixtures

This directory contains sample markdown files used to verify the three core workflows (ingest, query, lint).

## Ingest Fixture

**File**: `ingest-fixture.md`

A sample raw source about "The Memex" by Vannevar Bush. Used to test that the ingest workflow:

- Creates a source page in `wiki/sources/`.
- Extracts and creates entity pages (e.g., Vannevar Bush).
- Extracts and creates concept pages (e.g., associative trails).
- Updates `wiki/index.md`.
- Appends to `wiki/log.md`.

## Query Fixture

**File**: `query-fixture.md`

A sample question and expected answer format. Used to test that the query workflow:

- Reads `wiki/index.md`.
- Reads relevant pages.
- Synthesizes an answer with citations.
- Optionally files a synthesis page.

## Lint Fixture

**File**: `lint-fixture.md`

A deliberately broken mini-wiki. Used to test that the lint workflow:

- Detects contradictions between pages.
- Identifies stale claims.
- Finds orphan pages.
- Notes missing cross-references.

---

## How to Use Fixtures

1. Place the fixture in `raw/sources/`.
2. Run the corresponding workflow skill.
3. Compare the output against the expected results.
4. If they match, the workflow is verified.

## Ingest Acceptance Criteria

Given a raw source in `raw/sources/`:

- **Raw stays untouched**: The raw source file is not modified.
- **Source page created**: A new file appears in `wiki/sources/` with correct frontmatter and all sections.
- **Entity pages updated**: Any entities mentioned get new or updated pages in `wiki/entities/`.
- **Concept pages updated**: Any concepts mentioned get new or updated pages in `wiki/concepts/`.
- **Index updated**: `wiki/index.md` reflects the new pages.
- **Log appended**: `wiki/log.md` has a new entry.

## Query Acceptance Criteria

Given a question about the wiki:

- **Answer is synthesized**: The LLM combines information from multiple pages.
- **Citations present**: The answer cites specific pages using wikilinks.
- **No hallucination**: The answer only uses information from the wiki.
- **Optional filing**: If the answer is reusable, a synthesis page is created.

## Lint Acceptance Criteria

Given a wiki with known issues:

- **Contradictions flagged**: The report identifies conflicting claims.
- **Stale claims noted**: Outdated information is highlighted.
- **Orphans found**: Pages with no inbound links are listed.
- **Missing pages noted**: Important concepts lacking pages are identified.
- **Fixes applied**: Agreed fixes are applied and logged.
