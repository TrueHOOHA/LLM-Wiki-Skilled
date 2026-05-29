---
type: concept
aliases: ["Heartbeats", "agent heartbeat", "recurring agent monitor"]
tags: [agent-engineering, monitoring, workflow, automation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent Heartbeat Loop

An Agent Heartbeat Loop is a recurring, thread-local agent schedule that checks for new external state and advances a bounded task until a condition is met or a human review gate is reached.

## Definition

In [[Codex-maxxing]], Heartbeats let a [[Codex]] thread check Slack/Gmail every 30 minutes, monitor feedback on PRs or Google Docs, watch Slack threads for video-review comments, or poll a support chat until an agent appears. The important pattern is recurrence plus task-local context: the loop remembers what it is monitoring and can adapt cadence after state changes.

## Scope

This concept covers recurring checks for messages, comments, PRs, previews, support chats, feedback threads, and other asynchronous work surfaces. It overlaps with cron, watchers, reminders, and Kanban heartbeats, but is narrower: it is tied to an agent workstream and should preserve its state in a durable task record or memory artifact. In Hermes/Beta, creating cron jobs or recurring automation is outside this card; only the knowledge pattern is preserved.

## Contrasts

- Versus scheduler-only cron: a heartbeat carries workstream context and may draft or decide next steps, not just run a fixed script.
- Versus one-time reminder: it can recur until a condition changes and adjust cadence.
- Versus autonomous execution: safe heartbeat loops still need approval boundaries for external messages, uploads, purchases/refunds, credentialed browser actions, and destructive changes.

## Evidence

- [[Codex-maxxing]] provides practitioner examples: Chief of Staff checks, Slack/Google Docs/PR feedback monitoring, animation re-render loops, and Amazon support polling.
- [[Durable Agent Operating Loop]] uses Heartbeats as the recurrence layer in the broader operating-loop pattern.
- [[Hermes Agent]] already has Kanban/cron/process heartbeat concepts, but translating this product pattern into Hermes automation would require explicit approval and evaluation.

## Related

- [[Durable Agent Operating Loop]]
- [[Queued Agent Steering]]
- [[Remote Agent Control]]
- [[Memory Hygiene for AI Agents]]
- [[Hermes Agent]]
- [[Chat Intake Kanban Mirror Pattern]]

## Open Questions

- Which heartbeat uses should be draft-only versus allowed to act after pre-approval?
- What audit trail is required for recurring loops that inspect email, Slack, browser sessions, or support chats?
- How should a heartbeat stop itself when the original task is done, stale, denied, or no longer worth the cost?
