---
type: entity
aliases: ["Cognee", "Topoteretes Cognee", "cognee"]
tags: [agent-memory, knowledge-graph, mcp]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Cognee

## Identity
Cognee is an open-source memory platform and managed cloud product for AI agents that stores, retrieves, improves, and deletes agent memory through a hybrid graph/vector/relational architecture. In Tolaria it is a concrete [[Agent Memory Control Plane]] and [[Hybrid Graph-vector Agent Memory]] reference architecture plus a cautionary [[Persistent Agent Memory Evaluation]] case, not an approved [[Hermes Agent]] integration.

## Aliases
- Cognee
- Topoteretes Cognee
- cognee

## Key Attributes
| Attribute | Current evidence |
|---|---|
| Category | AI agent memory platform / knowledge-graph memory system |
| Core operations | `remember`, `recall`, `improve`, `forget` |
| Storage model | Relational provenance/storage plus vector and graph stores for retrieval |
| Memory modes | Session cache for fast short-term memory; permanent graph memory for durable indexed retrieval |
| Agent access | SDK/CLI plus MCP server surface with memory tools |
| Structured-memory model | Custom typed DataPoints and PipelineContext-style dataset/data/user provenance |
| Architecture patterns | [[Agent Memory Control Plane]], [[Hybrid Graph-vector Agent Memory]], [[Session-to-Graph Memory Bridge]], [[Typed DataPoint Memory Model]] |
| Evaluation claim | Vendor benchmark over 24 HotPotQA questions and 45 runs; Cognee leads DeepEval metrics but not the public chart's Human-like Correctness metric |
| Evidence caveat | Vendor-authored docs/evals/case studies; benchmark is small and not a complete persistent-agent-memory eval |

## Evidence
- [[Cognee - Open Source Memory Platform for Agents]] preserves the source-backed architecture mechanisms: memory verbs, session/permanent memory modes, hybrid graph/vector/relational stores, typed DataPoints, PipelineContext provenance, MCP memory tools, and ontology grounding.
- [[Cognee Memory Architecture Patterns Assessment]] maps those mechanisms into Tolaria architecture concepts while explicitly avoiding adoption or integration.
- [[Cognee AI Memory Platform, Evals, and Case-study Claims]] records the captured benchmark and case-study source cluster and grades claims by evidence strength.
- [[Cognee Memory and Evaluation Claims Assessment]] separates Cognee's useful evaluation lessons from unsupported adoption and performance claims.

## Related
- [[Agent Memory Control Plane]]
- [[Hybrid Graph-vector Agent Memory]]
- [[Session-to-Graph Memory Bridge]]
- [[Typed DataPoint Memory Model]]
- [[Persistent Agent Memory Evaluation]]
- [[Memory Hygiene for AI Agents]]
- [[Graph-aware Retrieval Evals]]
- [[MCP Tool Connectors]]
- [[Hermes Agent]]
- [[Codex]]

## Open Questions
- Can Cognee's eval harness be reproduced independently on larger persistent-memory tasks rather than only a 24-question HotPotQA subset?
- Which Cognee primitives, if any, are useful as design inspiration for Tolaria without importing a runtime dependency?
- If Overseer later approves any non-knowledge work, should the first comparison evaluate Cognee-style memory against Tolaria wiki/qmd/Hermes baselines on provenance, deletion, stale facts, redaction, retrieval quality, latency, cost, and operator auditability?
