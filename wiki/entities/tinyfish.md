---
type: entity
aliases: ["TinyFish", "TinyFish AI", "tinyfish.ai"]
tags: [agent-tooling, web-search, mcp]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# TinyFish

## Identity
TinyFish is presented in the current Tolaria evidence as a web-access layer for agents with Search, Fetch, Agent, Browser, MCP, CLI, and SDK surfaces. The best-supported claim from [[Divyansh Tiwari X post on TinyFish free Search/Fetch for agents]] is not that all agent browsing is free, but that TinyFish's official docs/pricing describe Search and Fetch as zero-credit endpoints while heavier Agent and Browser automation remains metered.

## Aliases
- TinyFish
- TinyFish AI
- tinyfish.ai

## Key Attributes
| Attribute | Current evidence |
|---|---|
| Search API | Official docs captured in the source say Search returns structured ranked results from `GET https://api.search.tinyfish.ai`, requires `X-API-Key`, and costs 0 credits/request. |
| Fetch API | Official docs captured in the source say Fetch renders URLs and extracts markdown/html/json from `POST https://api.fetch.tinyfish.ai`, costs 0 credits/URL, and accepts at most 10 URLs/request. |
| Metered surfaces | Pricing/docs captured in the source say Agent consumes credits per step and Browser consumes credits per time window. |
| Integration surfaces | The source records MCP registry/cookbook surfaces, OpenClaw skill, Python SDK, TypeScript SDK, and npm CLI paths. |
| Evidence quality | Medium for existence/pricing of official APIs; weak for the tweet author's Hermes/OpenClaw success claim and for first-party benchmark/anti-bot marketing metrics. |

## Evidence
- [[Divyansh Tiwari X post on TinyFish free Search/Fetch for agents]] separates the weak social claim from the stronger official docs/pricing evidence for zero-credit Search and Fetch.
- [[TinyFish Search/Fetch Agent Web Access Assessment]] grades the practical Hermes/Tolaria implication as promising but unvalidated: useful as a candidate ingestion primitive, not an adopted tool.

## Related
- [[Zero-credit Search-Fetch Agent Ingestion]]
- [[Hermes Agent]]
- [[OpenClaw]]
- [[Agent-native CLI]]
- [[Notebook-grounded Retrieval via MCP]]

## Open Questions
- Which MCP endpoint is canonical for current use: `https://agent.tinyfish.ai/mcp` or `https://mcp.tinyfish.ai`?
- Do Search results remain fresh and useful under real Tolaria queries, and when does Fetch return cached content unless `ttl=0`?
- What are the actual failure rates for 402/403/429, `bot_blocked`, timeout, JavaScript-heavy pages, and anti-bot sites in Overseer's workflows?
- Is there any official Hermes-specific TinyFish integration, or would Hermes rely on generic MCP/CLI/SDK surfaces?
