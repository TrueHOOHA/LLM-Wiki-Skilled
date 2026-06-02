---
type: concept
aliases: ["graph-aware retrieval", "retrieval evals", "resolver evals"]
tags: [retrieval, evaluation, knowledge-management]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# Graph-aware Retrieval Evals

## Definition
Graph-aware retrieval evals measure whether a knowledge system can retrieve not only lexically similar documents but also related entity, backlink, timeline, and graph-neighbor context needed to answer real questions.

## Scope
The concept covers retrieval recall, resolver reachability, citation accuracy, stale-claim detection, and human correction rates. It does not by itself validate productivity or answer quality unless tied to task-level evals.

## Contrasts
- Plain vector retrieval optimizes semantic similarity.
- Graph-aware retrieval also weights entity links, backlinks, timelines, and relationship edges.
- Resolver evals check whether a workflow can be found and invoked, not just whether a note exists.
- [[Persistent Agent Memory Evaluation]] extends graph-aware retrieval evaluation into session continuity, update/forget behavior, provenance, and memory-scope safety.

## Evidence
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] cites GBrain-evals retrieval-recall results and recommends trigger/reachability checks for skills and resolvers.
- [[Cognee AI Memory Platform, Evals, and Case-study Claims]] supplies a cautionary vendor-eval case: graph/vector memory systems need metrics beyond EM/F1, but small HotPotQA/LLM-judge benchmarks can still overstate claims or hide contradictions between metric families.
- [[adxtyahq X post on RAG pipeline for 10M docs]] is weak social evidence, but its checklist usefully broadens the eval map for large-corpus RAG: hybrid retrieval, reranking, source confidence, citation support, abstention thresholds, adversarial queries, cache/memory invalidation, and observability should be evaluated separately.

## Related
- [[GBrain]]
- [[LLM Wiki Pattern]]
- [[Compounding AI Knowledge Stack]]
- [[Skillify]]
- [[Persistent Agent Memory Evaluation]]
- [[Memory Hygiene for AI Agents]]

## Open Questions
- What gold query set would represent Tolaria's real retrieval and synthesis workload?
- Which graph-aware retrieval failures should be separated in evals: missing entity-neighbor context, missing source provenance, stale graph edges, weak citations, or wrong cross-session memory reuse?
