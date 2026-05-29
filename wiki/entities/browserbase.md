---
type: entity
aliases: ["Browserbase"]
tags: [browser-agents, company, agent-infrastructure]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Browserbase

## Identity
Browserbase is the browser-agent infrastructure company behind [[Autobrowse]], [[Browse.sh]], Stagehand, Browserbase browser primitives, web data APIs, runtime, identity, model gateway, and observability surfaces described in [[Browserbase Autobrowse browser-skill loop]].

## Aliases
- Browserbase

## Key Attributes
- Category: browser-agent infrastructure company
- Relevant products in this source: [[Autobrowse]], [[Browse.sh]], Browse CLI, browser/web-data/runtime/identity/model/observability primitives, Stagehand, Director
- Internal-agent pattern in related source: one generalized `bb` agent using ephemeral Linux sandboxes, OpenCode, markdown skills, scoped permissions, proxy-mediated integrations, and short-lived credential references
- Evidence quality: primary/vendor; strong for what Browserbase says it built, medium/weak for performance or productivity claims without independent replication

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] summarizes Browserbase's article and related links, including concrete workflow mechanics and unverified benchmark claims.

## Related
- [[Autobrowse]]
- [[Browse.sh]]
- [[Agent-generated Browser Skills]]
- [[Browser Agent Discovery Tax]]
- [[OpenCode]]
- [[Hermes Agent]]

## Open Questions
- Which Browserbase claims have independent benchmark data or reproducible traces outside the vendor articles?
- Which parts of the Browserbase internal-agent model are transferable to Hermes without adopting Browserbase-specific infrastructure?
