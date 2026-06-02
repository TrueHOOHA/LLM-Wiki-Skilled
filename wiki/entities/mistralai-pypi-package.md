---
type: entity
aliases: ["mistralai", "mistralai PyPI", "Mistral AI Python SDK"]
tags: [pypi, ai-ml-security, supply-chain]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# mistralai PyPI package

## Identity
`mistralai` is the PyPI package name used for Mistral AI's Python client/SDK; in this Tolaria source it matters as an AI/ML developer dependency that was reported by Microsoft Threat Intelligence as compromised in release v2.4.6.

## Aliases
- `mistralai`
- Mistral AI Python SDK
- mistralai PyPI package

## Key Attributes
| Attribute | Value |
|---|---|
| Package ecosystem | PyPI / Python |
| Reported compromised version | 2.4.6, according to the quoted Microsoft Threat Intelligence post |
| Reported compromised file | `mistralai/client/__init__.py` |
| Reported malicious behavior | import-time download and Linux second-stage execution |
| PyPI state checked by Alpha/Beta | latest 2.4.8; release 2.4.6 absent from JSON on 2026-05-29 |
| Evidence caveat | absence from PyPI JSON is consistent with removal/yanking but does not prove the incident details |

## Evidence
- [[LaurieWired X post on mistralai PyPI locale evasion]] records the captured Microsoft Threat Intelligence indicators and PyPI JSON check.

## Related
- [[Microsoft Threat Intelligence]]
- [[AI/ML Package Supply-chain Compromise]]
- [[Malicious Package Import-time Execution]]
- [[Locale and Geofence Malware Evasion]]

## Open Questions
- Is there a non-X Microsoft advisory, Mistral incident note, PyPI admin record, or package-diff report confirming the full compromise timeline and artifact hashes?
- Which dependency-resolution patterns made affected environments select v2.4.6 despite later clean releases?
