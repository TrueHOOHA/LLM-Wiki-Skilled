---
type: concept
aliases: ["async MCP job flow", "create-wait-result MCP workflow", "MCP scan job workflow", "agentic scan-poll-apply loop"]
tags: [agent-engineering, mcp, async-workflow, seo]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Async MCP Scan Job Workflow

An Async MCP Scan Job Workflow is an agent pattern where an MCP tool starts a long-running analysis job, returns a job identifier, a wait/poll helper retrieves a bounded customer-safe result, and the agent applies only minimal, evidence-linked changes before producing an audit trail. [[On-Page.ai automate SEO / MCP workflow]] is a concrete vendor example in the SEO domain.

## Definition
This concept covers tool workflows that are too slow or stateful for a single synchronous call but still need agent-friendly semantics: create a job, wait or poll with graceful timeout behavior, fetch the result, follow domain-specific guidance inside the result, make bounded edits or recommendations, and report evidence/uncertainty. The reusable primitive is not SEO-specific; SEO is the captured case study.

## Scope
The pattern includes:
- async job creation tools such as `scan_page`, `scan_page_lite`, `scan_page_deep`, or `classify_text`
- explicit wait/poll/result helpers such as `wait_for_job`, `check_job`, and `get_job_result`
- cost/credit awareness before large batches
- domain result schemas and top-level guidance such as `agent_guidance`
- minimal edit policies, skipped-item reporting, and audit trails
- batch manifests or progress ledgers when the workflow spans many URLs/pages

It does not prove that the underlying analysis is correct, that the edits improve business outcomes, that the agent can safely mutate production content, or that a vendor MCP server should be configured without a separate approval/eval.

## Contrasts
- Versus [[MCP Tool Connectors]]: this is a specific connector interaction pattern; MCP itself is only the transport/tool interface.
- Versus [[Durable Agent Operating Loop]]: durable loops manage longer workstreams; async scan jobs are one sub-loop inside a workstream.
- Versus [[Agent-Computer Interface Design]]: ACI is the design discipline; async job helpers are one concrete affordance for making slow tools less error-prone.
- Versus generic SEO advice: a scan job gives a structured cohort/result object; whether that object is valid or useful remains an empirical question.

## Evidence
- [[On-Page.ai automate SEO / MCP workflow]] documents On-Page.ai's recommended async flow: create with scan/classify tools, prefer `wait_for_job`, optionally use `check_job` for lightweight progress, and fetch completed output with `get_job_result`.
- [[On-Page.ai MCP SEO Workflow Assessment]] extracts the broader agent-engineering pattern and downgrades ranking-effectiveness claims to weak-to-medium vendor evidence.

## Related
- [[On-Page.ai]]
- [[MCP Tool Connectors]]
- [[Agent-Computer Interface Design]]
- [[Context-first MCP Workflow]]
- [[Durable Agent Operating Loop]]
- [[Codex]]
- [[Claude Code]]
- [[Hermes Agent]]

## Open Questions
- What should the standard error contract be for long-running MCP tools: timeout payloads, retry guidance, partial progress, result fetch URLs, or resumable job IDs?
- How should agents decide when to continue polling, block for human review, fall back to a lighter scan, or stop with an incomplete status?
- Which audit fields are mandatory before an agent applies scan-derived edits to live content: original text, changed text, source metric, confidence, rollback path, and human approval state?
- Can this pattern be evaluated generically across domains such as SEO, browser automation, data extraction, code analysis, and compliance checks?
