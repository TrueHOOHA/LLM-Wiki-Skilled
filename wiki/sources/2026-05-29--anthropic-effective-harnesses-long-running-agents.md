---
type: source
source_path: raw/sources/2026-05-29-anthropic-effective-harnesses-long-running-agents.md
title: "Effective harnesses for long-running agents"
author: "Justin Young / Anthropic"
date: 2025-11-26
tags: [agent-engineering, harnesses, evaluation, coding-agent]
created: 2026-05-29
source_type: article
credibility_tier: primary
evidence_grade: strong
---

# Effective Harnesses for Long-running Agents

## Summary
Anthropic argues that context compaction alone is insufficient for long-running coding agents because each new session can inherit partial, ambiguous, or stale state. Their proposed harness separates the first session from later sessions: an initializer agent bootstraps the repo, feature ledger, progress log, init script, and initial git commit; subsequent coding agents choose one unfinished feature, verify the current app state, make incremental progress, test like a user, and leave clean git/progress artifacts for the next session. The article is strong primary evidence for Anthropic's recommended Claude Agent SDK harness pattern and the shipped autonomous-coding quickstart mechanics, but only medium evidence that the same design generalizes unchanged to non-Claude, non-web-app, or Hermes/Tolaria workloads. The main reusable Tolaria lesson is not "make agents autonomous"; it is that long-running work needs durable, checkable state, scoped increments, and verification before status changes.

## Key Claims
1. Long-running agents fail when they try to one-shot broad goals across context windows; compaction can preserve some context but does not reliably communicate clean next-step state.
2. A first-window initializer prompt should create the environment future agents need: a structured feature/test ledger, `init.sh`, progress notes, and an initial git commit.
3. Later sessions should work one feature at a time, start by rediscovering project state (`pwd`, progress file, feature list, git log, init script), run a smoke/end-to-end check before implementation, and leave the repo clean.
4. A JSON feature ledger with `passes` booleans is less prone to inappropriate model edits than Markdown; coding agents should only flip status after careful testing and should not remove or rewrite tests to make progress look better.
5. Human-like end-to-end verification, such as browser automation through Puppeteer MCP for a web app, catches failures that unit tests or curl checks can miss; tool limitations still leave blind spots such as browser-native alert modals.
6. The article leaves open whether one general coding agent or specialized testing/QA/cleanup agents perform better across context windows, and whether the pattern transfers beyond full-stack web apps.

## Notable Quotes
- "However, compaction isn’t sufficient."
- "The very first agent session uses a specialized prompt that asks the model to set up the initial environment: an init.sh script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit that shows what files were added."
- "After some experimentation, we landed on using JSON for this, as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."
- "Only mark features as 'passing' after careful testing."
- "It’s still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture."

## Entities Mentioned
- [[Anthropic]]
- [[Claude Code]]

## Concepts Mentioned
- [[Long-running Agent Harness]]
- [[Durable Agent Operating Loop]]
- [[File-backed Agent Memory]]
- [[Agent-Computer Interface Design]]
- [[Thin Harness Fat Skills]]
- [[Evaluator-Optimizer Workflow]]
- [[Orchestrator-Worker Workflow]]

## Evidence and Caveats
- Strong: Anthropic's own description of its long-running Claude Agent SDK harness pattern, failure modes, prompt split, feature ledger, progress log, git-state handoff, and browser-verification recommendations.
- Strong: the linked official quickstart and Agent SDK docs corroborate that the pattern is supported by first-party Claude tooling and examples.
- Medium: generalization to Hermes, Codex, non-Claude agents, non-web-app domains, or production reliability. The article is a practitioner/engineering report, not an independent benchmark with a public task corpus and measured ablations.
- Caveat: prior Learn Harness Engineering and Codex/Hermes cards already covered possible prototype implications, so this page preserves knowledge only and does not create any implementation work.

## Follow-ups
- If a future approval-gated eval is ever authorized, compare simple compaction-only, progress-log-only, JSON-ledger, and full initializer/coding-agent harness variants on one bounded task class.
- If the pattern is reused outside coding, define the equivalent of feature ledger, init script, progress log, git history, and end-to-end verification for that domain before adoption.
