---
type: concept
aliases: ["API-ification", "apps as APIs", "services as APIs", "businesses as APIs", "API-ified services"]
tags: [agent-engineering, platform, mcp, weak-evidence]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# API-ification of Services

## Definition
API-ification of Services is the thesis that businesses increasingly expose their core capabilities as APIs, tools, or service modules consumed by an agentic interface, while their standalone app frontend becomes less central to user acquisition and task completion. [[Molly Studio API-ification of Everything]] applies this to consumer services such as travel and accommodation: the company keeps operations and backend systems, but the user interacts through a shared AI/OS layer.

## Scope
The concept covers service APIs, tool schemas, provider selection, backend operations, user preferences, pricing/availability comparison, and a shift from app-frontend differentiation toward operational quality. It does not imply that APIs alone solve trust, liability, payments, authentication, customer support, brand, anti-fraud, legal compliance, or platform-dependence problems.

## Contrasts
- Versus [[Agent-native CLI]]: an agent-native CLI is a developer/operator-facing wrapper; API-ification of Services is a broader market/platform thesis about businesses becoming callable capabilities.
- Versus [[Catalog-backed Agent Tool Distribution]]: catalogs distribute tools; API-ified services are the underlying business capabilities those tools may expose.
- Versus [[Context Transfer Protocol]]: CTP concerns scoped user context portability; API-ification concerns capability exposure and task execution.
- Versus [[Post-app Interfaces]]: post-app interfaces describe the user experience; API-ification describes the service-provider architecture behind it.

## Evidence
- [[Molly Studio API-ification of Everything]] supplies the direct thesis and Airbnb-style example, but the article is weak evidence with no primary implementation or adoption data.
- [[Molly Studio OpenAI Endgame]] previously captured a similar claim that companies such as Airbnb, Uber, and Expedia could become APIs behind an [[OpenAI]] interface layer.
- [[Printing Press Ecosystem Assessment]], [[Agent-native CLI]], and [[Catalog-backed Agent Tool Distribution]] provide narrower agent-engineering analogues: capabilities can be wrapped as agent-usable tools, but these do not prove consumer app replacement.

## Related
- [[Intent-based Computing]]
- [[MCP Tool Connectors]]
- [[Interface-layer Marketplace Risk]]
- [[Post-app Interfaces]]
- [[Agentic OS]]
- [[Agent-Computer Interface Design]]
- [[Agent-native CLI]]
- [[Catalog-backed Agent Tool Distribution]]

## Open Questions
- Which service categories have APIs rich enough for reliable agent mediation without falling back to brittle browser automation?
- How should an agent expose provider ranking, sponsored placement, fees, substitutions, cancellations, and dispute boundaries?
- Does API-ification reduce interface waste or merely shift power from app owners to the owner of the routing/interface layer?
