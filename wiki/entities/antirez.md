---
type: entity
aliases: ["antirez", "Salvatore Sanfilippo"]
tags: [person, local-inference, open-source]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# antirez

## Identity
antirez is the handle of Salvatore Sanfilippo, referenced in this Tolaria source as the publisher of `antirez/deepseek-v4-gguf`, a GGUF quantization repository for [[DeepSeek V4 Flash]] aimed at DS4 local inference.

## Aliases
- antirez
- Salvatore Sanfilippo

## Key Attributes
- Relevant artifact: `antirez/deepseek-v4-gguf` on Hugging Face.
- Base model: [[DeepSeek V4 Flash]].
- Quantized files recorded in the README include an 80.8 GiB q2 mixed quant for 128 GB Mac machines, a 153.3 GiB q4 expert quant for machines with at least 256 GB RAM, and a 3.6 GiB optional MTP GGUF.
- Runtime caveat: the README says the quants are specific for the DS4 inference engine and may or may not work with other engines, especially the MTP model.

## Evidence
- [[Clement Delangue X post on local open-weight laptop AI progress]] cites antirez's mixed-Q2 GGUF as the artifact behind the 128 GB laptop-run claim and verifies that the Hugging Face repository exists.
- [[Local Open-weight Laptop Inference Trend Assessment]] treats the artifact existence as corroborated but the quality/speed/capability preservation as unverified.

## Related
- [[DeepSeek V4 Flash]]
- [[Local Open-weight Laptop Inference]]
- [[Artificial Analysis]]
- [[Multi-Token Prediction Local Inference]]

## Open Questions
- Is there an independent benchmark of the q2 GGUF on a 128 GB MacBook Pro?
- Does the q2 artifact preserve enough quality for Codex/Hermes tasks, or only demonstrate that the model can technically load/run?
- Which runtime path, DS4 or broader GGUF loaders, is currently reliable for this model family?
