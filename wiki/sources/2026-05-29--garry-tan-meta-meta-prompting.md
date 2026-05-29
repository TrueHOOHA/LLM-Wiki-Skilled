---
type: source
source_path: raw/sources/2026-05-29-historical-garrytan-meta-meta-prompting-2053127519872614419.md
title: "Meta-Meta-Prompting: The Secret to Making AI Agents Work"
author: "Garry Tan"
date: 2026-05-09
tags: [agent-framework, knowledge-management, skills, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# Meta-Meta-Prompting: The Secret to Making AI Agents Work

## Summary
Garry Tan argues that useful personal AI is not a chat window but a compounding operating system built from a thin harness, fat skills, fat data, deterministic code, resolver routing, and evaluation loops. The strongest reusable mechanism is not any single model; it is the loop where repeated workflows are turned into skill contracts, attached to resolvers, checked by evals, and grounded in a growing markdown knowledge graph. The source is valuable for Tolaria because it overlaps directly with [[Hermes Agent]], [[GBrain]], [[GStack]], [[OpenClaw]], [[LLM Wiki Pattern]], and [[Compounding AI Knowledge Stack]], but the article's largest production/productivity claims remain self-reported and weakly evidenced.

## Key Claims
1. Personal AI becomes more useful when treated as an operating system/second brain rather than a stateless chatbot.
2. Compounding value comes from fat knowledge data, reusable skills, deterministic helpers, resolver routing, and quality evals, not from model choice alone.
3. GBrain is presented as a markdown-backed brain with compiled truth, append-only timelines, entity propagation, hybrid/graph retrieval, installable skills, and retrieval benchmarks.
4. Skillify is a repeatable workflow for converting one-off successful or failed interactions into durable skills with triggers, edge cases, tests, and resolver wiring.
5. Cross-model review and retrieval citations are framed as trust mechanisms for book mirrors, meeting prep, and entity updates.
6. Prompt caching, LLM Wiki-style source preservation, and graph-aware retrieval are plausible mechanisms for making large repeated knowledge contexts cheaper and more reliable.
7. The strongest claims about 100k+ production pages, 100x-1000x productivity, and personal workflow outcomes remain weak because they are not independently audited.

## Notable Quotes
- "The harness is thin... The skills are fat... The data is fat."
- "When someone asks how I 'prompt' my AI, the answer is: I don't. The skills are the prompts."
- "The model is just the engine. Everything else is the car."
- "The future belongs to individuals who build compounding AI systems, not to individuals who use corporate-owned centralized AI tools."

## Evidence Map
| Evidence layer | Support level | Notes |
|---|---:|---|
| X article and prior X series | Weak to medium | Useful claim layer and terminology; not independent validation. |
| GBrain and GBrain-evals repos | Medium | Support existence of markdown brain, skills, hybrid/graph retrieval, eval orientation; benchmark scope is retrieval recall, not end-to-end productivity. |
| GStack repo | Medium | Supports portable skill/host-adapter framing and coding skill framework claims. |
| OpenClaw and Hermes docs | Medium | Support harness/runtime/channel/provider/skill architecture comparisons; "thin harness" is conceptual rather than literally small. |
| Anthropic prompt caching docs | Strong | Primary-source support for repeated-context cache mechanics, but Tolaria cost/latency benefits must be measured on Tolaria workloads. |
| Karpathy LLM Wiki gist | Medium | Conceptual support for raw immutable sources, LLM-maintained wiki pages, index/log, and ingest/query/lint workflows. |

## Entities Mentioned
- [[Garry Tan]]
- [[GBrain]]
- [[GStack]]
- [[OpenClaw]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[Compounding AI Knowledge Stack]]
- [[Thin Harness Fat Skills]]
- [[Skillify]]
- [[Graph-aware Retrieval Evals]]
- [[Prompt Caching for Agent Context]]
- [[LLM Wiki Pattern]]

## Follow-ups
- Proposal only: consider a knowledge-only Tolaria pilot/eval plan before adopting any GBrain-style mechanism.
- Open evidence question: whether GBrain's reported retrieval scores generalize to Tolaria's actual sources and task mix.
- Open design question: which mechanisms are already covered by Tolaria/Hermes and which would require separate approval for implementation.
