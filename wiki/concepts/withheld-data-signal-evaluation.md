---
type: concept
aliases: ["withheld-data evaluation", "out-of-sample signal evaluation", "central signal evaluation"]
tags: [evaluation, agent-engineering, finance, prediction-markets]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Withheld-data Signal Evaluation

## Definition
Withheld-data Signal Evaluation is an evaluation pattern where candidate predictive signals are first searched or screened locally, then scored by a central service on private or held-out data that the signal author cannot directly inspect. In the current Tolaria evidence, [[OpenForage]] uses this pattern to try to filter local overfitting before considering agent-submitted market signals for production.

## Scope
This concept covers out-of-sample checks, server-side verification, private benchmark slices, uniqueness or marginal-improvement scoring, and production-gate decisions for submitted signals. It is most useful when local search can overfit public/backtest data, but it creates trust and auditability questions whenever the held-out evaluator is off-chain or otherwise opaque.

## Contrasts
- Versus local backtesting: local tests are cheap but vulnerable to overfitting and repeated search leakage.
- Versus public leaderboards: public feedback can train participants toward the test set; withheld scoring limits that feedback but reduces transparency.
- Versus [[Graph-aware Retrieval Evals]]: both use evaluation beyond surface fit, but this concept is about predictive signal performance rather than knowledge retrieval.
- Versus [[Evaluator-Optimizer Workflow]]: the submitted artifact is a computable signal, not a generated answer being revised after critique.

## Evidence
- [[sysls X article on world prediction and OpenForage]] records that OpenForage docs describe local screening, server-side in-sample verification, server-side out-of-sample evaluation on withheld data, uniqueness/marginal-improvement checks, and possible production inclusion.
- [[OpenForage Agentic Signal-discovery Architecture Assessment]] treats the pattern as the most useful extract from the source while flagging missing public implementation and performance evidence.

## Related
- [[OpenForage]]
- [[Agent-sourced Signal Marketplace]]
- [[Evaluator-Optimizer Workflow]]
- [[Graph-aware Retrieval Evals]]
- [[Agentic Workflows and Agents]]

## Open Questions
- How much feedback can the central evaluator return before agents can infer or overfit the withheld set?
- What audit evidence is needed when withheld evaluation and strategy composition happen off-chain?
- How should evaluator design account for non-stationary markets where old held-out slices may not represent live conditions?
- Can marginal-improvement scoring be adapted to agent benchmarks outside finance without encouraging benchmark hacking?
