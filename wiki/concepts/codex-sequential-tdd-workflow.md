---
type: concept
aliases: ["sequential Codex workflow", "chat pseudo-plan TDD workflow", "small-step Codex TDD"]
tags: [agent-engineering, coding-agents, workflow, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Codex Sequential TDD Workflow

## Definition
Codex Sequential TDD Workflow is the low-confidence hypothesis that [[Codex]] works best when the operator gives explicit requirements, uses chat-guided research to form a pseudo-plan, then asks for smaller sequential implementation steps validated by TDD, Playwright, or other QA checks before cleanup and PR/merge. [[How AI assistance impacts the formation of coding skills]] adds that when the task goal includes learning, tests alone are not enough: the loop should also preserve human comprehension and debugging practice.

## Scope
This concept covers coding-agent task framing and execution cadence: upfront requirements, codebase/library research, pseudo-planning in chat, small steps, tests, browser checks, cleanup, and review readiness. It does not mean "no planning" literally, does not prove Codex is superior to [[Claude Code]], and does not authorize Hermes skill/config changes or coding-workflow changes without Overseer approval. For unfamiliar-library work, it overlaps with [[Learning-preserving AI Assistance]] because the operator may need to understand the code rather than merely accept it.

## Contrasts
- Versus separate plan-document workflows: this pattern keeps planning lighter and closer to chat/research unless a durable Markdown plan is explicitly useful.
- Versus broad autonomous implementation: the pattern constrains scope and sequence so the model has a clear destination before code changes.
- Versus untested code generation: the pattern treats tests, Playwright, QA, and cleanup as part of the loop, aligning with [[Evaluator-Optimizer Workflow]] and [[Two-lane Agent Review]] concerns.
- Versus pure learning mode: this workflow can remain delivery-focused unless the task explicitly asks for skill acquisition.

## Evidence
- [[Ben Holmes on Codex vs Claude Code workflow]] provides the direct but weak/social practitioner claim for this workflow.
- [[Codex vs Claude Code Workflow Hypothesis Assessment]] compares the claim with existing Tolaria agent-workflow material and keeps it as a hypothesis rather than an adoption rule.
- [[How AI assistance impacts the formation of coding skills]] does not test Codex, but it supports a caution that high-pass-rate AI coding can still leave the operator weak at debugging, code reading, and conceptual explanation.

## Related
- [[Codex]]
- [[Claude Code]]
- [[Ben Holmes]]
- [[Context Engineering]]
- [[Agentic Workflows and Agents]]
- [[Evaluator-Optimizer Workflow]]
- [[Two-lane Agent Review]]
- [[Learning-preserving AI Assistance]]
- [[AI-assisted Coding Skill Formation]]
- [[Hermes Agent]]

## Open Questions
- What task size threshold makes sequential Codex tasks more reliable than a broader plan-and-implement pass?
- Which checks matter most for local Codex work: unit tests, TDD red/green discipline, Playwright/browser checks, lint/typecheck, human spec review, PR cleanup, or no-AI comprehension checks?
- Does the pattern hold for non-UI tasks where Playwright is irrelevant?
- Which Codex tasks should be explicitly labeled learning mode instead of delivery mode?
