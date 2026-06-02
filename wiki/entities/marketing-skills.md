---
type: entity
aliases: ["Marketing Skills for AI Agents", "coreyhaines31/marketingskills", "marketingskills"]
tags: [skills, agent-engineering, marketing]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Marketing Skills

## Identity
Marketing Skills is Corey Haines's public `coreyhaines31/marketingskills` repository of Agent Skills-style marketing workflows for AI agents, covering CRO, copywriting, SEO, analytics, growth engineering, email, paid acquisition, launch, pricing, retention, and related domains.

## Aliases
- Marketing Skills for AI Agents
- coreyhaines31/marketingskills
- marketingskills

## Key Attributes
- Repository shape: `skills/` directories with `SKILL.md` files, a `tools/` area with zero-dependency Node CLI files and integration guides, `AGENTS.md` agent instructions, and `.claude-plugin/marketplace.json` packaging.
- Cross-skill architecture: `product-marketing` is documented as the root context skill read before other marketing skills, creating a shared product/audience/positioning layer.
- Distribution claims: README says the skills work with Claude Code, OpenAI Codex, Cursor, Windsurf, and clients that support the [[Agent Skills]] spec.
- Tool ecosystem: `tools/REGISTRY.md` indexes marketing tools by API, MCP, CLI, SDK, and integration guide availability.
- v2.0 repo-backed migration pattern: README and `VERSIONS.md` document 17 breaking skill renames, `page-cro`/`form-cro` consolidation into `cro`, cleanup instructions for stale old-name folders, and migration of product context from `.claude/product-marketing-context.md` to `.agents/product-marketing.md` with fallbacks.
- Support-file/eval shape: current repo tree inspection found 42 `skills/*/SKILL.md` files, 42 `skills/*/evals/evals.json` files, 85 skill reference files, 64 Node CLI wrappers, `.claude-plugin/` manifests, `tools/REGISTRY.md`, `AGENTS.md`, and `VERSIONS.md`.
- Evidence quality: existence, structure, and scope are source-backed; social launch claims, marketing performance, safety, eval quality, and Hermes fit remain unproven.

## Evidence
- [[LLMJunky X post on Marketing Skills for AI Agents]] records the weak social discovery layer plus Alpha's source-check against README, AGENTS.md, the Agent Skills spec, GitHub tree counts, and `tools/REGISTRY.md`.
- [[Corey Haines X post on Marketing Skills v2.0]] records the author announcement and a fresh repo-tree check for the v2 skill-pack architecture: shorter/breaking names, unified CRO, root product context, support-file layout, plugin metadata, tool registry, and per-skill eval file presence.

## Related
- [[Agent Skills]]
- [[Hermes Agent]]
- [[Domain-specific Agent Skill Libraries]]
- [[Skill Validation Patterns]]
- [[Thin Harness Fat Skills]]
- [[Catalog-backed Agent Tool Distribution]]

## Open Questions
- Does the `product-marketing` root context skill measurably improve downstream marketing-skill outputs compared with independent skills?
- Which compatibility claims hold across Claude Code, Codex, Cursor, Windsurf, Hermes, and generic Agent Skills clients in practice?
- How should large skill packs communicate breaking renames so agents do not keep invoking stale installed folder names?
- What review, sandbox, provenance, and eval gates would be required before any Marketing Skills pattern or tool is adapted into Hermes-owned skills?
