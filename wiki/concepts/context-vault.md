---
type: concept
aliases: ["Context Vault", "context provider vault", "AI context vault"]
tags: [agent-engineering, context, memory, privacy]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Context Vault

## Definition
A Context Vault is Molly Studio's proposed encrypted repository for storing AI-derived user patterns and preferences as mathematical representations that applications can query for scoped personalization without accessing the raw source data.

## Scope
In the CTP thesis, a Context Vault belongs to a context provider such as an AI assistant platform and supports authorization, audit, revocation, context-vector queries, and privacy-preserving feedback. In Tolaria, the term should remain low-confidence and conceptual because the source does not define the storage model, embedding/vector semantics, encryption scheme, revocation behavior, privacy budget, deletion guarantees, or provider API.

## Contrasts
- Versus durable agent memory: [[Memory Hygiene for AI Agents]] is about what an agent should remember and how stale/low-confidence memory is controlled; a Context Vault is a proposed provider-side store and sharing boundary.
- Versus a knowledge wiki: [[LLM Wiki Pattern]] keeps source-backed markdown pages for human/agent inspection; a Context Vault is described as a machine-readable encrypted personalization substrate.
- Versus [[Dynamic Context Loading]]: dynamic loading selects context for a task; a vault would be one possible source from which scoped context is requested.
- Versus unscoped user-data sharing: the CTP claim is that applications receive computed intelligence instead of raw behavioral records, though the source does not prove this can be done safely.

## Evidence
- [[Context Transfer Protocol (CTP)]] describes the vault as encrypted and mathematical but does not provide technical detail.
- [[Context Transfer Protocol]] preserves the proposed protocol shape and its unresolved authorization, cryptography, reconstruction, and differential-privacy questions.
- [[Context Transfer Protocol and Hermes Context-portability Assessment]] compares the idea to Hermes/Tolaria memory boundaries and recommends no adoption without stronger evidence.

## Related
- [[Context Transfer Protocol]]
- [[Context Engineering]]
- [[Memory Hygiene for AI Agents]]
- [[Dynamic Context Loading]]
- [[LLM Wiki Pattern]]
- [[Hermes Agent]]

## Open Questions
- Can a Context Vault expose useful personalization without leaking sensitive attributes through the returned vectors or model behavior?
- What user-facing audit screen would make provider-held memory understandable and safely revocable?
- How would source provenance and confidence travel with a computed context vector?
- What abuse cases are most likely: cross-app profiling, opaque provider lock-in, consent theater, poisoning, or impossible-to-verify deletion?
