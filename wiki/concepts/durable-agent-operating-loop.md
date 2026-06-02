---
type: concept
aliases: ["durable agent loop", "agent operating loop", "long-running agent workstream"]
tags: [agent-engineering, workflow, codex, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 4
---

# Durable Agent Operating Loop

A Durable Agent Operating Loop is a long-running agent workstream where continuity, steering, memory, tool access, review surfaces, and verification let the work keep moving across human attention gaps instead of ending at one prompt/answer exchange.

## Definition

A Durable Agent Operating Loop combines a persistent thread or task record, high-context inputs, queued steering, explicit memory artifacts, computer/browser/connectors, remote review/unblock ability, scheduled monitoring, and success criteria. In [[Codex-maxxing]], [[Jason Liu]] frames this as the reason [[Codex]] starts to feel like a place where work lives, not only a tool that edits code.

## Scope

This concept covers agentic knowledge work and coding work that needs continuity: PR monitoring, Slack/Gmail triage drafts, feedback loops, artifact review, presentations, local apps, customer support, and long-running migration goals. It does not mean the agent should act without approvals, send messages autonomously, take over credentials, or replace the canonical system of record. In [[Hermes Agent]], the analogous system-of-record layer is still Kanban/Tolaria, with approval-gated proposals for non-knowledge changes.

## Contrasts

- Versus one-shot prompting: a loop persists state, has scheduled or resumed checks, and can be steered after intermediate tool calls.
- Versus raw long chat history: durable loops externalize reusable memory into files or knowledge notes, aligning with [[File-backed Agent Memory]] and [[Memory Hygiene for AI Agents]].
- Versus autonomous cron: Heartbeats and schedules are useful only when coupled to scope, review boundaries, and explicit success criteria.
- Versus [[Long-running Agent Harness]]: the operating loop is the broad supervised workstream; the harness is the task-local continuity scaffold of ledgers, logs, restart scripts, commits, and verification gates.
- Versus code-only agents: the loop can operate over artifacts, browsers, slides, spreadsheets, PDFs, Slack/Gmail/calendar, or GUI surfaces.

## Evidence

- [[Codex-maxxing]] is the direct practitioner source: durable threads, voice input, steering, memory, computer/browser use, remote control, Heartbeats, Goals, and side panel form the operating loop.
- [[Effective Harnesses for Long-running Agents]] adds strong primary Anthropic evidence for the code-work variant: a first-session initializer, later one-feature coding agents, JSON feature ledger, progress file, git history, init script, and end-to-end verification.
- [[Work with Codex from anywhere]] adds primary OpenAI docs support for several surrounding primitives: mobile steering, host-bound execution, secure relay reachability, SSH/devbox routing, workspace-scoped automation identity, hooks, notifications, and review of diffs/test output/screenshots.
- [[Codex Remote/mobile Workflow Primitives for Hermes Assessment]] keeps those primitives proposal/eval-scoped rather than treating them as proof of better outcomes.
- [[Codex-maxxing Durable Operating Loop Assessment]] grades the overall pattern as a strong concept map but weak-to-medium evidence for productivity outcomes.
- [[Codex Sequential TDD Workflow]] is adjacent for code-specific task cadence, but durable operating loops are broader than sequential coding work.
- [[KingBootoshi tweet on Codex 5.5 goal escape hatch]] adds a weak social hypothesis that durable goal loops should include explicit [[Agent Escape Hatch]] status markers so impossible or damaging subgoals do not become hallucinated success or poisoned progress state.
- [[Compounding AI Knowledge Stack]] and [[Context Engineering]] provide existing Tolaria frames for why explicit state and curated context can compound.

## Related

- [[Codex]]
- [[Jason Liu]]
- [[Queued Agent Steering]]
- [[Agent Heartbeat Loop]]
- [[File-backed Agent Memory]]
- [[Remote Agent Control]]
- [[Host-bound Agent Execution]]
- [[Workspace-scoped Automation Identity]]
- [[Agent Lifecycle Hooks]]
- [[Long-running Agent Harness]]
- [[Artifact Review Surface]]
- [[Context Engineering]]
- [[Agent-Computer Interface Design]]
- [[Hermes Agent]]
- [[Agent Escape Hatch]]

## Open Questions

- Which Hermes/Codex work classes benefit most from durable loops: Tolaria ingestion, code review, PR follow-up, customer/inbox triage, web research, or artifact generation?
- What minimum review and approval gates are needed before a heartbeat loop can monitor external services or draft responses safely?
- What metric should decide whether continuity is worth the added cost: fewer restarts, fewer missed loops, better citation/spec fidelity, lower human interruption count, or faster turnaround?
- In a bounded eval, which continuity artifact contributes most: feature ledger, progress log, git history, init script, or user-like verification?
- Should durable loops require a bounded incomplete/escape-hatch marker before they can skip, defer, or stop a subgoal?
