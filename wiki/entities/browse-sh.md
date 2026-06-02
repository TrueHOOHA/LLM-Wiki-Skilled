---
type: entity
aliases: ["Browse.sh", "Browse CLI", "browse"]
tags: [browser-agents, skills, cli]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Browse.sh

## Identity
Browse.sh is Browserbase's public catalog and CLI ecosystem for installable browser skills, described as an open catalog of 100+ curated skills powered by [[Autobrowse]].

## Aliases
- Browse.sh
- Browse CLI
- browse

## Key Attributes
- Provider: [[Browserbase]]
- Claimed install path in related source: `npm i -g browse`, then `browse skills add ...`
- Claimed artifact shape: a browser-focused `SKILL.md` plus helper scripts and site-specific gotchas
- Claimed categories: marketplaces, food/dining, travel, government, developer tools, and enterprise SaaS partner integrations
- Relevance: concrete example of [[Agent-generated Browser Skills]] distributed through a [[Agent-native CLI]]-like catalog
- Evidence quality: primary/vendor; credible for launch mechanics, unverified for catalog quality and production reliability

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] includes the related Browse.sh launch article and records the claimed catalog, CLI, install flow, and skill examples.

## Related
- [[Browserbase]]
- [[Autobrowse]]
- [[Agent Skills]]
- [[Agent-generated Browser Skills]]
- [[Agent-native CLI]]
- [[Catalog-backed Agent Tool Distribution]]

## Open Questions
- How many Browse.sh skills are independently validated beyond Browserbase's own status labels?
- What permission, credential, and sandbox boundaries are needed before an agent should run third-party browser skills locally?
