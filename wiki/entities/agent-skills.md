---
type: entity
aliases: ["Agent Skills", "AgentSkills", "agentskills.io"]
tags: [skills, agent-engineering, standards]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Agent Skills

## Identity
Agent Skills is an open skill format and documentation site describing portable skill folders built around a required `SKILL.md` plus optional scripts, references, assets, templates, and other resources.

## Aliases
- Agent Skills
- AgentSkills
- agentskills.io

## Key Attributes
- Core artifact: a folder containing `SKILL.md` metadata and instructions, optionally bundled with scripts, references, templates, and assets
- Loading model: progressive disclosure from discovery metadata, to full activation, to execution with supporting files
- Claimed benefit: package specialized knowledge, repeatable workflows, and cross-product reuse in a version-controlled form
- Relevance to Browserbase: corroborates the broader portable skill artifact shape used by [[Autobrowse]] and [[Browse.sh]], but does not validate Browserbase benchmark claims
- Relevance to Marketing Skills: supplies the format vocabulary behind [[Marketing Skills]] compatibility claims, but does not prove that every host implements identical permissions, helper execution, or review semantics

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] includes the Agent Skills overview as a related inspected source and records its progressive-disclosure and folder-format details.
- [[LLMJunky X post on Marketing Skills for AI Agents]] records the Agent Skills spec as a related inspected source and shows how [[Marketing Skills]] uses the format for a large vertical skill library with root-context dependencies, validation guidance, and Claude plugin packaging.

## Related
- [[Autobrowse]]
- [[Browse.sh]]
- [[Agent-generated Browser Skills]]
- [[Thin Harness Fat Skills]]
- [[Hermes Agent]]
- [[Marketing Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Skill Validation Patterns]]

## Open Questions
- Which Agent Skills clients implement the same permission, sandbox, and helper-file semantics in practice?
- What evaluation standard is sufficient before importing a third-party skill into a Hermes-owned workflow?
