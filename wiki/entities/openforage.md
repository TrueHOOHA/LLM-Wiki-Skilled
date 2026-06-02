---
type: entity
aliases: ["OpenForage", "openforage.ai", "systematic-long-short/openforage"]
tags: [agent-tooling, finance, prediction-markets, evaluation]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# OpenForage

## Identity
OpenForage is presented in the current Tolaria evidence as a closed-beta protocol and Python-library workflow for AI-agent-discovered market signals. The strongest captured evidence is not the marketing claim of institutional yield, but the documented architecture: agents search locally over market data, submit mathematical signal expressions, and rely on centralized server-side evaluation before any signal can be selected for production use in a finance protocol.

## Aliases
- OpenForage
- openforage.ai
- systematic-long-short/openforage

## Key Attributes
| Attribute | Current evidence |
|---|---|
| Public positioning | Marketing site claims "institutional yield, powered by autonomous agents" and an organized agent network for market prediction. |
| Agent interface | Captured docs describe a Python package with registration, era-scoped data sync, local feature download, local search/backtesting, and signal submission. |
| Signal representation | Signals are described as compute graphs that transform feature nodes into time-by-instrument exposure matrices. |
| Evaluation path | Local screening is followed by server-side in-sample verification, server-side withheld out-of-sample evaluation, uniqueness/marginal-improvement checks, and possible production inclusion. |
| Protocol split | Captured notes describe off-chain library/signal service/data platform/execution engine plus on-chain RISKUSD, atRISKUSD vaults, treasuries, and FORAGE governance token. |
| Evidence quality | Weak for yield/performance/product adoption; medium-low for the existence of the docs-level architecture; no independent benchmark or full implementation was inspected. |

## Evidence
- [[sysls X article on world prediction and OpenForage]] records the personal essay, linked site/docs, public repo/PyPI summary, and caveats from Alpha's follow-through capture.
- [[OpenForage Agentic Signal-discovery Architecture Assessment]] preserves the useful architecture pattern while downgrading the broad world-prediction and yield claims.

## Related
- [[Agent-sourced Signal Marketplace]]
- [[Withheld-data Signal Evaluation]]
- [[Agentic Workflows and Agents]]
- [[Evaluator-Optimizer Workflow]]
- [[Graph-aware Retrieval Evals]]

## Open Questions
- Does OpenForage publish enough implementation, audit, and performance evidence to verify signal evaluation or production allocation claims?
- How are uniqueness and marginal improvement measured, and can agents game those metrics through correlated or overfit submissions?
- What parts of the evaluation are publicly auditable versus trusted off-chain service behavior?
- Does the claimed agent workflow produce useful marginal alpha once invite-only/private data and central evaluation constraints are removed?
