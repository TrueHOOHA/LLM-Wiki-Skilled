---
type: entity
aliases: ["local-client-prospector", "local-client-prospector-skill", "Kappaemme local-client-prospector-skill"]
tags: [codex, skills, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Local Client Prospector

## Identity
Local Client Prospector is a public [[Codex]] skill repository by Kappaemme for assisted local-business prospecting. In Tolaria it is evidence for [[NPM-packaged Codex Skills]] and guarded browser-assisted research workflows, not evidence that the resulting leads are high-quality or that the workflow should be installed locally.

## Aliases
- local-client-prospector
- local-client-prospector-skill
- Kappaemme local-client-prospector-skill

## Key Attributes
| Attribute | Value |
| --- | --- |
| Repository | `Kappaemme-git/local-client-prospector-skill` |
| Package name | `local-client-prospector-skill` |
| Install target | `~/.codex/skills/local-client-prospector` |
| Primary artifact | `local-client-prospector/SKILL.md` |
| Claimed task | Find and qualify local businesses that may need websites or digital-marketing help |
| Evidence grade | Weak for business/lead outcomes; medium for repo/package mechanics captured in the raw source |
| Adoption status | Knowledge-only; no install, import, or Hermes/Codex configuration change |

## Evidence
- [[Kappaemme X post on Local Client Prospector Codex skill]] records the social claim, README, `SKILL.md`, `package.json`, and installer code. The repo supports the existence of the skill folder, npm package metadata, install target, browser workflow, scoring fields, and compliance guardrails.
- [[Local Client Prospector Codex Skill Packaging Assessment]] concludes the reusable value is packaging and guardrail design, while lead quality, legal/compliance adequacy, and scalable verification remain unproven.

## Related
- [[Codex]]
- [[NPM-packaged Codex Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Skill Validation Patterns]]
- [[Thin Harness Fat Skills]]

## Open Questions
- Does Codex's local skill loader treat `~/.codex/skills/<name>/SKILL.md` semantics consistently across versions, or is this repo relying on an unstable/local convention?
- What provenance, pinning, and overwrite safeguards should exist before using npm packages to write into local agent-skill directories?
- Does the workflow produce useful, lawful, non-duplicative leads when tested against a real market and rate-limited public sources?
