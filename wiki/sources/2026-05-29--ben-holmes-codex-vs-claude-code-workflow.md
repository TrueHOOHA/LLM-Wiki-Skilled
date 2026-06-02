---
type: source
source_path: raw/sources/2026-05-29-bholmesdev-codex-vs-claude-code-workflow-2055045492137177362.md
title: "Ben Holmes on Codex vs Claude Code workflow"
author: "Ben Holmes"
date: 2026-05-14
tags: [agent-engineering, coding-agents, workflow, social-source]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# Ben Holmes on Codex vs Claude Code workflow

## Summary
Ben Holmes argues that [[Codex]] should be used differently from [[Claude Code]]: not by opening a separate planning mode and asking for a broad plan, but by giving clearer requirements up front, using chat research to converge on a pseudo-plan, then stepping through smaller implementation tasks. The source is weak/social evidence: it is a practitioner X post with a short narrated video transcript and no repo, benchmark, diff comparison, failure-rate data, or reproducible protocol. Its durable value for Tolaria is a workflow hypothesis that connects to [[Context Engineering]], [[Agentic Workflows and Agents]], [[Evaluator-Optimizer Workflow]], and [[Hermes Agent]] review/approval gates: planning should still exist, but may live in chat plus tests rather than in a heavyweight plan document. Treat the tweet phrase "no plans" as shorthand for "avoid a separate planning-mode/document by default," because the video itself describes research and pseudo-planning.

## Key Claims
1. Holmes says his [[Claude Code]] workflow usually starts with planning mode, a vague ask, research/discussion, a phased implementation plan, implementation, then edge-case and code-quality QA.
2. Holmes says his [[Codex]] workflow is more explicit up front: state requirements, let Codex research current libraries and the codebase, reach a pseudo-plan in chat, and optionally write that plan to Markdown.
3. He claims Codex does better when scope is smaller, tasks are sequential, and the destination is clear before implementation.
4. He recommends test-driven development where possible, plus Playwright or other QA checks, before cleanup and PR/merge.
5. The source provides concrete heuristics but not evidence that these heuristics outperform planning-mode or broader agentic workflows across tasks.

## Notable Quotes
- "You should use Codex differently than how you use Claude Code."
- "I just get a little bit more explicit with my requirements upfront."
- "I let Codex as bias towards research, guide us towards a pseudo plan that we get at the end of our chat discussions."
- "CodeX really thrives on just working sequentially through tasks, ideally with test driven development."
- "We queue a together or use playwright test or other means to test that work."
- "Then we do some cleanup at the end before we pull request or merge a feature."

## Entities Mentioned
- [[Ben Holmes]]
- [[Codex]]
- [[Claude Code]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[Codex Sequential TDD Workflow]]
- [[Context Engineering]]
- [[Agentic Workflows and Agents]]
- [[Evaluator-Optimizer Workflow]]
- [[Two-lane Agent Review]]

## Follow-ups
- Preserve as a low-confidence Codex workflow hypothesis, not as an operating rule.
- If Overseer later asks for practical validation, the natural non-knowledge follow-up would be an approved eval comparing chat pseudo-planning plus small TDD tasks against separate plan-document workflows on local Codex tasks; Beta must not create that eval or workflow change from this card.
