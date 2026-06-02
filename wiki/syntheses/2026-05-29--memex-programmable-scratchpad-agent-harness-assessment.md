---
type: synthesis
question: "Should Tolaria preserve MemEx as an agent-harness design pattern for externalized programmable scratchpads, and should Hermes/Tolaria investigate it further?"
tags: [agent-engineering, harnesses, context, evaluation]
created: 2026-05-29
updated: 2026-05-29
---

# MemEx Programmable Scratchpad Agent Harness Assessment

## Question / Purpose
Assess [[Databricks MemEx programmable scratchpad for LLM agents]] as a source for agent-harness design. The requested focus is MemEx as an externalized programmable scratchpad pattern, compared against CodeAct, ReAct, Anthropic Programmatic Tool Calling / Managed Agents, and Cloudflare Code Mode, with a knowledge-only proposal for Hermes/Tolaria.

## Answer / Analysis
Strongest counterargument first: MemEx is not adoption-grade evidence for Hermes or Tolaria. The originating X post is weak social evidence, and the stronger Databricks blog is still vendor-owned, first-party practitioner evidence with no public MemEx/aroll repository or independent reproduction in the captured source. Reported OfficeQA Pro and Enterprise Structured Retrieval gains should therefore be treated as hypotheses to evaluate, not facts to operationalize.

The useful durable pattern is narrower and worth preserving: the context window is a poor persistence layer for bulky tool outputs and agent trajectories. A [[Programmable Agent Scratchpad]] moves live execution state into a typed runtime, keeps object-level traces available for audit or aggregation, and only materializes selected observations back into model context. This pattern connects directly to [[Context Engineering]] and [[Agent-Computer Interface Design]]: the agent-facing interface should be typed, compact, inspectable, and hard to misuse rather than a stream of repeatedly serialized strings.

For Hermes/Tolaria, the most relevant design concept is not "run arbitrary Python for every agent." It is a scoped state object with typed tool outputs, typed `submit()` or return contracts, replayable traces, and async sub-agent aggregation that can preserve evidence without forcing lossy summaries. That could improve source ingestion, trace audit, and multi-agent synthesis if later validated; it could also create new hazards around sandboxing, stale hidden state, secret leakage, object lifetime, and non-reproducible side effects.

## Comparison Table
| Pattern | Core mechanism | Relationship to MemEx | Tolaria/Hermes implication | Evidence grade |
|---|---|---|---|---|
| ReAct | Observe-act loop with reasoning and tool observations | MemEx preserves the loop but changes the action substrate | Keep the useful status/observation loop, but do not assume text context must carry all state | Medium as established research lineage; not newly evaluated here |
| CodeAct | Executable code as agent action space | MemEx sits in this family and adds persistent scoped objects, typed returns, and async sub-agents in the captured Databricks framing | Code-as-action is powerful but demands sandboxing, determinism, and review gates | Medium for existence; low here for Hermes transfer |
| Anthropic Programmatic Tool Calling | Code runtime manipulates tool outputs and avoids repeated context materialization | Similar motivation: keep intermediate tool state outside context; MemEx emphasizes a drop-in ReAct harness and typed scope primitives | Good comparison point for stateful tool execution and context economy | Medium for practitioner mechanism, not outcome generality |
| Anthropic Managed Agents | Hosted durable sessions/sandboxes with files, network controls, resource caps, and replayable work state | A possible production substrate for MemEx-style kernels rather than the scratchpad idea itself | Any future Hermes analogue would need isolation, caps, audit, and replay before use | Medium for hosted-agent pattern |
| Cloudflare Code Mode | MCP tools exposed as typed code APIs in a sandbox | Related typed-code API surface; captured Databricks article says Code Mode lacks persistent scope | Typed APIs are useful; persistence and replay are separate design decisions | Medium for mechanism; low for outcome |
| Databricks MemEx | Persistent Python scope, typed tool functions, `submit()`, `spawn_agent()`, trace-object audit | The pattern being assessed | Preserve as knowledge and propose independent eval/design exploration only | Medium for first-party mechanics; weak-to-medium for performance claims |

## Evidence Grades
- Strong: The general design pressure is real across Tolaria's existing notes: large context, tool-output serialization, trace handoff, and multi-session continuity all create reliability/cost problems in [[Context Engineering]], [[Long-running Agent Harness]], and [[Durable Agent Operating Loop]].
- Medium: Databricks' first-party article provides specific architecture vocabulary and internal benchmark claims for MemEx, but it is not independently reproduced.
- Weak: The X layer, engagement metrics, future rollout claims, and broad generalization to Hermes/Tolaria.
- Unknown: Whether MemEx/aroll will be publicly available, whether OfficeQA Pro/Enterprise Structured Retrieval results reproduce externally, and whether the same gains appear on Tolaria/Hermes tasks.

## Approval Proposal
Proposal for Overseer approval: investigate a knowledge-only design concept for Hermes/Tolaria called "persistent scoped tool outputs". The scope would be a written design/eval brief only, not implementation: define typed tool-output handles, validated submit/return contracts, replayable trace objects, and async sub-agent aggregation; identify safety requirements; propose small eval tasks where lossy context summaries currently hurt outcomes.

Recommended decision: approve research/design exploration only if Overseer wants Hermes/Tolaria harness ideas prioritized. Do not approve implementation, prototype, config changes, cron jobs, or skill patches from this card. Confidence: moderate that the concept is worth tracking; low-to-moderate that it will outperform current Hermes/Tolaria patterns without careful eval.

## Citations
- [[Databricks MemEx programmable scratchpad for LLM agents]] — primary captured source for MemEx mechanics, reported evals, trace audit, and parallel aggregation claims.
- [[Programmable Agent Scratchpad]] — concept page extracting the reusable pattern and caveats.
- [[Agent-Computer Interface Design]] — adjacent Tolaria principle for typed, compact, mistake-resistant agent tool surfaces.
- [[Context Engineering]] — broader framing that context includes tools, memory, execution state, and task-specific substrate, not just prompt text.
- [[Long-running Agent Harness]] — comparison for externalizing state into inspectable artifacts and verification gates.
- [[Hermes Agent]] — local system comparator; any non-knowledge work remains approval-gated.

## Implications
- Treat MemEx as a design vocabulary source, not as an implementation target.
- If future investigation is approved, start with eval design and threat model: context savings, correctness, replayability, sandbox isolation, object lifetime, secret handling, and trace auditability.
- For Tolaria, the immediate knowledge value is to name the difference between durable knowledge, live scratchpad state, and model context; conflating them causes lossy summaries or hidden state.
- For Hermes, the most plausible future question is whether tool outputs should become typed, scoped, replayable objects with explicit submit contracts, especially for long-running tasks and sub-agent aggregation.

## Follow-up Questions
- Does Overseer want a separate approved design/eval brief for persistent scoped tool outputs, or should this remain archive-only knowledge for now?
- Which Hermes/Tolaria workload is the best candidate for eventual evaluation: Tolaria ingestion, trace auditing, Codex coding loops, browser research, or parallel reviewer aggregation?
- What sandbox/replay standard would be mandatory before any code-as-action scratchpad entered a real agent lane?
