---
type: entity
aliases: ["Anthropic", "Anthropic Engineering"]
tags: [company, ai-lab, agent-engineering]
created: 2026-05-29
updated: 2026-05-29
source_count: 5
---

# Anthropic

## Identity
Anthropic is an AI company and research lab whose Tolaria sources currently cover practitioner agent-design guidance, a primary randomized study on AI coding assistance and skill formation, a source-checked Claude/Claude Code Learning Mode and output-styles report, a Claude Blog practitioner essay about self-contained HTML artifacts in [[Claude Code]], and a primary engineering article on [[Long-running Agent Harness]] design. These sources inform [[Agent-Computer Interface Design]], evaluation-gated complexity, [[AI-assisted Coding Skill Formation]], [[Learning-preserving AI Assistance]], [[Agent Output Styles]], [[TODO(human) Human-in-the-loop Coding]], the [[HTML Artifact Review Loop]], and multi-context-window continuity patterns.

## Aliases
- Anthropic
- Anthropic Engineering

## Key Attributes
- Category: AI company / lab
- Relevant agent-design source: [[Alok Kumar X post on Building Effective Agents video and Anthropic agent patterns]] and the inspected "Building effective agents" article
- Relevant skill-formation source: [[How AI assistance impacts the formation of coding skills]], published January 29, 2026, by Judy Hanwen Shen and Alex Tamkin / Anthropic
- Relevant output-styles source: [[Anthropic brings Claude's Learning Mode to regular users and devs]], an Engadget report with Alpha-captured primary checks against Anthropic Education, Claude Code output-style docs, changelog, and consumer styles-to-skills support page
- Relevant artifact-source: [[Using Claude Code: The Unreasonable Effectiveness of HTML]], mirrored on Claude Blog and paired with the public `anthropics/html-effectiveness` examples repo
- Relevant long-running-agent source: [[Effective Harnesses for Long-running Agents]], published November 26, 2025, by Justin Young / Anthropic Engineering
- Tolaria evidence posture: stronger than social X layers for primary article/paper/engineering claims, but still medium for broad adoption because source-specific results may not generalize to other models, domains, or Hermes/Codex workflows without evaluation

## Evidence
- [[Alok Kumar X post on Building Effective Agents video and Anthropic agent patterns]] preserves the social lead and the inspected Anthropic article claims about workflows, agents, tool interfaces, and guarded autonomous execution.
- [[How AI assistance impacts the formation of coding skills]] reports a randomized trial where AI-assisted developers scored about 17% lower on a short-term no-AI quiz after unfamiliar Trio tasks, while learning-preserving interaction patterns correlated with better retention.
- [[Anthropic brings Claude's Learning Mode to regular users and devs]] preserves the Claude Learning Mode rollout report and primary-source-backed Claude Code output-style mechanics: Explanatory insights, Learning mode, `TODO(human)` markers, system-prompt-level policy changes, token overhead, and a later consumer shift from styles toward skills.
- [[AI Assistance and Coding Skill Formation Assessment]] translates the study into a knowledge-only Hermes/Codex learning-mode proposal, not an implementation change.
- [[Using Claude Code: The Unreasonable Effectiveness of HTML]] provides practitioner evidence for HTML artifacts as dense review and custom-editing surfaces; it demonstrates examples but does not benchmark productivity, comprehension, or safety outcomes.
- [[Effective Harnesses for Long-running Agents]] provides primary Anthropic engineering evidence for a multi-context-window harness built around an initializer agent, coding-agent loop, JSON feature ledger, `init.sh`, progress log, git commits, and end-to-end verification.

## Related
- [[Agentic Workflows and Agents]]
- [[Agent-Computer Interface Design]]
- [[Orchestrator-Worker Workflow]]
- [[Evaluator-Optimizer Workflow]]
- [[AI-assisted Coding Skill Formation]]
- [[Learning-preserving AI Assistance]]
- [[Agent Output Styles]]
- [[TODO(human) Human-in-the-loop Coding]]
- [[Hermes Agent]]
- [[Claude Code]]
- [[HTML Artifact Review Loop]]
- [[Artifact Review Surface]]
- [[Long-running Agent Harness]]
- [[Durable Agent Operating Loop]]

## Open Questions
- Which Anthropic agent-design practices should be evaluated against Hermes/Tolaria workloads before any workflow or tool-interface change is approved?
- Do Anthropic's coding skill-formation findings replicate for agentic coding tools, longer tasks, senior engineers, and durable long-term retention?
- Do Claude Code output styles and `TODO(human)` markers measurably improve retention or review quality, or do they mainly add explanatory prose and token cost?
- Do Anthropic's HTML artifact examples improve human review quality enough to justify generated-JavaScript and diff-review overhead?
- Which parts of Anthropic's long-running-agent harness transfer outside Claude Agent SDK web-app tasks: JSON ledger, init script, progress log, git history, browser verification, or the initializer/coding-agent prompt split?
