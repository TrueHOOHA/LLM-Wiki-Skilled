---
type: concept
aliases: ["delayed AI assistance", "scaffolded AI assistance", "assistance timing", "human-first AI assistance"]
tags: [agent-engineering, learning, context, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Timing-sensitive AI Assistance

## Definition
Timing-sensitive AI Assistance is the design pattern of choosing when AI help enters a task loop so that the tool supports the goal without prematurely replacing the human cognitive work needed for learning, ownership, recall, or judgment.

## Scope
This concept covers human-first drafting, search-before-generation, Socratic hints, delayed critique, generation-after-comprehension, and explicit delivery-versus-learning mode selection. It is relevant to [[Hermes Agent]], [[Codex]], [[Claude Code]], [[ChatGPT]], and [[Context Engineering]] whenever the goal includes human mastery rather than only shipped output.

## Contrasts
- Versus immediate delegation: the assistant produces the main answer before the human has formed a model of the problem.
- Versus no-AI purism: delayed assistance can still be valuable after the human first engages with the material.
- Versus generic tutoring: timing-sensitive assistance treats the moment of intervention as a first-class design variable, not just the tone or amount of explanation.

## Evidence
- [[Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task]] reports that Brain-to-LLM participants in session 4 had higher recall and wider re-engagement than prior LLM users switched to brain-only writing, suggesting that prior human-only effort followed by LLM assistance may differ from immediate LLM drafting.
- [[How AI assistance impacts the formation of coding skills]] supports an adjacent mode distinction in coding: conceptual inquiry and generation-then-comprehension correlated with better mastery than delegation/offloading patterns.

## Related
- [[AI-assisted Cognitive Debt]]
- [[Learning-preserving AI Assistance]]
- [[AI-assisted Coding Skill Formation]]
- [[Context Engineering]]
- [[Evaluator-Optimizer Workflow]]
- [[Hermes Agent]]

## Open Questions
- What is the minimum useful human-first work before AI assistance: outline, explanation, failed attempt, retrieval notes, test plan, or self-quiz?
- Which Hermes/Codex task types should expose a learning-mode flag instead of relying on operator memory?
- How should a workflow measure ownership and recall without creating too much friction?
