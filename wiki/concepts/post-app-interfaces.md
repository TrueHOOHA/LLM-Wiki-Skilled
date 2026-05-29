---
type: concept
aliases: ["post-app UI", "API-ified apps", "apps as APIs"]
tags: [agent-engineering, interface-design, platform, weak-evidence]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# Post-app Interfaces

## Definition
Post-app Interfaces are user experiences where a high-level agent or command surface composes services behind the scenes, while standalone applications become APIs, data providers, or capability modules rather than primary user destinations. [[Molly Studio OpenAI Endgame]] and [[Molly Studio API-ification of Everything]] frame this as companies such as Airbnb, Uber, Expedia, Google Maps, Yelp, or Booking-style services becoming plugged-in providers behind an [[OpenAI]]-style [[Agentic OS]] or intent layer.

## Scope
The concept covers app abstraction, service/API composition, generated flows, command palettes, task-specific interface surfaces, and marketplace-like agent capabilities. It does not assume that apps disappear, that platform economics become fairer, or that generated flows automatically handle edge cases better than dedicated apps.

## Contrasts
- Versus mobile app stores: app stores distribute fixed app bundles; post-app interfaces expose task capability through a common intent surface.
- Versus web search: search finds destinations; a post-app interface attempts to complete or coordinate the task directly.
- Versus [[Agent-native CLI]]: an agent-native CLI is usually operator/developer-facing; post-app interfaces are consumer-facing task surfaces.

## Evidence
- [[Molly Studio OpenAI Endgame]] supplies the central thesis and examples, but the API-ification claim is mostly speculative.
- [[Molly Studio API-ification of Everything]] supplies the direct "intent over applications" version of the thesis and names MCP as a connector layer, but provides weak evidence and no primary protocol or adoption support.
- [[Molly Studio AI-native Interface Thesis Collection]] adds the [[Shopify]] commerce framing: Molly argues that commerce actions may happen inside AI interactions and that Shopify's SKU repository could become more valuable in that environment. This is strategically useful but still not product-roadmap evidence.
- [[Agent-native CLI]] and [[Catalog-backed Agent Tool Distribution]] show a narrower agent-engineering analogue: tools can be packaged as capability surfaces for agents, but this does not prove consumer app replacement.
- [[Browserbase Autobrowse browser-skill loop]] preserves an adjacent pattern where repeated browser tasks become reusable skills, again narrower than a full post-app consumer OS.

## Related
- [[Agentic OS]]
- [[Adaptive UI Generation]]
- [[Intent-based Computing]]
- [[API-ification of Services]]
- [[MCP Tool Connectors]]
- [[Interface-layer Marketplace Risk]]
- [[AI-native Commerce Interfaces]]
- [[Shopify]]
- [[AI-native Identity-context Layer]]
- [[Agent-native CLI]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Agent-generated Browser Skills]]
- [[Deterministic-first Browser Automation]]

## Open Questions
- Which app categories are most likely to become agent-mediated API surfaces first: search/maps, travel, commerce, productivity, messaging, or developer tools?
- How should an agentic platform handle service-specific constraints, liability, payments, authentication, anti-fraud checks, and human confirmation?
- What evidence would distinguish real post-app migration from normal app integrations and plugins?
