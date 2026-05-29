---
type: concept
aliases: ["goal escape hatch", "agent failure escape hatch", "incomplete marker", "bounded incomplete marker"]
tags: [agent-engineering, workflow, reliability, codex]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent Escape Hatch

## Definition
An Agent Escape Hatch is an explicit workflow rule that lets an agent mark a bounded subgoal as impossible, stale, too broad, unsafe, or damaging, then continue or stop honestly instead of fabricating success. In [[KingBootoshi tweet on Codex 5.5 goal escape hatch]], the proposed marker is `[incomplete]`; the durable idea is broader than that literal token.

## Scope
This concept covers technical and agentic failure boundaries in long-running work: incomplete markers, impossible-example handling, stale-goal detection, stop-digging rules, progress-log hygiene, and workspace-poisoning prevention. It does not mean an agent may silently skip requirements, lower acceptance criteria, or declare a whole task done after partial completion. The escape hatch must be bounded, visible, cited in the handoff, and reviewed when it affects the operator's objective.

## Contrasts
- Versus ordinary failure: an escape hatch preserves the exact failed subgoal and reason, rather than collapsing all failure into agent incompetence or tool error.
- Versus hallucinated success: the agent records `[incomplete]`, blocker evidence, or a scoped exception instead of pretending an impossible item passed.
- Versus lazy skipping: the agent must justify why the subgoal is impossible, stale, too broad, or damaging, and must keep remaining achievable work inside scope.
- Versus [[Long-running Agent Harness]]: the harness supplies durable ledgers, logs, and verification gates; the escape hatch is one status convention inside those artifacts.
- Versus [[Memory Hygiene for AI Agents]]: memory hygiene decides what should persist; the escape hatch prevents bad examples, broken links, stale goals, or failed claims from becoming misleading durable memory.

## Evidence
- [[KingBootoshi tweet on Codex 5.5 goal escape hatch]] is weak social evidence for the specific Codex story, but it captures the workflow mechanism directly: mark truly impossible examples `[incomplete]` rather than lying or poisoning progress state.
- [[Codex Goal Escape Hatch Workflow Hypothesis Assessment]] grades the mechanism as useful vocabulary but low-confidence adoption evidence because there is no reproducible Codex trace, benchmark, or full prompt.
- [[Effective Harnesses for Long-running Agents]] is adjacent stronger evidence that long-running agents need explicit ledgers, progress logs, and verification gates so resumed sessions do not inherit ambiguous or stale state.
- [[Codex-maxxing]] and [[Work with Codex from anywhere]] are adjacent Codex-loop sources: they support the importance of durable workstreams, remote steering, hooks, review, and goals, but not the specific escape-hatch behavior.

## Related
- [[Codex]]
- [[Hermes Agent]]
- [[Long-running Agent Harness]]
- [[Durable Agent Operating Loop]]
- [[Context Engineering]]
- [[Memory Hygiene for AI Agents]]
- [[File-backed Agent Memory]]
- [[Agent Lifecycle Hooks]]
- [[Agent-Computer Interface Design]]
- [[Evaluator-Optimizer Workflow]]

## Open Questions
- What evidence should an agent provide before marking a subgoal `[incomplete]`: failing tool output, source absence, contradiction notes, acceptance-test impossibility, or human-review requirement?
- Should incomplete markers be task-local only, or should repeated incomplete classes become durable Tolaria concepts after review?
- What prevents an escape hatch from becoming a permission slip for shallow work: mandatory retry count, bounded explanation, reviewer approval, or metric-based eval?
- Which Hermes/Tolaria artifacts would be safest to test later if approved: Kanban handoffs, progress logs, source-ingestion contradiction notes, Codex local task goals, or lint reports?
