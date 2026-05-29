---
type: entity
aliases: ["GStack", "garrytan/gstack"]
tags: [skills, agent-framework, coding]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# GStack

## Identity
GStack is described as a coding skill framework and host-adapter layer for agent systems including Claude, Codex, OpenCode, OpenClaw, Hermes, and GBrain.

## Aliases
- GStack
- garrytan/gstack

## Key Attributes
| Attribute | Current evidence |
|---|---|
| Role | Portable coding skills and host adapters, rather than the primary brain store. |
| Tolaria relevance | Useful comparator for skill portability and [[Thin Harness Fat Skills]]. |
| Caveat | The source summary says Hermes/OpenClaw integration is largely methodology/prompt artifacts rather than deep runtime code. |

## Evidence
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] lists GStack as part of the open-source stack and describes it as the coding skill framework used inside OpenClaw/Hermes-style agents.

## Related
- [[GBrain]]
- [[OpenClaw]]
- [[Hermes Agent]]
- [[Skillify]]

## Open Questions
- Which GStack skill patterns are portable as knowledge-only references versus requiring implementation approval in Hermes?
