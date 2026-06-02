---
type: synthesis
question: "When should agents produce self-contained HTML artifacts instead of Markdown for output and review surfaces?"
tags: [agent-engineering, review, artifacts, interface, tolaria]
created: 2026-05-29
updated: 2026-05-29
---

# HTML Artifacts as Agent Output and Review Surfaces

## Question / Purpose
Assess [[Using Claude Code: The Unreasonable Effectiveness of HTML]] as a source for reusable agent-output conventions, preserving the useful [[HTML Artifact Review Loop]] pattern while avoiding an unsupported rule that agents should replace Markdown with HTML.

## Answer / Analysis
Strongest counterargument first: the source does not prove HTML artifacts are more effective than Markdown. It is a practitioner essay plus a gallery/repo of examples, not a benchmark with controlled tasks, review-speed measurements, comprehension tests, defect-detection rates, token/time accounting, or security review. Confidence is moderate that the workflow exists and is useful for the author's Claude Code practice; confidence is low-to-medium that it generalizes across operators and tasks without extra cost or review risk.

The durable pattern is artifact selection. Markdown should remain the default for canonical notes, simple plans, durable logs, source summaries, and anything that needs readable diffs. HTML becomes attractive when the bottleneck is human review or manipulation rather than plain text authoring: dense code review, multi-approach planning, visual design comparison, incident timelines, repo/module maps, research explainers, and custom editing tasks where controls can export a prompt/diff/JSON back to the agent.

The highest-leverage subpattern is not "make it pretty"; it is two-way feedback. A self-contained HTML page can encode state, choices, sliders, annotations, ticket order, feature-flag edits, prompt-template options, or design parameters, then emit a compact artifact for the agent to continue from. That makes HTML a specialized [[Artifact Review Surface]] and [[Agent-Computer Interface Design]] problem: controls must expose what they change, exports must be inspectable, and generated JavaScript must not smuggle side effects.

For Tolaria, canonical knowledge should stay Markdown. HTML artifacts may be useful later as disposable review packs for complex syntheses, diagrams, source maps, or proposal review, but the durable claims, citations, evidence grades, and decisions should be promoted back into `wiki/` Markdown. Beta should not create HTML deliverables or templates without Overseer approval.

## Comparison Table
| Use case | Prefer Markdown when | Consider HTML when | Caveat |
|---|---|---|---|
| Plans/specs | Linear plan, small scope, diffable durable doc | Multiple approaches, diagrams, mockups, dependency maps, long plan likely to be skimmed | HTML plan still needs Markdown summary/canonical decision record |
| PR/code review | Small diff, ordinary inline comments | Annotated diff, module map, severity colors, flow diagrams, reviewer briefing | Generated review UI must not replace actual diff/test review |
| Research/Tolaria reports | Source-backed durable note | Dense visual map, gallery, timeline, side-by-side comparison for human review | Final knowledge belongs in cited Markdown pages |
| Incident/status reports | Short status update | Timeline, ownership map, severity/status color, drilldowns | Avoid hiding uncertainty behind polished visuals |
| Design/prototype exploration | Textual requirements or static mockup description | Variant matrix, sliders, live preview, animation tuning | Prototype output is not production code |
| Custom editing interfaces | Simple text/list edits | Reordering, feature flags, prompt tuning, dataset curation, annotations | Export must be reviewable and side-effect-free |

## Citations
- [[Using Claude Code: The Unreasonable Effectiveness of HTML]] captures the X article, Claude Blog mirror, examples gallery, GitHub repo, and related playground/two-way interaction article.
- [[HTML Artifact Review Loop]] abstracts the reusable workflow pattern for self-contained browser-native review/edit/export artifacts.
- [[Artifact Review Surface]] frames HTML as one member of a broader class of rendered same-object review surfaces.
- [[Agent-Computer Interface Design]] supplies the design/safety lens for generated controls, visible state, and bounded export semantics.
- [[Codex-maxxing]] gives adjacent evidence for durable agent loops that use rendered artifacts as review surfaces.
- [[Claude Code]] and [[Anthropic]] anchor the source's product and publisher context.

## Implications
- For Hermes/Codex: HTML review packs are a candidate future convention for high-friction review tasks, but adoption should be approval-gated and evaluated against Markdown for comprehension, correction rate, defect detection, token/time cost, diffability, and safety.
- For Alpha/Beta/Tolaria: Beta may preserve this as knowledge and cite it in future syntheses, but should not generate HTML artifacts, patch skills, add templates, or change deliverable conventions without explicit approval.
- For deliverable design: use a decision gate, not a format preference. Ask: is the human bottleneck visual/spatial/interactive review? Is there a compact export loop? Is the artifact disposable? Are generated-JS risks bounded?
- For safety: prefer self-contained local files, no network calls, no credential access, explicit provenance, inspectable export text, and no hidden state-changing actions.

## Curated Top 10
1. Artifact-selection criteria: default Markdown unless visual/spatial/interactive review is the real bottleneck.
2. Copy/export loop: `copy as prompt`, `copy diff`, `copy JSON`, selected parameters, or ordered lists back to the agent.
3. Static-first HTML: use layout/SVG/tables/collapsibles before unnecessary JavaScript.
4. PR explainer pattern: annotated diff + module map + severity legend + test evidence, not a replacement for code review.
5. Planning pattern: compare approaches with diagrams, data flow, risks, and acceptance checks.
6. Research/report pattern: timeline, source map, claim/evidence matrix, contradiction callouts.
7. Incident/status pattern: timeline, ownership, current state, blockers, decision log.
8. Custom editor pattern: narrow interface for reordering/tuning/annotating with explicit export preview.
9. Safety baseline: self-contained, local/sandboxed, no external calls, visible JS, export-only controls.
10. Canonicalization rule: promote the final decisions and evidence back into Markdown/Tolaria.

## Recommended Next Actions
- Archive/preserve as knowledge now; do not implement from this Beta card.
- Approval proposal: Overseer could later authorize a Default/Overseer-lane review of an optional HTML artifact review-pack convention or skill/template, constrained to disposable artifacts, generated-JS safety rules, and Markdown canonicalization.
- If approved later, first eval should compare Markdown vs HTML for one or two recurring tasks such as complex PR review briefings or Tolaria synthesis review, measuring review time, correction count, missed issues, token/time cost, and reviewer preference.

## Follow-up Questions
- Should Overseer ever approve optional HTML review packs for complex Hermes/Codex/Tolaria outputs, or should Tolaria stay Markdown-only except for explicitly requested diagrams/prototypes?
- If approved later, which task should be tested first: complex PR review, implementation planning, Tolaria research synthesis, incident/status report, or custom prompt/config editing?
- What generated-JS safety baseline would be acceptable before any agent-produced HTML is opened or shared?
