---
type: source
source_path: raw/sources/2026-05-29-work-with-codex-from-anywhere.md
title: "Work with Codex from anywhere"
author: "OpenAI"
date: 2026-05-29
tags: [openai, codex, agent-engineering, remote-control]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# Work with Codex from anywhere

## Summary
OpenAI's article announces Codex access from the ChatGPT mobile app, so a user can steer Codex work from a phone while execution remains on connected laptops, always-on Macs, SSH hosts, devboxes, or managed remote environments. The linked primary docs explain the mechanism: the phone sends prompts, follow-ups, approvals, and review actions through a secure relay; the connected host supplies files, credentials, permissions, plugins, MCP servers, browser/computer-use setup, local tools, and sandbox/approval controls. The same source cluster documents Business/Enterprise access tokens for non-interactive `codex exec` automation and lifecycle hooks for prompt scanning, validation, logging, memory creation, repo/directory customization, and policy enforcement. Evidence is medium: product/docs mechanisms are primary and concrete, but the article's adoption and productivity claims are not independently benchmarked. For Tolaria, the durable payload is a set of remote-control, identity, hook, and review-loop primitives relevant to [[Codex]], [[Hermes Agent]], and [[Durable Agent Operating Loop]].

## Key Claims
1. Codex in ChatGPT mobile can connect to host machines and let the user start or continue threads, answer questions, steer active work, approve actions, review outputs, switch hosts/threads, and receive notifications when Codex finishes or needs attention.
2. Execution remains host-bound: repository files, shell commands, plugins, MCP servers, skills, signed-in browser state, Computer Use, and local tools come from the connected host or SSH environment rather than the phone.
3. OpenAI describes a secure relay layer that keeps trusted machines reachable across authorized ChatGPT devices without exposing them directly to the public internet.
4. Remote SSH support lets the Codex App discover SSH hosts from concrete `~/.ssh/config` aliases, start a remote Codex app server through SSH, and run project threads on a remote filesystem and shell.
5. Programmatic Codex access tokens let trusted automation run Codex local under a ChatGPT workspace user identity for non-interactive `codex exec` jobs, but tokens are Business/Enterprise-scoped secrets that need least-privilege issuance, trusted runners, finite expiration, rotation, and auditability.
6. Codex hooks are an extensibility framework for lifecycle events such as `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SessionStart`, `SubagentStart`, `SubagentStop`, and `Stop`; they can inject context, block or allow supported actions, run validators, log sessions, and create memory.
7. Hook trust is not a complete enforcement boundary: multiple matching hooks can run concurrently; non-managed hooks require review/trust by hash; supported interception currently covers only specific tool paths; and post-tool hooks cannot undo side effects that already happened.
8. The article's broad productivity framing is plausible but unproven; Tolaria should preserve the workflow primitives without treating them as evidence that mobile steering or hooks improve outcomes in Hermes/Codex work.

## Notable Quotes
- "Your files, credentials, permissions, and local setup stay on the machine where Codex is operating, while updates flow back to your phone in real time, including screenshots, terminal output, diffs, test results, and approvals."
- "Under the hood, Codex uses a secure relay layer that keeps trusted machines reachable across devices without exposing them directly to the public internet."
- "Remote access uses the connected host's projects, threads, files, credentials, permissions, plugins, Computer Use, browser setup, and local tools."
- "Your phone sends prompts, approvals, and follow-up messages to Codex. The connected host provides the environment Codex uses."
- "Codex access tokens let trusted automation run Codex local with a ChatGPT workspace identity."
- "Hooks are an extensibility framework for Codex."

## Entities Mentioned
- [[OpenAI|OpenAI / ChatGPT]]
- [[Codex]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[Remote Agent Control]]
- [[Host-bound Agent Execution]]
- [[Workspace-scoped Automation Identity]]
- [[Agent Lifecycle Hooks]]
- [[Durable Agent Operating Loop]]
- [[Queued Agent Steering]]
- [[Agent Heartbeat Loop]]
- [[Artifact Review Surface]]
- [[Agent-Computer Interface Design]]
- [[Context Engineering]]
- [[Memory Hygiene for AI Agents]]

## Follow-ups
- Knowledge-only recommendation: preserve these as candidate Hermes/Codex workflow primitives, not as adopted defaults.
- Approval-gated proposal: if Overseer wants action later, evaluate a bounded remote-attention loop or hook-policy loop only after threat-modeling credential locality, host trust, notification failure, hook coverage gaps, access-token rotation, audit logging, and human approval boundaries.
- Open evidence gap: no independent benchmark here shows whether mobile approvals, secure relay, access tokens, or hooks reduce task latency, rework, missed approvals, security incidents, or human interruption cost.
