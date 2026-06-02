---
type: source
source_path: raw/sources/2026-05-29-cognee-ai-memory-platform.md
title: "Cognee - Open Source Memory Platform for Agents"
author: "Cognee / topoteretes"
date: 2026-05-29
tags: [agent-engineering, memory, mcp, knowledge-graph]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# Cognee - Open Source Memory Platform for Agents

## Summary
Cognee is presented as an open-source memory platform for agents that turns documents, code, application data, decisions, and workflows into persistent AI memory. The source-backed mechanism is stronger than the adoption/performance claims: the captured docs and GitHub README describe a concrete memory API, storage architecture, MCP surface, DataPoint model, provenance context, and benchmark artifacts, while the product page and benchmark page remain vendor-authored. For Tolaria, Cognee is best preserved as a reference architecture for [[Agent Memory Control Plane]], [[Hybrid Graph-vector Agent Memory]], [[Session-to-Graph Memory Bridge]], and [[Typed DataPoint Memory Model]], not as an approved Hermes integration.

## Key Claims
1. Cognee exposes four primary v1.0 memory verbs: `remember`, `recall`, `improve`, and `forget`. `remember` ingests permanent graph-backed memory or fast session memory; `recall` auto-routes questions across session and graph retrieval; `improve` enriches existing graph memory and can bridge session memory into permanent memory; `forget` removes memory at item, dataset, user, or all-memory scope.
2. The architecture combines a relational store for documents/chunks/provenance, a vector store for semantic similarity, and a graph store for entities and relationships, producing both semantic search and structural retrieval paths.
3. Permanent `remember()` runs normalization, chunking, graph extraction, embedding, and an improvement pass; session `remember()` writes quickly to a session cache and only becomes permanent if self-improvement/bridging runs.
4. `recall()` is the recommended user-facing retrieval API: it can use session cache first, route by query pattern, return source-tagged results, fall through to graph-backed retrieval, and optionally return context only without generating or writing a new session QA entry.
5. `improve()` can perform graph enrichment, persist session Q&A, apply feedback weights to graph elements used in prior answers, and sync enriched graph context back into sessions.
6. Typed custom memory is modeled through Pydantic `DataPoint` classes; `PipelineContext` links inserted DataPoints to a user, dataset, and data item so provenance and dataset-scoped deletion can work.
7. Cognee MCP exposes memory management to MCP-compatible AI clients and supports standalone local mode or API mode against a centralized backend; the docs describe 14 specialized tools but this capture does not enumerate every tool in detail.
8. Cognee docs mention ontology support as external RDF/XML grounding for connecting domain data to established structures, but the capture is mechanism-level evidence rather than proof that ontology enrichment improves real agent outcomes.
9. Vendor evaluation pages and repo eval artifacts exist, including HotPotQA-subset comparisons against Mem0, Graphiti, and LightRAG, but they are not sufficient evidence for adoption: the benchmark is small, LLM-as-judge variance is noted, and Alpha observed a contradiction between broad vendor framing and repo summary details.

## Notable Quotes
- "Cognee turns documents, code, and application data into persistent AI memory that agents and applications can store, query, and improve over time." (captured docs `llms.txt`)
- "Cognee is an open source tool and platform that transforms your raw data into intelligent, searchable memory. It combines vector search with graph databases..." (core concepts overview)
- "Permanent memory: without `session_id` provided, `remember()` runs the full ingestion pipeline..." (remember docs)
- "Session memory: with `session_id`, `remember()` writes to the session cache for fast short-term memory." (remember docs)
- "Cognee combines three complementary storage systems" — relational, vector, and graph stores. (architecture docs)
- "When `ctx` carries all three values, each node and edge is tagged with `dataset_id` and `data_id` in the relational database." (custom data model docs)
- "Cognee MCP exposes 14 specialized tools through the MCP protocol." (MCP overview)

## Entities Mentioned
- [[Cognee]]
- [[Hermes Agent]]
- [[MCP Tool Connectors]]

## Concepts Mentioned
- [[Agent Memory Control Plane]]
- [[Hybrid Graph-vector Agent Memory]]
- [[Session-to-Graph Memory Bridge]]
- [[Typed DataPoint Memory Model]]
- [[Memory Hygiene for AI Agents]]
- [[Compounding AI Knowledge Stack]]
- [[Graph-aware Retrieval Evals]]

## Follow-ups
- Knowledge-only recommendation: use Cognee as a reference architecture and evaluation candidate for agent memory, not as an adopted component.
- Open evaluation question: if Overseer later approves non-knowledge work, compare Cognee-like memory against current Tolaria/Hermes memory for retrieval accuracy, provenance, staleness, deletion semantics, privacy, cost, latency, and operator control.
- Evidence caveat: performance claims should not be treated as validated until an independent, task-relevant memory benchmark is run.
