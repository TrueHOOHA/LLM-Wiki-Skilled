---
type: concept
aliases: ["agent tool catalog", "registry-backed CLI distribution", "catalog-backed skills", "registry-backed agent tool catalogs", "Printing Press Library"]
tags: [agent-tooling, cli, skills, supply-chain]
created: 2026-05-29
updated: 2026-05-29
source_count: 4
---

# Catalog-backed Agent Tool Distribution

## Definition
Catalog-backed agent tool distribution is the pattern of publishing installable tools plus their matching agent skills through a searchable registry, so an agent or operator can discover, install, update, and uninstall domain tools by name or category.

## Scope
In the Printing Press case, the catalog layer is the public library and npm-backed installer for generated Go CLIs and focused skills. In the [[Marketing Skills]] case, `tools/REGISTRY.md` is a knowledge/index layer that maps marketing tools by API, MCP, CLI, SDK, and integration guide availability. In the [[Local Client Prospector]] case, the catalog is minimal—a tweet/portfolio/repo/npm package rather than a full registry—but it still illustrates the boundary between discovery metadata and executable installation into a local agent-skill path. The pattern includes registry metadata, category filters, install/update/uninstall semantics when a live installer exists, auth/env/license caveats, and links between executable tools and agent-facing skills. It is useful for discovery and reproducibility, but it is also a supply-chain boundary because installers, scripts, MCP servers, and credentialed APIs can modify local state or call external services.

## Contrasts
- Versus ad hoc tool installation: a catalog gives searchable metadata, categories, and install/update/uninstall commands.
- Versus a knowledge-only index: a live installer changes the system; a Tolaria index can preserve discovery metadata without executing installation.
- Versus a package manager alone: the catalog couples executable CLIs with agent-facing usage skills and MCP metadata.

## Evidence
- [[Printing Press — agent-native CLIs from a single prompt]] records the library repo and homepage claims about registry search, install, update, uninstall, categories, skills, and MCP metadata.
- [[Printing Press Ecosystem Assessment]] recommends discovery-only indexing or candidate evaluation only after explicit approval.
- [[LLMJunky X post on Marketing Skills for AI Agents]] records the Marketing Skills tool registry as a domain-specific registry of marketing APIs, MCPs, CLIs, SDKs, and integration guides.
- [[Corey Haines X post on Marketing Skills v2.0]] adds a fresh repo-tree check: `tools/REGISTRY.md` exists alongside many zero-dependency Node CLI wrappers and integration docs, but this verifies discovery structure only, not runtime safety or credential handling.
- [[Kappaemme X post on Local Client Prospector Codex skill]] shows a small single-skill distribution path: social/portfolio discovery points to a GitHub repo and npm package whose installer writes a Codex skill into `~/.codex/skills`, making package provenance and overwrite behavior part of the distribution risk.

## Related
- [[Printing Press]]
- [[Agent-native CLI]]
- [[Hermes Agent]]
- [[Marketing Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Local Client Prospector]]
- [[NPM-packaged Codex Skills]]

## Open Questions
- Should Tolaria maintain a non-installing discovery index for Printing Press entries relevant to Overseer?
- What provenance, pinning, and sandbox checks should be mandatory before installing any registry-backed agent tool?
- Should domain skill libraries keep tool registries knowledge-only until each credentialed API/CLI/MCP path passes a separate safety and usefulness review?
- Should npm-distributed agent skills require unpack-and-review workflows before `npx` execution writes into local agent directories?
