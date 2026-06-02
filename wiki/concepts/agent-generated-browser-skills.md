---
type: concept
aliases: ["browser skills", "agent-written browser skills", "autobrowsed skills", "browser-agent playbooks"]
tags: [browser-agents, skills, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent-generated Browser Skills

## Definition
Agent-generated Browser Skills are reusable, human-readable playbooks for website-specific browser tasks that an agent writes after learning a workflow through live runs, trace study, deterministic-helper discovery, and convergence checks.

## Scope
This concept covers the Browserbase pattern where [[Autobrowse]] graduates a browser workflow into `SKILL.md` plus helper files, CLI/fetch/search calls, selectors, endpoints, gotchas, and fallback methods. It is narrower than all skills: the target domain is web/browser automation where site-specific memory prevents repeated exploration.

## Contrasts
- Versus session traces: a browser skill is a maintained playbook, not a replay or screenshot reel.
- Versus generic browser agents: the skill starts future runs after discovery rather than forcing the model to rediscover the site.
- Versus deterministic scripts: the skill can describe when to use deterministic code, browser fallback, or higher-agency exploration.
- Versus manual Hermes skills: the Browserbase claim is that an agent can generate the skill from live-task experience; Hermes skill changes still require explicit approval when outside knowledge work.

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] explains Browserbase's claimed artifact shape and the Craigslist example.
- [[Browse.sh]] is the catalog/entity example for distributing these artifacts.
- [[Agent Skills]] corroborates the general portable `SKILL.md` folder and progressive-disclosure model.

## Related
- [[Autobrowse]]
- [[Browse.sh]]
- [[Browser Agent Discovery Tax]]
- [[Trace-driven Strategy Iteration]]
- [[Deterministic-first Browser Automation]]
- [[Thin Harness Fat Skills]]
- [[Agent-native CLI]]

## Open Questions
- What review, sandbox, credential, and eval gates are needed before an agent-generated browser skill is safe enough for a Hermes workflow?
- How often do such skills go stale when websites redesign flows or change hidden APIs?
