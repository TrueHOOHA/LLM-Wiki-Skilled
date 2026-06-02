---
type: concept
aliases: ["host/device separation", "host-local agent execution", "remote host agent execution"]
tags: [agent-engineering, remote-control, security, workflow]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Host-bound Agent Execution

## Definition
Host-bound Agent Execution is the pattern where a remote or mobile control surface sends instructions, approvals, and review actions while the agent's actual execution remains on the trusted host that owns the relevant files, shell, credentials, plugins, MCP servers, browser state, computer-use setup, sandboxing, and local tools. [[Work with Codex from anywhere]] is the primary current Tolaria source: OpenAI frames ChatGPT mobile as the steering surface and the connected Mac, always-on host, SSH host, devbox, or managed environment as the execution boundary.

## Scope
This concept covers local/remote host routing, mobile steering, SSH/devbox execution, secure relay reachability, and the distinction between control-plane messages and data/tool locality. It does not prove that a relay is safe for every threat model, that host-local credentials are automatically protected from prompt injection, or that Hermes should expose any new remote-control path without separate approval.

## Contrasts
- Versus cloud-only execution: files, credentials, signed-in browser sessions, and tools remain on a host already configured for the project.
- Versus raw remote desktop: the remote surface is oriented around agent threads, approvals, diffs, test output, screenshots, and action review rather than full interactive desktop control.
- Versus unattended local automation: the human can steer and approve away from the original keyboard, but side effects still happen in the host environment.
- Versus [[Workspace-scoped Automation Identity]]: host-bound execution is about where the work runs; workspace-scoped identity is about which organizational/user identity authorizes non-interactive runs.

## Evidence
- [[Work with Codex from anywhere]] says Codex mobile uses host projects, threads, files, credentials, permissions, plugins, Computer Use, browser setup, local tools, sandboxing, security controls, and action approvals.
- [[Remote Agent Control]] captures the human-in-the-loop review/unblock layer built on top of this host/device separation.
- [[Durable Agent Operating Loop]] uses host-bound execution as one way to keep long-running agent work available without moving all credentials or project state into a cloud-only surface.

## Related
- [[Remote Agent Control]]
- [[Codex]]
- [[OpenAI]]
- [[Hermes Agent]]
- [[Durable Agent Operating Loop]]
- [[Agent-Computer Interface Design]]
- [[Workspace-scoped Automation Identity]]
- [[Agent Lifecycle Hooks]]

## Open Questions
- Which host classes are acceptable for Overseer's workflows: daily laptop, always-on Mac, SSH devbox, disposable worktree host, or managed cloud dev environment?
- What host health checks are required before remote steering is trustworthy: awake/online status, correct workspace/account, sandbox mode, repo cleanliness, secrets policy, hook trust, and audit logging?
- How should a system distinguish safe mobile review actions from actions that require returning to the primary workstation?
