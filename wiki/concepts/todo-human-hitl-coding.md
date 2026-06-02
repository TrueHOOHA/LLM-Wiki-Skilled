---
type: concept
aliases: ["TODO(human)", "human TODO markers", "human-in-the-loop coding pedagogy", "learn-by-doing coding mode"]
tags: [agent-engineering, coding-agents, learning, workflow]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# TODO(human) Human-in-the-loop Coding

## Definition
TODO(human) Human-in-the-loop Coding is a learning-oriented coding-agent pattern where the agent deliberately leaves small, strategic implementation gaps for the human to fill, marking them explicitly so the human practices code comprehension and production inside an otherwise agent-assisted workflow.

## Scope
The concrete source is Claude Code Learning output style in [[Anthropic brings Claude's Learning Mode to regular users and devs]], where official docs captured by Alpha describe `TODO(human)` markers and Engadget reports that the user may be asked to write roughly five to ten lines of code. The concept is narrower than human approval: the point is not merely to approve a patch or click through a permission request, but to force bounded participation that can preserve debugging skill, code ownership, and architectural understanding. It is relevant to [[Learning-preserving AI Assistance]], [[AI-assisted Coding Skill Formation]], [[Codex Sequential TDD Workflow]], and [[Hermes Agent]] only when the task goal includes learning or oversight development.

## Contrasts
- Versus approval gates: approval gates decide whether the agent may proceed; TODO(human) markers give the human a small implementation responsibility.
- Versus code review: review happens after generated work; TODO(human) coding interrupts generation so the human participates before completion.
- Versus pair programming: TODO(human) is a structured, asymmetric variant where the agent still does most scaffolding but reserves selected pieces for the learner/operator.
- Versus delivery mode: it is intentionally slower and more token-heavy when learning or future oversight is the goal.

## Evidence
- [[Anthropic brings Claude's Learning Mode to regular users and devs]] preserves Engadget's launch report plus Alpha's primary-source check that Claude Code Learning inserts `TODO(human)` markers for small strategic pieces.
- [[AI-assisted Coding Skill Formation]] supplies the adjacent evidence problem: delegation can complete tasks while leaving the user weaker on later no-AI debugging or explanation.
- [[Learning-preserving AI Assistance]] names the broader design response: keep enough human cognitive effort in the loop to support retention and ownership.

## Related
- [[Agent Output Styles]]
- [[Learning-preserving AI Assistance]]
- [[AI-assisted Coding Skill Formation]]
- [[Claude Code]]
- [[Anthropic]]
- [[Codex Sequential TDD Workflow]]
- [[Evaluator-Optimizer Workflow]]
- [[Hermes Agent]]

## Open Questions
- How should a coding agent choose which lines or functions become TODO(human) without making the exercise arbitrary or blocking progress unnecessarily?
- What completion check proves the human learned the relevant concept: tests, explanation, later modification, debugging quiz, or review quality?
- Should TODO(human) ever appear in production code, or must it always be resolved before commit/merge?
- Could a local Codex workflow emulate the pattern with prompt instructions and review gates without adding a persistent mode abstraction?
