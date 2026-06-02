---
type: concept
aliases: ["chat intake to Kanban mirror", "Discord Kanban bridge", "chat-to-kanban system of record pattern"]
tags: [agent-engineering, hermes, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Chat Intake Kanban Mirror Pattern

## Definition
Chat Intake Kanban Mirror Pattern is an agent-orchestration workflow where a chat surface accepts conversational commands, a Kanban system remains the durable system of record for task identity, assignment, execution, status, logs, and proof of work, and the chat surface receives mirrored status updates for operator visibility.

## Scope
This concept covers the boundary between conversational intake and durable execution state. In the JUMPERZ source, Discord is the proposed chat layer and [[Hermes Agent]] Kanban is the proposed system of record. The pattern is useful only if there is one authoritative task identity, one authoritative status lifecycle, and an auditable path from chat request to Kanban task to completion evidence. It does not imply that Discord or any chat task board should own task truth, worker assignment, proof of work, or retry state.

## Contrasts
- Versus chat-only orchestration: chat is convenient for intake and mobile visibility, but it is weak as the only audit ledger for assignment, retries, logs, and completion proof.
- Versus native synchronization: the current source explicitly says Discord and Hermes Kanban do not sync natively out of the box; any bridge would be custom and approval-gated.
- Versus [[Orchestrator-Worker Workflow]]: orchestrator-worker describes dynamic task decomposition; chat-intake/Kanban-mirror describes the operator interface and state-boundary layer around task execution.
- Versus [[Agentic Workflows and Agents]]: the pattern can support fixed workflows, worker dispatch, or autonomous agents, but it is not itself evidence that more autonomy is warranted.

## Evidence
- [[JUMPERZ X post on Hermes Kanban + Discord task-board bridge]] frames Discord as the place to talk to the system and Hermes Kanban as the place that assigns, tracks, runs, logs, and proves work. Evidence grade is weak/social: screenshots illustrate the idea but do not provide implementation details.

## Risks and Design Checks
- Duplicate-state drift: Discord-visible task status can diverge from Hermes Kanban if the mirror fails, races, or retries incorrectly.
- Identity mapping: every mirrored task needs a stable Hermes task ID and a clear mapping to a Discord message, channel, thread, card, or user command.
- Permission boundaries: chat users should not gain task-creation, approval, or execution powers beyond their intended roles.
- Auditability: Hermes Kanban should remain the durable ledger for task state, worker handoffs, logs, and proof; chat should be treated as a view or intake queue.
- Mobile visibility: chat mirroring can be valuable for quick supervision, but convenience should not override review gates or source-of-truth boundaries.
- Failure recovery: bridge downtime, duplicate messages, deleted Discord objects, and partial task creation need deterministic handling before adoption.

## Related
- [[Hermes Agent]]
- [[Agentic Workflows and Agents]]
- [[Orchestrator-Worker Workflow]]
- [[Agent-Computer Interface Design]]
- [[Thin Harness Fat Skills]]

## Open Questions
- Should Overseer later approve a small bridge evaluation that keeps Hermes Kanban authoritative and tests only intake/mirror behavior before any production use?
- What should the first approved evaluation optimize for: mobile visibility, task identity mapping, permission safety, drift detection, auditability, or operator latency?
- Which events, if any, should be mirrored back to chat: task created, claimed, heartbeat, blocked, completed, failed, review-required, or all state changes?
