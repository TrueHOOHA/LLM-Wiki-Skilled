---
type: source
source_path: raw/sources/2026-05-29-x-jumperz-hermes-kanban-discord-bridge.md
title: "JUMPERZ X post on Hermes Kanban + Discord task-board bridge"
author: "JUMPERZ (@jumperz)"
date: 2026-05-10
tags: [agent-engineering, hermes, orchestration]
created: 2026-05-29
---

# JUMPERZ X post on Hermes Kanban + Discord task-board bridge

## Summary
JUMPERZ argues that [[Hermes Agent]] Kanban should remain useful even for operators who already use Discord as an orchestration surface. The proposed architecture is: Discord handles plain-English intake, Hermes Kanban becomes the system of record for assigning, running, tracking, logging, and proving work, and a bridge mirrors task state back to Discord for mobile-friendly visibility. The post explicitly says Discord and Hermes Kanban do not sync natively out of the box, so the durable value is a workflow hypothesis rather than evidence of a working integration. Evidence is weak: social assertion plus screenshots, with no repository, docs, API schema, bridge implementation, or reproducible setup.

## Key Claims
1. Hermes Kanban is valuable because it is the place where work is actually assigned, run, tracked, logged, and proven.
2. Discord can still be useful as a conversational intake and visibility layer, especially on mobile.
3. A bridge could create real Hermes Kanban tasks from Discord commands, then mirror Hermes task state back to a Discord task board.
4. Discord and Hermes Kanban do not sync natively out of the box; any bridge would be a custom integration.
5. The concept is relevant to [[Chat Intake Kanban Mirror Pattern]], but the source does not prove reliability, security, identity mapping, or operational correctness.

## Notable Quotes
- "kanban is the system that actually runs the work, discord is just where i talk to it"
- "discord for plain english commands"
- "hermes Kanban for assigning, tracking, running, logging, and proving the work"
- "they don’t sync natively out of the box"
- "bridge creates a real task in Hermes Kanban" and "bridge mirrors that task back to Discord task board"

## Entities Mentioned
- [[Hermes Agent]]

## Concepts Mentioned
- [[Chat Intake Kanban Mirror Pattern]]
- [[Agentic Workflows and Agents]]
- [[Orchestrator-Worker Workflow]]

## Follow-ups
- Approval proposal question for Overseer: Should a future approved eval test a read-only or minimal bridge design where Discord is only intake/visibility and Hermes Kanban remains the sole system of record, with checks for task identity mapping, duplicate-state drift, auditability, permission boundaries, and failure recovery?
- Do not implement from this source alone. The evidence is weak and the post provides no bridge API, schema, security model, or reproducible workflow.
