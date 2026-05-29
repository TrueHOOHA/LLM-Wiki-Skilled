---
type: concept
aliases: ["weird machines", "abstraction gaps", "unintended programmable substrate", "exploitability"]
tags: [security, systems-thinking, agent-engineering, cognitive-patterns]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
confidence: medium
---

# Weird Machines and Abstraction Gaps

## Definition
Weird Machines and Abstraction Gaps are cases where a supposedly bounded system exposes enough unintended lower-level states, transitions, or side effects that an operator can compose them into capabilities the surface abstraction did not advertise.

## Scope
This concept covers exploitability, side channels, surprising Turing-complete substrates, protocol/CPU/state-machine leaks, and agent-tool abstractions that accidentally expose more or less power than the schema suggests. It does not imply every abstraction leak is exploitable, nor that a conceptual analogy proves a concrete Hermes failure without evidence.

## Contrasts
- Versus [[Abstraction-leak Reasoning]]: abstraction-leak reasoning is the analytic method; weird-machine analysis is the technical/security version where leaked substrate states become a programmable machine.
- Versus [[Security Mindset]]: security mindset asks how a system can be abused; weird-machine analysis asks what unintended computation or capability the implementation actually exposes.
- Versus normal feature extension: a weird machine is not designed as an API; it is assembled from unintended affordances.

## Evidence
- [[On Seeing Through and Unseeing: The Hacker Mindset]] explicitly connects hacker mindset to Gwern's "Surprisingly Turing-Complete" material and Dullien's weird-machines formalization: exploitability emerges when lower-level implementation states can be wired into a different system than the surface protocol promised.
- The source's examples include speculative-execution-like lower-level states, side channels below bit-level abstractions, and hidden Turing-complete substrates in non-computer systems.

## Related
- [[Security Mindset]]
- [[Abstraction-leak Reasoning]]
- [[Hacker Mindset]]
- [[Agent-Computer Interface Design]]
- [[AI Command-generation Safety Pattern]]
- [[Deterministic-first Browser Automation]]

## Open Questions
- In agent tooling, which abstraction gaps are most analogous to weird machines: permissive shell tools, ambiguous schemas, hidden browser state, stale memory, provider fallback behavior, or cross-task handoff state?
- What eval would distinguish a useful weird-machine analogy from vague "everything leaks" rhetoric?
