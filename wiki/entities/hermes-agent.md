---
type: entity
aliases: ["Hermes", "Hermes Agent"]
tags: [agent-framework, mcp, orchestration]
created: 2026-05-28
updated: 2026-05-29
source_count: 22
---

# Hermes Agent

## Identity
Hermes Agent is an open-source agent framework used for terminal and messaging workflows, with MCP integration support and skill-based orchestration.

## Aliases
- Hermes
- Hermes Agent

## Key Attributes
- Category: agent framework
- Claimed capability in NotebookLM source: connect to NotebookLM through MCP for notebook-grounded retrieval
- Relevance in Printing Press source: possible consumer of focused agent skills and agent-native CLIs, but installation or workflow changes require explicit approval
- Relevance in Garry Tan source: comparator harness for [[Thin Harness Fat Skills]], model/runtime/tool routing, and [[Compounding AI Knowledge Stack]] architecture
- Relevance in Anthropic effective-agents source: target system for applying [[Agentic Workflows and Agents]] boundaries, [[Agent-Computer Interface Design]], [[Orchestrator-Worker Workflow]], [[Evaluator-Optimizer Workflow]], sandbox/eval gates, and approval-worthy workflow proposals
- Relevance in TinyFish source: possible consumer of [[Zero-credit Search-Fetch Agent Ingestion]] through generic MCP/CLI/SDK surfaces, but no official Hermes-specific integration was found and any validation remains approval-gated
- Relevance in JUMPERZ Discord/Kanban source: proposed system of record for assignment, execution, status, logs, and proof of work inside [[Chat Intake Kanban Mirror Pattern]], while Discord/chat remains intake and mirrored visibility only
- Relevance in AI Hero skills source: comparator for [[Session Handoff Artifact]], [[Throwaway Prototype Spike]], [[Instruction Priority Control]], [[Agent-ready Triage Labeling]], and [[Two-lane Agent Review]] patterns; any skill/template/routing change remains approval-gated
- Relevance in pi-llamacpp source: possible future consumer of a [[Managed Local llama.cpp Provider]] pattern for Codex/Hermes local-runtime loops, but only after separate approval and target-machine evaluation
- Relevance in Browserbase Autobrowse source: comparator for skill-based agent memory; Browserbase's generated browser-skill loop is relevant to Hermes skills and Tolaria knowledge promotion, but any harness, skill patch, CLI install, or browser eval remains approval-gated
- Relevance in Marketing Skills source: comparator for large vertical skill-library design, root context skills, cross-skill dependency maps, Agent Skills compatibility, plugin packaging, validation patterns, and tool registries; any import, skill patch, validation script, or local CLI/tool evaluation remains approval-gated
- Relevance in Jean-Michel Lemieux onboarding source: comparator for a possible future [[Institutional Memory Mount]] or project-context-pack evaluation, but the source is weak/social and no Hermes onboarding feature should be implemented without separate Overseer approval
- Relevance in Ben Holmes Codex/Claude Code source: comparator for local coding-agent workflow design; [[Codex Sequential TDD Workflow]] is preserved as a weak hypothesis about explicit requirements, chat pseudo-planning, small sequential tasks, TDD/Playwright checks, and cleanup before PR/merge, not as a Hermes rule change
- Relevance in Molly Studio CTP source: comparator for privacy-bounded context portability, user authorization/revocation, provider-held memory, and scoped context sharing; [[Context Transfer Protocol]] is preserved as a weak conceptual thesis, not as an implementation target
- Relevance in Molly Studio OpenAI Endgame source: comparator for [[Agentic OS]], [[Post-app Interfaces]], [[Adaptive UI Generation]], and [[AI-native Identity-context Layer]] pressures; useful for context/permission/UI evaluation questions, not a Hermes roadmap mandate
- Relevance in Molly Studio API-ification source: comparator for [[Intent-based Computing]], [[API-ification of Services]], [[MCP Tool Connectors]], and [[Interface-layer Marketplace Risk]]; useful for tool/service routing, permission, ranking, provenance, and generated-UI evaluation questions, not an implementation mandate
- Relevance in Anthropic skill-formation source: possible future consumer of explicit delivery-mode versus learning-mode task framing through [[AI-assisted Coding Skill Formation]] and [[Learning-preserving AI Assistance]], but any Hermes prompt/profile/skill change remains approval-gated
- Relevance in Claude Code output-styles source: comparator for [[Agent Output Styles]] and [[TODO(human) Human-in-the-loop Coding]] as behavior-policy layers; any Hermes behavior-mode abstraction, persistent mode metadata, prompt/profile change, skill, or eval checklist remains approval-gated
- Relevance in Jason Liu Codex-maxxing source: comparator for durable workstream loops spanning pinned/compacted threads, queued steering, file-backed memory, remote review, heartbeat monitors, artifact surfaces, and verification goals; useful as approval-oriented knowledge, not a Hermes feature mandate
- Relevance in OpenAI Codex remote/mobile source: source-backed comparison point for host-bound execution, secure relay control surfaces, mobile approvals, SSH/devbox routing, workspace-scoped automation identity, and lifecycle hooks; any Hermes/Codex remote-control, token, hook, notification, or eval implementation remains approval-gated
- Relevance in Thariq Shihipar HTML artifact source: comparator for optional future review-pack conventions where self-contained HTML may improve human review of plans, PR explainers, research reports, incident timelines, diagrams, or custom editing interfaces; any HTML template/skill/convention remains approval-gated and should preserve Markdown canonicalization
- Relevance in Cognee source: comparator for [[Agent Memory Control Plane]], [[Hybrid Graph-vector Agent Memory]], [[Session-to-Graph Memory Bridge]], typed DataPoint provenance, MCP memory tools, and feedback-aware improvement loops; any Cognee installation, plugin, MCP configuration, benchmark, or prototype remains approval-gated
- Relevance in Databricks MemEx source: comparator for [[Programmable Agent Scratchpad]], persistent scoped tool outputs, typed `submit()`/return contracts, replayable trace objects, and async sub-agent aggregation; any Hermes scratchpad, code-runtime, sandbox, tool-schema, or eval implementation remains approval-gated
- Evidence quality: mixed; social claims remain weak, while primary article/repo/docs mechanics are stronger for existence and design guidance than for productivity or adoption claims

