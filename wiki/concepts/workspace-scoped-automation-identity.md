---
type: concept
aliases: ["Codex access tokens", "workspace-scoped Codex access tokens", "automation identity for Codex"]
tags: [agent-engineering, security, automation, codex]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Workspace-scoped Automation Identity

## Definition
Workspace-scoped Automation Identity is the pattern where a trusted non-interactive agent or script runs under a bounded workspace/user identity rather than a generic platform API key or an ad hoc local browser login. In [[Work with Codex from anywhere]], OpenAI's Codex access-token docs describe Business/Enterprise tokens issued from ChatGPT workspace settings so `codex exec` automation can run Codex local with the creator's ChatGPT workspace identity and appear in workspace governance data.

## Scope
This concept covers non-interactive `codex exec` jobs, CI/release/internal automation identity, token ownership, workspace controls, auditability, and credential lifecycle. It does not cover general OpenAI Platform API calls, public CI/forked PR runners, shared service accounts without ownership, or any automatic adoption inside [[Hermes Agent]] without Overseer approval.

## Contrasts
- Versus Platform API keys: access tokens are specifically for Codex local workflows needing ChatGPT workspace access, ChatGPT-managed Codex entitlements, or enterprise workspace controls.
- Versus interactive OAuth/browser login: an access token can start non-interactive runs without a user completing a browser sign-in.
- Versus shared secrets: OpenAI's docs warn that one person's token reused across unrelated teams weakens ownership and audit trails.
- Versus [[Host-bound Agent Execution]]: this is the identity/authorization layer; host-bound execution is the file/tool/environment locality layer.

## Evidence
- [[Work with Codex from anywhere]] records OpenAI's access-token docs: tokens are tied to a ChatGPT user and workspace, checked when a run starts, and intended for trusted automation such as `codex exec` jobs, local scripts, CI, release workflows, or internal automations.
- The same source lists risks: leaked secrets, untrusted runners, shared identities, stale credentials, wrong credential type, and lack of finite expiration or rotation.
- [[Agent-Computer Interface Design]] and [[Memory Hygiene for AI Agents]] are adjacent because automation identity should be understandable to agents and operators, and should not leak into prompts, logs, wiki pages, or durable memory.

## Related
- [[Codex]]
- [[OpenAI]]
- [[Hermes Agent]]
- [[Host-bound Agent Execution]]
- [[Agent Lifecycle Hooks]]
- [[Agent-Computer Interface Design]]
- [[Memory Hygiene for AI Agents]]
- [[Security Mindset]]

## Open Questions
- If Overseer later approves Codex automation, should identity be per workflow, per host, per project, or per human operator?
- What minimum token controls would be required: secret manager storage, trusted runners only, finite expiration, rotation test, revocation path, redacted logs, and ownership metadata?
- How should Hermes distinguish Codex access tokens from OpenAI Platform API keys in prompts, docs, and operator workflows so the wrong credential type is not used?
