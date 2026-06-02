---
type: source
source_path: raw/sources/2026-05-29-kappaemme-local-client-prospector-codex-skill.md
title: "Kappaemme X post on Local Client Prospector Codex skill"
author: "Kappaemme / @Kappaemme1926"
date: 2026-05-14
tags: [agent-engineering, skills, codex, social-source]
created: 2026-05-29
source_count: 0
---

# Kappaemme X post on Local Client Prospector Codex skill

## Summary
This weak social source announces [[Local Client Prospector]], a Codex skill for browser-assisted local-business prospecting. The X post is promotional and does not prove lead quality, outreach value, compliance safety, or scalable extraction. The stronger evidence layer is the linked GitHub repository: it contains a `local-client-prospector/SKILL.md`, an npm package named `local-client-prospector-skill`, and a Node installer that copies the skill folder into `~/.codex/skills/local-client-prospector`. For Tolaria, the reusable signal is [[NPM-packaged Codex Skills]] plus explicit research, lead-scoring, quality-check, and compliance guardrails; adoption or installation remains outside this knowledge-only card.

## Key Claims
1. The X post claims the skill helps find nearby local businesses that may need a website by checking standalone websites versus social-only presence, scoring leads, and returning contact fields in chat or CSV-style output.
2. The repository corroborates the one-command distribution pattern: `npx local-client-prospector-skill` runs a package binary that deletes and recopies a local skill folder into `~/.codex/skills/local-client-prospector`.
3. The `SKILL.md` uses compact frontmatter (`name`, `description`) and procedural sections for input defaults, compliance guardrails, browser research workflow, website-status classification, lead scoring, output columns, and final quality checks.
4. The browser-assisted workflow is manual/research-oriented rather than an auditable API-backed scraping pipeline: it tells Codex to use the integrated browser, build candidate lists from visible/public results, check exact business names, and cross-check details with public sources.
5. The lead-scoring schema is simple and operational: `Hot` for no site/social-only with phone/contact and active local fit, `Warm` for weak site or marketplace/booking-only presence, `Low` for good site or low confidence, and `Skip` for closed/duplicate/out-of-scope candidates.
6. The compliance guardrails explicitly warn against bypassing CAPTCHAs, login walls, rate limits, bot protections, paywalls, bulk scraping, Google Maps data extraction at scale, and personal-data collection without a lawful basis.

## Notable Quotes
- X post: "CODEX SKILL THAT TURNS LOCAL SEARCH INTO CLIENT LEADS!"
- X post: "Search nearby shops, gyms, restaurants, salons, and local activities while Codex checks who has a real website and who only has socials."
- README: "This installs the skill to: `~/.codex/skills/local-client-prospector`."
- `SKILL.md`: "Use the integrated browser as an assisted research tool, not as a bulk scraper."
- `SKILL.md`: "Do not label a lead `Hot` if a real standalone website was found."

## Entities Mentioned
- [[Local Client Prospector]]
- [[Codex]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[NPM-packaged Codex Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Skill Validation Patterns]]
- [[Thin Harness Fat Skills]]

## Follow-ups
- Knowledge-only implication: this is a useful example of distributing a single local Codex skill through npm while bundling behavioral guardrails directly inside `SKILL.md`.
- Approval-gated practical question: if Overseer later wants to adapt this pattern, the safe next step would be a separate non-Beta review/eval of local Codex skill packaging, provenance pinning, overwrite behavior, compliance wording, and task-quality checks before installing or publishing any skill pack.
