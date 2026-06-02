---
type: concept
aliases: ["dynamic UI generation", "generated interfaces", "intent-conditioned UI"]
tags: [agent-engineering, interface-design, ui-generation]
created: 2026-05-29
updated: 2026-05-29
source_count: 3
---

# Adaptive UI Generation

## Definition
Adaptive UI Generation is the creation or selection of user interfaces based on user intent, task context, brand/style constraints, device constraints, and runtime state instead of relying only on static predesigned screens. In [[Molly Studio OpenAI Endgame]], it is the most evidence-supported part of the broader [[Agentic OS]] thesis because the related Coframe/OpenAI link points to concrete UI/code-generation work; [[Molly Studio API-ification of Everything]] adds a weaker interface-standardization claim around intent-based service flows.

## Scope
The concept includes generated task-specific UIs, natural-language-to-interface workflows, brand-constrained UI/code generation, adaptive maps/productivity surfaces, and evaluation of interface quality. It does not prove that generated UIs are safe, accessible, conversion-optimized, brand-correct, or ready to replace application design without verification.

## Contrasts
- Versus static application UI: the interface can change by task and context rather than being fixed in advance.
- Versus ordinary personalization: the surface itself may be generated or recomposed, not merely reordered or themed.
- Versus [[Agent-Computer Interface Design]]: ACI focuses on interfaces for agents to use tools correctly; adaptive UI generation often targets human-facing interfaces, though both need evaluability and affordance clarity.

## Evidence
- [[Molly Studio OpenAI Endgame]] cites Coframe/OpenAI work as evidence that a dedicated model for interface generation could emerge; Alpha's raw notes say this is the strongest supporting evidence in the source cluster.
- The same source gives weaker examples of ChatGPT maps, Canvas, and productivity surfaces as dynamic interfaces, but does not provide benchmarked UX or safety data.
- [[Molly Studio API-ification of Everything]] argues that every service could get "fluid, natural, highest-converting components" behind one interface layer, but supplies no UX benchmark, accessibility check, conversion study, or safety evaluation.
- [[Molly Studio AI-native Interface Thesis Collection]] connects the generated-UI question to [[Shopify]] and [[AI-native Commerce Interfaces]], where generated surfaces would need stricter checks around price, inventory, payment confirmation, ranking, and support.
- [[Agent-Computer Interface Design]] provides a useful caution: generated or tool-facing interfaces must make correct use obvious and failure modes inspectable.

## Related
- [[Agentic OS]]
- [[Post-app Interfaces]]
- [[OpenAI]]
- [[Intent-based Computing]]
- [[API-ification of Services]]
- [[Interface-layer Marketplace Risk]]
- [[Agent-Computer Interface Design]]
- [[Context Engineering]]
- [[AI-native Commerce Interfaces]]
- [[Coframe]]
- [[Evaluator-Optimizer Workflow]]
- [[Two-lane Agent Review]]

## Open Questions
- What evaluation harness would catch bad generated UI: accessibility, task completion, hallucinated affordances, legal/brand violations, conversion harm, security mistakes, or user confusion?
- Which constraints should be explicit in prompts/specs versus learned by a model: brand, design-system tokens, platform conventions, permissions, and safety gates?
- Where should generated UI stop and deterministic service/API workflows begin?
