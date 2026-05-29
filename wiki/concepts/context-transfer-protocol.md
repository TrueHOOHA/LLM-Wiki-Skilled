---
type: concept
aliases: ["CTP", "Context Transfer Protocol", "context portability protocol"]
tags: [agent-engineering, context, memory, privacy, interoperability]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Context Transfer Protocol

## Definition
Context Transfer Protocol is Molly Studio's proposed framework for letting applications request scoped, AI-derived user context from a provider without receiving the raw source data used to build that context.

## Scope
The concept covers context providers, user authorization and revocation, encrypted [[Context Vault|Context Vaults]], domain-tailored context vectors, and privacy-preserving feedback from applications back into the provider. It does not currently describe an implementable protocol: the captured source gives no API, message format, key-management scheme, threat model, differential-privacy parameters, context-vector schema, or reference implementation.

## Contrasts
- Versus normal OAuth/social login: OAuth grants identity or API access; CTP imagines access to computed personalization intelligence, not raw account data.
- Versus app-owned user profiles: the receiving app would use scoped context while avoiding custody of the underlying behavioral data.
- Versus generic [[Context Engineering]]: CTP is a portability and authorization thesis; context engineering is the broader practice of deciding what context an agent sees and why.
- Versus Tolaria's [[LLM Wiki Pattern]]: Tolaria preserves source-backed knowledge in inspectable notes; CTP imagines cryptographically scoped machine-readable user models across applications.

## Evidence
- [[Context Transfer Protocol (CTP)]] is the only captured source. It states the problem, proposed actors, and claimed benefits, but provides no technical proof or linked primary specification.
- [[Context Transfer Protocol and Hermes Context-portability Assessment]] grades the CTP article as weak evidence and recommends knowledge-only preservation unless stronger sources appear.
- [[Context Engineering]], [[Memory Hygiene for AI Agents]], and [[Dynamic Context Loading]] provide adjacent Tolaria frames for deciding which user/task context should be durable, scoped, loaded, or excluded.

## Related
- [[Context Vault]]
- [[Molly Studio]]
- [[Hermes Agent]]
- [[Context Engineering]]
- [[Memory Hygiene for AI Agents]]
- [[Dynamic Context Loading]]
- [[LLM Wiki Pattern]]

## Open Questions
- What exact data structure is a "context vector," and how would it be generated, queried, audited, versioned, and deleted?
- What cryptographic primitive prevents raw-data reconstruction while still enabling useful personalization?
- How would a provider prove user authorization, scope, revocation, retention, and downstream deletion to the user and receiving application?
- How would differential-privacy feedback avoid cross-app leakage, re-identification, or poisoned personalization loops?
