---
type: concept
aliases: ["programmable scratchpad", "persistent typed scratchpad", "MemEx-style scratchpad", "externalized agent scratchpad"]
tags: [agent-engineering, harnesses, context, memory]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Programmable Agent Scratchpad

## Definition
A Programmable Agent Scratchpad is an agent-harness design pattern where bulky tool outputs, intermediate computations, helper functions, and agent trajectories live in a persistent language runtime as typed objects, while the model receives only selected observations or validated returns. In [[Databricks MemEx programmable scratchpad for LLM agents]], the concrete substrate is a Python kernel with typed tool wrappers, persistent scope, `submit()` for structured final returns, and `spawn_agent()` for asynchronous sub-agent calls.

## Scope
This concept covers externalized state for tool-heavy or data-heavy agent tasks: DataFrames, retrieved documents, SQL results, trace objects, partial computations, helper functions, and candidate trajectories can remain outside the context window until the agent deliberately prints, summarizes, slices, or submits them. It does not mean arbitrary unsandboxed code execution is safe, nor does it prove that Databricks' reported MemEx gains generalize to Hermes, Codex, or Tolaria. For Tolaria, the useful pattern is narrower: context should hold the decision-relevant observation, while object-level state should remain inspectable, replayable, and typed in the harness.

## Contrasts
- Versus JSON/XML tool calling: standard tool calls usually serialize observations back into model context; a programmable scratchpad keeps objects in runtime scope and passes references or selected values forward.
- Versus ReAct: ReAct describes an observe-act reasoning loop; a programmable scratchpad can keep that loop while changing the action substrate from tool-call JSON to code blocks.
- Versus CodeAct: CodeAct uses executable code as the action space; the MemEx variant emphasizes drop-in tool-schema preservation, live object injection, typed `submit()` returns, and async sub-agent aggregation.
- Versus Anthropic Programmatic Tool Calling: both use code to manipulate tool state and avoid re-materializing intermediates; MemEx's captured distinction is persistent scoped objects plus explicit sub-agent and typed-return primitives.
- Versus Cloudflare Code Mode: both expose tools as typed code APIs in a sandbox; the captured Databricks article says Code Mode lacks persistent cross-turn scope, while MemEx makes scope persistence central.
- Versus [[Long-running Agent Harness]]: a long-running harness externalizes task continuity across sessions; a programmable scratchpad externalizes live tool state within a rollout or replayable trajectory.
- Versus [[Agent Memory Control Plane]]: memory-control planes manage durable cross-session knowledge; programmable scratchpads manage active execution state and may or may not persist beyond the run.

## Evidence
- [[Databricks MemEx programmable scratchpad for LLM agents]] is the primary source. Evidence is medium for the described design mechanism because the blog is first-party and specific, but weak-to-medium for performance superiority because results are vendor-owned and not independently reproduced.
- [[Agent-Computer Interface Design]] supplies the adjacent principle that agent-facing tools should expose schemas, typed failures, compact outputs, and mistake-resistant affordances.
- [[Context Engineering]] supplies the broader framing: not all useful state belongs in the prompt; task state, tools, memory, and execution artifacts are part of the context architecture.
- [[Long-running Agent Harness]] and [[Durable Agent Operating Loop]] supply the continuity caution: persistent state should be inspectable and verified, not merely hidden inside an agent runtime.

## Related
- [[Databricks]]
- [[Hermes Agent]]
- [[Agent-Computer Interface Design]]
- [[Context Engineering]]
- [[Long-running Agent Harness]]
- [[Durable Agent Operating Loop]]
- [[Agent Memory Control Plane]]
- [[Hybrid Graph-vector Agent Memory]]
- [[Typed DataPoint Memory Model]]
- [[Orchestrator-Worker Workflow]]
- [[Evaluator-Optimizer Workflow]]

## Open Questions
- What is the minimal safe Hermes/Tolaria analogue: persistent object handles in tool results, replayable trajectory objects, typed submit contracts, or all of them?
- How would a scratchpad expose state to future agents without hiding stale variables, secrets, oversized objects, or irreproducible side effects?
- Which tasks would actually benefit: Tolaria ingestion, query synthesis, Codex coding loops, browser automation, trace audits, or parallel evaluator aggregation?
- What independent eval would distinguish token-cost savings from correctness gains and from vendor benchmark overfit?
