---
type: concept
aliases: ["customer outcomes vs PR volume", "AI coding metrics", "AI coding outcome metrics"]
tags: [agent-engineering, coding-agents, evaluation, metrics]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# AI Coding Outcome Measurement

## Definition

AI Coding Outcome Measurement is the practice of judging AI-assisted engineering by delivered customer/workflow value and system quality rather than by raw activity metrics such as token spend, generated lines, number of pull requests, or agent turns. [[Zeb Evans on ClickUp 100x Organization]] frames the risk as companies celebrating 500% more pull requests while customer outcomes do not match the code volume.

## Scope

This concept covers metric selection for coding-agent adoption, engineering-process changes, and AI-native organization claims. Candidate measures include customer-impact latency, defect/incident rate, revert rate, review latency, accepted-diff ratio, test pass plus user-like verification, support load, operator correction burden, specification fidelity, and maintainability. It does not say PR count is useless; PR count can be an activity signal, but it is insufficient as a success metric by itself.

## Contrasts

- Versus output volume: volume measures how much was generated, not whether the generated work solved the right problem safely.
- Versus benchmark-only evaluation: benchmarks can compare model/tool capability, but organization adoption needs production/workflow outcomes.
- Versus [[Graph-aware Retrieval Evals]] or [[Persistent Agent Memory Evaluation]]: those are domain-specific eval families; this concept is the broader metric discipline for AI coding.
- Versus compensation claims: weak evidence about million-dollar bands should not be accepted without a credible attribution method for outsized AI-system impact.

## Evidence

- [[Zeb Evans on ClickUp 100x Organization]] provides the weak-social claim that PR/code volume can rise without matching customer outcomes. It is useful as a warning, but it does not define a concrete measurement framework or provide ClickUp data.

## Related

- [[AI Coding Orchestration and Review Bottleneck]]
- [[AI-native Organization Design]]
- [[Agent Manager Role]]
- [[Evaluator-Optimizer Workflow]]
- [[Two-lane Agent Review]]
- [[AI-assisted Coding Skill Formation]]
- [[Long-running Agent Harness]]
- [[Grounded RAG Reliability Pattern]]

## Open Questions

- What minimum metric pack should accompany any serious AI coding adoption claim: shipped customer outcomes, defects, review latency, rework, incident rate, operator correction burden, cost, or maintainability?
- How can a company attribute outcomes to AI-system owners without rewarding vanity metrics or shifting unmeasured burden to reviewers, support, or customers?
- Which Hermes/Tolaria measurement surfaces could distinguish real workflow outcomes from raw AI output volume if Overseer later approves a separate eval?
