---
type: concept
aliases: ["HTML artifacts", "self-contained HTML artifact", "agent-generated HTML review UI", "HTML playground loop"]
tags: [agent-engineering, review, artifacts, interface]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# HTML Artifact Review Loop

## Definition
The HTML Artifact Review Loop is a human-agent workflow where an agent produces a self-contained browser-native HTML file as a dense, inspectable, sometimes interactive [[Artifact Review Surface]], then the human uses that page to understand, tune, annotate, reorder, or choose options and exports a compact result back into the agent.

## Scope
This concept covers static or lightly interactive HTML files for plans/specs, PR reviews, code explainers, diagrams, research reports, incident/status reports, design variants, decks, and purpose-built editing interfaces. The key mechanism is the export loop: `copy as prompt`, `copy diff`, `copy JSON`, selected parameters, ordered tickets, annotated choices, or another compact representation the agent can consume. It does not cover full application development, production UI generation, autonomous browser operation, or canonical Tolaria knowledge storage.

## Contrasts
- Versus Markdown plans/reports: HTML can improve scanability and information density with layout, color, visual hierarchy, SVG diagrams, tabs, collapsibles, and inline controls, but it is slower/noisier and less diff-friendly.
- Versus [[Adaptive UI Generation]]: HTML artifacts are local review surfaces for a specific task, not a standing product UI or app/platform replacement.
- Versus [[Throwaway Prototype Spike]]: a prototype answers a design/business-logic question by exercising behavior; an HTML artifact may be only a review/report surface, though the two overlap for interactive playgrounds.
- Versus canonical Tolaria pages: Tolaria should keep durable knowledge in Markdown with citations; HTML should be considered optional, disposable, approval-gated review packaging.

## Evidence
- [[Using Claude Code: The Unreasonable Effectiveness of HTML]] preserves Thariq Shihipar's practitioner claim, the Claude Blog mirror, the examples gallery, the public `anthropics/html-effectiveness` repo, and the related playground article.
- [[Codex-maxxing]] and [[Artifact Review Surface]] provide adjacent evidence that rendered artifacts can become same-object review surfaces inside durable agent loops.
- [[Agent-Computer Interface Design]] supplies the safety lens: HTML controls need visible state, bounded actions, clear export semantics, and reviewable generated JavaScript rather than hidden side effects.

## Related
- [[Artifact Review Surface]]
- [[Agent-Computer Interface Design]]
- [[Claude Code]]
- [[Anthropic]]
- [[Hermes Agent]]
- [[Two-lane Agent Review]]
- [[Adaptive UI Generation]]
- [[Throwaway Prototype Spike]]
- [[Durable Agent Operating Loop]]
- [[Codex-maxxing]]

## Open Questions
- Which task classes actually benefit enough from HTML to justify token cost, generation time, review overhead, and JavaScript safety checks?
- Should future approved Hermes/Alpha/Beta conventions allow HTML review packs for complex plans, PR explanations, research briefings, and incident timelines while keeping Markdown as canonical output?
- What safety baseline is sufficient: no external network calls, no credential access, inline source-visible JS only, export-only controls, sandboxed local viewing, and explicit provenance?
