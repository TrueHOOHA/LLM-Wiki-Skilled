---
type: concept
aliases: ["import-time malware", "malicious import side effects", "package import backdoor"]
tags: [supply-chain, malware, pypi, python]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Malicious Package Import-time Execution

## Definition
Malicious package import-time execution is a supply-chain attack pattern where attacker-controlled code runs when a package or module is imported, before the calling program explicitly asks for dangerous behavior.

## Scope
The pattern is especially dangerous in Python because imports happen inside notebooks, CLIs, tests, build scripts, REPL sessions, agents, and production services. A payload hidden in `__init__.py` can execute during ordinary dependency use and may download second stages, start background processes, or steal credentials before the developer notices.

## Contrasts
- Versus install-time malware: import-time code runs when the module is used, not only during `pip install`.
- Versus explicit malicious API calls: the user may only import a package and trigger side effects unknowingly.
- Versus normal package initialization: legitimate initialization should not fetch opaque payloads, spawn detached processes, or hide network activity.

## Evidence
- [[LaurieWired X post on mistralai PyPI locale evasion]] quotes Microsoft Threat Intelligence saying injected code in `mistralai/client/__init__.py` executes on import, downloads `transformers.pyz`, and launches a second-stage payload on Linux.
- [[mistralai PyPI package]] records the reported affected file and PyPI release-state check.

## Related
- [[AI/ML Package Supply-chain Compromise]]
- [[Locale and Geofence Malware Evasion]]
- [[Microsoft Threat Intelligence]]
- [[mistralai PyPI package]]

## Open Questions
- What static or dynamic checks should be standard before importing freshly updated AI/ML packages in agent or CI environments?
- Can notebook and agent runtimes safely restrict import-time network egress without breaking legitimate package behavior?
