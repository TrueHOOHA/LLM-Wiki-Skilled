---
type: concept
aliases: ["context architecture", "context infrastructure", "context engineering"]
tags: [agent-engineering, context, knowledge-management]
created: 2026-05-29
updated: 2026-05-29
source_count: 7
---

# Context Engineering

## Definition
Context Engineering is the practice of designing the information environment an LLM sees before and during a task: instructions, source files, memory, examples, retrieval results, tools, constraints, task-specific state, and now explicit mode goals such as delivery versus learning.

## Scope
The concept covers context architecture, persistent context, source-backed working memory, reusable standards, selection rules, live tool state, and interaction-mode framing. It does not mean that every larger prompt is better, nor that social claims about context quality should be adopted without evaluation. For learning-sensitive coding work, context engineering includes telling the assistant whether the objective is fast delivery, human comprehension, or both.

## Contrasts
- Versus prompt engineering: prompt wording is one ingredient; context engineering manages the surrounding information system.
- Versus plain RAG: retrieval is one possible context-supply mechanism, but context engineering also covers curated files, memory hygiene, instructions, examples, tools, and task modes.
- Versus generic personalization: the useful version is explicit, inspectable, and revisable, not an opaque accumulation of stale preferences.
- Versus [[Learning-preserving AI Assistance]]: context engineering is the broader system; learning-preserving assistance is one mode or policy it can encode.

## Evidence
- [[Khairallah X article on mastering context engineering]] provides a weak social curriculum and vocabulary for the concept, including immediate/session/persistent context layers and four reusable context files.
- [[Meta-Meta-Prompting: The Secret to Making AI Agents Work]] supports a neighboring mechanism through fat data, fat skills, resolver routing, and a markdown-backed knowledge stack.
- [[Anthropic Building Effective Agents and Hermes Workflow Implications]] supports the principle that tool/context design and evaluation gates matter more than hidden framework complexity.
- [[Jean-Michel Lemieux X post on AI-native onboarding as institutional-memory mounting]] adds a weak-social onboarding example where context engineering spans developer environment setup, permissions, backlog/docs retrieval, Slack/Linear/PR lookup, and decision provenance.
- [[Context Transfer Protocol (CTP)]] adds a weak practitioner thesis about context portability: applications could request scoped context vectors from provider-held user context rather than receiving raw data, but the source does not define an implementable protocol.
- [[Molly Studio OpenAI Endgame]] adds an adjacent weak-to-medium thesis: a platform such as [[OpenAI]] could use accumulated context as the missing layer that unifies apps, communication, generated interfaces, and identity, but the source does not prove that such centralization is safe or planned.
- [[How AI assistance impacts the formation of coding skills]] adds a primary-study reason to encode task mode explicitly: delegation/offloading can complete code while weakening short-term mastery, so unfamiliar learning tasks may need context that demands explanation, conceptual inquiry, or comprehension checks.
- [[Codex-maxxing]] adds a workstream-loop example where context is not only a prompt prefix: voice/transcripts, queued steering, file-backed memory, browser/computer state, remote review, Heartbeats, and artifact surfaces all become context channels that need priority, privacy, and verification boundaries.
- [[Databricks MemEx programmable scratchpad for LLM agents]] adds the live-state version of this problem: large tool outputs and agent trajectories can be kept as typed objects in a persistent runtime while only selected observations enter model context.

## Related
- [[Dynamic Context Loading]]
- [[Memory Hygiene for AI Agents]]
- [[Context-first MCP Workflow]]
- [[Compounding AI Knowledge Stack]]
- [[LLM Wiki Pattern]]
- [[Thin Harness Fat Skills]]
- [[Institutional Memory Mount]]
- [[Context Transfer Protocol]]
- [[Context Vault]]
- [[Agentic OS]]
- [[AI-native Identity-context Layer]]
- [[Adaptive UI Generation]]
- [[Learning-preserving AI Assistance]]
- [[AI-assisted Coding Skill Formation]]
- [[Durable Agent Operating Loop]]
- [[Queued Agent Steering]]
- [[File-backed Agent Memory]]
- [[Artifact Review Surface]]
- [[Programmable Agent Scratchpad]]

## Open Questions
- Which context components most improve Hermes/Tolaria outputs: identity, standards, project state, examples, source summaries, retrieval hits, tool affordances, or explicit mode goals?
- What measurable threshold should justify adding more persistent context rather than keeping a workflow prompt-only?
- How can an AI platform use cross-app context without turning personalization into opaque surveillance, lock-in, or stale-memory leakage?
- How should an agent distinguish tasks where the operator wants delivery from tasks where the operator wants skill formation?