## Evidence
- [[2026-05-28--ibuzovskyi-hermes-notebooklm-mcp-claim|X post claim summary]] states a 4-step setup and claims notebook-grounded task execution.
- [[2026-05-28--hermes-notebooklm-mcp-claim-assessment|Assessment]] grades the NotebookLM claim as weak until primary docs or repo evidence is found.
- [[Printing Press — agent-native CLIs from a single prompt]] says Printing Press can install focused skills for Hermes/OpenClaw-style agents and recommends approval before installation.
- [[Printing Press Ecosystem Assessment]] frames Printing Press as relevant to Hermes tool orchestration, but only as knowledge/evaluation material until approved.
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] includes Hermes as one possible harness and notes that the X-rendered GitHub repo link was stale/404; active docs/source should use the NousResearch Hermes Agent materials.
- [[Alok Kumar X post on Building Effective Agents video and Anthropic agent patterns]] connects Anthropic's workflow/agent distinction, ACI/tool guidance, evaluator loops, orchestrator-worker patterns, and sandbox/eval gates to Hermes as knowledge-only proposal material.
- [[Anthropic Building Effective Agents and Hermes Workflow Implications]] argues that Hermes should preserve a simplest-solution bias and approval-gate any non-knowledge workflow or tool-interface changes.
- [[Divyansh Tiwari X post on TinyFish free Search/Fetch for agents]] claims Hermes was switched to TinyFish, but the durable evidence is limited to TinyFish official Search/Fetch pricing/docs and generic integration surfaces.
- [[TinyFish Search/Fetch Agent Web Access Assessment]] recommends a small approved validation before any Hermes/Tolaria adoption.
- [[JUMPERZ X post on Hermes Kanban + Discord task-board bridge]] proposes Discord/chat intake plus Hermes Kanban as system of record, but provides only weak social evidence and screenshots.
- [[Discord Intake and Hermes Kanban Mirror Assessment]] preserves the system-of-record boundary and recommends approval-gated evaluation only, not implementation.
- [[Matt Pocock AI Hero skills changelog]] provides weak-to-medium evidence for reusable workflow primitives from AI Hero skills, but not proof that Hermes should adopt them directly.
- [[AI Hero Skills Workflow Patterns Assessment]] recommends reference-only preservation plus a possible approval-gated future review of Hermes handoff/review templates.
- [[Armin Ronacher X post on pi-llamacpp Qwen3.6 local provider]] preserves a weak-social lead plus stronger linked repo evidence for local llama.cpp provider lifecycle mechanics.
- [[pi-llamacpp Managed Local Provider Pattern Assessment]] recommends knowledge-only preservation and a separate approval-gated eval before any Hermes/Codex local-runtime adoption.
- [[Browserbase Autobrowse browser-skill loop]] records Browserbase's trace-to-skill mechanism, Browse.sh catalog, Agent Skills context, and deterministic-first caveat as knowledge-only material for Hermes skill-workflow thinking.
- [[Browserbase Autobrowse and Hermes Skill Loop Assessment]] argues that Hermes can learn from the memory/artifact mechanism but should not create an Autobrowse harness, import third-party skills, or patch skills without separate approval.
- [[LLMJunky X post on Marketing Skills for AI Agents]] records Marketing Skills as a repo-backed but still weak/socially-discovered case study for domain-specific skill-library structure, validation patterns, and registry-backed tool discovery.
- [[Marketing Skills Agent Skill Library Assessment]] preserves the reusable design implications for Hermes/Tolaria while explicitly avoiding import, prototype, config, skill, or tool changes.
- [[Jean-Michel Lemieux X post on AI-native onboarding as institutional-memory mounting]] records a weak-social claim about agentic developer onboarding, decision-provenance retrieval, and institutional-memory mounting.
- [[AI-native Onboarding as Institutional-memory Mount Assessment]] preserves the concept as knowledge-only and frames any Hermes/Tolaria context-pack evaluation as approval-gated.
- [[Ben Holmes on Codex vs Claude Code workflow]] and [[Codex vs Claude Code Workflow Hypothesis Assessment]] preserve a weak Codex workflow hypothesis relevant to local coding-agent practice, while explicitly avoiding Hermes workflow or skill changes without approval.
- [[Context Transfer Protocol (CTP)]] and [[Context Transfer Protocol and Hermes Context-portability Assessment]] preserve Molly Studio's weak CTP thesis as a privacy/context-portability comparison point for Hermes memory boundaries, not as an implementation proposal.
- [[Molly Studio OpenAI Endgame]] and [[OpenAI Agentic OS Thesis Assessment]] preserve Molly Studio's OpenAI OS/identity thesis as a skeptical concept map for context, permission, generated UI, app/API, and identity risks; no Hermes implementation follows from it.
- [[Molly Studio API-ification of Everything]] and [[API-ification and Intent-based Computing Agent Engineering Assessment]] preserve the API-ification/intent-routing thesis as weak knowledge-only input for service/tool contracts, connector safety, provider-ranking transparency, and marketplace-risk analysis.
- [[How AI assistance impacts the formation of coding skills]] and [[AI Assistance and Coding Skill Formation Assessment]] preserve a medium-evidence warning that coding assistance can trade off against short-term skill formation when used as delegation; any Hermes learning/explanatory mode should be an approved opt-in experiment, not a silent default.
- [[Anthropic brings Claude's Learning Mode to regular users and devs]] and [[Claude Code Output Styles and Hermes Behavior-mode Implications]] preserve Claude Code output styles as a source-checked behavior-mode pattern; Hermes should treat delivery/explanatory/learning modes as proposal/eval vocabulary only until Overseer approves non-knowledge work.
- [[Codex-maxxing]] and [[Codex-maxxing Durable Operating Loop Assessment]] preserve the durable operating-loop pattern for Hermes/Codex thinking while explicitly avoiding any cron, remote-control, skill, config, artifact, or system change without approval.
- [[Work with Codex from anywhere]] and [[Codex Remote/mobile Workflow Primitives for Hermes Assessment]] preserve primary OpenAI Codex primitives for host/device separation, secure relay reachability, SSH/devbox host routing, workspace-scoped access tokens, lifecycle hooks, mobile approvals, and output review; Tolaria treats them as proposal/eval material only.
- [[Using Claude Code: The Unreasonable Effectiveness of HTML]] and [[HTML Artifacts as Agent Output and Review Surfaces]] preserve HTML artifacts as a knowledge-only candidate review surface for Hermes/Codex/Tolaria, not a deliverable convention or skill change.
- [[Cognee - Open Source Memory Platform for Agents]] and [[Cognee Memory Architecture Patterns Assessment]] preserve Cognee as source-backed agent-memory architecture vocabulary for Hermes/Tolaria design questions, while explicitly avoiding integration or evaluation work without approval.
- [[Databricks MemEx programmable scratchpad for LLM agents]] and [[MemEx Programmable Scratchpad Agent Harness Assessment]] preserve MemEx as a knowledge-only agent-harness pattern for externalized typed state, replayable trajectories, and sub-agent aggregation; no Hermes implementation or eval follows without Overseer approval.

## Related
- [[NotebookLM]]
- [[Notebook-grounded Retrieval via MCP]]
- [[Printing Press]]
- [[Agent-native CLI]]
- [[Catalog-backed Agent Tool Distribution]]
- [[OpenClaw]]
- [[GStack]]
- [[Thin Harness Fat Skills]]
- [[Prompt Caching for Agent Context]]
- [[Agentic Workflows and Agents]]
- [[Agent-Computer Interface Design]]
- [[Orchestrator-Worker Workflow]]
- [[Evaluator-Optimizer Workflow]]
- [[2026-05-28--hermes-notebooklm-mcp-claim-assessment]]
- [[TinyFish]]
- [[Zero-credit Search-Fetch Agent Ingestion]]
- [[Chat Intake Kanban Mirror Pattern]]
- [[Session Handoff Artifact]]
- [[Throwaway Prototype Spike]]
- [[Instruction Priority Control]]
- [[Agent-ready Triage Labeling]]
- [[Two-lane Agent Review]]
- [[pi-llamacpp]]
- [[llama.cpp]]
- [[Qwen3.6]]
- [[Managed Local llama.cpp Provider]]
- [[Multi-Token Prediction Local Inference]]
- [[Autobrowse]]
- [[Browse.sh]]
- [[Agent-generated Browser Skills]]
- [[Browser Agent Discovery Tax]]
- [[Deterministic-first Browser Automation]]
- [[Marketing Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Skill Validation Patterns]]
- [[Institutional Memory Mount]]
- [[Codex]]
- [[Claude Code]]
- [[Codex Sequential TDD Workflow]]
- [[OpenAI]]
- [[Agentic OS]]
- [[Post-app Interfaces]]
- [[Adaptive UI Generation]]
- [[AI-native Identity-context Layer]]
- [[Intent-based Computing]]
- [[API-ification of Services]]
- [[MCP Tool Connectors]]
- [[Interface-layer Marketplace Risk]]
- [[AI-assisted Coding Skill Formation]]
- [[Learning-preserving AI Assistance]]
- [[Agent Output Styles]]
- [[TODO(human) Human-in-the-loop Coding]]
- [[Durable Agent Operating Loop]]
- [[Queued Agent Steering]]
- [[Agent Heartbeat Loop]]
- [[File-backed Agent Memory]]
- [[Remote Agent Control]]
- [[Artifact Review Surface]]
- [[HTML Artifact Review Loop]]
- [[Host-bound Agent Execution]]
- [[Workspace-scoped Automation Identity]]
- [[Agent Lifecycle Hooks]]
- [[Cognee]]
- [[Agent Memory Control Plane]]
- [[Hybrid Graph-vector Agent Memory]]
- [[Session-to-Graph Memory Bridge]]
- [[Typed DataPoint Memory Model]]
- [[Programmable Agent Scratchpad]]

## Open Questions
- Which exact GitHub repository is meant by "NotebookLM skill" in the earlier post?
- Does the NotebookLM workflow provide reproducible evidence beyond marketing copy?
- Which Printing Press catalog entries, if any, are worth sandboxed evaluation for Hermes workflows?
- Which Garry Tan/GBrain mechanisms are already covered by current Hermes skills/Tolaria and which would need explicit implementation approval?
- Which Anthropic pattern fits each Hermes work type: simple augmented call, fixed workflow, orchestrator-worker, evaluator-optimizer, or autonomous agent?
- Which Hermes tool interfaces would most benefit from ACI review if Overseer later approves non-knowledge system work?
- Should Overseer later approve a TinyFish Search/Fetch validation focused on freshness, cost, failure behavior, MCP endpoint correctness, and Hermes fit?
- Should Overseer later approve a minimal chat-intake/Kanban-mirror evaluation where Hermes Kanban remains authoritative and Discord/chat is only an intake and visibility layer?
- Should Overseer later approve a Hermes handoff/review-template audit against AI Hero's artifact-reference, redaction, suggested-skills, and two-lane review patterns?
- Should Overseer authorize a separate Default/Overseer evaluation of a Hermes-managed local llama.cpp provider pattern for Codex/Hermes, including lifecycle cleanup and Qwen3.6 MTP performance checks?
- Should Overseer ever approve a browser-task discovery-tax eval, and if so should it compare fetch/search, deterministic parser, normal browser tool use, and high-agency trace iteration?
- Should Overseer approve a separate evaluation of root-context skills, dependency maps, and validation gates before any Marketing Skills-inspired pattern is adapted into Hermes skills?
- Should Overseer later approve a small Hermes/Tolaria project-context-pack evaluation that tests [[Institutional Memory Mount]] benefits against permission, freshness, and decision-provenance risks?
- Should a future non-Beta Codex workflow eval compare separate plan documents against chat pseudo-planning plus small TDD tasks?
- If Overseer later approves an agentic-OS evaluation, which risk should dominate first: generated UI correctness, app/API confirmation boundaries, context-permission scoping, or identity/memory safety?
- If an intent-router or API-ified-service pattern is ever evaluated, what should dominate first: connector permission safety, provider-ranking transparency, generated UI correctness, or service/API task-completion reliability?
- Should Overseer later approve a session-scoped Hermes/Codex learning-mode experiment for unfamiliar-library tasks, and what comprehension/debugging metric should decide success?
- Should a future behavior-mode eval start with prompt-scoped local Codex instructions, Hermes task metadata, or a durable skill/profile abstraction?
- Should any future durable-loop eval prioritize draft-only inbox/Slack monitoring, Codex PR follow-up, Tolaria ingestion continuity, or artifact-review surfaces?
- Should Overseer ever approve optional HTML review packs for complex Hermes/Codex/Tolaria outputs, and what generated-JavaScript safety baseline would be required?
- Should Overseer later approve an agent-memory eval that compares Cognee-style session/graph memory against Tolaria wiki/qmd/Hermes memory baselines?
- Should Overseer approve a knowledge-only design/eval brief for persistent scoped tool outputs, typed submit contracts, replayable traces, and async sub-agent aggregation before any scratchpad implementation is considered?

