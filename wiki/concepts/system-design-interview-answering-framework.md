---
type: concept
aliases: ["seven-phase system design interview framework", "system design answering framework", "system design interview method"]
tags: [system-design, interviews, methodology]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# System Design Interview Answering Framework

## Definition
The System Design Interview Answering Framework is a seven-phase structure captured from the linked AlgoMaster interview page: requirements clarification, back-of-envelope estimation, API design, high-level design, database design, deep dives, and wrap-up.

## Scope
The framework is useful as an interview-answer scaffold. It helps a candidate move from problem framing to scale assumptions, interface contracts, architecture sketch, data model/storage decisions, selected bottleneck deep dives, and final tradeoff summary. It does not prove that this exact timing or ordering is universally optimal, nor does it replace source-specific technical knowledge about databases, queues, caches, distributed locks, consistency, observability, or failure modes.

## Contrasts
- Versus [[System Design Learning Taxonomy]]: the framework is process-oriented; the taxonomy is content-oriented.
- Versus [[AI Engineer Learning Roadmap Topic Map]]: this framework is traditional interview scaffolding and does not address LLM-specific concerns such as retrieval quality, hallucinations, model-routing, evals, or token costs unless the design prompt requires them.
- Versus production design review: the interview framework prioritizes communication and time-boxing; real production architecture requires evidence, constraints, migration planning, testing, and operational ownership.

## Evidence
- [[Awesome System Design Resources]] records the linked AlgoMaster page preview, including the seven phases and approximate time allocations: requirements clarification (5-7 minutes), back-of-envelope estimation (3-5 minutes), API design (3-5 minutes), high-level design (8-10 minutes), database design (5-7 minutes), deep dives (12-18 minutes), and wrap-up (3-5 minutes).
- [[Awesome System Design Resources Source Map]] treats this framework as the main concrete method-like artifact in an otherwise curated repository.

## Related
- [[AlgoMaster]]
- [[System Design Learning Taxonomy]]
- [[AI Engineer Learning Roadmap Topic Map]]
- [[Two-lane Agent Review]]
- [[Evaluator-Optimizer Workflow]]

## Open Questions
- Which interview phases map cleanly to Hermes/Codex design-review workflows, and which would need evidence from real engineering plans before any adaptation is proposed?
- Does the linked framework contain additional premium-only guidance beyond the captured phase list that would change Tolaria's classification?
