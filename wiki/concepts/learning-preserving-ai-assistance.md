---
type: concept
aliases: ["learning-preserving assistance", "explanatory coding mode", "AI learning mode", "anti-offloading AI assistance"]
tags: [agent-engineering, coding-agents, learning, context]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# Learning-preserving AI Assistance

## Definition
Learning-preserving AI Assistance is an interaction pattern where an AI tool helps complete a task while deliberately preserving the user's cognitive effort, comprehension checks, debugging practice, recall, ownership, and ability to explain or modify the result later.

## Scope
The pattern covers conceptual questions, explanation requests, hybrid code-plus-explanation prompts, generation-then-comprehension loops, human-first drafting, delayed critique, self-explanation checks, Socratic hints, optional output styles that make the assistant behave more like a tutor or reviewer than a pure delegate, and explicit [[TODO(human) Human-in-the-loop Coding]] where the human implements bounded pieces. It is relevant to [[Claude Code]], [[Codex]], [[Hermes Agent]], [[ChatGPT]], and [[Context Engineering]] when the goal includes skill formation. It does not mean every production task should be slowed down for pedagogy; delivery mode and learning mode should be explicit and opt-in.

## Contrasts
- Versus AI delegation: the assistant writes or debugs the solution while the human remains a shallow approver.
- Versus iterative AI debugging: the human repeatedly asks the assistant to fix errors without forming an independent model of why the error happened.
- Versus generic explanations: learning-preserving assistance should include task-specific comprehension checks or human participation, not just extra prose after a generated patch.

## Evidence
- [[How AI assistance impacts the formation of coding skills]] found that high-scoring study participants tended to ask conceptual questions, request code with explanations, or generate code and then ask follow-up questions to check understanding.
- [[Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task]] adds adjacent essay-writing evidence: immediate LLM drafting correlated with weaker EEG connectivity, lower essay ownership, and weaker quote recall, while prior brain-only writing followed by LLM use looked different from LLM-first use.
- The same source notes Claude Code Learning/Explanatory output styles and ChatGPT Study Mode as design responses; Tolaria should treat these as product-pattern hypotheses until outcome data exists.
- [[Anthropic brings Claude's Learning Mode to regular users and devs]] strengthens the mechanism detail for Claude Code: [[Agent Output Styles]] separate delivery/explanation/learning response policy, while [[TODO(human) Human-in-the-loop Coding]] asks the user to implement bounded sections instead of only reading extra explanation.

## Related
- [[AI-assisted Cognitive Debt]]
- [[Timing-sensitive AI Assistance]]
- [[AI-assisted Coding Skill Formation]]
- [[Agent Output Styles]]
- [[TODO(human) Human-in-the-loop Coding]]
- [[Context Engineering]]
- [[Codex Sequential TDD Workflow]]
- [[Evaluator-Optimizer Workflow]]
- [[Structured LLM Prompt Patterns]]
- [[Hermes Agent]]

## Open Questions
- What is the minimum friction needed to improve retention without making high-throughput delivery work impractically slow?
- Should a future approved Hermes/Codex experiment expose learning mode as a profile/session style, a task flag, a prompt template, or an explicit skill/instruction bundle?
- Which validation is more predictive for coding oversight: immediate quiz score, later modification task, debugging task, human explanation quality, source/quote recall, or ownership rating?
- How should assistance timing differ between drafting, editing, debugging, retrieval, and critique tasks?
