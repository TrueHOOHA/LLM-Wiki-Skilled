---
type: concept
aliases: ["prompt caching", "context caching", "prompt cache"]
tags: [agent-framework, cost, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Prompt Caching for Agent Context

## Definition
Prompt caching for agent context is the practice of reusing stable large prompt prefixes, such as project instructions, schemas, or source corpora, so repeated agent calls can reduce cost and latency while preserving context.

## Scope
For Tolaria, the relevant use is repeated large-context operations over stable schema/instructions/source clusters. It does not remove the need for source citations, freshness checks, or workload-specific measurement.

## Contrasts
- Retrieval decides what context to include.
- Prompt caching optimizes repeated inclusion of stable context.
- Knowledge promotion decides what becomes durable in the wiki.

## Evidence
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] links Anthropic prompt-caching materials and identifies prompt caching as a mechanism relevant to repeated large brain/project contexts.

## Related
- [[Hermes Agent]]
- [[Compounding AI Knowledge Stack]]
- [[LLM Wiki Pattern]]
- [[Graph-aware Retrieval Evals]]

## Open Questions
- Does Tolaria have enough repeated stable context per task to make prompt caching materially useful after provider-specific constraints are included?
