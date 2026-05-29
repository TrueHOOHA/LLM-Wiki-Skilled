---
type: concept
aliases: ["AI coding skill formation", "AI-assisted skill formation", "coding skill retention with AI"]
tags: [agent-engineering, coding-agents, learning, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# AI-assisted Coding Skill Formation

## Definition
AI-assisted Coding Skill Formation is the question of how using AI coding assistants while learning a new programming tool, library, codebase, or workflow changes the user's ability to later debug, read, write, recall, own, and conceptually explain the code without the assistant.

## Scope
This concept covers learning outcomes under AI-assisted coding, especially when the user is not merely producing a deliverable but trying to acquire durable oversight skill. It applies to [[Codex]], [[Claude Code]], and [[Hermes Agent]] coding workflows when tasks involve unfamiliar libraries or architecture. It does not claim that AI always reduces skill; [[How AI assistance impacts the formation of coding skills]] supports a narrower mode-dependent claim from one small randomized study.

## Contrasts
- Versus coding productivity: a tool can speed up familiar work while still weakening skill acquisition on unfamiliar material.
- Versus pure code quality: generated code can pass the task while leaving the user less able to inspect, debug, or extend it later.
- Versus [[Learning-preserving AI Assistance]]: this concept names the outcome problem; learning-preserving assistance names the interaction/design response.

## Evidence
- [[How AI assistance impacts the formation of coding skills]] reports that developers using a chat-based AI assistant scored about 17% lower on a no-AI post-task mastery quiz after completing unfamiliar Trio tasks, with the strongest gap on debugging.
- The same source links lower-scoring patterns to delegation/offloading and higher-scoring patterns to conceptual inquiry, explanation-seeking, and generation-then-comprehension, but the interaction-mode evidence is correlational.
- [[Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task]] is not a coding study, but it strengthens the adjacent concern that immediate LLM drafting can weaken ownership and recall even when output quality appears acceptable.
- [[Anthropic brings Claude's Learning Mode to regular users and devs]] adds a concrete product-pattern response: Claude Code Learning mode uses [[TODO(human) Human-in-the-loop Coding]] to preserve bounded human implementation practice, but the source does not prove retention outcomes.

## Related
- [[AI-assisted Cognitive Debt]]
- [[Timing-sensitive AI Assistance]]
- [[Learning-preserving AI Assistance]]
- [[Agent Output Styles]]
- [[TODO(human) Human-in-the-loop Coding]]
- [[Context Engineering]]
- [[Codex Sequential TDD Workflow]]
- [[Evaluator-Optimizer Workflow]]
- [[Hermes Agent]]
- [[Anthropic]]

## Open Questions
- Do agentic coding tools produce larger skill-formation effects than the sidebar chat assistant tested by Anthropic?
- How long do the measured short-term quiz differences persist?
- Which task classes should default to delivery mode versus learning mode in local Codex/Hermes practice?
- Do `TODO(human)` markers outperform explanation-only modes for later debugging and modification tasks?
