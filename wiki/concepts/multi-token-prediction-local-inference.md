---
type: concept
aliases: ["MTP local inference", "Multi Token Prediction", "speculative decoding with MTP", "draft-mtp"]
tags: [local-inference, inference, model]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Multi-Token Prediction Local Inference

## Definition
Multi-Token Prediction Local Inference is the use of MTP heads or draft-token speculative decoding in local LLM runtimes to predict and accept multiple future tokens per step, potentially increasing generation throughput for suitable models and tasks.

## Scope
This concept covers the local inference pattern surfaced by llama.cpp PR #22673 and Qwen3.6 MTP GGUF model cards: `--spec-type draft-mtp` or related flags, draft-token limits, acceptance-rate tradeoffs, prompt-processing overhead, model-specific task fit, and version-compatibility risk. It does not treat model-card or PR benchmark claims as independently verified production evidence.

## Contrasts
- Versus baseline local decoding: MTP adds draft-token prediction and acceptance logic, trading extra computation/data movement for fewer sequential generation steps.
- Versus generic speculative decoding with a separate draft model: the source cluster focuses on MTP heads/layers attached to or merged with the target model.
- Versus cloud inference: local MTP is constrained by the operator's hardware, llama.cpp build, quantization, KV cache, and context settings.

## Evidence
- [[Armin Ronacher X post on pi-llamacpp Qwen3.6 local provider]] records llama.cpp PR #22673 claims of MTP support, 75% steady-state acceptance around three draft tokens, more than 2x speedup over baseline in cited benchmarks, and possible prompt-processing penalties.
- [[pi-llamacpp Managed Local Provider Pattern Assessment]] keeps MTP as a candidate eval dimension, not an adoption recommendation, because evidence is PR/model-card-level and may drift across llama.cpp releases.

## Related
- [[llama.cpp]]
- [[Qwen3.6]]
- [[pi-llamacpp]]
- [[Managed Local llama.cpp Provider]]
- [[Hermes Agent]]

## Open Questions
- Which task classes actually benefit on Overseer's hardware: coding/debugging, factual Q&A, analysis, creative writing, or agent tool-use loops?
- How often do draft acceptance rates translate into lower end-to-end latency after startup, prompt processing, context length, and model quality are included?
- Which llama.cpp version and flags are now canonical for Qwen3.6 MTP, given the captured version drift between PR pins and model-card release guidance?
