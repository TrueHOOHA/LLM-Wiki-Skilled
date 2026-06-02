---
type: concept
aliases: ["graph-vector memory", "hybrid graph and vector memory", "graph-backed semantic memory"]
tags: [agent-engineering, memory, retrieval, knowledge-graph]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Hybrid Graph-vector Agent Memory

## Definition
Hybrid Graph-vector Agent Memory is an agent-memory architecture that combines vector embeddings for semantic similarity with graph entities/relationships for structural retrieval, usually alongside relational metadata for source, chunk, dataset, and provenance tracking. The goal is to make stored memory both searchable by meaning and navigable by relationships.

## Scope
It covers retrieval architectures where vector search, graph search, graph completion, lexical chunks, summaries, temporal retrieval, and provenance metadata may all contribute to an answer. It does not prove that hybrid retrieval beats simpler search for every workload; its value must be measured against task-specific recall, citation accuracy, latency, cost, and failure behavior.

## Contrasts
- Versus pure vector RAG: graph relationships can expose connections and multi-hop context that nearest-neighbor chunks may miss, but graph extraction can introduce errors and cost.
- Versus pure knowledge graph search: vectors can recover semantically related passages even when entity extraction or schema coverage is incomplete.
- Versus [[Graph-aware Retrieval Evals]]: the architecture is the retrieval design; graph-aware evals measure whether that design actually helps.
- Versus [[LLM Wiki Pattern]]: wiki pages precompile human-readable relationships; hybrid graph-vector memory may compute and rank relationships inside a database.

## Evidence
- [[Cognee - Open Source Memory Platform for Agents]] states that Cognee uses relational storage for documents/chunks/provenance, vector storage for embeddings, and graph storage for entities/relationships, with `recall()` choosing or accepting retrieval strategies.
- [[Cognee Memory Architecture Patterns Assessment]] identifies hybrid retrieval as a useful reference pattern but grades Cognee's performance claims as not independently validated for Hermes/Tolaria.

## Related
- [[Cognee]]
- [[Agent Memory Control Plane]]
- [[Graph-aware Retrieval Evals]]
- [[Memory Hygiene for AI Agents]]
- [[Dynamic Context Loading]]
- [[LLM Wiki Pattern]]

## Open Questions
- Which Hermes/Tolaria queries actually require graph-neighbor or multi-hop retrieval beyond source-backed wiki links and text search?
- How should graph extraction errors, stale edges, duplicate entities, and weak inferred relationships be surfaced to the operator?
- What is the smallest benchmark that can compare pure wiki search, vector retrieval, graph retrieval, and hybrid retrieval fairly?
