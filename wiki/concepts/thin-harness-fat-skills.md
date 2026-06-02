---
type: concept
aliases: ["thin harness fat skills", "fat skills thin harness", "fat data fat skills"]
tags: [agent-framework, skills, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 7
---

# Thin Harness Fat Skills

## Definition
Thin Harness Fat Skills is an agent-architecture pattern where the runtime focuses on routing, tool/model access, and dispatch, while domain behavior lives in rich skill files, deterministic helpers, and accumulated knowledge pages.

## Scope
The pattern covers model-agnostic harnesses, reusable skills, resolver routing, context minimization, and deterministic work outside latent model space. [[Effective Harnesses for Long-running Agents]] is an adjacent caution: even when the runtime harness is relatively simple, long-running tasks may need fat, task-local state artifacts such as feature ledgers, progress logs, init scripts, and verification gates. It should not be read as a literal claim that every useful harness has a small codebase.

## Contrasts
- Thin harnesses route; they should not embed every domain workflow.
- Fat skills encode repeatable procedures, edge cases, tests, and filing rules.
- Fat data preserves the memory that makes future runs more specific.
- [[Agent-generated Browser Skills]] are a browser-specific example: site knowledge, hidden endpoints, selectors, deterministic helpers, and fallback rules live in the skill rather than in the generic browser loop.
- [[Domain-specific Agent Skill Libraries]] are a vertical example: many focused skills share a root context layer and dependency map rather than forcing every host adapter to encode the domain.

## Evidence
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] presents the pattern through GBrain, GStack, OpenClaw, Hermes, and the prior X series on fat skills, resolvers, and naked models.
- [[Anthropic Building Effective Agents and Hermes Workflow Implications]] reinforces the pattern from another direction: keep the harness/workflow simple, make planning transparent, and move complexity into explicit workflow choices, tool interfaces, tests, and review gates rather than hidden framework abstraction.
- [[Matt Pocock AI Hero skills changelog]] supplies concrete skill-file examples of the pattern: handoff, prototype, label, and review workflows live in explicit skill prompts rather than hidden framework behavior.
- [[Browserbase Autobrowse browser-skill loop]] adds a browser-agent variant: Browserbase says Autobrowse moves learned site-specific memory from repeated browser traces into a durable `SKILL.md` plus deterministic helpers.
- [[LLMJunky X post on Marketing Skills for AI Agents]] adds a vertical library variant: [[Marketing Skills]] splits marketing work into many Agent Skills-style folders coordinated by `product-marketing`, related-skill links, validation guidance, and a tool registry.
- [[Corey Haines X post on Marketing Skills v2.0]] adds the maintenance angle: fat skill libraries need stable short names, explicit breaking-change cleanup, support-file layout, and per-skill eval loops so the thin harness does not need to encode domain migration logic.
- [[Effective Harnesses for Long-running Agents]] adds the long-running-task angle: project-local JSON ledgers, progress logs, git history, restart scripts, and browser checks can carry continuity that neither the model nor a generic harness should be expected to infer.

## Related
- [[Hermes Agent]]
- [[OpenClaw]]
- [[GStack]]
- [[Skillify]]
- [[Compounding AI Knowledge Stack]]
- [[Agentic Workflows and Agents]]
- [[Agent-Computer Interface Design]]
- [[AI Hero]]
- [[Session Handoff Artifact]]
- [[Throwaway Prototype Spike]]
- [[Two-lane Agent Review]]
- [[Autobrowse]]
- [[Agent-generated Browser Skills]]
- [[Deterministic-first Browser Automation]]
- [[Marketing Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Skill Validation Patterns]]
- [[Long-running Agent Harness]]

## Open Questions
- Which Hermes behavior belongs in skills versus Tolaria knowledge pages versus deterministic tools?
- If browser-agent skills are ever evaluated for Hermes, what review gate prevents vendor-generated or agent-generated skills from bypassing human audit and sandboxing?
- For large vertical skill families, when should shared domain context live in a root skill, Tolaria page, project file, or explicit task input?
