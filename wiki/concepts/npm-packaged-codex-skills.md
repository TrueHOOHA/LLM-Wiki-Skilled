---
type: concept
aliases: ["npm-distributed Codex skills", "one-command Codex skill install", "Codex skill npm packaging", "~/.codex/skills packaging"]
tags: [codex, skills, supply-chain, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# NPM-packaged Codex Skills

## Definition
NPM-packaged Codex Skills are local Codex skill folders distributed through npm packages whose installer writes a `SKILL.md`-based directory into `~/.codex/skills/<skill-name>`. The pattern makes skill sharing convenient, but it also turns a skill install into a local filesystem mutation and package-supply-chain boundary.

## Scope
This concept covers one-command distribution of Codex skill folders, install-target conventions, package metadata, overwrite behavior, bundled instructions, and provenance/safety review before local adoption. It does not imply that npm is the only or preferred distribution path, that Codex skill semantics are stable across versions, or that published skills should be installed without sandboxing and review.

## Contrasts
- Versus [[Domain-specific Agent Skill Libraries]]: npm packaging can distribute one skill or a library; the library pattern is about coordinated domain knowledge and dependency maps.
- Versus [[Catalog-backed Agent Tool Distribution]]: npm is the package/install channel, while a catalog is the discovery/index layer that may or may not execute anything.
- Versus [[Skill Validation Patterns]]: package installation proves only that files can be copied; it does not prove the skill is safe, compatible, effective, or compliant.
- Versus [[Thin Harness Fat Skills]]: the packaging pattern moves behavior into a skill folder, but the host harness still needs loading, permission, sandbox, and review semantics.

## Evidence
- [[Kappaemme X post on Local Client Prospector Codex skill]] records `package.json` metadata for `local-client-prospector-skill`, including `bin.local-client-prospector-skill`, `files: ["bin", "local-client-prospector"]`, Node `>=18`, and public npm publishing metadata.
- [[Local Client Prospector]] records the installer mechanism: Node `fs.rmSync(target, { recursive: true, force: true })` followed by copying the bundled skill directory to `~/.codex/skills/local-client-prospector`.

## Related
- [[Codex]]
- [[Local Client Prospector]]
- [[Catalog-backed Agent Tool Distribution]]
- [[Domain-specific Agent Skill Libraries]]
- [[Skill Validation Patterns]]
- [[Agent Skills]]
- [[Thin Harness Fat Skills]]

## Open Questions
- Should a local Codex skill package be installed only from a pinned version, a reviewed Git commit, or a sandboxed unpack step rather than direct `npx` execution?
- What minimum manifest should a packaged skill expose: source URL, version, license, target path, overwrite behavior, required tools, data-handling policy, and eval/check commands?
- How should a host distinguish knowledge-only skill files from executable helpers that can affect credentials, network calls, or local filesystem state?
