---
type: concept
aliases: ["instruction loudness", "supporting-info tags", "XML priority control", "context loudness control"]
tags: [context-engineering, agent-engineering, prompt-design]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Instruction Priority Control

## Definition
Instruction Priority Control is the practice of making the relative authority of task instructions, supporting information, examples, references, and constraints explicit so the model does not over-weight contextual material that should be advisory.

## Scope
The AI Hero example uses XML-like `<supporting-info>` tags to lower the "loudness" of supporting context compared with core instructions. In Hermes/Tolaria terms, the broader pattern is useful for separating mandatory system/developer/card rules from background sources, examples, prior attempts, and weak social claims. It is a context-engineering pattern, not proof that a particular tag name is universally effective.

## Contrasts
- Versus adding more instructions: priority control changes hierarchy, not just volume.
- Versus hiding context: supporting material remains visible but clearly lower-priority.
- Versus hard policy: XML tags are a prompting convention and need validation in the target model/runtime.

## Evidence
- [[Matt Pocock AI Hero skills changelog]] reports that `/grill-with-docs` was too eager to implement, and that wrapping supporting information in XML tags reduced its priority relative to core instructions.

## Related
- [[Context Engineering]]
- [[Dynamic Context Loading]]
- [[Agent-Computer Interface Design]]
- [[Memory Hygiene for AI Agents]]
- [[AI Hero]]

## Open Questions
- Should future approved Hermes prompt/skill reviews distinguish mandatory directives, operator preferences, source evidence, examples, and optional hints with explicit markers?
- Which failure should be measured first: implementing when asked to ask questions, following weak evidence as hard fact, or over-weighting examples?
