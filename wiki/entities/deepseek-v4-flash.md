---
type: entity
aliases: ["DeepSeek V4 Flash", "DeepSeek-V4-Flash", "DeepSeek V4 Flash Max", "DeepSeek-V4-Flash-Max"]
tags: [model, local-inference, open-weights]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# DeepSeek V4 Flash

## Identity
DeepSeek V4 Flash is an open-weights Mixture-of-Experts language model from DeepSeek, listed by Artificial Analysis with an Intelligence Index score of 47 and used in Tolaria as the high-end example in a weak social claim about local open-weight laptop inference progress.

## Aliases
- DeepSeek V4 Flash
- DeepSeek-V4-Flash
- DeepSeek V4 Flash Max
- DeepSeek-V4-Flash-Max

## Key Attributes
- Model family: DeepSeek V4.
- Parameters from the Hugging Face model card: 284B total, 13B activated.
- Context length from the model card and Artificial Analysis page: 1M tokens.
- License/source status: MIT/open weights in the inspected pages.
- Precision in the official model card: FP4 + FP8 mixed for DeepSeek-V4-Flash.
- Artificial Analysis inspected score: 47 on Artificial Analysis Intelligence Index for the reasoning/max-effort listing.
- Local artifact relevant to 128 GB Macs: [[antirez]]'s `antirez/deepseek-v4-gguf` q2 GGUF, 80.8 GiB, intended for DS4 and 128 GB Mac machines.

## Evidence
- [[Clement Delangue X post on local open-weight laptop AI progress]] records the social progress claim and later checks against Artificial Analysis, Hugging Face, and antirez's GGUF repository.
- [[Local Open-weight Laptop Inference Trend Assessment]] treats DeepSeek V4 Flash as a corroborated model and score, while keeping local usability and quantized-quality claims uncertain.

## Related
- [[Artificial Analysis]]
- [[antirez]]
- [[Local Open-weight Laptop Inference]]
- [[Multi-Token Prediction Local Inference]]
- [[Qwen3.6]]

## Open Questions
- How much quality is lost in the q2 mixed GGUF compared with the model configuration scored by Artificial Analysis?
- What throughput, context length, memory pressure, and tool-use reliability are achievable on an actual 128 GB MacBook Pro?
- Is DS4 the required runtime for the current GGUF/MTP path, or can broader runtimes support it reliably?
