---
type: source
source_path: raw/sources/2026-05-29-trq212-html-effectiveness-2052809885763747935.md
title: "Using Claude Code: The Unreasonable Effectiveness of HTML"
author: "Thariq Shihipar"
date: 2026-05-20
tags: [agent-engineering, claude-code, artifacts, interface, review]
created: 2026-05-29
---

# Using Claude Code: The Unreasonable Effectiveness of HTML

## Summary
Thariq Shihipar argues that [[Claude Code]] agents should sometimes produce self-contained HTML artifacts instead of long Markdown files when the human needs dense visual structure, diagrams, UI controls, or an export loop back into the agent. The original X article is weak social evidence, but the mirrored Claude Blog post and public `anthropics/html-effectiveness` gallery/repo strengthen the claim that this is a real [[Anthropic]] practitioner workflow and not merely a viral screenshot. The reusable Tolaria pattern is not "always use HTML"; it is an artifact-selection rule for high-friction review/editing tasks where browser-native layout and interactivity improve human inspection. Caveats remain substantial: HTML can cost more tokens, take longer to generate, create noisy diffs, and introduce generated-JavaScript safety/review risk.

## Key Claims
1. Markdown remains useful for simple text, but long agent-generated Markdown plans/specs/reports become hard to read and easy to ignore.
2. Self-contained HTML can encode richer structure: tables, SVG diagrams, code snippets, colored severity markers, responsive layout, tabs, collapsibles, sliders, knobs, drag/reorder behavior, and copy/export buttons.
3. HTML artifacts are especially useful as [[Artifact Review Surface|artifact review surfaces]] for planning, PR explanation, codebase understanding, design exploration, incident/status reporting, research explainers, and custom editing interfaces.
4. The strongest two-way pattern is an HTML micro-interface that lets the human review/tune/reorder/annotate, then export `copy as prompt`, `copy diff`, or `copy JSON` back into Claude Code.
5. The author warns against prematurely converting this into a generic `/html` skill; the better primitive is deciding what an artifact should do and asking the agent for a suitable HTML artifact when the review problem warrants it.
6. Evidence supports existence and plausibility of the workflow, not measured superiority over Markdown or other review surfaces.

## Notable Quotes
- "Core claim" captured by Alpha: Thariq has started preferring HTML as an output format instead of Markdown and sees the pattern among others on the Claude Code team.
- Alpha's capture summarizes the selection rule: use HTML when outputs need information density, visual clarity, sharing, two-way interaction, or context-rich reports rather than plain editable text.
- Alpha's capture also records the caveat: HTML may use more tokens, take 2-4x longer than Markdown, and produce noisy version-control diffs.

## Entities Mentioned
- [[Anthropic]] — publisher of the Claude Blog mirror and owner of the public examples repo.
- [[Claude Code]] — the agent surface where the author applies the HTML-artifact workflow.
- [[Hermes Agent]] — relevant comparator for approval-gated artifact conventions, not a system to change from this source alone.

## Concepts Mentioned
- [[HTML Artifact Review Loop]] — new concept capturing self-contained browser-native artifacts with copy/export feedback into the agent.
- [[Artifact Review Surface]] — existing concept updated to include HTML as a concrete browser-native review surface.
- [[Agent-Computer Interface Design]] — adjacent interface-design principle for clear affordances, visible state, and safe export/confirmation boundaries.
- [[Adaptive UI Generation]] — broader UI-generation concept; HTML artifacts here are narrower, task-local review UIs rather than app/platform replacement.
- [[Two-lane Agent Review]] — adjacent review-loop concept for separating standards/spec review from artifact-specific inspection.

## Follow-ups
- Approval proposal for Overseer: consider a future non-Beta convention or skill/template for optional HTML artifact review packs only after defining safety rules for generated JavaScript, export-only controls, provenance, and when Markdown remains the default.
- Open evidence need: no benchmark compares HTML artifacts against Markdown for review speed, comprehension, correction rate, token/time cost, or defect detection.
- Practical caveat: Tolaria canonical knowledge should remain Markdown; HTML artifacts, if ever approved, should be disposable review surfaces or exported summaries, not the canonical source of record.
