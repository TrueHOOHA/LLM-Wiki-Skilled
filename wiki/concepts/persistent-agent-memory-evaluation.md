---
type: concept
aliases: ["AI memory evals", "persistent memory benchmark", "agent memory benchmark", "memory-system evaluation"]
tags: [agent-memory, evaluation, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Persistent Agent Memory Evaluation

## Definition
Persistent Agent Memory Evaluation is the practice of testing whether an AI memory system can store, update, retrieve, connect, and safely forget useful context across sessions, documents, users, tools, and tasks. It is broader than ordinary QA accuracy because real memory systems must preserve provenance, handle stale or contradictory information, respect scope, and retrieve context when the next task arrives.

## Scope
This concept covers multi-session recall, source provenance, graph/vector retrieval, forgetting/deletion boundaries, LLM-as-judge variance, human-style correctness checks, and benchmark mismatch. It does not imply that a vendor memory platform is production-ready just because it performs well on a small multi-hop QA subset.

## Contrasts
- Versus HotPotQA-only evaluation: HotPotQA tests constrained multi-hop reasoning, but not long-lived session memory, permission scopes, source drift, forgetting, or operational updates.
- Versus EM/F1: exact-match and token-overlap metrics can underrate paraphrased correct answers and overrate surface matches that miss the actual memory task.
- Versus LLM-as-judge: semantic judging helps but adds model variance, prompt sensitivity, and possible vendor-controlled evaluation bias.
- Versus case studies: customer narratives can show possible use cases, but they do not replace reproducible benchmarks or independently measured outcomes.

## Evidence
- [[Cognee AI Memory Platform, Evals, and Case-study Claims]] provides the current cautionary example: Cognee's public eval artifacts are useful, but the research page overstates a "most human-like" conclusion relative to the repo chart where LightRAG has higher Human-like Correctness.
- [[Graph-aware Retrieval Evals]] already captures the need to evaluate graph-neighbor/entity/backlink retrieval rather than only lexical similarity; persistent memory evals add session, provenance, update, and forgetting dimensions.
- [[Memory Hygiene for AI Agents]] supplies the operational discipline that memory evals should test: what gets preserved, excluded, corrected, and surfaced later.

## Related
- [[Cognee]]
- [[Graph-aware Retrieval Evals]]
- [[Memory Hygiene for AI Agents]]
- [[Context Engineering]]
- [[MCP Tool Connectors]]
- [[Long-running Agent Harness]]

## Open Questions
- What Tolaria/Hermes task set best represents persistent memory: Alpha source routing, Beta citation faithfulness, Kanban handoff recall, project convention recall, stale-memory rejection, or forgetting/scope enforcement?
- Which metric should dominate a future approved eval: task success, citation faithfulness, stale-claim detection, human correction rate, retrieval recall, deletion compliance, latency, or cost?
