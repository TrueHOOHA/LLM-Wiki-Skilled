---
type: concept
aliases: ["evaluator optimizer", "critique loop", "LLM evaluator loop"]
tags: [agent-engineering, evaluation, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Evaluator-Optimizer Workflow

## Definition
The Evaluator-Optimizer Workflow is an agentic workflow where one LLM generates an output and another evaluates it, feeding critique back into an iterative improvement loop.

## Scope
This concept fits tasks with clear evaluation criteria where iterative refinement demonstrably improves the result. Anthropic names literary translation and complex multi-round search as examples; for Hermes/Tolaria, the equivalent pattern would require explicit acceptance criteria, stop conditions, and evidence that another iteration improves correctness rather than just adding cost.

## Contrasts
- Versus one-shot generation: evaluator-optimizer spends extra latency and tokens to improve outputs through critique.
- Versus [[Orchestrator-Worker Workflow]]: evaluator-optimizer loops over one output; orchestrator-workers decompose a broader task into dynamic subtasks.
- Versus unbounded self-critique: the loop should have measurable criteria and stopping conditions.

## Evidence
- [[Alok Kumar X post on Building Effective Agents video and Anthropic agent patterns]] summarizes Anthropic's guidance that evaluator-optimizer works when clear evaluation criteria exist and human feedback can be articulated.
- [[Garry Tan Meta-Meta-Prompting and Tolaria Compounding Knowledge Proposal]] separately recommends Tolaria-specific evals for retrieval recall, citation faithfulness, stale-claim detection, human correction rate, and cost/latency before adoption of new workflows.
- [[Matt Pocock AI Hero skills changelog]] previews a related but more parallel review pattern: one lane checks coding standards, while another checks spec or PRD fidelity.

## Related
- [[Agentic Workflows and Agents]]
- [[Orchestrator-Worker Workflow]]
- [[Hermes Agent]]
- [[Graph-aware Retrieval Evals]]
- [[Anthropic]]
- [[Two-lane Agent Review]]
- [[AI Hero]]

## Open Questions
- Which Tolaria synthesis tasks have clear enough rubrics for evaluator-optimizer loops?
- What maximum iteration count and failure criteria would prevent evaluator loops from becoming expensive rituals?
