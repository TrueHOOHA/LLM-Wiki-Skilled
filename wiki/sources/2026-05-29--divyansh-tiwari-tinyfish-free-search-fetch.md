---
type: source
source_path: raw/sources/2026-05-29-historical-divyansh-tinyfish-free-web-search-2052474052841984110.md
title: "Divyansh Tiwari X post on TinyFish free Search/Fetch for agents"
author: "Divyansh Tiwari"
date: 2026-05-07
tags: [tinyfish, web-search, agent-tooling, evidence-triage]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Divyansh Tiwari X post on TinyFish free Search/Fetch for agents

## Summary
This source is a weak social lead claiming that web search is "basically free now for AI agents" after the author switched OpenClaw and Hermes agents to [[TinyFish]]. The durable finding is narrower: Alpha's linked-source inspection found official TinyFish docs/pricing support zero-credit Search and Fetch APIs, while Agent and Browser automation are metered. Treat the tweet as discovery evidence, not proof of Hermes production fit, author-specific results, or all web browsing becoming free. The useful mechanism for Tolaria is the split between cheap/free discovery+content extraction and paid browser/agent automation, captured in [[Zero-credit Search-Fetch Agent Ingestion]] and assessed in [[TinyFish Search/Fetch Agent Web Access Assessment]].

## Key Claims
1. The tweet claims web search is effectively free for agents and says switching OpenClaw and Hermes agents to TinyFish enabled browsing, research, and live retrieval at scale for $0.
2. Official TinyFish docs/pricing, as captured in the raw source, support the narrower claim that Search is 0 credits/request and Fetch is 0 credits/URL, with API-key access and rate limits.
3. The same inspected sources contradict any broad reading that all TinyFish web automation is free: Agent uses credits per step and Browser uses credits per time window.
4. Fetch should not automatically be treated as live: the raw source records cache behavior unless `ttl=0`, plus per-URL/batch timeouts, `bot_blocked`, and 402/403/429 caveats.
5. Integration evidence is plausible but unresolved: MCP, OpenClaw, Python SDK, TypeScript SDK, and CLI surfaces exist, but no official Hermes-specific TinyFish integration was found and MCP URLs differ across inspected sources.

## Notable Quotes
- Tweet text captured in raw source: "Web search is basically free now for AI agents."
- Tweet text captured in raw source: "I switched my OpenClaw and Hermes agents to TinyFish, and suddenly my agents could browse, research, and retrieve live info at scale… for $0."
- Raw source summary of official docs/pricing: "Search and Fetch are zero-credit/free-on-plan APIs with rate limits and API-key access."

## Entities Mentioned
- [[TinyFish]]
- [[Hermes Agent]]
- [[OpenClaw]]

## Concepts Mentioned
- [[Zero-credit Search-Fetch Agent Ingestion]]
- [[Agent-native CLI]]
- [[Notebook-grounded Retrieval via MCP]]

## Follow-ups
- Approval proposal for Overseer: authorize a small future validation of TinyFish Search/Fetch freshness, cost, failure behavior, MCP URL correctness, and Hermes MCP/CLI fit before any Hermes/Tolaria adoption.
- Keep the knowledge-only stance unless a later approved experiment tests `ttl=0` freshness, rate-limit behavior, error modes, Search result quality, Fetch clean-content quality, and the correct MCP endpoint.
