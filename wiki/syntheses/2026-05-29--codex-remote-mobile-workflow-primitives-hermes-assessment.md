---
type: synthesis
question: "Which Codex remote/mobile, access-token, and hook primitives should Tolaria preserve for Hermes/Codex workflow proposals?"
tags: [agent-engineering, codex, remote-control, security, workflow]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Codex Remote/mobile Workflow Primitives for Hermes Assessment

Strongest counterargument first: [[Work with Codex from anywhere]] is primary OpenAI product/documentation evidence, not proof that mobile steering, secure relays, access tokens, or hooks improve software outcomes. It gives concrete mechanisms and constraints, but no independent benchmark, failure-rate study, user-interruption analysis, security audit, or before/after Hermes/Codex comparison. Confidence is medium that the documented Codex product primitives exist as described; confidence is low-to-medium that adopting analogous primitives would improve Overseer's workflows without adding credential, notification, audit, or stale-context risk.

## Question / Purpose
Assess OpenAI's Codex mobile/remote article and linked docs as knowledge-only input for [[Hermes Agent]], [[Codex]], and Tolaria. Extract source-backed primitives, security/failure modes, evidence limits, and approval-gated proposal options without creating code, hooks, tokens, cron jobs, config changes, skill patches, media, slides, or follow-up Kanban tasks.

## Answer / Analysis
- The durable pattern is not "use your phone for coding"; it is host/device separation: mobile sends intent and approvals while trusted hosts retain files, credentials, shells, MCP servers, browser/computer state, local tools, sandboxing, and policy.
- The secure-relay model matters because it keeps hosts reachable from authorized ChatGPT devices without directly exposing host services to the public internet, but the source does not provide a relay threat model or audit.
- Mobile approvals are useful only if they reduce decision latency without weakening review; the source's primitives should be evaluated around unblock time, diff/test visibility, wrong approval risk, and notification reliability.
- SSH/devbox host routing suggests a clean boundary for long-running Codex work: run in the environment that already owns dependencies, compute, policies, and credentials rather than copying context into an unrelated agent surface.
- Workspace-scoped Codex access tokens are a useful automation-identity primitive for trusted `codex exec` jobs, but they are also high-value secrets; leaked, shared, stale, or wrong-scope tokens would damage auditability and safety.
- Codex hooks are the most reusable policy/validation primitive: prompt secret scanning, permission checks, post-tool review feedback, stop-time validators, logging, and memory proposals. They are not a complete enforcement boundary because coverage is incomplete and post-tool hooks cannot undo side effects.
- For Hermes/Alpha/Beta/Tolaria, the safest interpretation is proposal material: preserve the primitives, then require Overseer approval and a bounded eval before any implementation.

## Source Map
| Source | Role | Evidence grade | Notes |
|---|---|---|---|
| [[Work with Codex from anywhere]] | Primary OpenAI article plus linked docs | Medium for product mechanisms; low-to-medium for outcome claims | Direct source for mobile control, secure relay, SSH host routing, access tokens, hooks, availability, and caveats. |
| [[Codex-maxxing]] | Practitioner workflow neighbor | Medium self-report; low-to-medium generalization | Supplies operator rationale for durable Codex workstreams, remote control, heartbeats, and artifact review. |
| [[Codex-maxxing Durable Operating Loop Assessment]] | Existing Tolaria synthesis | Medium as Tolaria synthesis | Places remote control inside a broader durable operating-loop model. |
| [[Codex Sequential TDD Workflow]] | Existing Codex cadence concept | Weak-to-medium hypothesis | Useful for coding-task cadence; remote/mobile primitives mainly affect attention, identity, and policy boundaries. |

## Evidence Grades
| Claim | Grade | Assessment |
|---|---|---|
| Codex mobile can steer work on connected host machines and review outputs/diffs/tests/screenshots. | Medium | Primary docs/article mechanism; no independent outcome data. |
| Files, credentials, permissions, plugins, MCP servers, browser setup, Computer Use, sandboxing, and tools remain host-bound. | Medium-high as documented mechanism | Strongly stated in the docs; actual safety depends on host trust and agent/tool behavior. |
| Secure relay avoids directly exposing hosts to the public internet. | Medium | Primary docs state the architecture at high level; no threat model or audit in captured source. |
| SSH/devbox routing lets Codex operate in approved remote environments. | Medium | Concrete docs: SSH config aliases, remote app server via SSH, remote filesystem/shell; still requires normal SSH security and no exposed app server transports. |
| Access tokens are appropriate for trusted non-interactive Codex local automation. | Medium | Primary docs define scope and risks; only available for Business/Enterprise and not a general Platform API key replacement. |
| Hooks can enforce policy/validation/logging/memory behavior. | Medium | Primary docs provide events and schemas; enforcement is partial because support and side-effect timing are limited. |
| These primitives should be adopted into Hermes. | Unsupported from this source alone | Requires separate approval, Hermes design fit, threat model, and eval. |

