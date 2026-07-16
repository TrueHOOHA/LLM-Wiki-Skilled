# Raw Source Policy

## What lives here

`raw/` holds your immutable source documents. These are the ground truth. The LLM reads from them but never modifies them.

* `raw/sources/` — Text-based sources: articles, papers, transcripts, meeting notes, book chapters, etc.
* `raw/assets/` — Binary or media files: images, charts, data files, PDFs, etc.

## Immutability rule

**Once a file is placed in `raw/`, it must not be edited.** If you have a revised version of a source, add it as a new file (e.g. `article-v2.md`) and re-ingest. This preserves the provenance chain of knowledge.

## Naming conventions

* Use descriptive kebab-case filenames.
* For time-sensitive sources, add a date prefix: `YYYY-MM-DD--article-title.md`.
* Examples:
  * `2026-05-15--attention-is-all-you-need.md`
  * `2026-05-15--meeting-transcript-project-kickoff.md`
  * `report-on-market-trends-2026.md`

## Adding a source

1. Save or clip the source file into `raw/sources/`.
2. (Optional) Download any referenced images into `raw/assets/`.
3. Tell your LLM agent to ingest it.
4. The agent will read, summarize, and integrate it into the knowledge base.

## Asset handling

* Images referenced by a source should be downloaded to `raw/assets/` under a descriptive name.
* The LLM can view images standalone (inline image reads are not always reliable).
* Link to an asset from a source file in `raw/sources/` using a relative path: `../assets/image-name.png`.
