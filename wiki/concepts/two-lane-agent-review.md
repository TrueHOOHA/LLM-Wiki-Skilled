---
type: concept
aliases: ["two-lane review", "standards and spec review", "parallel agent review"]
tags: [agent-engineering, code-review, evaluation, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Two-lane Agent Review

## Definition
Two-lane Agent Review is a review pattern that separates code-quality/standards review from spec-or-PRD-fidelity review, optionally running the two checks in parallel with distinct agent roles.

## Scope
The pattern is useful because many agent-generated diffs can be locally well-written while solving the wrong problem, or faithful to a spec while violating repository conventions. In Hermes, this maps to existing review-required handoffs and code-review skills, but any change to reviewer routing or skills must be approval-gated. Tolaria should preserve the review dimensions and failure modes.

## Contrasts
- Versus single-pass review: two-lane review avoids blending style, architecture, tests, and spec fidelity into one vague approval.
- Versus evaluator-optimizer loops: this is primarily a parallel classification/check pattern, not necessarily an iterative generation loop.
- Versus human code review replacement: weak evidence does not justify replacing human approval gates.

## Evidence
- [[Matt Pocock AI Hero skills changelog]] previews a review skill that kicks off two parallel sub-agents: one checking repository coding standards and another checking whether the diff faithfully implements the original issue or PRD.

## Related
- [[Evaluator-Optimizer Workflow]]
- [[Orchestrator-Worker Workflow]]
- [[Agent-Computer Interface Design]]
- [[Hermes Agent]]
- [[AI Hero]]

## Open Questions
- Should Overseer approve a future evaluation of two-lane review against current Hermes/Codex review practice?
- What should be the blocking criteria for each lane: standards violations, missing tests, diff/spec mismatch, unimplemented acceptance criteria, security risk, or unclear provenance?
