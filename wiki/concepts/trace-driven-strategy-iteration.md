---
type: concept
aliases: ["strategy.md loop", "trace study loop", "trace-driven browser skill iteration", "convergence heuristic"]
tags: [browser-agents, evaluation, skills]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Trace-driven Strategy Iteration

## Definition
Trace-driven Strategy Iteration is an agent-learning loop where the agent runs a real task, studies its own browser/tool trace, records what worked or failed in a strategy scratchpad, and uses that accumulated context to improve the next iteration until marginal gains flatten.

## Scope
In [[Autobrowse]], the strategy file is described as `strategy.md`: it records stalls, guesses, token waste, failed paths, deterministic helper opportunities, and next experiments. Browserbase says the loop usually runs only a few iterations and short-circuits when consecutive runs stop improving cost or turn count.

## Contrasts
- Versus one-shot prompting: the loop explicitly carries observations across runs.
- Versus offline eval only: the loop learns from live traces on the target site.
- Versus unlimited self-improvement: the source uses low iteration caps and blunt convergence heuristics, so it is not a guarantee of global optimality.
- Versus Hermes/Tolaria knowledge maintenance: Tolaria can preserve the pattern, but creating an actual Autobrowse-like harness would be non-knowledge work requiring approval.

## Evidence
- [[Browserbase Autobrowse browser-skill loop]] describes the Objective → Run → Study → Strategy → Iterate → Converge → Graduate loop and Browserbase's current convergence caveats.

## Related
- [[Autobrowse]]
- [[Agent-generated Browser Skills]]
- [[Browser Agent Discovery Tax]]
- [[Evaluator-Optimizer Workflow]]
- [[Agent-Computer Interface Design]]

## Open Questions
- What convergence signal is robust enough: cost, turns, success rate, trace structure, endpoint stability, human review, or repeated cross-region validation?
- How much random exploration should be preserved to discover hidden APIs without wasting iterations?
