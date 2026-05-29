---
type: entity
aliases: ["Databricks", "Databricks AI Research", "DbrxMosaicAI"]
tags: [company, agent-engineering, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Databricks

## Identity
Databricks is a data and AI platform company. In Tolaria's current evidence, Databricks is relevant as the first-party publisher of [[Databricks MemEx programmable scratchpad for LLM agents]], which presents MemEx as a programmable agent scratchpad integrated with Databricks production/research agent systems such as Genie, Agent Bricks, KARL, and the aroll rollout framework.

## Aliases
- Databricks
- Databricks AI Research
- DbrxMosaicAI

## Key Attributes
| Attribute | Value |
|---|---|
| Category | Data/AI platform company and AI research publisher |
| Tolaria relevance | Source for [[Programmable Agent Scratchpad]] and agent-harness evaluation claims |
| Evidence grade | Medium for first-party blog mechanics; weak-to-medium for vendor-owned performance claims; weak for originating social post |
| Adoption status | Knowledge-only; no MemEx/aroll implementation or Databricks integration is approved |

## Evidence
- [[Databricks MemEx programmable scratchpad for LLM agents]] captures the X post and linked Databricks blog. The source states that MemEx is built on aroll, has been validated inside Databricks internal/production agents, and will roll out across first-party agents and Agent Bricks, but Tolaria has not found public implementation code or independent reproduction.

## Related
- [[Programmable Agent Scratchpad]]
- [[Agent-Computer Interface Design]]
- [[Context Engineering]]
- [[Long-running Agent Harness]]
- [[Hermes Agent]]

## Open Questions
- Is MemEx or aroll publicly documented or released beyond the Databricks blog?
- Which parts of the reported evaluation can be independently reproduced outside Databricks?
- Are the cost savings mostly from lower token serialization, fewer tool calls, better model behavior, or benchmark-specific task structure?
