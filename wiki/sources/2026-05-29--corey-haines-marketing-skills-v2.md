---
type: source
source_path: raw/sources/2026-05-29-coreyhainesco-marketingskills-v2-status-2055011827600572668.md
title: "Corey Haines X post on Marketing Skills v2.0"
author: "Corey Haines / @coreyhainesco"
date: 2026-05-14
tags: [agent-engineering, skills, marketing, social-source]
created: 2026-05-29
source_count: 0
---

# Corey Haines X post on Marketing Skills v2.0

## Summary
This weak social source announces Marketing Skills v2.0 with shorter skill names, a consolidated CRO skill, more refinements, tool integrations, and claimed full eval coverage. The social post is promotional and does not independently prove quality, outcomes, safety, or that the evals were executed successfully. The stronger evidence layer is the linked [[Marketing Skills]] GitHub repository, which currently corroborates the artifact architecture: 42 Agent Skills-style `SKILL.md` files, 42 per-skill `evals/evals.json` files in the repository tree, `product-marketing` as shared context, optional `references/` support files, `.claude-plugin/` marketplace metadata, `VERSIONS.md` migration notes, and a `tools/REGISTRY.md` plus Node CLI/tool-integration layer.

## Key Claims
1. The X post claims v2.0 is a major release with shorter names, 100+ refinements, one unified `/cro` skill, 40 skills, 52 tool integrations, and 100% eval coverage.
2. The repo corroborates the naming/migration pattern: `VERSIONS.md` and README describe v2.0 as a breaking change with 17 renames, a `page-cro`/`form-cro` consolidation into `cro`, and stale-folder cleanup instructions for old installs.
3. The repo corroborates the shared-foundation pattern: README says `product-marketing` is read first by other skills to establish product, audience, and positioning context.
4. The repo corroborates the support-file architecture: `skills/<skill>/SKILL.md` folders can include `references/`, `scripts/`, `assets/`, and `evals/evals.json`, while `AGENTS.md` recommends keeping `SKILL.md` concise and moving details to support files.
5. The repo corroborates a registry-backed tool-discovery layer: `tools/REGISTRY.md` maps marketing tools by API, MCP, CLI, SDK, and integration guide, and the current tree contains many zero-dependency Node CLI wrappers.
6. The repo tree corroborates the presence of per-skill eval files, but this ingestion did not run those evals or verify that every eval is meaningful, current, or quality-improving.

## Notable Quotes
- X post: "The biggest release yet. Shorter names, one unified CRO skill, and a foundation built to scale."
- X post: "40 skills. 52 tool integrations. 100% evals coverage."
- X post: "v2.0 is a breaking change, so reinstall to get the new names."
- README: "The `product-marketing` skill is the foundation — every other skill checks it first to understand your product, audience, and positioning before doing anything."
- AGENTS.md: "Keep `SKILL.md` under 500 lines (move details to `references/`)."

## Entities Mentioned
- [[Marketing Skills]]
- [[Agent Skills]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[Domain-specific Agent Skill Libraries]]
- [[Skill Validation Patterns]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Thin Harness Fat Skills]]
- [[Agent-Computer Interface Design]]

## Follow-ups
- Knowledge-only implication: large skill packs should make naming/versioning migrations explicit, preserve a dependency map, keep support files outside the main `SKILL.md`, separate tool registries from skill instructions, and treat per-skill eval files as claims requiring execution and quality review rather than as proof by existence.
- Approval-gated practical question: if Overseer later wants to adapt this pattern, the safe next step would be a separate evaluation of root-context skill loading, dependency maps, and per-skill eval quality before changing Hermes skills or configuration.
