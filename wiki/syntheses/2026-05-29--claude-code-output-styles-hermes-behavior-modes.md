---
type: synthesis
question: "What should Claude Code output styles and Learning Mode imply for Hermes/Codex behavior modes?"
tags: [agent-engineering, coding-agents, learning, workflow]
created: 2026-05-29
updated: 2026-05-29
---

# Claude Code Output Styles and Hermes Behavior-mode Implications

## Question / Purpose
Assess [[Anthropic brings Claude's Learning Mode to regular users and devs]] as source-checked evidence for coding-agent behavior modes, then translate the useful parts into Tolaria/Hermes/Codex implications without creating any skill, prompt, config, eval, prototype, or follow-up task.

## Answer / Analysis
Strongest counterargument first: Anthropic's output styles do not prove that Hermes or local Codex should add a behavior-mode abstraction. The source proves a product mechanism exists in Claude Code and that Anthropic frames it as educational, but it does not provide controlled outcome data showing better code quality, faster review, stronger retention, fewer defects, or lower operator burden. Explanatory and Learning modes also carry explicit token/cost overhead, and hidden/persistent modes can confuse auditability if task records do not show which mode was active.

The useful signal is narrower and practical. [[Agent Output Styles]] separates behavior policy from project knowledge: the same codebase, model, and tools can run in delivery mode, explanatory mode, or learning/HITL mode. That maps cleanly onto existing Tolaria concepts: [[Context Engineering]] controls what the model sees; [[Thin Harness Fat Skills]] and skills/instructions hold durable behavior; [[Memory Hygiene for AI Agents]] prevents temporary mode choices from silently becoming permanent preferences; [[Learning-preserving AI Assistance]] defines when slower pedagogy is appropriate.

The strongest mechanism is [[TODO(human) Human-in-the-loop Coding]]. It turns learning from "the assistant explains more" into a bounded work-allocation rule: the agent scaffolds the task but marks small pieces for the human to implement. This is more testable than vague educational tone. A future eval could compare delivery-only, explanation-only, and TODO(human) variants on unfamiliar-library tasks by measuring later debugging, modification, and explanation performance.

For [[Hermes Agent]], the implication is approval-gated design vocabulary, not immediate implementation. A safe behavior-mode checklist would require explicit mode declaration, task-local persistence, cost/latency expectation, visible logs/metadata, exit criteria, and a proof metric. For [[Codex]], this should be treated as a local workflow question: prompt-scoped learning/HITL instructions may be enough before any new persistent skill or system-prompt machinery is justified.

## Comparison Table
| Mode | Primary goal | Human role | Risk | Tolaria interpretation |
| --- | --- | --- | --- | --- |
| Delivery/default | Complete the task efficiently | Specify/review/approve | Shallow understanding on unfamiliar work | Appropriate when learning is not a goal and verification is strong. |
| Explanatory | Complete plus explain decisions | Read insights and ask follow-ups | Extra prose can become costly noise | Useful for review and onboarding if measured against comprehension/review quality. |
| Learning/TODO(human) | Preserve skill through participation | Implement bounded pieces | Slower, may block progress or create awkward TODOs | Best candidate for an explicit eval because it changes work allocation, not only style. |
| Skill/instruction bundle | Durable reusable behavior | Select or invoke explicit skill | Skill sprawl or stale instructions | More auditable than hidden style state when behavior should persist across sessions. |

## Citations
- [[Anthropic brings Claude's Learning Mode to regular users and devs]]: secondary article plus captured primary-source checks for Claude Code output styles, `TODO(human)`, token overhead, and consumer styles moving toward skills.
- [[Agent Output Styles]]: concept extracted from the Claude Code mechanism.
- [[TODO(human) Human-in-the-loop Coding]]: focused HITL learning pattern extracted from Claude Code Learning mode.
- [[Learning-preserving AI Assistance]] and [[AI-assisted Coding Skill Formation]]: existing Tolaria evidence base for why delivery-only assistance can conflict with skill formation.
- [[Hermes Agent]], [[Codex]], and [[Claude Code]]: entities affected by the workflow comparison.

## Implications
- Behavior mode should be explicit and task-local; hidden persistent mode state is dangerous for auditability.
- Learning/HITL mode should be opt-in for unfamiliar material, onboarding, or oversight-skill formation; it should not slow ordinary production work by default.
- A useful future checklist would evaluate three separate outcomes: deliverable correctness, human comprehension/retention, and cost/latency overhead.
- Anthropic's consumer migration from styles to skills supports a Hermes-relevant hypothesis: durable behavior belongs in explicit skills/instructions, while temporary mode choices belong in visible task/session metadata.

## Follow-up Questions
- Approval proposal for Overseer: authorize a future non-Beta eval/checklist for Hermes/Codex behavior modes comparing delivery, explanatory, and TODO(human) learning modes on unfamiliar-codebase tasks. Suggested success metrics: later debugging task, modification task, concise explanation quality, tests passed, human correction burden, and token/time cost.
- If such an eval is approved later, should it start as prompt-scoped Codex practice, a Hermes task-metadata convention, or a true skill/profile abstraction?
