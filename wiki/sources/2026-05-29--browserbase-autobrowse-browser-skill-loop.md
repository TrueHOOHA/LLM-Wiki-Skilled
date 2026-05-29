---
type: source
source_path: raw/sources/2026-05-29-browserbase-autobrowse.md
title: "Autobrowse: The Mythos moment for Browser Agents is here"
author: "Kyle Jeong; Shubhankar Srivastava"
date: 2026-05-06
tags: [browser-agents, skills, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# Browserbase Autobrowse browser-skill loop

## Summary
Browserbase presents [[Autobrowse]] as a browser-agent learning loop that turns expensive exploration of a real website into a durable browser skill: markdown plus deterministic helpers, endpoints, selectors, gotchas, and fallback paths. The core claim is that browser agents suffer from a repeated discovery tax: every generic run must rediscover site structure, JavaScript behavior, hidden APIs, anti-bot friction, and workflow edge cases unless that knowledge is written into reusable memory. The strongest source-backed mechanism is the iteration loop: run a real task, study the trace, update `strategy.md`, prefer cheaper deterministic helpers such as fetch/search/Python when possible, stop after cost/turn-count convergence, and graduate the result to `SKILL.md`. Evidence is medium rather than strong: Browserbase supplies concrete examples and benchmark numbers, but the article is vendor-authored and does not include a reproducible benchmark harness or independent results. The related Browse.sh and Agent Skills material corroborates the general artifact shape, not the performance claims.

## Key Claims
1. Generic browser agents pay an avoidable [[Browser Agent Discovery Tax]] because they re-learn site-specific paths on every run.
2. [[Autobrowse]] tries to convert the first expensive run into reusable memory by iterating on a live browser task, studying traces, and recording lessons in a strategy scratchpad before graduating the result into [[Agent-generated Browser Skills]].
3. The preferred skill artifact is human-readable and agent-executable: `SKILL.md` plus deterministic glue such as CLI calls, `browse fetch`, `browse search`, selectors, custom Python, and helper files.
4. Browserbase says its Craigslist skill reduced a generic Claude Code-style loop from about $0.22 and 71 seconds to about $0.12 and 27 seconds, and that a form-fill experiment dropped from $1.40/run to $0.24/run in four iterations; these are vendor claims without attached reproducible data.
5. The article explicitly warns against using high-agency browser loops for deterministic parsing; a static 167-row catalog reportedly cost about $24 across four Autobrowse iterations before deterministic Python plus `browse fetch` solved it sub-second.
6. [[Browse.sh]] is presented as a public catalog/CLI of 100+ browser skills powered by Autobrowse, while the Agent Skills overview corroborates a broader portable `SKILL.md` folder format with progressive disclosure.
7. The related Browserbase internal-agent article describes one generalized `bb` agent built around ephemeral Linux sandboxes, OpenCode, lazy-loaded markdown skills, integration proxies, short-lived tokens, and scoped permissions; those details are useful architecture context but remain Browserbase self-report.

## Notable Quotes
- "Browser agents have an amnesia problem. They re-discover every site from scratch on every run, paying the full discovery tax forever."
- "Autobrowse fixes that by letting an agent iterate on a real task until it converges, then graduating the winning approach into a durable, reusable skill."
- "The artifact is the point. Every Autobrowse run produces a durable markdown file any future agent can load and execute."
- "Once consecutive iterations stop yielding meaningful improvements in cost or turn count, short-circuit."
- "Autobrowse is not the right tool when the task is deterministic parsing."
- "A skill is legible. It's durable, debuggable, human-auditable, and ownable."

## Entities Mentioned
- [[Browserbase]]
- [[Autobrowse]]
- [[Browse.sh]]
- [[Agent Skills]]
- [[Hermes Agent]]
- [[OpenCode]]

## Concepts Mentioned
- [[Agent-generated Browser Skills]]
- [[Browser Agent Discovery Tax]]
- [[Trace-driven Strategy Iteration]]
- [[Deterministic-first Browser Automation]]
- [[Thin Harness Fat Skills]]
- [[Agent-Computer Interface Design]]
- [[Compounding AI Knowledge Stack]]
- [[Agent-native CLI]]

## Follow-ups
- Open evidence gap: independent reproduction of Browserbase's Craigslist and form-fill benchmark claims is not provided in the source.
- Practical Hermes implication: the mechanism is relevant to Hermes skill workflows, but any harness, skill patch, code, cron, or browser-automation eval would require separate Overseer approval.
- Knowledge decision: preserve Autobrowse as a medium-evidence pattern for browser-agent skill graduation, not as adoption guidance.
