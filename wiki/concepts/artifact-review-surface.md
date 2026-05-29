---
type: concept
aliases: ["agent artifact review surface", "side-panel review", "shared artifact surface"]
tags: [agent-engineering, review, artifacts, interface]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Artifact Review Surface

An Artifact Review Surface is a shared interface where the human and agent can inspect, annotate, operate, and revise the same output object without leaving the work loop.

## Definition

In [[Codex-maxxing]], the Codex side panel is the artifact surface: Markdown, spreadsheets, CSVs, PDFs, slides, `index.html`, Storybook, Remotion Studio, Slidev, Streamlit, and future Jupyter-like apps can be rendered or operated where the agent can also see them. [[Using Claude Code: The Unreasonable Effectiveness of HTML]] narrows one concrete member of this class: self-contained HTML files that make plans, PR explanations, diagrams, reports, or editing controls easier to inspect and export back into [[Claude Code]]. The point is not artifact generation alone; it is commentable, inspectable, same-object review.

## Scope

This concept covers rendered documents, slide decks, tables, PDFs, local static HTML, web previews, UI components, animation frames, data apps, browser panels, and review comments. In Tolaria, canonical knowledge remains Markdown; richer artifacts such as HTML/Slidev/Rich-style displays are useful hypotheses for future human-review surfaces, not deliverables Beta should generate without approval. The [[HTML Artifact Review Loop]] adds a sharper criterion: use HTML when browser-native layout or interaction materially improves review and produces a compact export such as a prompt, diff, JSON object, or selected parameter set.

## Contrasts

- Versus plain Markdown output: richer surfaces can expose layout, formulas, visual state, interactivity, and cut-off content that text alone hides.
- Versus blind file generation: the human can annotate and the agent can inspect the same rendered state before acting.
- Versus autonomous UI operation: a shared review surface should make state and changes more visible, not hide side effects behind a model.

## Evidence

- [[Codex-maxxing]] gives the direct side-panel pattern and examples across Markdown, spreadsheets, PDFs, slides, local HTML, Storybook, Remotion, Slidev, Streamlit, and Jupyter-like apps.
- [[Using Claude Code: The Unreasonable Effectiveness of HTML]] provides a practitioner source, Claude Blog mirror, examples gallery, and public repo for self-contained HTML artifacts as review, report, planning, and custom-editing surfaces.
- [[Agent-Computer Interface Design]] supplies the adjacent tool/interface principle: agents need clear affordances, visible state, constraints, and typed failures.
- [[Living Architecture Diagram]] and [[Multi-altitude Agent Code Review]] are related because artifacts can serve as higher-altitude review surfaces for generated systems.

## Related

- [[Durable Agent Operating Loop]]
- [[Queued Agent Steering]]
- [[Agent-Computer Interface Design]]
- [[Living Architecture Diagram]]
- [[Multi-altitude Agent Code Review]]
- [[HTML Artifact Review Loop]]
- [[Slidev]]
- [[Hermes Agent]]

## Open Questions

- Which artifact review surfaces are worth future approval-gated evaluation for Hermes/Codex: Markdown-only, static HTML, Slidev, Rich terminal reports, browser previews, or lightweight tables?
- How should canonical Markdown knowledge stay primary while richer review artifacts remain optional, generated, and disposable?
- What generated-JavaScript safety baseline is required before HTML review artifacts become acceptable for shared or repeated Hermes/Codex use?
