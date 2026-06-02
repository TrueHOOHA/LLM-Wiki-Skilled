# Legacy Tolaria Quarantine

This directory preserves pre-cutover or nonconforming Tolaria-derived notes while the canonical wiki structure lives under `wiki/`.

Migration policy, confirmed by Overseer on 2026-05-26:

- Keep sources. Do not delete or edit source material.
- Treat `raw/` as immutable. Existing source files, links, transcripts, PDFs, and source stubs stay durable.
- Derived legacy notes are replaceable and should be quarantined here before selective promotion.
- Promote only useful, source-backed knowledge into the canonical structure:
  - `wiki/sources/`
  - `wiki/entities/`
  - `wiki/concepts/`
  - `wiki/syntheses/`
- Do not blindly import malformed old notes into `wiki/`.
- Do not create non-knowledge artifacts or follow-up work from migration findings without Overseer approval.

Use `legacy/derived-notes/` for old synthesized notes that are not canonical yet. Reprocess them as source/reference material, then update `wiki/index.md` and `wiki/log.md` after promotion.
