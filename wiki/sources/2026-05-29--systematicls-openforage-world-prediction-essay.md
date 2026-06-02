---
type: source
source_path: raw/sources/2026-05-29-systematicls-my-obsession-predicting-world.md
title: "sysls X article on world prediction and OpenForage"
author: "sysls / @systematicls"
date: 2026-05-13
tags: [agent-engineering, evaluation, prediction-markets, finance]
created: 2026-05-29
---

# sysls X article on world prediction and OpenForage

## Summary
This weak social source is a personal essay about the author's long-running ambition to build systems that predict useful parts of the world, starting with liquid-market prediction as a financing and testing ground. The essay's broad claims about world models, market efficiency, and human-system prediction are speculative and not independently supported by the captured source. The durable Tolaria value comes from the linked [[OpenForage]] docs and site: they describe an [[Agent-sourced Signal Marketplace]] where agents locally search for market signals, submit compute-graph signals, and rely on server-side withheld-data checks before a signal can affect production allocation.

## Key Claims
1. The author claims that better data, compute, and models could make useful predictions across human systems, eventually reducing inefficiency beyond financial markets.
2. The author frames liquid-market prediction as the initial testbed and funding engine for that larger ambition.
3. OpenForage is presented as related to that ambition, but the captured public evidence supports only a narrower agentic signal-discovery protocol.
4. OpenForage's docs describe local agent search/backtesting, compute-graph signal representations, server-side in-sample verification, withheld out-of-sample evaluation, uniqueness/marginal-improvement scoring, and production inclusion decisions.
5. Public evidence is weak for performance: the beta is invite/closed, the full implementation is not inspectable, visible public metrics were zero at capture, and there was no independent yield or benchmark history.

## Notable Quotes
- "I've been driven by a desire to build a world model so adept at predicting the world that it can drive out inefficiencies in all markets, public or private."
- "The markets are the ultimate testing field for your ability to predict the future across various timescales."
- Captured OpenForage docs summary: signals are compute graphs that produce time-by-instrument exposure matrices, then undergo local screening plus server-side withheld-data evaluation.
- Captured caveat: out-of-sample evaluation is off-chain, strategy composition is not publicly disclosed, and some PnL timing is operationally determined.

## Entities Mentioned
- [[OpenForage]] — project/protocol described by the linked docs and marketing site.
- No separate entity page was created for sysls / @systematicls from this single weak source.

## Concepts Mentioned
- [[Agent-sourced Signal Marketplace]] — the main durable architecture pattern extracted from the OpenForage docs.
- [[Withheld-data Signal Evaluation]] — the evaluation pattern used to distinguish local overfit signals from centrally tested candidates.
- [[Agentic Workflows and Agents]] — adjacent broader frame for model-directed search over open-ended candidate spaces.
- [[Evaluator-Optimizer Workflow]] — adjacent evaluation loop concept, but OpenForage evaluates submitted market signals rather than iteratively critiquing generated text.
- [[Graph-aware Retrieval Evals]] — adjacent idea: both patterns value held-out or graph-aware tests over surface similarity, but the domains differ.

## Follow-ups
- Archive/use as weak evidence only. The source does not justify installing OpenForage, investing in it, adopting its mechanism, or creating a Hermes eval harness.
- Knowledge-only assessment filed in [[OpenForage Agentic Signal-discovery Architecture Assessment]].
- Stronger evidence gaps: full implementation, independent performance history, public contract addresses/audit status, reproducible evaluation method, and evidence that uniqueness/marginal-improvement scoring resists overfitting or gaming.
