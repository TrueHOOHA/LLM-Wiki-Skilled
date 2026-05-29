---
type: concept
aliases: ["prototype spike", "throwaway code", "question-answering prototype"]
tags: [agent-engineering, prototyping, evaluation, workflows]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Throwaway Prototype Spike

## Definition
A Throwaway Prototype Spike is deliberately disposable code whose purpose is to answer a concrete product, UI, state-machine, or business-logic question before committing to a real implementation.

## Scope
The pattern covers UI variation prototypes that expose multiple radically different options for human taste judgment, and business-logic/terminal prototypes that push state transitions through edge cases. The durable artifact is not the prototype code; it is the answered question, decision rationale, and constraints learned. In the current Beta lane, creating prototypes remains non-knowledge work and requires Overseer approval; Tolaria may preserve the pattern and evaluation criteria only.

## Contrasts
- Versus production implementation: a spike is explicitly disposable, unpolished, and should have no persistence by default.
- Versus a design document: a spike answers questions that are hard to settle on paper.
- Versus Tolaria synthesis: Tolaria can record findings and proposals, but Beta must not create code prototypes from this source.

## Evidence
- [[Matt Pocock AI Hero skills changelog]] quotes the prototype skill: "A prototype is throwaway code that answers a question," with separate logic and UI branches and a requirement to capture the answer durably when done.

## Related
- [[AI Hero]]
- [[Agent-Computer Interface Design]]
- [[Evaluator-Optimizer Workflow]]
- [[Human-Token Mode Separation]]
- [[Hermes Agent]]

## Open Questions
- If Overseer approves future non-knowledge work, which Hermes/Codex problem class most benefits from throwaway spikes: UI taste, state machines, tool APIs, prompt/skill behavior, or source-ingestion workflows?
- What rule should guarantee prototype deletion or absorption after it answers the question?
