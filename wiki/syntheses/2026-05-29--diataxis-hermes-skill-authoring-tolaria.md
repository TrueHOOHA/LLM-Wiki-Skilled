---
type: synthesis
question: "How should Diátaxis inform Hermes skill authoring, documentation structure, and Tolaria note organization?"
tags: [documentation, skills, agent-engineering, knowledge-management]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Diátaxis Implications for Hermes Skill Authoring and Tolaria

## Question / Purpose
Assess the weak-social DataThoughts Diátaxis tweet as a Tolaria source and preserve the useful documentation framework implications for [[Hermes Agent]], skill authoring, and Tolaria knowledge organization without making skill, code, configuration, or workflow changes.

## Answer / Analysis
The strongest counterargument against acting on the tweet is evidentiary: the tweet claims a docs skill exists but exposes no actual skill, repository, prompt, transcript, or before/after artifact. Confidence is low for the tweet author's specific skill claim.

Confidence is moderate for Diátaxis as a useful documentation framework because the linked primary site directly explains the model and gives practitioner-oriented guidance. Diátaxis says documentation should separate four user needs: learning through tutorials, accomplishing work through how-to guides, consulting facts through reference, and understanding context through explanation. That distinction maps cleanly onto common Hermes skill failure modes: over-explaining inside procedural steps, burying command/reference facts in prose, or turning reusable operating procedures into broad essays.

For Hermes skill authoring, Diátaxis suggests a review lens rather than an automatic rewrite rule. A skill's main body usually behaves like a how-to guide for an already-capable agent: triggers, ordered steps, tool choices, pitfalls, and verification. Reference-like material should be compact and easy to scan: exact commands, schemas, environment variables, paths, option tables, and failure modes. Explanation should justify non-obvious boundaries, tradeoffs, and approval gates, but should not interrupt the action path. Tutorial-style walkthroughs are useful when teaching a new agent pattern, but they should not replace a direct execution checklist.

For Tolaria, Diátaxis supports the existing [[LLM Wiki Pattern]] separation. Raw files are source material, source notes summarize and extract, concept pages behave partly like reference/definition pages, and syntheses carry explanation, implications, caveats, and decision support. The framework argues against dumping every kind of content into a single note: if a source summary starts becoming a policy recommendation, move that reasoning into a synthesis; if a synthesis needs canonical definitions, link concept pages rather than restating them everywhere.

## Comparison Table
| Diátaxis mode | User need | Hermes/Tolaria analogue | Risk when blurred |
|---|---|---|---|
| Tutorial | Acquire skill through guided practice | Worked examples, first-run walkthroughs, onboarding skill examples | Agents get long teaching prose when they need execution steps |
| How-to guide | Apply skill to a real task | Skill workflow steps, Kanban worker procedures, task-specific playbooks | Procedure gets polluted with background, optional variants, or reference dumps |
| Reference | Consult accurate facts | Tool schemas, command flags, frontmatter contracts, paths, checks | Facts become hard to find or accidentally softened into prose |
| Explanation | Understand why/context | Syntheses, design rationale, caveats, approval-boundary explanations | Rationale interrupts action or becomes treated as a mandate |

## Citations
- [[DataThoughts tweet on Diátaxis docs skill]] records the weak social claim, the linked primary Diátaxis site, the four documentation modes, and the caveat that no actual docs skill artifact was exposed.
- [[Diátaxis Documentation Framework]] captures the reusable concept for future Tolaria cross-reference and review.
- [[Skillify]] and [[Thin Harness Fat Skills]] explain why skill content quality matters in Hermes-like systems: reusable behavior lives in skill files and supporting knowledge, not only in hidden harness code.
- [[Agent-Computer Interface Design]] is adjacent because Diátaxis can make agent-facing instructions and reference surfaces more mistake-resistant.

## Implications
- Preserve Diátaxis as a documentation-quality concept, not as an implementation directive.
- For future approved skill reviews, classify each section by intended mode before editing: action path, reference facts, explanatory rationale, or tutorial/example.
- For Tolaria notes, keep source summaries descriptive, concepts definition/reference-like, and syntheses explanatory/decision-oriented.
- Treat weak social claims about agent skills as discovery only unless the skill artifact or measurable outcome can be inspected.

## Follow-up Questions
- Is there a specific Hermes skill class where Overseer has noticed confusion between procedure, reference, and explanation?
- Should future approved audits target high-use worker skills first, or Tolaria note templates first?
- What failure should matter most if this becomes an approved eval later: fewer tool-use mistakes, faster task completion, better handoff quality, or easier human review?
