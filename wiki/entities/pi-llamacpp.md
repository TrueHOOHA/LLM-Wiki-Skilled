---
type: entity
aliases: ["pi-llamacpp", "mitsuhiko/pi-llamacpp"]
tags: [local-inference, agent-framework, llama-cpp]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# pi-llamacpp

## Identity
pi-llamacpp is an experimental Pi extension by Armin Ronacher that manages local Qwen3.6 inference through llama.cpp, registering models under a `llamacpp` provider and wrapping `llama-server` behind Pi's provider lifecycle.

## Aliases
- pi-llamacpp
- mitsuhiko/pi-llamacpp

## Key Attributes
- Category: local inference provider extension
- Runtime: [[llama.cpp]] / `llama-server`
- Model family: [[Qwen3.6]] dense and MoE GGUF variants
- Provider ID: `llamacpp`
- State path: `~/.pi/llamacpp` with source, runtime, downloads, models, clients, `server.json`, and log state
- Lifecycle pattern: lazy setup, dynamic localhost endpoint, client leases, heartbeat/TTL, lifecycle lock, watchdog shutdown
- Reproducibility pattern: pinned Hugging Face revisions plus pinned llama.cpp source/PR snapshot
- Evidence quality: primary repo for mechanism existence; weak or unverified for performance and adoption claims

## Evidence
- [[Armin Ronacher X post on pi-llamacpp Qwen3.6 local provider]] records the original social post and linked repository inspection, including model IDs, state paths, runtime pins, endpoint behavior, and watchdog mechanics.
- [[pi-llamacpp Managed Local Provider Pattern Assessment]] treats pi-llamacpp as a reference pattern for future approval-gated Hermes/Codex local-runtime evaluation, not as an implementation task.

## Related
- [[llama.cpp]]
- [[Qwen3.6]]
- [[Managed Local llama.cpp Provider]]
- [[Multi-Token Prediction Local Inference]]
- [[Hermes Agent]]
- [[Thin Harness Fat Skills]]

## Open Questions
- Which Pi provider APIs and lifecycle assumptions would map cleanly to Hermes, and which are Pi-specific?
- Are the pinned llama.cpp and model revisions still the right compatibility set, or has upstream MTP support superseded the PR snapshot?
- Does the lease/watchdog pattern reliably avoid orphaned `llama-server` processes under crashes, agent interrupts, and concurrent clients?
