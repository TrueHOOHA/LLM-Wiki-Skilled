---
type: concept
aliases: ["domain skill library", "domain-specific skill ecosystem", "vertical skill library", "agent skill ecosystem"]
tags: [skills, agent-engineering, knowledge-management]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# Domain-specific Agent Skill Libraries

## Definition
Domain-specific Agent Skill Libraries are curated collections of related agent skills that share a domain model, naming conventions, dependency map, validation rules, and optional tool registry so an agent can perform many tasks in one vertical without loading a monolithic prompt.

## Scope
This concept covers large vertical libraries such as [[Marketing Skills]], where individual skills are narrow enough for task routing but are coordinated by a root context skill, related-skill links, support files, version/migration notes, and optional registry/eval layers. It does not mean importing third-party skills directly into Hermes; adoption changes future agent behavior and requires separate approval and evaluation.

## Contrasts
- Versus a single umbrella skill: a library can route to focused skills while maintaining shared context through a root skill.
- Versus unrelated skill folders: a domain library exposes dependency maps, related-skill sections, stable naming conventions, migration notes for breaking renames, and consistent frontmatter/validation expectations.
- Versus a tool catalog alone: a skill library teaches when/how to act, while a registry such as [[Catalog-backed Agent Tool Distribution]] documents external tool surfaces.
- Versus Tolaria source notes: a skill library changes execution behavior; Tolaria preserves source-backed knowledge until an approved system-development lane adapts it.

## Evidence
- [[LLMJunky X post on Marketing Skills for AI Agents]] records [[Marketing Skills]] as a concrete large vertical library: 42 marketing `SKILL.md` files, `product-marketing` as a root context skill, related-skill links, Agent Skills compatibility claims, Claude plugin packaging, validation notes, and a marketing tool registry.
- [[Corey Haines X post on Marketing Skills v2.0]] adds the versioning case study: the author announcement claims shorter names and a unified CRO skill; repo inspection corroborates v2.0 breaking rename notes, stale-folder cleanup guidance, current per-skill eval-file presence, support-file layout, plugin metadata, and registry-backed tool discovery.
- [[Kappaemme X post on Local Client Prospector Codex skill]] is a much smaller single-skill case: it shows how one domain procedure can bundle input defaults, browser workflow, scoring schema, output schema, quality checks, and compliance guardrails into a focused `SKILL.md` rather than a full library.

## Related
- [[Marketing Skills]]
- [[Agent Skills]]
- [[Thin Harness Fat Skills]]
- [[Skill Validation Patterns]]
- [[Agent-Computer Interface Design]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Local Client Prospector]]
- [[NPM-packaged Codex Skills]]

## Open Questions
- When does a root context skill improve outputs versus become stale, oversized, or over-authoritative?
- What dependency-map and migration-note format should Hermes/Tolaria prefer for large skill families if Overseer later approves a workflow/system lane?
- How should skill-library quality be evaluated: task success, source fidelity, tool safety, routing accuracy, maintenance cost, or human correction rate?
