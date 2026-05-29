---
type: source
source_path: raw/sources/2026-05-29-x-dbrxmosaicai-memex-programmable-scratchpad-2056818063215878618.md
title: "Databricks MemEx programmable scratchpad for LLM agents"
author: "Databricks AI Research Team / @DbrxMosaicAI"
date: 2026-05-19
tags: [agent-engineering, harnesses, context, evaluation]
created: 2026-05-29
---

# Databricks MemEx programmable scratchpad for LLM agents

## Summary
Databricks AI Research presents MemEx as a programmable Python scratchpad for LLM agents: tool outputs and intermediate trajectories stay as typed live objects in a persistent kernel, while only selected print/output material enters the model context. The linked Databricks blog is the useful evidence layer; the originating X post is weak social evidence, while the blog is medium practitioner evidence because it is first-party, vendor-owned, and not independently reproduced. MemEx is positioned as a drop-in change to a ReAct-style observe-act loop: the loop stays similar, but the action substrate changes from JSON/XML tool calls to executable code with persistent scope, typed tool wrappers, `submit()` returns, and async `spawn_agent()` calls. Databricks reports cost/accuracy gains on OfficeQA Pro and Enterprise Structured Retrieval, but the capture found no public MemEx/aroll repository, so Tolaria should treat the result as a design pattern and eval hypothesis rather than an adoptable implementation.

## Key Claims
1. The ordinary context window is the wrong persistent substrate for large tool outputs: SQL rows, document corpora, and trajectories should not be repeatedly serialized into every later turn.
2. A persistent typed Python scope can keep bulky tool results and helper functions outside model context, letting the model slice, transform, batch, and compose tool outputs before deciding what to materialize.
3. MemEx preserves the ReAct-style observe-act loop while changing the action space to code blocks, extending the CodeAct / Anthropic Programmatic Tool Calling / Cloudflare Code Mode lineage with persistent scope, `submit()`, and `spawn_agent()` primitives.
4. Databricks reports improvements across nine models on OfficeQA Pro and Enterprise Structured Retrieval, including 2-5 accuracy points at 25-30% lower cost for frontier models and larger relative gains for some Qwen models.
5. MemEx enables trajectory audit and parallel-thinking aggregation because full agent traces can remain object-level inputs rather than lossy text summaries.
6. Evidence remains incomplete for adoption: the claims are vendor-owned, figures are not reproduced by Tolaria, and no public MemEx/aroll implementation was found in the captured source.

## Notable Quotes
- "the context window is the only persistent substrate today's LLM agents have, and it floods fast" — X post capture.
- "MemEx gives the LLM a programmable scratchpad: a typed Python kernel that holds tool outputs, transforms them with code, and materializes only the print statements as tokens in the context" — Databricks blog capture.
- "Same observe-act loop. Different action space" — X post capture.
- "The only difference is the action space, JSON/XML structured tool calls versus MemEx's Python code blocks" — Databricks blog capture.

## Entities Mentioned
- [[Databricks]]
- [[Anthropic]]
- [[Hermes Agent]]
- [[Qwen3.6]]

## Concepts Mentioned
- [[Programmable Agent Scratchpad]]
- [[Agent-Computer Interface Design]]
- [[Context Engineering]]
- [[Long-running Agent Harness]]
- [[Durable Agent Operating Loop]]
- [[Orchestrator-Worker Workflow]]
- [[Evaluator-Optimizer Workflow]]

## Follow-ups
- Approval proposal: investigate a knowledge-only design concept for Hermes/Tolaria around persistent scoped tool outputs, typed submit/returns, replayable traces, and async sub-agent aggregation before any implementation work.
- Open evidence gap: find independent reproductions, public benchmark harnesses, or public MemEx/aroll code before treating reported cost/accuracy gains as adoption-grade.
