---
type: concept
aliases: ["skill validation", "agent skill linting", "skill QA", "skill eval gates"]
tags: [skills, evaluation, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# Skill Validation Patterns

## Definition
Skill Validation Patterns are checks that keep agent skills well-formed, discoverable, compatible, safe, and empirically useful before they are published, imported, or allowed to influence agent execution.

## Scope
The minimal layer is structural validation: required `SKILL.md` frontmatter, matching directory names, description length, naming constraints, supporting-file layout, and syntax checks for bundled scripts. Stronger layers include dependency-map checks, migration/rename checks, sandboxed helper execution, provenance review, security review, and task-level evals showing that a skill improves outcomes. Eval files are evidence that a maintainer intended to test behavior, not evidence that the skill is good unless the evals are run, reviewed for coverage, and tied to task outcomes. Tolaria records these as knowledge; implementing validation scripts or changing Hermes skill gates requires separate approval.

## Contrasts
- Versus frontmatter lint only: structural validity says a skill can be loaded; it does not prove task quality or safety.
- Versus repo popularity: stars and forks are weak social signals, not validation of individual skill performance.
- Versus eval harnesses: validation catches format and safety defects; evals measure whether the skill changes task outcomes.
- Versus [[Agent-Computer Interface Design]]: validation is the gate; ACI is the design discipline that makes skill/tool use obvious and hard to misuse.

## Evidence
- [[LLMJunky X post on Marketing Skills for AI Agents]] records [[Marketing Skills]] AGENTS.md guidance: `name` must match directory, lowercase/hyphen constraints, `description` length constraints, `SKILL.md` line-count guidance, optional `references/`, `scripts/`, and `assets/`, and Node CLI syntax/usage/dry-run checks.
- [[Corey Haines X post on Marketing Skills v2.0]] records the v2.0 claim of "100% evals coverage" and a fresh repo-tree check showing 42 per-skill `evals/evals.json` files, while explicitly leaving eval execution, coverage quality, and outcome improvement unverified.
- [[Kappaemme X post on Local Client Prospector Codex skill]] adds a compact single-skill example: final checks require duplicate removal, exact-name search before claiming a missing website, no `Hot` label when a real standalone site exists, fewer verified leads over many weak guesses, and reporting search location/radius/categories/date.

## Related
- [[Marketing Skills]]
- [[Agent Skills]]
- [[Domain-specific Agent Skill Libraries]]
- [[Agent-Computer Interface Design]]
- [[Evaluator-Optimizer Workflow]]
- [[Thin Harness Fat Skills]]
- [[Local Client Prospector]]
- [[NPM-packaged Codex Skills]]

## Open Questions
- Which checks should be mandatory before Hermes imports or adapts a third-party skill pattern?
- What is the smallest eval that can distinguish a useful domain skill from a well-formatted but ineffective one, and how should it handle renamed or consolidated skills?
- How should validation handle skills that bundle executable helpers, API credentials, MCP tools, or plugin manifests?
- Should local skill installers require a dry-run/manifest mode before writing or overwriting `~/.codex/skills` directories?