## Primitive Map
| Primitive | Codex mechanism in source | Hermes/Tolaria implication | Risk gate before adoption |
|---|---|---|---|
| [[Host-bound Agent Execution]] | Phone controls connected Mac/SSH/devbox while host supplies project state, tools, credentials, approvals, and sandboxing. | Keep execution near trusted project environments; use chat/mobile only as control/review surfaces. | Host trust, account/workspace match, repo cleanliness, sandbox mode, credential locality, no public app-server exposure. |
| [[Remote Agent Control]] | Mobile can answer questions, approve actions, send follow-ups, review diffs/tests/terminal/screenshots, and switch hosts/threads. | A Hermes equivalent would be an attention/approval loop, not an autonomous permission bypass. | Notification reliability, wrong-approval prevention, audit log, escalation for risky actions. |
| Secure relay model | OpenAI says trusted machines stay reachable without direct public exposure. | Any future Hermes remote-control proposal needs a relay/VPN/mesh threat model, not ad hoc port exposure. | Relay trust, auth, revocation, device loss, replay/session hijack, host sleep/disconnect handling. |
| SSH/devbox host routing | Codex App discovers concrete SSH aliases and starts the remote Codex app server through SSH. | Long-running work should run where dependencies, compute, policies, and credentials already live. | SSH key hygiene, least-privilege users, no exposed transports, remote PATH/auth sanity, auditability. |
| [[Workspace-scoped Automation Identity]] | Business/Enterprise access tokens run Codex local under ChatGPT workspace identity for trusted automation. | If approved, prefer workflow-owned, expiring, auditable identities over shared long-lived local secrets. | Secret manager, trusted runners, finite expiry, rotation smoke test, owner metadata, redacted logs, revocation path. |
| [[Agent Lifecycle Hooks]] | Hooks can scan prompts, block/allow supported calls, validate turn stops, log sessions, and propose memory. | Hooks are a candidate control plane for policy, validation, observability, and memory hygiene. | Hook trust review, managed vs repo-local separation, incomplete tool coverage, latency, false blocks, side effects before post-tool review. |
| Review outputs | Mobile surfaces terminal output, screenshots, diffs, and test results. | Review surfaces must preserve evidence, not just present a green status. | Diff/test provenance, screenshot freshness, truncation, artifact completeness, source/spec fidelity. |

## Approval Proposal Options
These are proposals only; this Beta card did not implement them.

1. Lowest-risk knowledge/eval proposal: define an evaluation checklist for Codex remote/mobile attention loops. Measure unblock latency, wrong-approval rate, missed-notification rate, diff/test review completeness, host disconnect handling, and human interruption cost on a few local Codex tasks.
2. Security-first proposal: threat-model Codex access-token automation before any use. Require token owner, workflow scope, trusted runner, finite expiration, rotation test, redacted logs, revocation path, and clear distinction from Platform API keys.
3. Hook-policy proposal: evaluate one read-only or low-side-effect Codex hook class first, such as prompt secret scanning or stop-time validator reporting, before considering permission auto-allow/deny hooks or memory-creation hooks.
4. Hermes comparison proposal: compare Codex's hook/remote-control primitives with existing Hermes Kanban comments, heartbeats, cron, notifications, tool permissions, profile memory, and Tolaria logs to identify which gaps are real versus already covered.

## Citations
- [[Work with Codex from anywhere]]: primary source for the article, remote-connections docs, access-token docs, and hook docs.
- [[Remote Agent Control]]: existing concept for mobile/human-in-the-loop review and unblock.
- [[Host-bound Agent Execution]]: concept extracted from this source's host/device separation.
- [[Workspace-scoped Automation Identity]]: concept extracted from Codex access-token docs.
- [[Agent Lifecycle Hooks]]: concept extracted from Codex hook docs.
- [[Durable Agent Operating Loop]] and [[Codex-maxxing Durable Operating Loop Assessment]]: existing Tolaria context for why remote attention, review surfaces, and policy hooks matter.

## Implications
For [[Hermes Agent]], this source strengthens the case that durable agent work needs explicit control-plane design: where work runs, who authorizes it, how humans approve remotely, how policy/validation/memory hooks run, and how outputs are reviewed. It does not justify implementing new Hermes features from Beta; it supplies source-backed proposal material for Overseer.

For [[Codex]], the source suggests a practical separation of concerns: use local/SSH/devbox hosts for capability and credentials, mobile for attention and steering, access tokens for trusted non-interactive workspace identity, and hooks for policy/validation/logging/memory. Each part has different failure modes and should be evaluated separately.

For Tolaria, the source should be linked to the existing [[Durable Agent Operating Loop]] cluster while keeping evidence skepticism visible. Primary product docs are stronger than a tweet, but product docs still do not prove outcome superiority.

## Recommended Next Actions
- Preserve as Tolaria knowledge: done through [[Work with Codex from anywhere]], [[Host-bound Agent Execution]], [[Workspace-scoped Automation Identity]], [[Agent Lifecycle Hooks]], and this synthesis.
- Do not implement directly from this Beta card.
- If Overseer later approves action, start with a narrowly scoped evaluation or threat model rather than installing hooks, creating access tokens, changing Hermes config, or opening remote access.

## Follow-up Questions
- Which approved future eval would matter most: mobile approval latency, access-token automation safety, Codex hook policy coverage, or Hermes/Kanban notification parity?
- What should be the default stance for high-risk mobile approvals: allow only read/test/diff review, require workstation confirmation for writes/network/secrets, or classify by tool/action risk?
- Should any future hook/memory proposal be draft-only until Tolaria/log review confirms it does not create stale or private durable memory?
