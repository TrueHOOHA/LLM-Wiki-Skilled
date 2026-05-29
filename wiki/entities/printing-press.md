---
type: entity
aliases: ["Printing Press", "CLI Printing Press", "Public Library", "printing-press-library"]
tags: [agent-tooling, cli, mcp, printing-press, supply-chain]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Printing Press

## Identity
Printing Press is a project and public catalog for generating and distributing agent-native Go CLIs, agent skills, and MCP server surfaces for APIs, apps, websites, and community projects. The current Tolaria evidence supports its generator/catalog mechanics, but not unbenchmarked claims about arbitrary generated-tool quality, token efficiency, or safe unsandboxed adoption.

## Aliases
- Printing Press
- CLI Printing Press
- Public Library
- printing-press-library

## Key Attributes
| Attribute | Value |
|---|---|
| Builders named on homepage | Matt Van Horn and Trevin Chow |
| Generator repo described in raw capture | `github.com/mvanhorn/cli-printing-press` |
| Library repo described in raw capture | `github.com/mvanhorn/printing-press-library` |
| Main outputs claimed | Go/Cobra CLI, Claude Code/OpenClaw skills, MCP server or MCP metadata/surface |
| Catalog mechanism | `registry.json` inventory, npm installer, category search/list/install/update/uninstall |
| Agent-facing affordances | compact output, JSON/agent modes, dry-run, typed failures, local SQLite/FTS5, sync/search/sql, compound commands, CLI/MCP dual interface |
| Reusable quality gates | spec parse, build, vet, govulncheck, help/version/doctor, dogfood/runtime verification, scorecard, MCP parity, agent-readiness review |
| Main risk | supply-chain and credential exposure from `npx`, `go install @latest`, global skill installation, and third-party API wrappers |

## Evidence
- [[Printing Press — agent-native CLIs from a single prompt]] summarizes the captured homepage and linked repo inspection notes.
- [[Printing Press Ecosystem Assessment]] grades the project as useful for knowledge promotion but not yet ready for unsandboxed adoption.

## Related
- [[Agent-native CLI]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Hermes Agent]]

## Open Questions
- Which generated tools are highest quality after independent dogfood testing rather than homepage demos?
- Which install surfaces can be pinned, sandboxed, or audited before any Hermes use?
- Are MCP metadata and CLI behavior consistently equivalent across the catalog, or only for mature entries?
