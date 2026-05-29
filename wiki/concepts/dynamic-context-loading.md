---
type: concept
aliases: ["task-specific context loading", "selective context loading", "context loading rules"]
tags: [agent-engineering, context, retrieval, token-efficiency]
created: 2026-05-29
updated: 2026-05-29
source_count: 4
---

# Dynamic Context Loading

## Definition
Dynamic Context Loading is the practice of selecting the smallest task-relevant bundle of context before an LLM run instead of loading every available memory, note, source, or tool description.

## Scope
It covers task-to-context routing rules, source selection, token budgeting, retrieval filtering, and the decision to include or exclude memories, examples, project files, standards, and tool descriptions. It does not guarantee better outputs by itself; the selection policy has to be evaluated against task quality, missed-context failures, and source-fidelity loss from compaction.

## Contrasts
- Versus loading everything: less token waste and lower risk of irrelevant-context dilution, but higher risk of omitting a needed fact.
- Versus static system prompts: adapts context to writing, analysis, research, strategy, coding, or tool-use tasks.
- Versus black-box retrieval: selection rules can be explicit and auditable, especially when backed by [[LLM Wiki Pattern|wiki]] links and source pages.

## Evidence
- [[Khairallah X article on mastering context engineering]] argues for mapping recurring work types to specific context files and testing each configuration against all-context baselines; this is a weak social source but a useful framing.
- [[Prompt Caching for Agent Context]] captures a complementary optimization for stable large prefixes, while dynamic loading is about selecting what belongs in the prefix at all.
- [[Graph-aware Retrieval Evals]] points toward measuring whether a retrieval/context system brings in the related graph context needed for real questions.
- [[Context Transfer Protocol (CTP)]] is an adjacent but weak thesis where applications request scoped domain-tailored context vectors from a provider; it reinforces the need to evaluate what context is selected, omitted, and overexposed.
- [[Molly Studio OpenAI Endgame]] frames [[OpenAI]] as a possible command layer that dynamically selects models, interfaces, and service/API surfaces from user intent; this reinforces dynamic loading/routing questions but remains speculative as roadmap evidence.
- [[Unseeing Abstractions and Agent-engineering Lessons]] adds the abstraction-leak caution: compacted context is an abstraction over raw sources, board state, tool outputs, and memory; review loops should check what decisive state was lost or over-compressed.

## Related
- [[Context Engineering]]
- [[Memory Hygiene for AI Agents]]
- [[Prompt Caching for Agent Context]]
- [[Graph-aware Retrieval Evals]]
- [[LLM Wiki Pattern]]
- [[Context Transfer Protocol]]
- [[Context Vault]]
- [[Agentic OS]]
- [[Post-app Interfaces]]
- [[Adaptive UI Generation]]
- [[Abstraction-leak Reasoning]]
- [[Memory Hygiene for AI Agents]]

## Open Questions
- How should Tolaria score a context-loading policy: answer quality, citation faithfulness, correction rate, latency, token cost, or missed critical context?
- Should dynamic loading be rule-based, retrieval-based, graph-aware, or hybrid for Overseer's Alpha/Beta knowledge workflow?
- When an agentic platform dynamically routes to apps/APIs or generated UIs, which routing decisions need to be visible to the user or reviewer?
