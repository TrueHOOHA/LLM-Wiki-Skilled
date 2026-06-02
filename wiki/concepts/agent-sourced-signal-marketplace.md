---
type: concept
aliases: ["agent signal marketplace", "agent-sourced market signals", "predictive signal marketplace"]
tags: [agent-engineering, finance, prediction-markets, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Agent-sourced Signal Marketplace

## Definition
An Agent-sourced Signal Marketplace is a workflow where many autonomous or semi-autonomous agents search for predictive signals, submit candidate signal definitions to a central evaluator, and receive rewards or allocation only when those signals add unique predictive value. In the current Tolaria evidence, [[OpenForage]] is the concrete example, but its performance and incentive claims remain unverified.

## Scope
This concept covers the architecture pattern: open-ended agent search, local backtesting, standardized signal representation, central held-out evaluation, uniqueness/marginal-contribution scoring, and incentives tied to accepted or profitable signals. It does not prove that the resulting marketplace produces alpha, institutional yield, or general world-prediction capability.

## Contrasts
- Versus a normal prediction market: participants do not merely buy/sell outcomes; agents submit computable signals or strategies for central evaluation.
- Versus a static benchmark leaderboard: submissions may affect production allocation and compensation, so gaming, leakage, private-data access, and incentive design matter.
- Versus [[Evaluator-Optimizer Workflow]]: the evaluator scores predictive signal candidates; it is not primarily a text critique loop.
- Versus [[Agentic Workflows and Agents]]: this is a domain-specific application of agentic search rather than a general definition of agents.

## Evidence
- [[sysls X article on world prediction and OpenForage]] reports OpenForage's docs-level mechanism: local signal search/backtesting, compute-graph submissions, withheld-data checks, uniqueness/marginal-improvement scoring, and production inclusion decisions.
- [[OpenForage Agentic Signal-discovery Architecture Assessment]] grades the architecture as useful to remember but weakly supported for performance or adoption claims.

## Related
- [[OpenForage]]
- [[Withheld-data Signal Evaluation]]
- [[Agentic Workflows and Agents]]
- [[Evaluator-Optimizer Workflow]]
- [[Graph-aware Retrieval Evals]]

## Open Questions
- What metric best distinguishes genuinely unique predictive value from correlated variants of already-known signals?
- How should a marketplace prevent data leakage, overfitting to server feedback, Sybil submissions, and reward gaming?
- Which parts of the evaluator need to be public, private, or cryptographically/verifiably constrained for participants to trust it?
- Are there non-finance analogues where agents can submit reusable hypotheses and receive reward based on withheld-task marginal improvement?
