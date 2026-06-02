---
type: concept
aliases: ["browser agent amnesia", "discovery tax", "site rediscovery tax"]
tags: [browser-agents, skills, cost-optimization]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Browser Agent Discovery Tax

## Definition
Browser Agent Discovery Tax is the repeated cost, latency, and failure risk incurred when a browser agent re-discovers the same website structure, hidden APIs, selectors, JavaScript behavior, and workflow gotchas on every run instead of loading durable site-specific memory.

## Scope
The concept applies to messy web workflows: dynamic rendering, undocumented endpoints, multi-step forms, login or wizard flows, bot friction, redirects, and site-specific quirks. It does not imply every browser task needs high-agency exploration; deterministic parsing should be probed first.

## Contrasts
- Versus one-time exploration: paying discovery once may be acceptable if the result becomes reusable.
- Versus [[Compounding AI Knowledge Stack]]: discovery tax is one browser-agent failure mode; the compounding stack is the larger memory and evaluation architecture.
- Versus prompt caching: caching stable context can reduce repeated prompt cost, but skill artifacts preserve operational knowledge for future agents and humans.

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] makes this the central problem statement and gives Browserbase's Craigslist/form-fill examples.
- [[Agent-generated Browser Skills]] captures the proposed reusable-memory solution.

## Related
- [[Autobrowse]]
- [[Agent-generated Browser Skills]]
- [[Trace-driven Strategy Iteration]]
- [[Compounding AI Knowledge Stack]]
- [[Prompt Caching for Agent Context]]

## Open Questions
- Which recurring Hermes/Tolaria browser tasks, if any, pay enough discovery tax to justify a future approved skill/eval rather than ordinary fetch/search tooling?
- What instrumentation is needed to measure this tax without adding more overhead than it saves?
