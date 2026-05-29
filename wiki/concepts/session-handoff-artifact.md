---
type: concept
aliases: ["handoff document", "session compaction", "context handoff"]
tags: [agent-engineering, context, skills, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Session Handoff Artifact

## Definition
A Session Handoff Artifact is a compact, durable document that lets another agent or future session continue work without replaying the full conversation. It should preserve the task focus, intent, current state, relevant artifacts, suggested skills, risks, and redaction requirements while avoiding duplicated content already captured in PRDs, plans, ADRs, commits, diffs, or issues.

## Scope
This concept covers transfer between long-context sessions, fire-and-forget helper agents, DIY sub-agent loops, and retry/resume handoffs. In Hermes, the analogous mechanisms already include Kanban comments, structured completion metadata, block reasons, worker-context injection, and optional progress/handoff templates; the AI Hero pattern adds a sharper artifact-reference rule and explicit suggested-skills section.

## Contrasts
- Versus raw transcript transfer: a handoff artifact selects task-relevant state instead of copying everything.
- Versus memory: handoff is task/session state and should not be promoted to durable profile memory unless it captures stable preference or environment knowledge.
- Versus Kanban completion metadata: completion metadata proves what was done; a handoff artifact helps another run decide what to do next.

## Evidence
- [[Matt Pocock AI Hero skills changelog]] includes the raw handoff skill excerpt requiring a temporary markdown file, suggested skills, artifact references instead of duplication, and sensitive-information redaction.

## Related
- [[Hermes Agent]]
- [[AI Hero]]
- [[Thin Harness Fat Skills]]
- [[Memory Hygiene for AI Agents]]
- [[Orchestrator-Worker Workflow]]

## Open Questions
- Should Overseer approve a future review of Hermes Kanban handoff templates against the AI Hero artifact-reference and suggested-skills rules?
- Which fields are mandatory for a Hermes handoff: task objective, current state, artifacts, tests/checks, decisions, risks, credentials omitted, suggested skills, or next action?
