---
type: concept
aliases: ["Codex hooks", "agent hooks", "lifecycle hooks", "hook-based agent policy"]
tags: [agent-engineering, policy, validation, observability, codex]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent Lifecycle Hooks

## Definition
Agent Lifecycle Hooks are configured callbacks that run at defined points in an agent session, turn, subagent lifecycle, compaction step, prompt submission, tool call, permission request, or stop event so a system can inject context, scan inputs, enforce policy, validate outputs, log events, or create memory. [[Work with Codex from anywhere]] is the current primary Tolaria source: OpenAI documents Codex hooks for events including `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SubagentStart`, `SubagentStop`, and `Stop`.

## Scope
This concept covers hook placement, event schemas, trust review, managed hooks, policy/validation/logging/memory use cases, and hook limitations. It does not imply hooks are a complete security boundary, that hook scripts should be created from this Beta card, or that Hermes should mirror Codex hook semantics without an approved design/eval.

## Contrasts
- Versus static prompt instructions: hooks can inspect runtime events and tool inputs/outputs, but their coverage depends on what the agent runtime exposes.
- Versus external audit logs: hooks can run inline and shape the session, but post-tool hooks cannot undo completed side effects.
- Versus [[Skill Validation Patterns]]: validation patterns decide whether reusable skills are safe and useful; lifecycle hooks enforce or observe behavior during live runs.
- Versus [[Agent-Computer Interface Design]]: hooks are one mechanism for shaping the interface between agent, tools, policy, and operator.

## Evidence
- [[Work with Codex from anywhere]] records OpenAI's docs that hooks can log conversations, scan prompts for secrets, summarize conversations into persistent memories, run validators when a turn stops, and customize behavior for repositories/directories.
- The same source documents trust boundaries: non-managed command hooks need review and hash-based trust; managed hooks can be enforced by admin policy; project-local hooks load only when the project `.codex/` layer is trusted.
- The same source documents limitations: matching hooks from multiple files all run; multiple command hooks for one event can launch concurrently; async handlers and prompt/agent handlers are parsed but skipped today; supported interception is incomplete; and `PostToolUse` feedback cannot undo side effects.
- [[Codex-maxxing Durable Operating Loop Assessment]] supplies the broader operating-loop context where hook-like validators, logging, and memory gates could matter, but only as approval-gated future work.

## Related
- [[Codex]]
- [[OpenAI]]
- [[Hermes Agent]]
- [[Host-bound Agent Execution]]
- [[Workspace-scoped Automation Identity]]
- [[Agent-Computer Interface Design]]
- [[Skill Validation Patterns]]
- [[Memory Hygiene for AI Agents]]
- [[Evaluator-Optimizer Workflow]]
- [[Security Mindset]]

## Open Questions
- Which hook class would be lowest risk to evaluate if Overseer later approves non-knowledge work: prompt secret scanning, stop-time validation, read-only logging, memory proposal drafts, or permission-request policy?
- What failure mode should dominate an approved hook eval: false blocks, missed dangerous actions, untrusted hook mutation, stale memory creation, log leakage, hook latency, or side effects before post-tool review?
- How should managed hooks, repo-local hooks, and user-level hooks be separated so policy cannot be silently bypassed or overloaded by untrusted projects?
