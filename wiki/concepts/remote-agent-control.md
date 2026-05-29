---
type: concept
aliases: ["remote Codex control", "mobile agent steering", "work with agents from anywhere"]
tags: [agent-engineering, remote-control, human-in-the-loop]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# Remote Agent Control

Remote Agent Control is the ability to review, steer, approve, or unblock an agent running on the machine where the relevant files, credentials, permissions, and local environment already live.

## Definition

In [[Codex-maxxing]], remote control lets [[Jason Liu]] start [[Codex]] on the work machine, leave, and later check in from mobile to answer a question, approve the next step, or change direction. [[Work with Codex from anywhere]] provides stronger primary-doc support for the product mechanism: ChatGPT mobile can send prompts, follow-ups, and approvals while the connected host supplies projects, threads, files, credentials, permissions, plugins, MCP servers, browser setup, Computer Use, local tools, sandboxing, and action approvals through a secure relay.

## Scope

This concept covers mobile review/unblock loops, secure relays, approval prompts, remote access to local artifacts, and preservation of host-local state. It does not imply that credentials should be copied into chat, that an agent can bypass approval gates, or that remote control is safer than local operation without threat-model review.

## Contrasts

- Versus cloud-only agents: remote control can keep execution near the user's trusted local setup and files.
- Versus local-only unattended runs: the human can intervene away from the desk.
- Versus arbitrary remote desktop control: useful agent remote control needs scoped approvals, audit logs, and clear separation between review, steering, and action.

## Evidence

- [[Codex-maxxing]] provides the practitioner rationale for portable steering of long-running Codex tasks.
- [[Work with Codex from anywhere]] provides primary OpenAI docs evidence for mobile/remote control, host-bound execution, secure relay reachability, SSH host routing, notifications, diffs/test-output/screenshot review, and action approvals.
- [[Codex Remote/mobile Workflow Primitives for Hermes Assessment]] grades the mechanism as useful proposal material but not as proof of productivity or safety outcomes.
- [[Durable Agent Operating Loop]] treats remote control as the unblock/review layer in a larger workstream loop.
- [[Agent Heartbeat Loop]] becomes more useful when remote review can respond to decision points without waiting for the operator to return to the original machine.
- [[0xSero tweet on AImaxing tool list]] places Termius, Codex/ChatGPT, and kittylitter under mobile control. The tweet is weak evidence for tool choice, but it independently reinforces the category that remote/mobile steering is now a visible part of agent workflows.

## Related

- [[Durable Agent Operating Loop]]
- [[Queued Agent Steering]]
- [[Agent Heartbeat Loop]]
- [[Agent-Computer Interface Design]]
- [[Hermes Agent]]
- [[Codex]]
- [[Host-bound Agent Execution]]
- [[Workspace-scoped Automation Identity]]
- [[Agent Lifecycle Hooks]]

## Open Questions

- What approvals and audit records are required before a remote agent can act on local files, terminals, browsers, or authenticated services?
- Which local-vs-cloud execution boundary best protects host-local credentials while still allowing mobile review?
