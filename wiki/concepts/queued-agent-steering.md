---
type: concept
aliases: ["agent steering", "queued steering", "mid-run steering"]
tags: [agent-engineering, workflow, human-in-the-loop]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Queued Agent Steering

Queued Agent Steering is the pattern where a human adds intent while an agent is still working, so the next directions are queued after tool calls instead of waiting for the current step to finish.

## Definition

In [[Codex-maxxing]], steering lets [[Jason Liu]] comment while reviewing a website or artifact: make something smaller, fix copy, adjust spacing, open a PR, wait for preview deploy, or send a review link after the agent reaches that point. The mechanism turns voice or chat feedback into a queue of future instructions inside a [[Durable Agent Operating Loop]].

## Scope

Queued steering covers human-in-the-loop guidance during long-running agent work. It is especially useful when the human can see the artifact or external thread while the agent is mid-run. It does not remove the need for instruction priority, safety review, or explicit confirmation before irreversible side effects.

## Contrasts

- Versus synchronous prompting: the operator need not wait for each tool call to finish before shaping the next step.
- Versus autonomous planning: the human is still supplying intent and can correct the loop while it runs.
- Versus hidden memory updates: steering is task-local direction, not necessarily durable memory unless it captures a stable decision or preference.

## Evidence

- [[Codex-maxxing]] gives concrete steering examples for UI review, PR/deploy follow-through, and Slack handoff after work completes.
- [[Context Engineering]] is relevant because queued instructions can conflict with earlier goals unless priority and scope are explicit.
- [[Agent-Computer Interface Design]] is relevant because steering works best when the agent and human share a clear artifact/browser/tool surface.

## Related

- [[Durable Agent Operating Loop]]
- [[Artifact Review Surface]]
- [[Agent Heartbeat Loop]]
- [[Context Engineering]]
- [[Instruction Priority Control]]
- [[Hermes Agent]]

## Open Questions

- How should a system expose queued intent so the human can inspect, reorder, or cancel it before an agent acts?
- What queued instructions require explicit approval because they involve messages, purchases, credentials, file uploads, or external side effects?
