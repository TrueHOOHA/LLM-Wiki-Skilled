---
type: concept
aliases: ["free Search/Fetch for agents", "zero-credit Search and Fetch", "cheap web ingestion layer", "agent web search/fetch layer"]
tags: [agent-tooling, web-search, ingestion]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Zero-credit Search-Fetch Agent Ingestion

## Definition
Zero-credit Search-Fetch Agent Ingestion is the pattern of using low-cost or zero-credit web search plus clean-content fetch endpoints as the discovery and extraction layer for agent research, while reserving metered browser or autonomous agent automation for cases where search/fetch cannot answer the task. In the current Tolaria evidence, [[TinyFish]] is the concrete example because [[Divyansh Tiwari X post on TinyFish free Search/Fetch for agents]] records official docs/pricing that make Search and Fetch zero-credit while Agent and Browser remain paid.

## Scope
This concept covers web discovery, URL ranking, page rendering, markdown/html/json extraction, rate limits, caching behavior, API-key access, and failure handling for ingestion/research tasks. It does not cover full browser control, autonomous web workflows, or production reliability claims unless those are separately tested and cited.

## Contrasts
- Versus metered browser automation: Search/Fetch can be cheaper and lower-risk, but cannot replace interactive login, form submission, or stateful browsing.
- Versus raw browser scraping: a Search/Fetch API may provide cleaner structured output, but it introduces service dependency, API-key requirements, rate limits, cached content, and provider-specific failure modes.
- Versus [[Notebook-grounded Retrieval via MCP]]: Search/Fetch starts from the open web, while notebook-grounded retrieval starts from a curated corpus.
- Versus [[Agent-native CLI]]: Search/Fetch is an external web-access primitive; an agent-native CLI is a local interface contract. They can be combined if a CLI wraps Search/Fetch with stable outputs and dry-run/error semantics.

## Evidence
- [[Divyansh Tiwari X post on TinyFish free Search/Fetch for agents]] captures the social lead plus official TinyFish docs/pricing evidence for 0-credit Search and Fetch and metered Agent/Browser.
- [[TinyFish Search/Fetch Agent Web Access Assessment]] recommends treating the pattern as promising but validation-gated for Tolaria/Hermes.

## Related
- [[TinyFish]]
- [[Hermes Agent]]
- [[OpenClaw]]
- [[Agent-native CLI]]
- [[Notebook-grounded Retrieval via MCP]]

## Open Questions
- What minimum eval demonstrates that Search/Fetch is fresh enough, cheap enough, and reliable enough for Tolaria ingestion?
- Which Tolaria source types should use Search/Fetch before browser automation, if a future experiment is approved?
- How should cached Fetch output be labeled so "live" evidence does not silently become stale evidence?
