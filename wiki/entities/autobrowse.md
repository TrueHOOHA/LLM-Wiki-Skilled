---
type: entity
aliases: ["Autobrowse"]
tags: [browser-agents, skills, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Autobrowse

## Identity
Autobrowse is Browserbase's workflow for having an AI browser agent learn a live website task through repeated runs, trace study, strategy iteration, and graduation into reusable [[Agent-generated Browser Skills]].

## Aliases
- Autobrowse

## Key Attributes
- Creator/operator in source: [[Browserbase]]
- Artifact: `SKILL.md` plus helper files, deterministic calls, endpoints, selectors, gotchas, and fallback methods
- Loop: objective, run, study trace, update `strategy.md`, iterate, converge, graduate
- Iteration policy in source: usually capped around 3-5 iterations with aggressive short-circuiting when cost or turn count stops improving
- Best fit: dynamic or exploratory browser tasks with hidden APIs, heavy client-side rendering, multi-step flows, login/wizard paths, and non-trivial shortest-path discovery
- Poor fit: deterministic parsing problems where direct fetch plus parser logic solves the task more cheaply
- Evidence quality: medium primary/vendor evidence for mechanism, weaker for performance magnitude

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] captures the Browserbase explanation, Craigslist and form-fill cost claims, deterministic-parsing failure case, and related Browse.sh/Agent Skills context.

## Related
- [[Browserbase]]
- [[Browse.sh]]
- [[Agent-generated Browser Skills]]
- [[Trace-driven Strategy Iteration]]
- [[Deterministic-first Browser Automation]]
- [[Thin Harness Fat Skills]]

## Open Questions
- What task-completion, latency, cost, maintenance, and safety metrics should decide whether an Autobrowse-like loop beats a hand-written helper or ordinary skill update?
- How much of the convergence heuristic is stable across sites, models, and browser environments?
