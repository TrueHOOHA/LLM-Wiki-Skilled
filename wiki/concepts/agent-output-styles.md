---
type: concept
aliases: ["agent output styles", "coding-agent output styles", "behavior mode", "agent behavior modes", "response policy layer"]
tags: [agent-engineering, coding-agents, context, workflow]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent Output Styles

## Definition
Agent Output Styles are explicit response-policy modes that change how an AI agent communicates and allocates work while leaving the underlying task substrate, tools, codebase context, and model knowledge mostly unchanged.

## Scope
This concept covers delivery versus explanatory versus learning/HITL behavior over the same coding-agent substrate. In [[Anthropic brings Claude's Learning Mode to regular users and devs]], Claude Code output styles are the concrete example: Default, Proactive, Explanatory, and Learning modes are selected through Claude Code settings and implemented as system-prompt-level behavior changes. The broader agent-engineering lesson applies to [[Hermes Agent]] and [[Codex]] only as a design hypothesis: a mode should be explicit, opt-in, visible in task state, and evaluated before it changes workflows.

## Contrasts
- Versus [[Context Engineering]]: context engineering decides what information and constraints the agent sees; output styles decide how the agent behaves with that information.
- Versus [[Thin Harness Fat Skills]]: a skill can contain durable domain procedure and supporting files; an output style is narrower when it mainly changes response policy, but Anthropic's consumer migration from styles to skills shows the boundary can blur.
- Versus generic prompt tone: a serious output style changes task allocation, explanation density, human checkpoints, and sometimes cost/latency, not just voice.
- Versus model selection: the same model can run in different modes; mode quality still needs evaluation.

## Evidence
- [[Anthropic brings Claude's Learning Mode to regular users and devs]] reports the secondary launch framing and preserves Alpha's primary-source checks against Claude Code output-style docs and changelog.
- [[Claude Code]] records output styles as a product-surface pattern for learning-preserving coding, not proof that the styles improve skill retention.
- [[Learning-preserving AI Assistance]] explains why mode separation matters when the user wants durable understanding rather than only task completion.

## Related
- [[Claude Code]]
- [[Anthropic]]
- [[Learning-preserving AI Assistance]]
- [[TODO(human) Human-in-the-loop Coding]]
- [[Context Engineering]]
- [[Thin Harness Fat Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Codex]]
- [[Hermes Agent]]

## Open Questions
- Should behavior modes be represented in Hermes as task metadata, profile/session selection, a skill, a prompt template, or an eval-only checklist?
- What is the minimum visible mode state needed so users know whether an agent is optimizing for speed, explanation, learning, review, or safety?
- When does the token/cost overhead of explanatory or learning mode produce enough comprehension or review benefit to justify itself?
- If consumer styles move into skills, should agent frameworks prefer explicit skill/instruction bundles over hidden style dropdowns for auditability?
