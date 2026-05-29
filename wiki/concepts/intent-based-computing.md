---
type: concept
aliases: ["intent computing", "intent-driven computing", "intent over applications", "intent-based interface"]
tags: [agent-engineering, interface-design, platform, weak-evidence]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Intent-based Computing

## Definition
Intent-based Computing is an interaction model where the user states a goal and an agentic interface chooses tools, service providers, workflows, and interface surfaces to satisfy it, rather than requiring the user to open a specific app and navigate a fixed flow. [[Molly Studio API-ification of Everything]] frames this as "intent over applications": the user expresses a task such as travel booking, and competing providers operate behind one interface.

## Scope
This concept covers goal-level task expression, provider/tool routing, preference-aware ranking, generated or selected task-specific UI, and confirmation/permission boundaries. It does not prove that fixed apps disappear, that users stop caring which provider is chosen, or that central routing will be neutral, safe, or legally straightforward.

## Contrasts
- Versus [[Post-app Interfaces]]: intent-based computing is the interaction model; post-app interfaces are the resulting product/platform shape where services are hidden behind the intent layer.
- Versus [[Agentic OS]]: an Agentic OS is one possible platform owner for intent-based computing, but intent routing can also happen inside narrower tools, assistants, or enterprise workflows.
- Versus [[Agentic Workflows and Agents]]: agentic workflows describe system execution; intent-based computing describes the user-facing abstraction that triggers execution.
- Versus ordinary search: search returns destinations or information; intent-based computing attempts to complete or coordinate the task.

## Evidence
- [[Molly Studio API-ification of Everything]] is the direct source for the "intent over applications" framing, but it supplies weak/practitioner evidence only.
- [[Molly Studio OpenAI Endgame]] provides adjacent vocabulary about command layers, generated UIs, and app/API abstraction, but remains speculative roadmap evidence.
- [[Agent-Computer Interface Design]] supplies a stricter agent-engineering constraint: goal-level interfaces still need visible affordances, safe tool contracts, confirmations, and failure modes.

## Related
- [[API-ification of Services]]
- [[MCP Tool Connectors]]
- [[Interface-layer Marketplace Risk]]
- [[Post-app Interfaces]]
- [[Agentic OS]]
- [[Adaptive UI Generation]]
- [[Context Engineering]]
- [[Hermes Agent]]

## Open Questions
- Which tasks are safe for automatic provider/tool selection, and which require explicit user choice or confirmation?
- What ranking objective should an intent router optimize: price, quality, user preference, platform revenue, provider reliability, privacy, or explicit human policy?
- What evidence would show true intent-based adoption rather than a normal chatbot/plugin integration?
