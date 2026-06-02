---
type: concept
aliases: ["context-first tools-second", "context-first MCP", "MCP context workflow"]
tags: [agent-engineering, mcp, tool-use, context]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Context-first MCP Workflow

## Definition
A Context-first MCP Workflow is a tool-use pattern where the agent first receives the relevant role, standards, priorities, domain facts, and task state, then uses MCP tools or other integrations to act on that curated context. [[Molly Studio API-ification of Everything]] makes the complementary platform claim that MCP-style connectors could let services plug into an LLM-native operating environment, but Tolaria treats that as weak until primary connector evidence is added.

## Scope
The pattern covers sequencing and separation of responsibilities: context explains why and what matters, tools expose capabilities and data access, and the task prompt binds them to a concrete action. It does not imply that MCP tools are safe or sufficient without credentials, permissions, sandboxing, and evaluation.

## Contrasts
- Versus tools-first automation: tool calls without curated context can produce generic, misprioritized, or unsafe actions.
- Versus context-only advising: context without tools can explain but not inspect current state or perform operations.
- Versus open-web retrieval: MCP can expose curated stores or domain APIs, but each server still needs source-quality and permission checks.

## Evidence
- [[Khairallah X article on mastering context engineering]] states the pattern explicitly: system prompt/context establishes what matters, MCP servers provide capabilities, and the task prompt joins them.
- [[Notebook-grounded Retrieval via MCP]] is a weaker but related claim about querying a curated notebook corpus through MCP.
- [[Molly Studio API-ification of Everything]] names MCP as a universal service connector, but does not provide protocol details, server examples, auth/permission analysis, or adoption evidence.
- [[Agent-Computer Interface Design]] and [[Agent-native CLI]] provide stronger adjacent design constraints: tools for agents need clear schemas, compact outputs, safe affordances, and eval gates.

## Related
- [[Context Engineering]]
- [[Dynamic Context Loading]]
- [[Notebook-grounded Retrieval via MCP]]
- [[MCP Tool Connectors]]
- [[Agent-Computer Interface Design]]
- [[Agent-native CLI]]
- [[Hermes Agent]]

## Open Questions
- Which MCP servers provide enough provenance, permissions clarity, and failure transparency for Tolaria/Hermes use?
- Should future evaluations compare context-first tool use against tool-only baselines for recurring Alpha/Beta workflows?
