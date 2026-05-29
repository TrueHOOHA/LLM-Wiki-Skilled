---
type: source
source_path: raw/sources/2026-05-29-x-system-monarch-ai-ml-system-design-fundamentals-2054913454142796040.md
title: "Puneet Patwari X post on AI/ML system-design fundamentals"
author: "Puneet Patwari / @system_monarch"
date: 2026-05-14
tags: [agent-engineering, evaluation, retrieval, cost, reliability, weak-social]
created: 2026-05-29
---

# Puneet Patwari X post on AI/ML system-design fundamentals

## Summary
This weak social source is an X post by Puneet Patwari listing fundamentals he would ask Sr-to-Staff+ AI/ML system-design interview candidates to understand before interview practice. Its useful payload is a taxonomy: LLM basics, RAG/retrieval, AI system architecture, cost/performance, evaluation/quality, and reliability/security. The source provides no primary citations, examples, benchmark data, implementation details, or reproducible method, so Tolaria should treat it as a vocabulary and coverage-gap prompt rather than evidence that the list is complete, correctly ordered, or sufficient for real system design.

## Key Claims
1. AI system design remains system design, but the bottlenecks now include tokens, context windows, retrieval quality, inference cost, hallucinations, model latency, evals, and user trust.
2. Senior AI/ML system-design preparation should include LLM concepts such as tokens, context windows, prompt/system prompts, sampling controls, structured outputs, tool/function calling, agents, memory, guardrails, hallucinations, model routing, and fine-tuning versus prompting.
3. RAG/retrieval fundamentals should include embeddings, vector and hybrid search, chunking, metadata filtering, reranking, recall/precision, query rewriting, freshness, permission-aware retrieval, citation grounding, evidence selection, context packing, and missing-information detection.
4. AI system architecture should include gateways, routing, model/prompt/inference/retrieval/ranking services, feature stores, offline/online serving, queues, streaming, rate limiting, fan-out/fan-in, batch and real-time inference, human-in-the-loop systems, and fallbacks.
5. Cost/performance, evaluation/quality, and reliability/security should be first-class design topics, including caching, quantization/distillation, latency and throughput budgets, offline/online evals, human review, LLM-as-judge, regression testing, monitoring, drift, timeouts, retries, circuit breakers, observability, tracing, privacy, access control, prompt injection, jailbreak defense, audit logs, and compliance.

## Notable Quotes
- "Because AI system design is still system design."
- "The only difference is that now your bottlenecks are not just databases, caches, and queues."
- "They are tokens, context windows, retrieval quality, inference cost, hallucinations, model latency, evals, and user trust."

## Entities Mentioned
- [[Hermes Agent]] — not named by the tweet, but relevant as Tolaria's local agent-system context where the taxonomy maps onto future knowledge/eval discussions.

## Concepts Mentioned
Existing Tolaria concepts with partial overlap:
- [[AI Engineer Learning Roadmap Topic Map]] — this source is best deduped into the existing weak-social roadmap synthesis rather than promoted as a separate authoritative roadmap.
- [[Context Engineering]]
- [[Dynamic Context Loading]]
- [[Prompt Caching for Agent Context]]
- [[Evaluator-Optimizer Workflow]]
- [[Graph-aware Retrieval Evals]]
- [[Agent-Computer Interface Design]]
- [[Agentic Workflows and Agents]]
- [[Thin Harness Fat Skills]]
- [[Managed Local llama.cpp Provider]]
- [[AI/ML Package Supply-chain Compromise]]

## Follow-ups
- Evidence gap: do not use this post to justify implementation, adoption, interview-prep prioritization, or Hermes workflow changes. The taxonomy overlaps [[AI Engineer Learning Roadmap Topic Map]], which already records missing primary-source backfill needs for structured-output fallback chains, semantic caching, LLM observability, model routing, cost attribution, and fine-tuning-versus-context decision frameworks.
- Practical Tolaria use: preserve the source as another weak signal that AI/ML system design spans retrieval, inference economics, evals, observability, and security/reliability, while requiring primary docs, papers, repos, postmortems, or local evals before any topic becomes operational guidance.
