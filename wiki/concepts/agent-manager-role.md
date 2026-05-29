---
type: concept
aliases: ["agent manager", "AI system owner", "systems manager"]
tags: [agent-engineering, ai-org-design, orchestration]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent Manager Role

## Definition

The Agent Manager Role is a proposed organizational role where a person owns, improves, monitors, and is accountable for AI agents or AI-mediated workflows rather than only performing the original manual task. [[Zeb Evans on ClickUp 100x Organization]] frames people who automate their jobs with AI as future owners of the AI systems they create.

## Scope

This concept covers responsibility for agent behavior, workflow automation, quality gates, system prompts/skills/context, review paths, escalation, and outcome measurement. It does not mean an agent manager should bypass human approvals, own production changes without review, or treat an automated workflow as proven just because it saves labor. In Hermes terms, the closest safe analogy is a person who owns a bounded [[Durable Agent Operating Loop]] with explicit review, evidence, and handoff gates.

## Contrasts

- Versus tool user: an agent manager owns the operating system around the tool, not only a single prompt or UI interaction.
- Versus people manager: the role may manage workflows/agents rather than direct human reports, but still needs accountability and escalation boundaries.
- Versus unchecked automation: automation ownership should include monitoring, rollback paths, source provenance, and [[AI Coding Outcome Measurement]] when coding agents are involved.

## Evidence

- [[Zeb Evans on ClickUp 100x Organization]] provides weak-social evidence for the role label and the claim that automation-minded workers become AI-system owners. The post names many examples at ClickUp but does not show artifacts, org charts, job descriptions, failure modes, or measured outcomes.

## Related

- [[AI-native Organization Design]]
- [[AI Coding Orchestration and Review Bottleneck]]
- [[AI Coding Outcome Measurement]]
- [[Durable Agent Operating Loop]]
- [[Agent Lifecycle Hooks]]
- [[Agent-Computer Interface Design]]
- [[Hermes Agent]]

## Open Questions

- What should an agent manager be accountable for: throughput, quality, incident rate, human time saved, customer outcomes, compliance, or explainability?
- What logs, evals, review gates, and rollback mechanisms are necessary before an automated workflow can be treated as owned rather than merely improvised?
- How should compensation and authority follow agent ownership without encouraging automation theater or hidden risk transfer?
