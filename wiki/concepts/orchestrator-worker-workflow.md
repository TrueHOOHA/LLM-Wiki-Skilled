---
type: concept
aliases: ["orchestrator-workers", "orchestrator worker pattern", "dynamic worker delegation"]
tags: [agent-engineering, orchestration, multi-agent]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Orchestrator-Worker Workflow

## Definition
The Orchestrator-Worker Workflow is an agentic workflow where a central LLM dynamically decomposes a task, delegates subtasks to worker LLMs, and synthesizes the worker outputs.

## Scope
This concept applies when subtasks cannot be predicted in advance but the overall work can still be bounded and reviewed. Anthropic's examples include complex coding changes across unknown files and search tasks that gather information from multiple sources. In Hermes, the analogous pattern appears in Kanban routing and subagent delegation, but any system changes remain approval-gated outside Tolaria knowledge work.

## Contrasts
- Versus parallelization: parallelization predefines subtasks or votes; orchestrator-workers decide subtasks dynamically.
- Versus a fully autonomous agent: the orchestrator-worker pattern can still operate inside explicit task boundaries, review gates, and stop conditions.
- Versus [[Thin Harness Fat Skills]]: orchestrator-workers describe runtime decomposition; thin-harness/fat-skills describes where durable behavior and domain knowledge should live.

## Evidence
- [[Alok Kumar X post on Building Effective Agents video and Anthropic agent patterns]] summarizes Anthropic's orchestrator-worker workflow and fit criteria.

## Related
- [[Agentic Workflows and Agents]]
- [[Evaluator-Optimizer Workflow]]
- [[Hermes Agent]]
- [[Thin Harness Fat Skills]]
- [[Anthropic]]

## Open Questions
- Which Tolaria/Hermes work types need dynamic decomposition, and which should stay as fixed Alpha/Beta workflows?
- What review evidence should an orchestrator collect before a worker output counts as complete?
