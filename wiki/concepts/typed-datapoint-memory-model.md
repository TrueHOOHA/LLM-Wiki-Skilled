---
type: concept
aliases: ["typed memory datapoints", "DataPoint graph memory", "typed graph memory model"]
tags: [agent-engineering, memory, knowledge-graph, data-modeling]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Typed DataPoint Memory Model

## Definition
A Typed DataPoint Memory Model is a graph-memory pattern where domain objects are represented as explicit typed nodes, indexed fields, and programmatic relationships rather than only as unstructured text chunks. In [[Cognee]], custom Pydantic `DataPoint` classes can become graph nodes, fields can become relationships, and `PipelineContext` can attach dataset/data provenance.

## Scope
This concept covers typed memory objects, explicit edges, relationship metadata, indexed fields, custom extraction tasks, direct graph insertion, and provenance-aware dataset linking. It does not imply that hand-modeled graph schemas are always worth their cost; they are most useful when the domain has stable entity types and relationships that retrieval must respect.

## Contrasts
- Versus chunk-only memory: DataPoints encode structured entities and relationships directly instead of waiting for retrieval to infer them from text chunks.
- Versus ad hoc JSON memory: typed models can define index fields, relationships, validation boundaries, and graph insertion behavior.
- Versus ontology enrichment: a DataPoint schema models local domain objects; ontology grounding connects them to external established structures.
- Versus [[LLM Wiki Pattern]]: wiki concepts/entities are human-readable typed pages; DataPoints are database graph objects that need inspection tooling and provenance.

## Evidence
- [[Cognee - Open Source Memory Platform for Agents]] captures the custom data model guide: `DataPoint` subclasses, `metadata: {"index_fields": [...]}`, relationships through fields or weighted edges, `add_data_points`, and `PipelineContext(user, dataset, data_item)` for dataset and data-item linking.
- [[Cognee Memory Architecture Patterns Assessment]] treats typed DataPoints as a useful pattern for evaluation, especially where provenance and deletion semantics matter.

## Related
- [[Cognee]]
- [[Agent Memory Control Plane]]
- [[Hybrid Graph-vector Agent Memory]]
- [[Memory Hygiene for AI Agents]]
- [[LLM Wiki Pattern]]
- [[Graph-aware Retrieval Evals]]

## Open Questions
- Which Hermes/Tolaria knowledge objects are structured enough to justify a typed graph model rather than markdown pages and source-backed summaries?
- How should typed graph memory expose diffs, reviews, and corrections to human operators?
- Can dataset-linked DataPoints provide reliable forgetting/deletion semantics when the same node appears in multiple datasets?
