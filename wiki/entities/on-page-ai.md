---
type: entity
aliases: ["On-Page API", "On-Page SEO API", "api.on-page.ai", "On-Page SEO MCP"]
tags: [seo, mcp, agent-engineering, vendor]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# On-Page.ai

On-Page.ai is a vendor SEO platform/API captured in [[On-Page.ai automate SEO / MCP workflow]] as an on-page optimization API and MCP server for AI agents. The source supports the existence and documented shape of the API/MCP workflow, but not the stronger marketing claims that its recipes reliably improve rankings.

## Identity
On-Page.ai exposes on-page SEO analysis through REST endpoints and an HTTP MCP server. In this source, it positions itself as an agent-facing SEO evidence layer that scans a URL against live Google SERP competitors for a keyword and returns structured recommendations for entities, internal links, topical coverage, structured data, and page-experience benchmarks.

## Aliases
- On-Page API
- On-Page SEO API
- api.on-page.ai
- On-Page SEO MCP
- on-page-seo MCP server

## Key Attributes
| Attribute | Value |
| --- | --- |
| Category | SEO API / MCP server vendor |
| Main captured URLs | `https://on-page.ai/pages/automate-seo/`, `https://api.on-page.ai/`, `https://api.on-page.ai/mcp/docs`, `https://api.on-page.ai/llms-full.txt` |
| MCP server URL | `https://api.on-page.ai/mcp` |
| MCP tools named | `classify_text`, `scan_page`, `scan_page_lite`, `scan_page_deep`, `check_job`, `wait_for_job`, `get_job_result`, `check_credits` |
| REST model | Async job submission plus status/result endpoints |
| Scan tiers | Lite, standard, deep, and classify; captured pricing says 1.5, 2, 3, and 0.2 credits respectively |
| Evidence grade | Medium for documented integration mechanics; weak-to-medium for SEO effectiveness, ranking outcome, and superiority claims |
| Tolaria status | Knowledge-only reference; no MCP server, API key, Codex config, Hermes config, or SEO automation was installed or executed |

## Evidence
- [[On-Page.ai automate SEO / MCP workflow]] records Alpha's recovered vendor article and docs bundle. It verifies that the original submitted URL was malformed/404 and that the useful integration surface is the recovered article plus API/MCP docs.
- [[On-Page.ai MCP SEO Workflow Assessment]] preserves the reusable workflow primitive as an async MCP job pattern, while separating concrete tool/server facts from vendor marketing claims.

## Related
- [[Async MCP Scan Job Workflow]]
- [[MCP Tool Connectors]]
- [[Agent-Computer Interface Design]]
- [[Codex]]
- [[Claude Code]]
- [[Hermes Agent]]
- [[Agent-native CLI]]

## Open Questions
- Does the MCP server's auth/token handling and timeout/failure behavior work cleanly across Codex, Claude Code, Cursor, and other clients in practice?
- Which independent SEO outcome evidence, if any, supports the claim that On-Page.ai's entity/internal-link/subheadline recipes improve rankings rather than merely producing plausible recommendations?
- How much human review is required to prevent over-optimization, incorrect edits, brand-voice damage, or unsafe changes when agents apply scan recommendations at site scale?
