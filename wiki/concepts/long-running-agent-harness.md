---
type: concept
aliases: ["long-running agent harness", "initializer/coding-agent harness", "multi-context-window agent harness", "feature-ledger harness"]
tags: [agent-engineering, harnesses, evaluation, workflow]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Long-running Agent Harness

## Definition
A Long-running Agent Harness is a structured environment for agent work that must survive multiple context windows: the first session bootstraps durable state and future sessions make scoped, verified, clean increments against that state. In [[Effective Harnesses for Long-running Agents]], [[Anthropic]] implements this with an initializer agent, coding-agent loop, JSON feature ledger, `init.sh`, progress log, git history, and end-to-end verification.

## Scope
This concept covers continuity scaffolds for multi-session coding and adjacent agentic work: explicit feature/test ledgers, restart scripts, progress logs, session rediscovery steps, clean-state requirements, commits or other diffable checkpoints, and verification before status changes. It does not prove that any one Claude-specific quickstart should be copied into [[Hermes Agent]], [[Codex]], or Tolaria without an approval-gated eval. It also does not mean broad autonomous loops are safer than fixed workflows; the source's strongest lesson is to constrain and verify long-running work.

## Contrasts
- Versus context compaction alone: compaction summarizes previous context, while a harness externalizes decisive state into files, tests, logs, and commits that later sessions can inspect.
- Versus one-shot prompting: the harness decomposes broad goals into one-feature increments and requires clean handoff state after each session.
- Versus [[Durable Agent Operating Loop]]: durable loops describe the broader supervised workstream; long-running harnesses are the task-local scaffolding that makes each resumed session safe and concrete.
- Versus [[File-backed Agent Memory]]: file-backed memory preserves knowledge/state; a long-running harness adds selection rules, verification gates, and status mutation discipline.
- Versus [[Evaluator-Optimizer Workflow]]: evaluation is embedded as a status gate rather than an unbounded self-critique loop.

## Evidence
- [[Effective Harnesses for Long-running Agents]] is the primary source. It says compaction alone was insufficient, identifies one-shotting and premature victory as failures, and recommends initializer/coding-agent prompts, `feature_list.json`, `init.sh`, `claude-progress.txt`, git commits, and browser/user-like tests.
- [[Anthropic Building Effective Agents and Hermes Workflow Implications]] supplies the adjacent Anthropic principle: start with the simplest pattern that evaluation justifies, and keep autonomous workflows guarded.
- [[Codex-maxxing Durable Operating Loop Assessment]] and [[Codex Remote/mobile Workflow Primitives for Hermes Assessment]] provide adjacent Tolaria patterns for durable workstreams, remote steering, hooks, review surfaces, and verification, but they do not independently validate Anthropic's specific harness.
- [[KingBootoshi tweet on Codex 5.5 goal escape hatch]] is weak social evidence, but its escape-hatch mechanism fits the harness problem: long-running ledgers need explicit non-success states for impossible, stale, too-broad, or damaging subgoals.

## Related
- [[Anthropic]]
- [[Claude Code]]
- [[Durable Agent Operating Loop]]
- [[File-backed Agent Memory]]
- [[Agent-Computer Interface Design]]
- [[Thin Harness Fat Skills]]
- [[Evaluator-Optimizer Workflow]]
- [[Orchestrator-Worker Workflow]]
- [[Hermes Agent]]
- [[Codex]]
- [[Agent Escape Hatch]]

## Open Questions
- Does the initializer/coding-agent split outperform a single general-purpose resumed agent when measured on the same task corpus?
- Which parts transfer to non-web domains: JSON feature ledgers, init scripts, progress logs, git commits, end-to-end checks, or all of them?
- For Hermes/Tolaria work, what is the correct domain-specific equivalent of a feature ledger and clean-state verification: acceptance checklist, source ledger, index/log checks, citation-fidelity eval, or Kanban handoff rubric?
