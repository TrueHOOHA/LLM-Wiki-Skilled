---
type: source
source_path: raw/sources/2026-05-29-anthropic-ai-assistance-coding-skills.md
title: "How AI assistance impacts the formation of coding skills"
author: "Judy Hanwen Shen and Alex Tamkin / Anthropic"
date: 2026-01-29
tags: [agent-engineering, coding-agents, learning, evaluation]
created: 2026-05-29
---

# How AI assistance impacts the formation of coding skills

## Summary
Anthropic reports a randomized controlled trial testing whether AI coding assistance helps or hinders short-term mastery when Python-experienced developers learn an unfamiliar library, Trio. The study assigned 52 mostly junior software engineers to complete Trio tasks either manually or with a chat-based GPT-4o-style assistant that could access their code and generate correct code; all then took a no-AI quiz covering concepts they had just used. The AI group scored about 17% lower on the quiz, with the largest gap on debugging questions, while the average speedup was slight and not statistically significant. The most useful Tolaria takeaway is not "AI always harms learning" but a mode distinction: delegation/offloading patterns correlated with worse mastery, while conceptual inquiry, explanation requests, hybrid code/explanation, and generation-then-comprehension correlated with better retention. Evidence is medium: the design is randomized and primary, but the sample is small, immediate, focused on one library/task family, and uses one assistant design rather than agentic coding tools such as [[Claude Code]] or local [[Codex]].

## Key Claims
1. In this setup, AI-assisted participants scored 4.15 points lower on a 27-point post-task quiz, roughly 17 percentage points lower than the hand-coding group, with reported Cohen's d ≈ 0.738 and p=0.01.
2. Average AI-assisted completion was only about two minutes faster and did not reach statistical significance, partly because several participants spent substantial time composing assistant queries.
3. The largest assessment gap appeared on debugging questions, which matters because debugging and code reading are exactly the oversight skills humans need when code is increasingly AI-generated.
4. Low-scoring interaction patterns were AI delegation, progressive AI reliance, and iterative AI debugging where the assistant solved the problem instead of clarifying the participant's understanding.
5. Higher-scoring interaction patterns were generation-then-comprehension, hybrid code-explanation, and conceptual inquiry, where the participant used the assistant to build or check understanding rather than merely outsource code production.
6. The paper/article explicitly caveats that the interaction-mode analysis is qualitative and correlational, not a causal proof that any one prompt style preserves learning.
7. Linked product responses such as Claude Code Learning/Explanatory output styles and ChatGPT Study Mode are plausible design hypotheses, but they are not validated outcome evidence for this study.

## Notable Quotes
- "Using AI assistance led to a statistically significant decrease in mastery."
- "Using AI sped up the task slightly, but this didn’t reach the threshold of statistical significance."
- "The participants who showed stronger mastery used AI assistance not just to produce code but to build comprehension while doing so."
- "Cognitive effort—and even getting painfully stuck—is likely important for fostering mastery."

## Entities Mentioned
- [[Anthropic]]
- [[Claude Code]]
- [[OpenAI]]
- [[Codex]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[AI-assisted Coding Skill Formation]]
- [[Learning-preserving AI Assistance]]
- [[Context Engineering]]
- [[Codex Sequential TDD Workflow]]
- [[Evaluator-Optimizer Workflow]]

## Follow-ups
- Knowledge-only approval proposal: if Overseer later wants a Hermes/Codex learning-mode experiment, the smallest reversible test should compare a normal delivery mode against an explicit learning/explanatory mode on a small unfamiliar-codebase or unfamiliar-library task, with no silent profile adoption.
- Evaluation design should measure immediate task completion, post-task comprehension/debugging quiz, source/code citation accuracy, user correction burden, latency/token cost, and whether the operator can later explain or modify the produced code.
- Open question: whether agentic coding tools produce stronger or weaker skill-formation effects than the sidebar chat assistant used here.
