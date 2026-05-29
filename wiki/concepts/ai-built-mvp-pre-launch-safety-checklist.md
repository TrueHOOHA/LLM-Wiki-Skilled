---
type: concept
aliases: ["AI MVP launch checklist", "vibe-coded app security checklist", "agent-coded app pre-launch checklist", "AI-built app privacy/security launch gate"]
tags: [ai-apps, security, privacy, product-launch, weak-social]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# AI-built MVP Pre-launch Safety Checklist

## Definition
AI-built MVP Pre-launch Safety Checklist is a lightweight, evidence-graded launch gate for applications built quickly with AI coding tools or agentic coding workflows. It asks whether the app is safe enough for real users across privacy/legal basics, common web-security failures, secrets handling, sensitive-data exposure, and API-abuse/cost controls before launch.

## Scope
This concept covers pre-launch checks for AI-built MVPs, vibe-coded apps, and agent-coded prototypes moving from private experimentation into real-user operation. It does not claim that AI-built apps have unique legal duties; the point is that fast AI-assisted development can make teams skip ordinary production hygiene. [[Prajwal Tomar tweet on vibe-coded app pre-launch checklist]] is weak social evidence for the need, while [[AI-built MVP Pre-launch Safety Checklist Assessment]] keeps the durable checklist explicitly downgraded until stronger primary guidance is ingested.

Minimum launch gate:
- Legal/privacy: if collecting personal or user data, publish an accurate privacy policy, know where the data is stored, limit collection to what the product needs, and verify retention/deletion/export expectations against jurisdiction-specific rules.
- Basic web security: check authentication, authorization, SQL injection, XSS, request validation, security headers, CORS, error handling, and safe response content types against a real standard such as OWASP ASVS or OWASP Cheat Sheet material rather than a tweet.
- Secrets handling: verify `.env` files, API keys, tokens, connection strings, and service credentials are not in frontend bundles, public repos, API responses, logs, screenshots, or crash reports.
- API abuse and cost controls: add rate limits, quotas, budget alerts, abuse detection, and model/API spend caps before exposing paid APIs or LLM-backed endpoints to real users.
- Logging and observability: log enough to diagnose abuse and failures without storing raw secrets, personal data, session tokens, or sensitive payloads.
- Human review boundary: do not rely only on "ask the AI to review my app"; use deterministic scanners, framework defaults, provider dashboards, and manual verification for high-risk flows.

## Contrasts
- Versus a legal compliance program: this is a triage checklist, not legal advice, jurisdictional policy generation, or a substitute for privacy/security counsel.
- Versus a full security audit: this is a baseline launch gate for MVPs. High-risk products still need deeper threat modeling, dependency review, penetration testing, and incident-response planning.
- Versus [[AI Command-generation Safety Pattern]]: command-generation safety controls executable strings. This checklist controls the broader app-launch boundary where generated code, secrets, data handling, and metered APIs become user-facing.
- Versus [[Agent-Computer Interface Design]]: ACI focuses on making agent/tool interactions mistake-resistant; this checklist turns launch-readiness into a concrete control surface for human and agent reviewers.

## Evidence
- [[Prajwal Tomar tweet on vibe-coded app pre-launch checklist]] supplies the weak-social checklist seed and the unsupported lawsuit/liability framing.
- [[AI-built MVP Pre-launch Safety Checklist Assessment]] separates weak social claims from stronger external verification targets: OWASP ASVS, OWASP Secure Headers, OWASP Secrets Management, Authentication, REST Security, Logging, and Denial of Service cheat sheets.
- Related Tolaria safety concepts include [[AI Command-generation Safety Pattern]] and [[Agent-Computer Interface Design]], which reinforce the need for explicit review, mistake-resistant interfaces, and verification before action.

## Related
- [[Prajwal Tomar tweet on vibe-coded app pre-launch checklist]]
- [[AI-built MVP Pre-launch Safety Checklist Assessment]]
- [[AI Command-generation Safety Pattern]]
- [[Agent-Computer Interface Design]]
- [[Codex]]
- [[Hermes Agent]]

## Open Questions
- Which stronger sources should Tolaria ingest next if this checklist becomes operational: OWASP ASVS, OWASP Top 10, Secure Headers, Secrets Management, REST Security, privacy-policy guidance, or provider-specific API-budget controls?
- What is the minimum launch gate for low-risk toy apps versus products collecting personal data, payments, health/finance data, or LLM prompts/files?
- Should future non-Beta work create an approved checklist/eval for Codex/Hermes-built MVPs, and if so should it prioritize secrets exposure, auth/authorization, rate limits, privacy policy accuracy, or API spend controls first?
