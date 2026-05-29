---
type: concept
aliases: ["institutional memory mounting", "AI-native onboarding mount", "developer onboarding context mount"]
tags: [agent-engineering, onboarding, knowledge-management, context]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Institutional Memory Mount

## Definition
An Institutional Memory Mount is a proposed onboarding/context surface where an agent gives a new worker task-ready access to curated organizational memory: developer environment state, permissions, repositories, backlog items, architecture documentation, internal discussions, issue tracker history, PRs, ownership metadata, and decision provenance.

## Scope
The concept covers the integration pattern implied by [[Jean-Michel Lemieux X post on AI-native onboarding as institutional-memory mounting]]: dev bootstrap plus permission routing plus retrieval over source-backed work history. It does not imply unrestricted access to all company data, automatic production authorization, or adoption of any specific Hermes feature. In Tolaria it should remain a low-confidence workflow hypothesis until supported by primary docs, security architecture, evals, or measured onboarding outcomes.

## Contrasts
- Versus ordinary onboarding: this pattern tries to make context queryable and provenance-linked rather than drip-fed through meetings, ad hoc Slack searches, and tribal knowledge.
- Versus generic RAG over company docs: the useful version must join docs, backlog, Slack/thread history, Linear/issues, PRs, ownership, and current workspace state while preserving source provenance and permissions.
- Versus durable agent memory: [[Memory Hygiene for AI Agents]] decides what should persist; an institutional-memory mount decides what context should be exposed for a role, project, and task at the moment of onboarding.
- Versus Tolaria itself: [[LLM Wiki Pattern]] compiles source-backed knowledge pages; an institutional-memory mount would be an operational context surface built from many systems and therefore would need approval, access controls, and evaluation before implementation.

## Evidence
- [[Jean-Michel Lemieux X post on AI-native onboarding as institutional-memory mounting]] supplies the term, workflow sketch, and decision-provenance claim, but only as an anecdotal social post.
- [[Context Engineering]] provides the adjacent frame: selecting and structuring the information environment an agent sees before and during work.
- [[Memory Hygiene for AI Agents]] provides the safety distinction between stable reusable facts, source-backed notes, temporary task state, and low-confidence material.
- [[Compounding AI Knowledge Stack]] and [[LLM Wiki Pattern]] provide the stronger Tolaria-local pattern for turning raw sources and decisions into reusable, inspected knowledge rather than opaque chat history.
- [[Notebook-grounded Retrieval via MCP]] is adjacent because it shows a narrower curated-corpus retrieval pattern, but the NotebookLM/MCP source is also weak and does not validate developer onboarding.

## Related
- [[Context Engineering]]
- [[Memory Hygiene for AI Agents]]
- [[Dynamic Context Loading]]
- [[Compounding AI Knowledge Stack]]
- [[LLM Wiki Pattern]]
- [[Notebook-grounded Retrieval via MCP]]
- [[Hermes Agent]]
- [[AI-native Onboarding as Institutional-memory Mount Assessment]]

## Open Questions
- What permission model prevents the agent from surfacing private, stale, or out-of-scope internal context during onboarding?
- Which source classes are mandatory for useful developer onboarding: repos, setup scripts, architecture docs, ADRs, Slack threads, issues, PRs, runbooks, incidents, or task-board state?
- What eval would prove this pattern helps: time to first safe PR, fewer human interruptions, better decision-provenance answers, fewer setup failures, or lower security/access mistakes?
- Should Overseer approve a later non-Beta evaluation of a small Hermes/Tolaria project-context pack before any implementation work?
