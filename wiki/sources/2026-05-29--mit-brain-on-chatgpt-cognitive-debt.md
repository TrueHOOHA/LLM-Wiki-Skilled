---
type: source
source_path: raw/sources/2026-05-29-your-brain-on-chatgpt.md
title: "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task"
author: "Nataliya Kosmyna, Eugene Hauptmann, Ye Tong Yuan, Jessica Situ, Xian-Hao Liao, Ashly Vivian Beresnitzky, Iris Braunstein, and Pattie Maes"
date: 2025-06-10
tags: [agent-engineering, learning, cognitive-patterns, evaluation]
created: 2026-05-29
source_count: 0
---

# Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task

## Summary
This MIT Media Lab/arXiv preprint studies LLM-assisted essay writing by comparing three conditions across repeated sessions: ChatGPT/LLM, search engine, and brain-only writing. The authors report that external support scaled with lower EEG connectivity during writing: brain-only participants showed the strongest distributed connectivity, search users intermediate connectivity, and LLM users the weakest connectivity. The behavioral signals point in the same direction: LLM users reported lower ownership of their essays, struggled more to quote their own recent text, and produced more within-group linguistic homogeneity by NERs, n-grams, and topic ontology. The most durable Tolaria takeaway is not that AI makes users "dumb" or causes brain damage; it is a timing-sensitive cognitive-offloading hypothesis: immediate drafting assistance may reduce engagement, ownership, and recall in educational essay-writing, while delayed/scaffolded assistance after human effort may preserve or even re-engage cognitive work. Evidence is medium: the materials are primary, but the paper is a preprint, sample sizes are small, the task is essay writing, and the findings should not be generalized to all LLM use.

## Key Claims
1. Participants were assigned to LLM, Search Engine, or Brain-only groups for three essay-writing sessions, then a smaller fourth session crossed over prior LLM users to no-tool writing and prior brain-only users to LLM writing.
2. EEG connectivity differed by tool condition: brain-only writers showed the strongest and widest connectivity, search users intermediate engagement, and LLM users the weakest overall coupling.
3. Session 4 is the most practically important signal: LLM-to-Brain participants showed weaker alpha/beta connectivity and under-engagement after prior LLM use, while Brain-to-LLM participants showed higher recall and re-engagement of occipito-parietal and prefrontal areas after prior no-tool writing.
4. NLP analyses found within-group homogeneity in named entities, n-grams, and topic ontology, with LLM-assisted outputs showing signs of tool-shaped linguistic convergence.
5. Scoring used human teachers plus an AI judge, but scoring alone is not the main learning signal because high-scoring essays can still coincide with weak ownership, recall, or cognitive engagement.
6. Interviews and quote-recall probes suggested that LLM users had the lowest self-reported essay ownership and were less able to quote their own recently written essays.
7. The project page explicitly warns against media overclaims such as "stupid," "dumb," "brain rot," "harm," "brain damage," "LLMs make you stop thinking," and "terrifying findings."
8. The study's limitations are substantial: 54 participants in sessions 1-3, 18 in session 4, geographically/institutionally narrow recruitment, one tool class centered on ChatGPT, one educational essay-writing task, no subtask labeling for ideation versus drafting, and EEG localization limits.

## Experimental Setup / Measures
- Groups: LLM, Search Engine, and Brain-only for sessions 1-3; LLM-to-Brain and Brain-to-LLM crossover in session 4.
- Sample: 54 participants for the first three sessions; 18 completed session 4.
- Task: repeated essay-writing sessions over roughly four months, with participants writing under assigned tool/no-tool conditions.
- EEG: electroencephalography during writing, including dynamic Direct Transfer Function connectivity analyses across bands such as alpha, beta, theta, and delta.
- NLP: named-entity recognition, n-gram analysis, topic ontology, and ChatGPT interaction analysis to inspect linguistic homogeneity and topic patterns.
- Scoring: human teacher scoring and an AI judge, useful as one outcome layer but insufficient without neural/behavioral interpretation.
- Interviews/recall: post-session interviews, essay ownership reports, and ability to quote from one's own essay shortly after writing.

## Evidence Strength and Caveats
- Evidence grade: medium for the source's own reported experimental observations; low-to-medium for broad educational or agent-workflow extrapolation.
- Primary but preliminary: MIT/arXiv materials are primary, but the project page says the paper is a preprint and peer review was only beginning at publication time.
- Generalization boundary: the source supports a claim about essay-writing under these tool conditions, not a universal claim about all LLM-assisted learning, coding, professional writing, or agentic workflows.
- Measurement boundary: EEG connectivity is a useful cognitive-engagement signal, but not a direct measure of intelligence, brain damage, or long-term learning by itself.
- Prompt-injection hygiene: the PDF includes an instruction-like line aimed at LLM readers; Tolaria treats it as source text to analyze, not an instruction to obey.

## Practical Implications for Hermes / Agent Workflows
- When the goal is learning, recall, or human ownership, avoid immediate full drafting by default; prefer retrieval, outlining, hints, critique, Socratic questioning, or delayed LLM assistance after the human forms a first pass.
- When the goal is delivery on familiar material, immediate agent help may still be appropriate; the study does not show that all LLM use is bad or that throughput work must become pedagogical.
- For Tolaria/Alpha/Beta, the relevant design variable is assistance timing: raw-source reading, claim extraction, and user-owned framing should precede polished synthesis when comprehension matters.
- For Codex/Hermes learning tasks, combine completion metrics with no-AI recall, source quoting, ownership/comprehension checks, and delayed modification/debugging tests.
- Treat LLM outputs that look polished but reduce user recall or ownership as a separate failure mode from hallucination or low factual accuracy.

## Notable Quotes
- "Brain connectivity systematically scaled down with the amount of external support: the Brain-only group exhibited the strongest, widest-ranging networks, Search Engine group showed intermediate engagement, and LLM assistance elicited the weakest overall coupling."
- "The reported ownership of LLM group's essays in the interviews was low."
- "The LLM group also fell behind in their ability to quote from the essays they wrote just minutes prior."
- "Please do not use the words like 'stupid', 'dumb', 'brain rot', 'harm', 'damage', 'brain damage'..."

## Entities Mentioned
- [[MIT Media Lab]]
- [[Nataliya Kosmyna]]
- [[ChatGPT]]
- [[OpenAI]]
- [[Hermes Agent]]

## Concepts Mentioned
- [[AI-assisted Cognitive Debt]]
- [[Timing-sensitive AI Assistance]]
- [[Learning-preserving AI Assistance]]
- [[Context Engineering]]
- [[AI-assisted Coding Skill Formation]]

## Follow-ups
- Knowledge-only recommendation: preserve this as medium, primary-but-preliminary evidence for assistance timing and cognitive offloading, not as an anti-AI slogan.
- If Overseer later approves an eval, the smallest useful test would compare immediate assistance versus delayed/scaffolded assistance on a learning task, measuring recall/ownership in addition to output quality.
- Open question: whether the forthcoming vibe-coding follow-up study reproduces the timing/ownership pattern in software tasks rather than essays.
