---
type: concept
aliases: ["AI identity layer", "AI-native identity", "identity-context layer"]
tags: [agent-engineering, identity, context, weak-evidence]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# AI-native Identity-context Layer

## Definition
An AI-native Identity-context Layer is a proposed account/profile/memory layer where identity, user preferences, social graph, communication history, task context, and authorization become available to an AI platform for personalization and action. [[Molly Studio OpenAI Endgame]] speculates that [[OpenAI]] profiles could become a hybrid of Apple ID, Instagram profile, Linktree, SSO, and AI-mediated communication identity.

## Scope
The concept covers identity profiles, SSO-like account mediation, context portability, personal memory, social/discovery graphs, messaging/translation/summarization, delegated representation, and authorization/revocation. It does not assume that any vendor has built this, that centralization is desirable, or that identity and context should be fused without strict privacy and security controls.

## Contrasts
- Versus SSO: SSO proves account identity and grants login access; an identity-context layer may also expose preferences, memory, task state, communication context, and delegated actions.
- Versus [[Context Vault]]: a Context Vault emphasizes provider-held derived user context; an identity-context layer adds social profile, account, communication, and platform-distribution dimensions.
- Versus [[Memory Hygiene for AI Agents]]: memory hygiene is the discipline required to keep such a layer safe, scoped, current, and inspectable.

## Evidence
- [[Molly Studio OpenAI Endgame]] is the current source, but its social-app/SSO/profile roadmap evidence is weak because the cited Sam Altman X link was inaccessible and the article extrapolates from a casual quote.
- [[Context Transfer Protocol (CTP)]] and [[Context Vault]] provide adjacent vocabulary for scoped, revocable, privacy-bounded context sharing, but also remain weak and underspecified.
- [[Memory Hygiene for AI Agents]] and [[Context Engineering]] provide the stronger Tolaria lenses: any identity-context layer needs provenance, confidence, revocation, auditability, stale-memory handling, and data-minimization boundaries.

## Related
- [[OpenAI]]
- [[Agentic OS]]
- [[Post-app Interfaces]]
- [[Context Vault]]
- [[Context Transfer Protocol]]
- [[Memory Hygiene for AI Agents]]
- [[Context Engineering]]
- [[Instruction Priority Control]]

## Open Questions
- What should an AI platform be allowed to infer from messages, browsing, purchases, documents, and tool activity, and how should those inferences be shown or revoked?
- Can identity, memory, and action permissions be separated enough to avoid turning personalization into surveillance or lock-in?
- What primary evidence exists for real OpenAI profile, social graph, or SSO ambitions beyond speculative commentary?
