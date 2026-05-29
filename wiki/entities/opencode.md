---
type: entity
aliases: ["OpenCode", "opencode"]
tags: [coding-agent, agent-framework, skills]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# OpenCode

## Identity
OpenCode is the coding-agent loop named in the Browserbase internal-agent context as preinstalled inside Browserbase's ephemeral Linux sandboxes and used with lazy-loaded markdown skills.

## Aliases
- OpenCode
- opencode

## Key Attributes
- Role in this source: part of Browserbase's internal `bb` agent environment, not the main Autobrowse product claim
- Claimed surrounding environment: ephemeral sandbox, pre-warmed snapshots, cloned repos, Bun/git/gh/ripgrep/prettier/pdftotext/TypeScript LSP/Tailscale, scoped tools, and skill loading
- Evidence quality: Browserbase self-report through related X longform; useful architecture context but not independently verified here

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] records the related Browserbase internal-agent article and its OpenCode/sandbox/skill/proxy architecture details.
- [[0xSero tweet on AImaxing tool list]] names OpenCode as “best TUI,” but supplies no method, repo comparison, task corpus, or benchmark. [[Skeptical AI Tooling Landscape from 0xSero AImaxing List]] keeps this as a weak lead adjacent to the stronger Browserbase sandbox context already captured here.

## Related
- [[Browserbase]]
- [[Autobrowse]]
- [[Thin Harness Fat Skills]]
- [[Hermes Agent]]
- [[GStack]]

## Open Questions
- Which OpenCode skill-loading and permission semantics differ from Hermes skills and Agent Skills?
- Is OpenCode mentioned here only as a Browserbase implementation detail, or as a transferable design precedent for other agent sandboxes?
