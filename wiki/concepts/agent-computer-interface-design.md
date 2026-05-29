---
type: concept
aliases: ["ACI", "agent-computer interface", "tool prompt engineering", "poka-yoke tools"]
tags: [agent-tooling, agent-engineering, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 10
---

# Agent-Computer Interface Design

## Definition
Agent-Computer Interface Design is the practice of designing tools, tool schemas, command surfaces, and documentation for LLM agents with the same seriousness that product teams apply to human-computer interfaces. The goal is to make correct tool use obvious, low-overhead, and hard to misuse.

## Scope
This concept covers examples, edge cases, input-format requirements, clear tool boundaries, mistake-resistant parameters, and empirical testing of how models actually use tools. In the Anthropic Building Effective Agents source, it includes a poka-yoke lesson from SWE-bench: requiring absolute file paths prevented relative-path mistakes after an agent changed directories. In [[Effective Harnesses for Long-running Agents]], the same interface-design discipline appears as task-local files and commands a fresh session can reliably inspect: `pwd`, progress notes, `feature_list.json`, git logs, `init.sh`, and browser automation checks. In the Browserbase source, the same principle appears as browser skills that tell agents when to use direct APIs, fetch/search, selectors, browser fallback, and site-specific gotchas. [[Databricks MemEx programmable scratchpad for LLM agents]] adds a tool-state substrate case: tool schemas can be exposed as typed Python functions whose outputs persist as live objects rather than repeatedly serialized context. [[On Seeing Through and Unseeing: The Hacker Mindset]] adds a failure-mode lens: every tool abstraction should be checked for the lower-level state, permissions, parsers, side effects, and error modes it hides.

## Contrasts
- Versus human-first CLI design: ACI optimizes for model reliability, compact context, unambiguous parameters, and machine-checkable failures.
- Versus prompt-only optimization: the Anthropic article says tool optimization took more effort than the overall prompt in a SWE-bench agent.
- Versus [[Agent-native CLI]]: agent-native CLIs are one possible ACI surface; ACI is broader and includes MCP tools, filesystem tools, browser tools, and workflow-specific tool contracts.
- Versus raw browser traces: ACI turns traces into instructions and deterministic affordances an agent can reliably use later.

## Evidence
- [[Alok Kumar X post on Building Effective Agents video and Anthropic agent patterns]] preserves Anthropic's claim that tool definitions should be prompt-engineered, tested, and made mistake-resistant.
- [[Printing Press Ecosystem Assessment]] and [[Agent-native CLI]] provide adjacent Tolaria evidence for agent-facing tool surfaces, compact outputs, dry-run modes, and safety checks.
- [[Matt Pocock AI Hero skills changelog]] adds skill-level ACI examples: handoff artifacts should reference existing artifacts and redact secrets; prototypes should expose the state/question being answered; review should split standards and spec fidelity.
- [[Browserbase Autobrowse browser-skill loop]] adds browser ACI examples: encode hidden endpoints, positional-array decoding, redirect/geolocation gotchas, fetch-first probes, and browser fallbacks in a skill so later agents do not infer them from scratch.
- [[Molly Studio OpenAI Endgame]] adds a human-facing interface-generation angle: if an agentic platform generates task UIs or turns apps into APIs behind a command layer, the resulting interface still needs explicit affordances, constraints, evaluation, and failure visibility rather than opaque model magic.
- [[Molly Studio API-ification of Everything]] reinforces the same ACI lesson for services-as-tools: if providers compete at the API/tool level, the agent-facing contract needs schemas, provenance, permissions, ranking transparency, confirmations, and typed failures.
- [[Unseeing Abstractions and Agent-engineering Lessons]] uses Gwern's abstraction-gap frame to ask where tool schemas leak actual parser behavior, cwd, auth, provider quirks, hidden browser state, or irreversible side effects.
- [[Codex-maxxing]] adds a shared-review-surface angle: browser/computer/connectors and a side panel are useful when the human and agent can inspect the same artifact or web state, but signed-in browser state, GUI takeover, uploads, refunds, and remote control need explicit affordances and approvals.
- [[Using Claude Code: The Unreasonable Effectiveness of HTML]] adds a task-local generated-interface case: HTML artifacts can improve review when controls, diagrams, and copy/export loops make state visible, but generated JavaScript and hidden side effects need explicit safety boundaries.
- [[Effective Harnesses for Long-running Agents]] adds a multi-context-window ACI case: initializer-created ledgers, scripts, logs, commits, and browser-verification tools make the project state legible to the next agent rather than relying on compaction.
- [[Databricks MemEx programmable scratchpad for LLM agents]] adds a programmable scratchpad case: typed tool wrappers, persistent scope, validated `submit()` returns, and async sub-agent calls can reduce context serialization, but require sandboxing, replay, and independent evaluation before adoption.

## Related
- [[Anthropic]]
- [[Hermes Agent]]
- [[Agent-native CLI]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Agentic Workflows and Agents]]
- [[Session Handoff Artifact]]
- [[Throwaway Prototype Spike]]
- [[Instruction Priority Control]]
- [[Two-lane Agent Review]]
- [[Autobrowse]]
- [[Agent-generated Browser Skills]]
- [[Deterministic-first Browser Automation]]
- [[Adaptive UI Generation]]
- [[Post-app Interfaces]]
- [[Agentic OS]]
- [[Intent-based Computing]]
- [[API-ification of Services]]
- [[MCP Tool Connectors]]
- [[Abstraction-leak Reasoning]]
- [[Security Mindset]]
- [[Weird Machines and Abstraction Gaps]]
- [[Artifact Review Surface]]
- [[HTML Artifact Review Loop]]
- [[Remote Agent Control]]
- [[Long-running Agent Harness]]
- [[Programmable Agent Scratchpad]]

## Open Questions
- Which Hermes tools produce the most model errors and would benefit from ACI review if Overseer later approves non-knowledge system work?
- Should absolute-path requirements, dry-run modes, typed failures, examples, and deterministic-first browser probes become a formal review checklist for future approved tool changes?
- What evaluation catches generated UI failures before users or agents act on hallucinated controls, hidden assumptions, or missing confirmation steps?
- When does a generated HTML micro-interface improve review enough to justify token cost, generation time, diff noise, and generated-JavaScript review risk?
