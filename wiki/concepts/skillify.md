---
type: concept
aliases: ["skillification", "meta-skill", "skillify loop"]
tags: [skills, agent-engineering, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Skillify

## Definition
Skillify is the meta-skill pattern of turning a repeated workflow, repeated mistake, or successful one-off run into a durable skill with triggers, edge cases, tests, resolver wiring, and filing rules.

## Scope
Skillify is about capturing operational procedure, not turning every note into executable automation. In Tolaria, it is currently a concept and proposal source; creating or patching actual Hermes skills requires Overseer approval outside this Beta knowledge-ingestion card.

## Contrasts
- A prompt is ad hoc; a skill is reusable and discoverable.
- A checklist documents a workflow; Skillify also asks whether the resolver can reach it and whether evals catch regressions.
- A knowledge note preserves claims; a skill changes future agent behavior and therefore needs stricter approval.

## Evidence
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] describes using /skillify in GBrain to convert book-mirror and meeting-prep workflows into reusable skills.

## Related
- [[GBrain]]
- [[GStack]]
- [[Thin Harness Fat Skills]]
- [[Compounding AI Knowledge Stack]]

## Open Questions
- Which recurring Tolaria corrections should become skill proposals versus remain knowledge-only annotations?
