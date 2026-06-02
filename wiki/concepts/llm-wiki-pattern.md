---
type: concept
aliases: ["Karpathy LLM Wiki", "LLM Wiki", "wiki-first knowledge base"]
tags: [knowledge-management, retrieval, schema]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# LLM Wiki Pattern

## Definition
The LLM Wiki Pattern is a knowledge-base design where immutable raw sources feed LLM-maintained source, entity, concept, and synthesis pages, with schema rules, an index, and an append-only log maintaining navigable compiled knowledge.

## Scope
It covers source preservation, wiki-page promotion, cross-links, contradiction handling, and deterministic verification. It does not by itself prove retrieval quality or automate downstream implementation.

## Contrasts
- Unlike open-web RAG, it compiles reusable knowledge once and updates it as sources accumulate.
- Unlike a raw document archive, it requires explicit entity/concept/synthesis pages and bookkeeping.

## Evidence
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] links Karpathy's LLM Wiki gist and frames GBrain as an extension of this idea.

## Related
- [[GBrain]]
- [[Compounding AI Knowledge Stack]]
- [[Graph-aware Retrieval Evals]]
- [[Hermes Agent]]

## Open Questions
- Which Tolaria pages should remain strictly source-backed versus becoming higher-level syntheses with weaker evidence grades?
