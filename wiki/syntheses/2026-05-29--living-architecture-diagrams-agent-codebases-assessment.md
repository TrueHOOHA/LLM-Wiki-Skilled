---
type: synthesis
question: "Should living architecture diagrams and multi-altitude review become a Tolaria/Hermes control-surface hypothesis for agent-written codebases?"
tags: [agent-engineering, architecture, code-review, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Living Architecture Diagrams for Agent-written Codebases Assessment

## Question / Purpose
Assess [[Chrys Bader X post on agent-written codebases and living architecture diagrams]] as a weak social source, compare its hypothesis with existing Tolaria notes on agent/code review and workflow gates, and preserve any useful Hermes/Codex implications without implementing or prototyping anything.

## Answer / Analysis
The strongest counterargument is that the tweet does not prove the workflow works. It gives an anecdote about an unnamed founder/CTO plus an explanatory diagram, but no repository, architecture artifact, before/after comparison, measurable review outcome, or maintenance protocol. Treat it as a vocabulary seed and eval candidate, not as adoption guidance.

The useful claim is still worth preserving because it matches several existing Tolaria patterns. [[Agent-Computer Interface Design]] says agent-facing tools and instructions should make correct action obvious; this source applies a parallel idea to codebases produced by agents: the software architecture itself needs an explicit interface for human oversight. [[Two-lane Agent Review]] separates standards review from spec fidelity; [[Multi-altitude Agent Code Review]] separates architecture, patterns/interfaces, and file-level implementation. Together they suggest future review rubrics should avoid vague "looks good" approvals and instead name which layer was checked.

The source also fits [[Thin Harness Fat Skills]] and [[Context Engineering]] indirectly. If a codebase is mostly agent-written, the durable context should not live only in scattered generated files or chat history. A maintained architecture diagram can become part of the task context given to Codex or other coding agents, while the harness remains thin and the reusable project knowledge stays explicit. That is plausible, but the evidence is currently weak.

## Evidence Grades
| Claim or pattern | Evidence grade | Tolaria interpretation |
|---|---:|---|
| Agent-made codebases can become unintelligible after months of unstructured generation | Weak | Plausible anecdote; needs stronger cases or internal examples before generalizing. |
| Architecture-first alignment should precede agentic building | Weak-to-medium as workflow advice | Consistent with ACI/context-engineering principles, but not directly validated by this source. |
| Agents should maintain a living architecture diagram | Weak | Useful eval hypothesis; needs a schema, update protocol, and drift checks before adoption. |
| Review attention should vary by altitude: architecture, patterns/interfaces, files | Weak but useful framing | Can be preserved as [[Multi-altitude Agent Code Review]] and compared to existing review gates. |
| File-level delegation is safer when architecture and critical interfaces are explicit | Weak-to-medium as risk model | Reasonable control-surface framing; needs Codex/Hermes task evidence before operational use. |

## Comparison Table
| Existing Tolaria pattern | Connection | Tension / caveat |
|---|---|---|
| [[Agent-Computer Interface Design]] | Both emphasize explicit interfaces and mistake-resistant control surfaces. | ACI is better supported by Anthropic/practitioner evidence; this source is only social. |
| [[Two-lane Agent Review]] | Adds a review-lane idea: code standards/spec fidelity can be crossed with architecture/pattern/file altitudes. | More lanes can create ceremony unless evals show better defect detection or faster review. |
| [[Evaluator-Optimizer Workflow]] | A living diagram could become an evaluator rubric or context artifact. | No evaluator loop should be created without a measurable rubric and approval. |
| [[Thin Harness Fat Skills]] | Places reusable project structure in explicit artifacts instead of hidden harness behavior. | Architecture diagrams can go stale unless updates are verified against code. |
| [[Context Engineering]] | Architecture diagrams can become high-value task context for Codex/Hermes. | Too much stale context can mislead agents; dynamic loading and freshness checks matter. |
| [[Session Handoff Artifact]] | Both prevent future agents/humans from replaying all prior work. | Handoffs are session-specific; architecture diagrams are persistent system-level context. |

## Practical Implications
- For Codex/Hermes coding work, a future approved eval could compare ordinary diff review against a compact architecture/pattern/file review checklist plus a living diagram update requirement.
- The lowest-risk use is knowledge-only: preserve the vocabulary and use it as a review lens when reading future coding-workflow sources.
- The highest-risk failure mode is stale diagram authority: an outdated architecture diagram could make agents and reviewers more confident while less aligned with the actual code.
- If tested later, success should be measured by concrete outcomes: interface break detection, spec-fidelity defects found, onboarding/review time, rework rate, diagram drift, and human correction count.

## Recommended Next Actions
1. Archive and synthesize now: completed by this source/concept/synthesis cluster.
2. Do not create diagrams, templates, scripts, Codex instructions, skill patches, review gates, or Kanban follow-up tasks from this Beta card.
3. Approval proposal candidate for Overseer: "Approve a small Default/Overseer-lane evaluation on one future Codex/Hermes coding task: require the coding agent to maintain a compact architecture/pattern/interface note, then compare review quality and drift against ordinary diff review. No workflow adoption unless the eval finds measurable benefit."
4. Until stronger evidence exists, treat living architecture diagrams as a weak but useful control-surface hypothesis rather than a standard practice.

## Citations
- [[Chrys Bader X post on agent-written codebases and living architecture diagrams]]: source for the architecture/pattern/file altitude claim and living-diagram hypothesis.
- [[Living Architecture Diagram]] and [[Multi-altitude Agent Code Review]]: concepts extracted from the source.
- [[Agent-Computer Interface Design]], [[Two-lane Agent Review]], [[Thin Harness Fat Skills]], [[Context Engineering]], [[Evaluator-Optimizer Workflow]], and [[Session Handoff Artifact]]: existing Tolaria concepts used for comparison.
- [[Anthropic Building Effective Agents and Hermes Workflow Implications]] and [[AI Hero Skills Workflow Patterns Assessment]]: existing syntheses that provide stronger adjacent practitioner context around evaluation gates and review separation.

## Implications
This source should not change Hermes/Codex workflows by itself. Its durable value is a compact frame for future review discussions: humans should make system-level meaning legible before asking agents to move quickly at file level. If Overseer later approves a test, the test should be narrow, reversible, and judged by drift and defect-detection evidence rather than by the aesthetic appeal of diagrams.

## Follow-up Questions
- Should Overseer later approve a small Default/Overseer-lane evaluation of a living architecture/pattern/interface note on one Codex/Hermes coding task?
- If approved, what should dominate the evaluation: interface break detection, spec fidelity, architecture drift, review speed, rework rate, or onboarding clarity?
