---
type: source
source_path: raw/sources/2026-05-29-x-akshay-pachaar-ai-engineer-learning-list-2053815461150859272.md
title: "Akshay Pachaar X post on AI engineer learning topics"
author: "Akshay / @akshay_pachaar"
date: 2026-05-11
tags: [agent-engineering, evaluation, inference, cost, observability]
created: 2026-05-29
---

# Akshay Pachaar X post on AI engineer learning topics

## Summary
This weak social source is a viral X post listing topics an AI engineer should learn: harness engineering, caching, KV cache management, speculative decoding, quantization, structured-output fallback chains, evals, cost attribution, agent guardrails, observability, routing/fallbacks, and fine-tuning versus in-context learning. It provides no primary sources, benchmarks, implementations, docs, or reproducible methods, so its durable value is a roadmap hypothesis rather than evidence. In Tolaria it is useful mainly as a topic-map seed for identifying what is already covered and where stronger primary-source backfill is missing.

## Key Claims
1. AI engineers should learn harness engineering rather than treating prompt engineering as the whole discipline.
2. Prompt caching and semantic caching involve distinct tradeoffs that should be understood separately.
3. KV cache management, speculative decoding, and quantization matter for inference/runtime efficiency.
4. Structured-output failures, fallback chains, model routing, and graceful fallback logic are reliability topics worth learning.
5. Evals should include both LLM-as-judge and human evaluation.
6. Cost should be attributed per feature rather than only per model.
7. Agent guardrails, loop budgets, and LLM observability should be first-class operating disciplines.
8. Engineers should know when fine-tuning is preferable to in-context learning.

## Notable Quotes
- "Harness engineering, not just prompt engineering"
- "Prompt caching vs. semantic caching tradeoffs"
- "Evals (LLM-as-judge + human evals)"
- "Agent guardrails & loop budgets"
- "Knowing when to fine-tune vs. in-context learning"

## Entities Mentioned
- [[Hermes Agent]] — the relevant Tolaria/Hermes application target, but the source does not mention Hermes directly.

## Concepts Mentioned
Existing Tolaria concepts with partial coverage:
- [[Prompt Caching for Agent Context]]
- [[Multi-Token Prediction Local Inference]]
- [[Evaluator-Optimizer Workflow]]
- [[Graph-aware Retrieval Evals]]
- [[Agentic Workflows and Agents]]
- [[Agent-Computer Interface Design]]
- [[Thin Harness Fat Skills]]
- [[Context Engineering]]
- [[Dynamic Context Loading]]
- [[Managed Local llama.cpp Provider]]

Topics not yet backed by dedicated Tolaria concept pages or strong source clusters:
- semantic caching
- KV cache management at scale
- structured-output failures and fallback chains
- feature-level cost attribution
- LLM observability
- model routing and graceful fallback logic
- fine-tuning versus in-context learning decision frameworks
- quantization as a production tradeoff distinct from speculative decoding/MTP

## Follow-ups
- Evidence gap: this source should not be used to justify adoption of any tool, runtime, eval harness, routing policy, or workflow change. Each roadmap topic needs primary-source backfill from vendor docs, runtime docs, papers, repos, benchmarks, or postmortems before becoming operational guidance.
- Knowledge-only next step completed in [[AI Engineer Learning Roadmap Topic Map]]: map this weak list against existing Tolaria coverage and record approval-gated questions without creating implementation work.
