---
type: synthesis
question: "Which reusable agent-engineering workflow patterns from Matt Pocock's AI Hero skills changelog should Tolaria preserve, and which require approval before operational adoption?"
tags: [agent-engineering, skills, workflows, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# AI Hero Skills Workflow Patterns Assessment

## Question / Purpose
Assess [[Matt Pocock AI Hero skills changelog]] as a source for reusable agent-engineering patterns relevant to [[Hermes Agent]], while keeping the task knowledge-only and avoiding direct Hermes skill changes.

## Answer / Analysis
The strongest counterargument is that this source is partly marketing: the X post, homepage, and changelog provide practitioner claims, repository popularity, and author experience, not controlled evidence that these skills improve outcomes. The GitHub skill files are stronger evidence only for what the skills instruct agents to do. Confidence is therefore moderate for the existence and shape of the mechanisms, but low for generalized effectiveness.

The useful Tolaria extraction is a compact pattern set. [[Session Handoff Artifact]] sharpens a known Hermes need: moving work across long sessions without dumping the whole transcript, while referencing existing artifacts instead of duplicating them and redacting secrets. Hermes already has stronger durable task-state machinery through Kanban worker context, comments, block reasons, metadata, and optional progress/handoff templates; AI Hero's comparative advantage is the explicit "suggested skills" and "reference existing artifacts" rule.

[[Throwaway Prototype Spike]] is a practical Codex/GPT workflow primitive, but it is outside Beta's authority to execute. The pattern is worth preserving because it frames prototypes as question-answering experiments for UI taste or business-logic/state-machine uncertainty. The durable artifact should be the answered question and decision rationale, not prototype code.

[[Instruction Priority Control]] is the most generally applicable prompt-design lesson. The reported `/grill-with-docs` bug suggests that supporting information can accidentally overpower core instructions, causing agents to implement when they should ask questions. XML-style supporting-info tags are a plausible convention for lowering priority, but they should be treated as a hypothesis to evaluate in Hermes' actual prompt stack rather than a universal fix.

[[Agent-ready Triage Labeling]] maps external issue labels to execution readiness. Hermes already has a stronger internal state model via Kanban, so this should remain a reference unless Overseer later approves GitHub/Kanban label mapping. [[Two-lane Agent Review]] is the most approval-worthy operational idea: split review into repo coding standards and spec/PRD fidelity, because agent diffs often fail along one axis while looking good on the other.

## Comparison Table
| Pattern | Evidence from source | Hermes/Tolaria comparison | Disposition |
|---|---|---|---|
| [[Session Handoff Artifact]] | Raw skill file specifies temporary markdown handoff, suggested skills, artifact references, and redaction. | Hermes already has Kanban comments/metadata/worker context; AI Hero adds useful field-level reminders. | Keep as reference; consider approved template review later. |
| [[Throwaway Prototype Spike]] | Raw prototype skill defines disposable logic/UI branches and durable answer capture. | Useful for Codex/business logic/UI uncertainty, but creating prototypes is non-knowledge work. | Preserve concept; prototype only if Overseer approves. |
| [[Instruction Priority Control]] | Changelog says XML supporting-info reduced instruction loudness. | Relevant to Hermes prompt/context hierarchy and weak-source handling. | Keep as hypothesis; eval before skill changes. |
| [[Agent-ready Triage Labeling]] | `/to-prd` and `/to-issues` changed label to `ready-for-agent-triage`. | Hermes Kanban already encodes readiness; external label mapping would be a system integration. | Reference only unless integration approved. |
| [[Two-lane Agent Review]] | Review preview splits standards check from issue/PRD fidelity check. | Aligns with review-required gates and code-review practice; needs evidence and routing design. | Draft as future approval proposal/eval candidate. |

## Citations
- [[Matt Pocock AI Hero skills changelog]]: source summary and raw excerpts for `/handoff`, `/prototype`, XML supporting-info, ready-for-agent-triage labels, and two-lane review preview.
- [[Hermes Agent]]: current Tolaria entity for Hermes as the relevant agent framework and approval-gated workflow target.
- [[Thin Harness Fat Skills]]: existing Tolaria pattern that frames rich skills as the right location for reusable procedures when approved.
- [[Agent-Computer Interface Design]]: existing design lens for making agent-facing tools and instructions mistake-resistant.
- [[Evaluator-Optimizer Workflow]] and [[Orchestrator-Worker Workflow]]: adjacent review/decomposition patterns that explain where two-lane review fits.

## Implications
- Do not patch Hermes skills from this source alone; the strongest claims are still weak-to-medium evidence.
- Treat AI Hero's handoff and prototype prompts as reference examples for future approved Hermes skill/template review.
- If Overseer wants an operational change, the best candidate is an eval or review of existing Hermes handoff/review workflows against: artifact-reference discipline, redaction, suggested skills, spec-fidelity lane, coding-standards lane, and durable answer capture for prototypes.
- The ready-for-agent-triage label should not displace Hermes Kanban state; at most it can inform a future GitHub/Kanban bridge mapping.

## Recommended Next Actions
1. Reference-only now: preserve the source, entities, concepts, and this synthesis.
2. Approval proposal candidate: "Approve a future knowledge-guided review of Hermes handoff/review templates against AI Hero's artifact-reference, redaction, suggested-skills, and two-lane review patterns; no code or skill patch without separate approval."
3. Eval candidate if later approved: compare current review-required handoff quality against a two-lane review rubric on a small set of completed Codex/Hermes tasks.
4. Prototype candidate if later approved: only use throwaway prototypes when a task has a crisp unanswered UI/state/business-logic question and a deletion/absorption rule.

## Follow-up Questions
- Should Overseer approve a later template/review audit for Hermes handoff and code-review workflows using these patterns as a checklist?
- If an eval is approved, which lane matters first: code standards, spec fidelity, handoff compactness, or context-priority failures?
