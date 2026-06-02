---
type: source
source_path: raw/sources/2026-05-29-matt-pocock-aihero-skills-changelog.md
title: "Matt Pocock AI Hero skills changelog"
author: "Matt Pocock"
date: 2026-05-11
tags: [agent-engineering, skills, workflows, social-source]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# Matt Pocock AI Hero skills changelog

## Summary
Matt Pocock's X post announces two new AI Hero skills, `/handoff` and `/prototype`, and points to a changelog, skills index, homepage, and GitHub repo. The social post is weak evidence for effectiveness, but the linked skill files are medium-strength evidence for concrete workflow mechanisms: compacting sessions into handoff documents, using throwaway prototypes to answer design or state-machine questions, lowering supporting-context priority with XML tags, marking generated issues as ready for agents, and previewing two parallel review lanes. For Tolaria, the useful payload is a set of reusable agent-engineering workflow primitives, not proof that AI Hero's repo outperforms Hermes' existing skills or Kanban lifecycle. This source should therefore inform references and approval proposals, not direct Hermes skill changes.

## Key Claims
1. `/handoff` compacts a long current session into a temporary markdown document so a fresh agent/session can continue with context, intent, suggested skills, artifact references, and redaction of sensitive material.
2. `/prototype` treats throwaway code as a way to answer a question: UI prototypes compare radically different variations, while business-logic prototypes exercise state transitions that are hard to reason about on paper.
3. The changelog reports a bug fix where wrapping supporting information in XML tags reduced its "loudness" relative to core instructions, decreasing the tendency for `/grill-with-docs` to implement too eagerly.
4. `/to-prd` and `/to-issues` changed their generated label from `needs-triage` to `ready-for-agent-triage`, signaling that generated issues are intended to be directly actionable by agents.
5. A planned review skill would run two parallel sub-agents: one checking a diff against repository coding standards, and another checking fidelity to the originating issue or PRD.
6. The AI Hero homepage frames software fundamentals as more important, not less, in agent-assisted development; this is a positioning claim and should not be treated as outcome evidence.

## Notable Quotes
- "Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace."
- "Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead."
- "A prototype is **throwaway code that answers a question**. The question decides the shape."
- "The answer is the only thing worth keeping from a prototype. Capture it somewhere durable... along with the question it was answering."
- "The fix was wrapping the supporting information in XML tags to reduce its 'loudness' compared to the core instructions."
- "Two parallel sub-agents: one checking if the diff follows the repo's coding standards, and another checking if it faithfully implements the original issue or PRD."

## Entities Mentioned
- [[Matt Pocock]]
- [[AI Hero]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[Session Handoff Artifact]]
- [[Throwaway Prototype Spike]]
- [[Instruction Priority Control]]
- [[Agent-ready Triage Labeling]]
- [[Two-lane Agent Review]]
- [[Thin Harness Fat Skills]]
- [[Agent-Computer Interface Design]]
- [[Evaluator-Optimizer Workflow]]

## Follow-ups
- Archive/reference: keep the AI Hero skill files as concrete examples of handoff, prototype, and review prompt design.
- Approval proposal: consider a future review of Hermes' current handoff/progress-log/review templates against the AI Hero patterns, especially artifact references, redaction, suggested skills, and spec-fidelity review lanes.
- Do not adopt popularity metrics, video views, or the author's endorsement as evidence that the skills improve outcomes without a small eval or supervised pilot.
