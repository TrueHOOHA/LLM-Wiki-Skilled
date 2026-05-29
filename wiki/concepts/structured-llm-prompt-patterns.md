---
type: concept
aliases: ["structured prompts", "prompt patterns", "LLM use-case patterns", "Claude prompt patterns"]
tags: [prompt-design, agent-engineering, learning]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Structured LLM Prompt Patterns

## Definition
Structured LLM Prompt Patterns are reusable task frames that specify the model's role, input assumptions, constraints, output sections, critique criteria, and interaction mode so a generic chat model can behave more like a research assistant, editor, tutor, coach, reviewer, or planner for a bounded task.

## Scope
This concept covers prompt-level workflow primitives such as multi-source synthesis, devil's advocate critique, steelmanning, style analysis, brutal editing, roleplay practice, mental-model tutoring, Feynman/Socratic tutoring, and curriculum design. It does not imply that viral prompt templates are validated workflows, that Claude-specific prompts transfer unchanged to Hermes/Codex, or that prompt wording alone is enough; stronger versions need source grounding, acceptance criteria, examples, and evaluation.

## Contrasts
- Versus [[Context Engineering]]: structured prompt patterns shape one task frame; context engineering manages the whole information environment, including files, memory, tools, sources, and constraints.
- Versus [[Thin Harness Fat Skills]]: a prompt pattern is a candidate primitive; a fat skill is a maintained artifact with triggers, procedures, edge cases, verification, and supporting files.
- Versus [[Evaluator-Optimizer Workflow]]: critique prompts can imitate evaluation, but evaluator-optimizer implies an explicit iterative loop with criteria and stopping conditions.
- Versus simple rewrite/summarize prompts: structured patterns usually demand explicit sections, assumptions, credibility flags, audience transforms, interactive checks, or adversarial review.

## Evidence
- [[Anatoli Kopadze X post on Karpathy LLM skill gap and Claude prompts]] supplies weak social examples of structured use cases: multi-source synthesis with source-credibility flags, devil's advocate review, steelmanning, mental-model tutoring, style mimicry, brutal editing, audience rewrites, negotiation/interview roleplay, legal/plain-English translation, finance/travel planning, Feynman tutoring, curriculum design, and Socratic questioning.

## Related
- [[Context Engineering]]
- [[Instruction Priority Control]]
- [[Evaluator-Optimizer Workflow]]
- [[Thin Harness Fat Skills]]
- [[Agent-Computer Interface Design]]
- [[Dynamic Context Loading]]

## Open Questions
- Which prompt patterns measurably improve Tolaria/Beta outputs versus adding ceremony and token cost?
- What minimum evidence should promote a pattern from weak social example to Hermes skill, reference, or eval candidate?
- Which patterns are safest as one-shot prompts, and which require explicit human review, source citations, or deterministic validation?
