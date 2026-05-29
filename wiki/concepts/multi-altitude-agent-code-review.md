---
type: concept
aliases: ["multi-altitude review", "architecture-pattern-file review", "agent code review altitude model"]
tags: [agent-engineering, code-review, architecture, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Multi-altitude Agent Code Review

## Definition
Multi-altitude Agent Code Review is a review model for agent-generated software that separates oversight into top-level architecture, mid-level patterns and abstractions, and low-level file implementation. The core hypothesis is that humans should spend the most attention on architecture and critical interfaces, then delegate file-level implementation more aggressively when the higher-altitude structure is explicit and current.

## Scope
This concept covers where human review effort should concentrate when agents write substantial amounts of code. It is not a license to skip tests, security review, or repository conventions. It suggests that file-level review is more meaningful when anchored to a known architecture, named patterns, and stable interfaces.

## Contrasts
- Versus single-pass code review: it separates architectural fit, pattern/interface consistency, and line-level correctness instead of mixing them into one vague approval.
- Versus [[Two-lane Agent Review]]: two-lane review separates code standards from spec fidelity; multi-altitude review separates system altitude levels. The two can combine, but neither source proves the combination is effective yet.
- Versus [[Evaluator-Optimizer Workflow]]: this is primarily a human oversight model; it could later become an evaluator rubric only with explicit approval and evidence.
- Versus hands-off agent autonomy: the model keeps human authority strongest where reversibility is lowest and system meaning is concentrated.

## Evidence
- [[Chrys Bader X post on agent-written codebases and living architecture diagrams]] states the three altitude levels and argues for architecture-first alignment, but provides weak evidence: anecdote plus infographic, no benchmark or reproducible workflow.

## Related
- [[Living Architecture Diagram]]
- [[Two-lane Agent Review]]
- [[Agent-Computer Interface Design]]
- [[Agentic Workflows and Agents]]
- [[Evaluator-Optimizer Workflow]]
- [[Hermes Agent]]

## Open Questions
- Which altitude should block merge/release when reviewers disagree: architecture, patterns/interfaces, file-level correctness, tests, or spec fidelity?
- How should a review handoff make architectural decisions visible without requiring reviewers to reread every generated file?
- Can a compact architecture/pattern checklist outperform ordinary diff review for Codex/Hermes coding tasks?
