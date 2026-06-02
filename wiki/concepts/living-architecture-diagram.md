---
type: concept
aliases: ["living architecture diagrams", "agent-maintained architecture diagram", "architecture diagram as control surface"]
tags: [agent-engineering, architecture, code-review, workflows]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Living Architecture Diagram

## Definition
A Living Architecture Diagram is an explicitly maintained, human-readable representation of a software system's boundaries, data flow, high-level components, constraints, patterns, abstractions, APIs, and interfaces. In the current Tolaria evidence, it is proposed as a control surface for agent-generated codebases: humans use it to steer and review the system at architectural altitude while agents keep file-level implementation moving.

## Scope
This concept covers architecture diagrams that are maintained during development rather than produced once as static documentation. For agent-written codebases, the diagram is valuable only if it stays synchronized with actual system decisions and critical interfaces. The source hypothesis is that a CTO or reviewer should understand this diagram deeply before delegating more file-level work to agents.

## Contrasts
- Versus static architecture documentation: a living diagram must be updated as agents add components, data flows, dependencies, and boundary changes.
- Versus file-level code review: it summarizes system meaning and control points rather than line-by-line implementation details.
- Versus [[Session Handoff Artifact]]: a handoff captures task/session continuity; a living architecture diagram captures persistent system structure.
- Versus [[Agent-Computer Interface Design]]: ACI is about interfaces between agents and tools; a living architecture diagram is about interfaces within the produced software system.

## Evidence
- [[Chrys Bader X post on agent-written codebases and living architecture diagrams]] proposes living architecture diagrams as a remedy for unintelligible agent-made codebases, but supplies only anecdotal social evidence and an explanatory infographic.

## Related
- [[Multi-altitude Agent Code Review]]
- [[Agent-Computer Interface Design]]
- [[Two-lane Agent Review]]
- [[Thin Harness Fat Skills]]
- [[Context Engineering]]
- [[Hermes Agent]]

## Open Questions
- What minimal diagram schema would be useful without becoming stale busywork: boundaries, data flow, components, dependencies, critical interfaces, invariants, ownership, risks, or test surfaces?
- Can agents reliably update architecture diagrams from their own code changes, or does that need human review gates?
- Which evidence would prove value: fewer review corrections, faster onboarding, lower rework, better spec fidelity, fewer interface breaks, or easier incident/debug sessions?
