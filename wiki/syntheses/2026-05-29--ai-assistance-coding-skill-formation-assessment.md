---
type: synthesis
question: "What should Tolaria preserve from Anthropic's AI coding skill-formation study for Hermes/Codex workflows?"
tags: [agent-engineering, coding-agents, learning, evaluation]
created: 2026-05-29
updated: 2026-05-29
---

# AI Assistance and Coding Skill Formation Assessment

## Question / Purpose
Assess [[How AI assistance impacts the formation of coding skills]] as evidence for AI coding skill formation, extract the cognitive-offloading versus learning-preserving usage patterns, and translate the result into a knowledge-only approval proposal for possible Hermes/Codex learning-mode experiments.

## Answer / Analysis
The strongest counterargument to over-applying this source is methodological: n=52, short-term quiz, one unfamiliar Python library, one constrained tutorial-like task family, and one sidebar chat assistant do not prove that AI coding agents broadly harm learning. The source is still valuable because it isolates a real operational tension for agentic coding: when a user delegates code production or debugging too early, the deliverable can be completed while the human fails to acquire the debugging, code-reading, and conceptual oversight skills needed for later review.

The study's practical signal is a mode distinction. Delivery mode optimizes for working output on familiar or production tasks. Learning mode optimizes for durable comprehension when the operator is learning a new library, codebase, architecture, or tool. Tolaria should not silently replace delivery mode with learning mode, because that would add friction to work whose goal is throughput. It should preserve the design hypothesis that [[Hermes Agent]], local [[Codex]], and [[Claude Code]] workflows may need an explicit learning/explanatory mode when the objective includes skill formation.

The interaction taxonomy is more useful than the headline 17% figure. Low-retention patterns were AI delegation, progressive reliance, and assistant-led debugging. Better-retention patterns were conceptual inquiry, hybrid code/explanation, and generation-then-comprehension. This fits existing Tolaria notes on [[Context Engineering]], [[Codex Sequential TDD Workflow]], and [[Evaluator-Optimizer Workflow]]: the context and acceptance criteria should tell the agent whether it is optimizing for shipped code, human understanding, or both.

## Comparison Table
| Pattern | Learning risk | Useful when | Tolaria/Hermes implication |
|---|---|---|---|
| AI delegation | High for unfamiliar material | Fast throwaway output or familiar task execution | Keep as delivery mode; do not pretend it teaches the operator |
| Progressive AI reliance | High | Unclear; may feel efficient while collapsing learning | Watch for it in novice/junior workflows and unfamiliar-codebase sessions |
| Iterative AI debugging | High-to-medium | Useful only if paired with explanation and human diagnosis | Add comprehension checks before accepting assistant fixes in learning mode |
| Generation-then-comprehension | Medium-to-low | When generated code is useful but user must understand it | Ask user/agent to explain invariants, failure modes, and change points |
| Hybrid code-explanation | Medium-to-low | When code generation is allowed but pedagogy matters | Require concise rationale and links to source/API docs |
| Conceptual inquiry | Low in this study | New library/codebase learning | Prefer questions, hints, and manual implementation when mastery matters |

## Knowledge-only Approval Proposal
Proposal for later Overseer approval, not implemented here: run a small reversible Hermes/Codex learning-mode experiment on one unfamiliar-library or unfamiliar-codebase task.

- Compare normal delivery mode against explicit learning/explanatory mode.
- Keep the test opt-in and session-scoped; do not alter default profiles, skills, cron jobs, or routing.
- Measure task completion, post-task debugging/code-reading quiz, later modification ability, human explanation quality, token/latency cost, and correction count.
- Include risks: added friction, false confidence from verbose explanations, lower throughput, inconsistent model behavior, and possible mismatch between quiz performance and real project outcomes.
- Smallest safe test: one non-production toy or sandbox task with pre-written acceptance checks and a short no-AI comprehension/debugging prompt after completion.

## Citations
- [[How AI assistance impacts the formation of coding skills]]: primary Anthropic research page and linked arXiv paper; medium evidence for the short-term RCT result.
- [[Anthropic]]: entity page for Anthropic research and agent-engineering sources.
- [[Codex]] and [[Claude Code]]: coding-agent/tooling comparators for local workflows and learning-mode product design.
- [[Context Engineering]] and [[Evaluator-Optimizer Workflow]]: existing Tolaria concepts for making task goals, rubrics, and mode boundaries explicit.

## Implications
- For [[Codex]]: unfamiliar codebase/library tasks should distinguish "ship a patch" from "learn enough to supervise future patches." The existing sequential/TDD hypothesis is compatible with learning mode only if it includes explanation and comprehension checks, not just tests.
- For [[Hermes Agent]]: any learning/explanatory interaction-mode experiment should remain approval-gated and opt-in. Beta should preserve the proposal in Tolaria, not patch Hermes prompts or skills.
- For [[Claude Code]]/[[OpenAI]] product patterns: Learning/Explanatory output styles and Study Mode are design hypotheses; they need outcome validation before being treated as proven solutions.
- For evaluation: the right eval is not only elapsed time or pass/fail. It should include no-AI debugging, code reading, and conceptual checks because those are oversight capabilities.

## Follow-up Questions
- Should Overseer later approve a non-knowledge learning-mode eval for Codex/Hermes, or leave this as reference-only until more primary outcome studies exist?
- If approved later, should the test focus on local Codex, Hermes agent profiles, Claude Code output styles, or a provider-agnostic prompt template?
- What outcome matters most for Overseer: later debugging ability, reduced review mistakes, faster onboarding to unfamiliar code, or lower correction burden?
