---
type: concept
aliases: ["agent memory platform", "AI memory control plane", "memory control plane for agents"]
tags: [agent-engineering, memory, knowledge-management]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent Memory Control Plane

## Definition
An Agent Memory Control Plane is a system layer that gives AI agents explicit operations for storing, retrieving, enriching, scoping, and deleting durable memory across sessions, datasets, users, and tools. [[Cognee]] is the current concrete example in Tolaria because it exposes `remember`, `recall`, `improve`, and `forget` around graph, vector, relational, session, and MCP memory surfaces.

## Scope
This concept covers memory APIs, storage topology, dataset/user ownership, provenance, session bridging, retrieval routing, feedback weighting, and deletion semantics. It does not mean that any vendor memory system should be adopted without independent evaluation, nor does it replace [[Memory Hygiene for AI Agents]]: a control plane can preserve bad memory faster if the source discipline is weak.

## Contrasts
- Versus [[File-backed Agent Memory]]: file-backed memory emphasizes inspectable markdown/files; a control plane emphasizes APIs, stores, retrieval, and lifecycle operations.
- Versus [[LLM Wiki Pattern]]: an LLM wiki is curated knowledge infrastructure; a memory control plane can ingest and retrieve operational agent state but may be less transparent if claims are hidden in embeddings or graph artifacts.
- Versus raw RAG: a control plane usually includes session scope, provenance, improvement, deletion, and graph relationships rather than only document chunk retrieval.
- Versus [[MCP Tool Connectors]]: MCP is one connector surface; the memory control plane is the backing lifecycle and retrieval model behind those tools.

## Evidence
- [[Cognee - Open Source Memory Platform for Agents]] documents a concrete memory API and storage/control pattern: `remember`, `recall`, `improve`, `forget`, session cache, dataset ownership, graph/vector/relational stores, MCP access, and feedback-aware improvement.
- [[Cognee Memory Architecture Patterns Assessment]] treats this as architecture evidence for Hermes/Tolaria design questions, not as implementation approval.

## Related
- [[Cognee]]
- [[Hybrid Graph-vector Agent Memory]]
- [[Session-to-Graph Memory Bridge]]
- [[Typed DataPoint Memory Model]]
- [[Memory Hygiene for AI Agents]]
- [[Compounding AI Knowledge Stack]]
- [[Hermes Agent]]

## Open Questions
- What minimum provenance, redaction, deletion, and audit guarantees should an agent memory control plane meet before it can hold operator or project memory?
- When should a memory operation remain human-curated markdown instead of entering an opaque or semi-opaque graph/vector store?
- Which task-specific evals best measure whether an agent memory control plane improves outcomes rather than only adding context volume?
