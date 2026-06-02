---
type: concept
aliases: ["system design roadmap", "system-design foundations", "system design topic map"]
tags: [system-design, distributed-systems, learning-roadmap]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# System Design Learning Taxonomy

## Definition
A System Design Learning Taxonomy is a coverage map for the concepts, tradeoffs, patterns, case studies, and practice problems used to learn scalable software-system design and prepare for system-design interviews.

## Scope
In the current Tolaria source, the taxonomy covers traditional system-design foundations: scalability, availability, reliability, single points of failure, latency/throughput/bandwidth, consistent hashing, CAP, failover, fault tolerance, networking, APIs, databases, caching, asynchronous communication, distributed systems, microservices, architecture patterns, tradeoffs, interview problems, courses, newsletters, books, engineering articles, and distributed-systems papers. It does not by itself prove correct prioritization, depth, or production relevance; each topic needs stronger primary sources before becoming guidance.

## Contrasts
- Versus [[AI Engineer Learning Roadmap Topic Map]]: this taxonomy is broader traditional system design and interview prep, while the AI roadmap focuses on LLM/RAG/eval/cost/reliability topics for AI systems.
- Versus [[System Design Interview Answering Framework]]: the taxonomy names what to learn; the framework names how to structure an interview answer.
- Versus production architecture guidance: a curated list points to resources but does not validate the correctness of any design choice.

## Evidence
- [[Awesome System Design Resources]] supplies the captured README section map and outbound-link counts for the topic categories.
- [[Awesome System Design Resources Source Map]] classifies which resource classes deserve future targeted ingestion versus archive-only treatment.

## Related
- [[AlgoMaster]]
- [[System Design Interview Answering Framework]]
- [[AI Engineer Learning Roadmap Topic Map]]
- [[Graph-aware Retrieval Evals]]
- [[Agentic Workflows and Agents]]

## Open Questions
- Which traditional system-design categories are worth backfilling with primary sources first: distributed-systems papers, company engineering case studies, databases/caching, networking/API fundamentals, or interview frameworks?
- Should Tolaria keep interview-prep practice prompts separate from production architecture concepts to avoid hardening interview heuristics into engineering guidance?
