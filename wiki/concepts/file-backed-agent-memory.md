---
type: concept
aliases: ["file-backed memory", "vault-backed agent memory", "diffable agent memory"]
tags: [agent-engineering, memory, knowledge-management]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# File-backed Agent Memory

File-backed Agent Memory is the practice of writing durable agent memory into inspectable, editable, diffable files or knowledge notes rather than relying only on raw chat history or opaque personalization state.

## Definition

In [[Codex-maxxing]], [[Jason Liu]] keeps long-running work in an Obsidian/GitHub-backed vault with instructions telling the agent to update people, project, TODO, agent, and notes pages as it learns. In [[Effective Harnesses for Long-running Agents]], [[Anthropic]] uses task-local files such as `feature_list.json`, `claude-progress.txt`, `init.sh`, and git history so later coding-agent sessions can resume safely. The claimed benefit is reviewability and continuity: memory becomes diffable state that the human or next agent can inspect, verify, and update.

## Scope

This concept covers project state, decisions, open loops, known preferences, people/context notes, daily notes, and thread-learned patterns that should survive compaction or thread loss. It does not mean storing every transcript, unverified inference, private screen capture, or temporary task detail. For Tolaria, immutable raw sources plus source/concept/entity/synthesis pages are the canonical stronger form of file-backed memory.

## Contrasts

- Versus raw conversation history: files require the agent to compress experience into inspectable statements.
- Versus opaque platform memories: files can be diffed, versioned, reviewed, edited, and removed by the operator.
- Versus profile memory: not all file-backed project/task state belongs in global assistant memory; [[Memory Hygiene for AI Agents]] still decides durability, scope, and privacy.

## Evidence

- [[Codex-maxxing]] gives the direct vault-backed memory workflow and links it to reviewable diffs.
- [[Effective Harnesses for Long-running Agents]] adds a stronger harness-specific memory pattern: progress logs, feature/test JSON, restart scripts, and git commits reduce the need for resumed agents to infer prior state from compaction.
- [[Memory Hygiene for AI Agents]] provides the broader Tolaria discipline for deciding what should become durable memory.
- [[LLM Wiki Pattern]] and [[Compounding AI Knowledge Stack]] are stronger local analogues: Tolaria stores sources and synthesis in structured markdown with index/log checks.
- The raw source's captured Chronicle note adds a caution: ambient screen-derived local Markdown memories are promising but carry permission, prompt-injection, rate-limit, and unencrypted-file risks.

## Related

- [[Memory Hygiene for AI Agents]]
- [[Context Engineering]]
- [[LLM Wiki Pattern]]
- [[Compounding AI Knowledge Stack]]
- [[Session Handoff Artifact]]
- [[Long-running Agent Harness]]
- [[Durable Agent Operating Loop]]
- [[Hermes Agent]]

## Open Questions

- Which Hermes/Tolaria state belongs in Tolaria source-backed notes, which belongs in project handoff files, and which belongs in profile memory?
- What review cadence prevents file-backed memories from becoming stale or silently over-personalized?
- How should ambient/screenshot-derived memory be sandboxed against prompt injection and accidental sensitive capture?
