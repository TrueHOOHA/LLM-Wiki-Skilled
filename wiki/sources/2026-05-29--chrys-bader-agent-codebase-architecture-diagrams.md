---
type: source
source_path: raw/sources/2026-05-29-chrysb-agent-codebase-architecture-diagrams.md
title: "Chrys Bader X post on agent-written codebases and living architecture diagrams"
author: "Chrys Bader / @chrysb"
date: 2026-05-09
tags: [agent-engineering, architecture, code-review, workflows]
created: 2026-05-29
---

# Chrys Bader X post on agent-written codebases and living architecture diagrams

## Summary
This weak social source argues that agent-written codebases can become hard for humans to understand if review happens only after months of file-level generation. The proposed remedy is to align humans and agents at the architecture level before building, then have the agent maintain a living architecture diagram that captures system boundaries, data flow, high-level components, key constraints, patterns, abstractions, APIs, and interfaces. The durable Tolaria value is a workflow hypothesis: human oversight should concentrate on architecture and critical interfaces while file-level implementation can be delegated more aggressively only when the higher-level structure is explicit.

## Key Claims
1. Agent-started codebases may become unintelligible to human technical leaders when there is no maintained architectural frame.
2. Teams should align on architecture before agentic building starts rather than trying to understand every generated file afterward.
3. A living architecture diagram can act as a maintained control surface for human oversight and agent iteration.
4. Three review altitudes matter: top-level architecture, mid-level patterns/abstractions/interfaces, and low-level file code.
5. Human review should be strongest at architecture and critical-interface levels; file-level code is where high-leverage delegation becomes safer after the first two levels are clear.

## Notable Quotes
- "if your codebase starts written by agents, don’t try to understand it"
- "align at the architectural level before any building happens"
- "ask the agent to maintain a living architecture diagram of how the system works"
- "there are three altitudes that matter: Top-level: architecture; Mid-level: patterns & abstractions; Low-level: file-level code"
- "as long as you understand the architecture and critical interfaces, it becomes much easier to reason about ground truth and meaningfully iterate"

## Entities Mentioned
- [[Hermes Agent]] — not mentioned directly, but the hypothesis is relevant to Hermes/Codex workflow proposals and approval-gated code-review practices.

## Concepts Mentioned
- [[Living Architecture Diagram]]
- [[Multi-altitude Agent Code Review]]
- [[Agent-Computer Interface Design]]
- [[Two-lane Agent Review]]
- [[Thin Harness Fat Skills]]
- [[Context Engineering]]
- [[Agentic Workflows and Agents]]

## Follow-ups
- Evidence gap: the tweet provides only an anecdote and explanatory infographic. It does not provide a repository, before/after comparison, evaluation harness, architecture-diagram template, maintenance protocol, or independent evidence that living diagrams improve agent-code maintainability.
- Knowledge-only synthesis completed in [[Living Architecture Diagrams for Agent-written Codebases Assessment]]: compare the hypothesis against existing Tolaria notes and preserve an approval-gated future eval question without creating implementation work.
