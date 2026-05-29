---
type: concept
aliases: ["agentic systems", "workflows vs agents", "LLM workflows", "autonomous agents"]
tags: [agent-engineering, orchestration, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agentic Workflows and Agents

## Definition
Agentic Workflows and Agents is the architectural distinction between LLM systems that follow predefined code paths and systems where an LLM dynamically controls its own process and tool use. Anthropic calls both "agentic systems," but separates predictable workflows from more autonomous agents.

## Scope
This concept covers the decision boundary for when to use a single LLM call, a structured workflow, or an autonomous agent. It includes Anthropic's advice to start with the simplest solution, add complexity only when evaluation shows a need, and reserve agents for open-ended tasks where the steps cannot be predicted or hardcoded.

## Contrasts
- Versus a single augmented LLM call: workflows and agents add latency, cost, and coordination overhead; a retrieval-augmented prompt may be enough for many tasks.
- Versus [[Orchestrator-Worker Workflow]]: orchestrator-workers are a flexible workflow pattern; they are not automatically full autonomous agents.
- Versus unrestricted autonomy: agents need sandboxed testing, guardrails, stopping conditions, and human checkpoints.

## Evidence
- [[Alok Kumar X post on Building Effective Agents video and Anthropic agent patterns]] summarizes Anthropic's distinction between workflows and agents and its simplest-solution-first recommendation.

## Related
- [[Anthropic]]
- [[Hermes Agent]]
- [[Orchestrator-Worker Workflow]]
- [[Evaluator-Optimizer Workflow]]
- [[Agent-Computer Interface Design]]
- [[Thin Harness Fat Skills]]

## Open Questions
- Which Hermes/Alpha/Beta tasks are structured enough for predefined workflows, and which genuinely require model-directed autonomy?
- What measured failure rate, latency, or human-review burden should trigger moving from a simple workflow to an agentic loop?
