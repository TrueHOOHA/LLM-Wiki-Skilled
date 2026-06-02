---
type: concept
aliases: ["ready-for-agent-triage", "agent-ready issue labeling", "agent triage label"]
tags: [agent-engineering, orchestration, workflow]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent-ready Triage Labeling

## Definition
Agent-ready Triage Labeling is a workflow convention where generated PRDs or issues are labeled to indicate they are ready for agent execution or triage, rather than being treated as unresolved human intake.

## Scope
The AI Hero changelog says `/to-prd` and `/to-issues` changed from `needs-triage` to `ready-for-agent-triage`. The reusable idea is not the exact label string but the state distinction: generated tasks can either require human triage, be ready for agent triage, or be ready for direct execution. Hermes Kanban already encodes related state through ready/running/blocked/review-required semantics, so this source is mostly a reference unless a future cross-system label mapping is approved.

## Contrasts
- Versus `needs-triage`: agent-ready labels imply the issue is sufficiently specified for agent-side planning or decomposition.
- Versus direct execution: agent-ready triage can still require an agent to inspect scope, prerequisites, and acceptance criteria.
- Versus chat intake: labels should map to the durable task system of record, not just chat visibility.

## Evidence
- [[Matt Pocock AI Hero skills changelog]] records the label change and frames generated issues as ready for agents without additional triage.

## Related
- [[Hermes Agent]]
- [[Chat Intake Kanban Mirror Pattern]]
- [[Orchestrator-Worker Workflow]]
- [[AI Hero]]

## Open Questions
- Should a future approved GitHub/Kanban integration map external labels like `ready-for-agent-triage` into Hermes Kanban statuses or priorities?
- What acceptance criteria distinguish human-triage, agent-triage, and ready-for-execution tasks?
