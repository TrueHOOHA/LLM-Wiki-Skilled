---
type: entity
aliases: ["Claude Code", "Cloud Code"]
tags: [coding-agent, agent-engineering, anthropic]
created: 2026-05-29
updated: 2026-05-29
source_count: 5
---

# Claude Code

## Identity
Claude Code is an Anthropic coding-agent/tooling comparator in Tolaria. It appears in a weak practitioner workflow comparison against [[Codex]], as a product surface with Learning/Explanatory output styles referenced by [[How AI assistance impacts the formation of coding skills]], as the first-party home for [[Agent Output Styles]] and [[TODO(human) Human-in-the-loop Coding]] in [[Anthropic brings Claude's Learning Mode to regular users and devs]], as the environment where [[Using Claude Code: The Unreasonable Effectiveness of HTML]] argues for self-contained HTML artifacts as richer review/output surfaces, and as adjacent product context for Anthropic's [[Long-running Agent Harness]] guidance.

## Aliases
- Claude Code
- Cloud Code (transcription artifact in the captured video)

## Key Attributes
| Attribute | Value |
| --- | --- |
| Category | Coding agent / coding assistant |
| Current Tolaria evidence | Weak practitioner social-source comparison plus primary Anthropic product-doc reference for output-style mechanics |
| Claimed workflow fit in Ben Holmes source | Planning mode, broad ask, research/discussion into a phased plan, implementation plus QA refinement |
| Learning-mode relevance | Learning/Explanatory output styles are a product-pattern hypothesis for [[Learning-preserving AI Assistance]], not outcome-validated proof |
| Output-style mechanics | [[Agent Output Styles]] change Claude Code response behavior through system-prompt-level policy without changing underlying codebase knowledge; built-in modes include Default, Proactive, Explanatory, and Learning |
| TODO(human) mechanism | [[TODO(human) Human-in-the-loop Coding]] asks the human to implement bounded pieces inside Learning mode rather than only approving generated code |
| HTML artifact relevance | [[HTML Artifact Review Loop]] is a practitioner workflow for plans, PR explainers, reports, diagrams, and custom editing interfaces that export prompts/diffs/JSON back into Claude Code |
| Long-running harness relevance | Anthropic's [[Effective Harnesses for Long-running Agents]] uses Claude Agent SDK context and quickstart mechanics rather than proving a Claude Code-specific workflow |
| Caveat | The sources do not prove a best Claude Code workflow, that output styles prevent skill decay, or that Anthropic's initializer/coding-agent harness generalizes unchanged to local Codex/Hermes workflows |

## Evidence
- [[Ben Holmes on Codex vs Claude Code workflow]] describes Holmes's Claude Code habit as starting in planning mode with a vague ask, using research and discussion to reach a step-by-step phased plan, then working through implementation, edge cases, and code quality.
- [[Codex vs Claude Code Workflow Hypothesis Assessment]] treats the comparison as a useful contrast frame but not a benchmark or tool-quality ranking.
- [[How AI assistance impacts the formation of coding skills]] notes Claude Code Learning and Explanatory output styles as design responses to the study's cognitive-offloading concern.
- [[Anthropic brings Claude's Learning Mode to regular users and devs]] adds source-checked product mechanics: output styles are system-prompt-level behavior modes, Explanatory adds educational insights, Learning uses `TODO(human)` markers for bounded human implementation, and longer modes cost more tokens.
- [[Using Claude Code: The Unreasonable Effectiveness of HTML]] frames self-contained HTML as an optional browser-native artifact format for dense review and two-way human-agent feedback.
- [[Effective Harnesses for Long-running Agents]] is not primarily a Claude Code workflow guide, but it supplies first-party Anthropic evidence for multi-context coding-agent continuity mechanics relevant to Claude-family agent tooling.

## Related
- [[Codex]]
- [[Ben Holmes]]
- [[Codex Sequential TDD Workflow]]
- [[Agentic Workflows and Agents]]
- [[Context Engineering]]
- [[Learning-preserving AI Assistance]]
- [[AI-assisted Coding Skill Formation]]
- [[Anthropic]]
- [[HTML Artifact Review Loop]]
- [[Artifact Review Surface]]
- [[Long-running Agent Harness]]
- [[Agent Output Styles]]
- [[TODO(human) Human-in-the-loop Coding]]
- [[Durable Agent Operating Loop]]

## Open Questions
- When does a separate planning-mode/document workflow outperform chat pseudo-planning and small sequential tasks?
- Are Holmes's Claude Code and Codex patterns caused by tool affordances, model behavior, task mix, or personal habit?
- Do Claude Code Learning/Explanatory output styles measurably improve coding skill retention, debugging skill, or later modification ability after accounting for token/cost overhead?
- Which Claude Code outputs actually benefit from HTML artifacts over Markdown after accounting for generation time, token cost, diff noise, and safety review?
- Does a Claude-family initializer/coding-agent harness outperform simpler resumed-session prompting on the same long-running task corpus?
