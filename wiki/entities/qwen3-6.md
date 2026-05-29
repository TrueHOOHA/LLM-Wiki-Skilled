---
type: entity
aliases: ["Qwen3.6", "Qwen 3.6", "Qwen3.6-27B", "Qwen3.6-35B-A3B"]
tags: [model, local-inference, qwen]
created: 2026-05-29
updated: 2026-05-29
source_count: 2
---

# Qwen3.6

## Identity
Qwen3.6 is the model family referenced by pi-llamacpp through dense 27B and 35B-A3B MoE GGUF variants, with linked model cards describing MTP/speculative-decoding use for local coding-agent workloads.

## Aliases
- Qwen3.6
- Qwen 3.6
- Qwen3.6-27B
- Qwen3.6-35B-A3B

## Key Attributes
- Variant in pi-llamacpp: `llamacpp/qwen-3.6-dense-*` for 27B dense GGUF quants
- Variant in pi-llamacpp: `llamacpp/qwen-3.6-moe-*` for 35B-A3B MoE GGUF quants
- Linked model sources: `froggeric/Qwen3.6-27B-MTP-GGUF` and `havenoammo/Qwen3.6-35B-A3B-MTP-GGUF`
- Claimed context: model cards mention 262K context and coding-agent-oriented MTP benefits
- Evidence caveat: hardware fit, speedups, task-specific acceptance rates, and quality tradeoffs are model-card/PR claims until independently evaluated

## Evidence
- [[Armin Ronacher X post on pi-llamacpp Qwen3.6 local provider]] records the pinned Qwen3.6 GGUF sources, model IDs, quant families, MTP-related llama.cpp requirements, and performance caveats.
- [[pi-llamacpp Managed Local Provider Pattern Assessment]] classifies Qwen3.6/MTP as promising but not yet adopted evidence for local coding-agent runtime proposals.
- [[0xSero tweet on AImaxing tool list]] names Qwen3.6-27B/35B as “best local agents,” but provides no hardware, quantization, task set, or benchmark. [[Skeptical AI Tooling Landscape from 0xSero AImaxing List]] treats this as weak corroboration of local-agent salience, not as model-quality evidence.

## Related
- [[pi-llamacpp]]
- [[llama.cpp]]
- [[Multi-Token Prediction Local Inference]]
- [[Managed Local llama.cpp Provider]]
- [[Hermes Agent]]

## Open Questions
- Do Qwen3.6 MTP variants materially improve local Codex/Hermes coding tasks on Overseer's actual hardware?
- Which quantization/context configuration is viable after accounting for memory, prompt processing speed, latency, and output quality?
- Are model-card claims about Anthropic-compatible endpoints and Claude Code usage robust enough for a future eval, or are they brittle examples?
