---
type: source
source_path: raw/sources/2026-05-29-prajwal-tomar-vibe-coders-prelaunch-checklist.md
title: "Prajwal Tomar tweet on vibe-coded app pre-launch checklist"
author: "Prajwal Tomar"
date: 2026-05-15
tags: [ai-apps, security, privacy, weak-social, social-source]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# Prajwal Tomar tweet on vibe-coded app pre-launch checklist

## Summary
Prajwal Tomar's tweet says "vibe coders are getting sued" and repeats a pre-launch checklist for people shipping AI-built apps with real users: privacy policy, data-storage awareness, security headers, OWASP basics, SQL injection/XSS/auth checks, `.env` and API-key handling, sensitive API/log output review, and rate limits. The source is weak social evidence: neither the tweet nor the attached Reddit screenshot provides lawsuit examples, legal citations, OWASP links, repo evidence, or a reproducible audit method. Its durable Tolaria value is the narrower [[AI-built MVP Pre-launch Safety Checklist]] pattern: AI-built MVPs and agent-coded apps need a lightweight launch gate for privacy, basic web security, secrets exposure, and API-abuse/cost controls before real users touch them.

## Key Claims
1. The tweet claims AI/vibe-coded app builders are launching products with real users while skipping privacy, security, and abuse checks.
2. It asserts that collecting user data triggers legal/privacy obligations such as having a privacy policy and knowing where user data is stored.
3. It recommends checking security headers, OWASP basics, SQL injection, XSS, and authentication issues before launch.
4. It recommends verifying that `.env` values, API keys, sensitive API responses, and secrets in logs are not exposed.
5. It recommends rate limits before a user or attacker can burn API spend.
6. The lawsuit/liability framing is unsupported by captured evidence and should not be promoted as fact.

## Notable Quotes
- "Vibe coders are getting sued."
- "People are launching apps with real users but skipping the boring stuff that can actually kill the product."
- "privacy policy if you collect user data"
- "check security headers"
- "scan against OWASP basics"
- "make sure .env values are not leaking"
- "never expose API keys in frontend code"
- "add rate limits before someone burns your API bill"

## Entities Mentioned
- None promoted. Prajwal Tomar and the visible Reddit username are source authors/context rather than recurring Tolaria entities.

## Concepts Mentioned
- [[AI-built MVP Pre-launch Safety Checklist]]
- [[AI Command-generation Safety Pattern]]
- [[Agent-Computer Interface Design]]

## Follow-ups
- Preserve as a weak/social checklist seed, not as evidence that vibe coders are actually being sued.
- Any operational checklist, scanner, template, legal/privacy policy workflow, or Hermes/Codex integration would require separate Overseer approval; this card only promotes knowledge.
