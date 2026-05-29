---
type: concept
aliases: ["AI coding review bottleneck", "orchestration/review bottleneck", "agent code review bottleneck"]
tags: [agent-engineering, coding-agents, code-review, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# AI Coding Orchestration and Review Bottleneck

## Definition

AI Coding Orchestration and Review Bottleneck is the pattern where agentic coding shifts scarce human effort away from writing code and toward specifying the right work, decomposing it, reviewing agent output, validating behavior, and deciding whether the result satisfies the product/customer goal. [[Zeb Evans on ClickUp 100x Organization]] states this directly as "orchestration" and "review" becoming the primary bottlenecks.

## Scope

This concept covers AI-assisted engineering at the organization level: task selection, prompt/spec quality, architecture decisions, code review, test selection, acceptance checks, and customer-outcome validation. It does not imply that human-written code review is always slower than agent-output review, or that best engineers should only review their own agents. Those are weak-social claims in the current source and need measured comparison across task classes.

## Contrasts

- Versus PR/code volume metrics: more agent-written code can increase downstream review and integration load without improving outcomes.
- Versus [[Two-lane Agent Review]]: two-lane review is one possible review structure; this bottleneck concept names the broader capacity constraint.
- Versus [[Evaluator-Optimizer Workflow]]: evaluator loops can help when criteria are clear, but can also amplify cost and review burden if the target outcome is vague.
- Versus [[Codex Sequential TDD Workflow]]: sequential TDD is a task-level mitigation; the bottleneck can still appear at portfolio/org scale.

## Evidence

- [[Zeb Evans on ClickUp 100x Organization]] is weak-social evidence that ClickUp's CEO sees organization-level AI coding bottlenecks moving to orchestration and review. The post supplies no measured review latency, defect rate, revert rate, customer impact, or comparison between human-authored and agent-authored code.

## Related

- [[AI Coding Outcome Measurement]]
- [[AI-native Organization Design]]
- [[Agent Manager Role]]
- [[Two-lane Agent Review]]
- [[Evaluator-Optimizer Workflow]]
- [[Codex Sequential TDD Workflow]]
- [[Multi-altitude Agent Code Review]]
- [[Agent-Computer Interface Design]]

## Open Questions

- Which measurable bottleneck grows fastest with agent coding: task specification, architecture review, code review, tests, QA, integration, incident response, or product/customer validation?
- Does reviewing one's own agent output outperform reviewing human PRs once defect discovery, blind spots, architectural drift, and production incidents are included?
- What guardrails prevent high-volume AI coding from transferring hidden work to a small group of senior reviewers?
