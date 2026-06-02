---
type: source
source_path: raw/sources/2026-05-29-clementdelangue-local-open-weight-ai-laptop.md
title: "Clement Delangue X post on local open-weight laptop AI progress"
author: "Clement Delangue"
date: 2026-05-11
tags: [local-inference, open-weights, benchmark, quantization, weak-social]
created: 2026-05-29
---

# Clement Delangue X post on local open-weight laptop AI progress

## Summary
This weak social source claims that the strongest open-weight model runnable on a 128 GB MacBook Pro improved from an Artificial Analysis Intelligence Index score near 10 in May 2024 to 47 in May 2026, while the laptop memory ceiling stayed fixed. The strongest corroborated points are narrower: [[Artificial Analysis]] currently lists [[DeepSeek V4 Flash]] as an open-weights April 2026 model with score 47, and Hugging Face hosts both the base [[DeepSeek V4 Flash]] model and [[antirez]]'s GGUF quantization repository. The unverified part is the full trend claim: whether every chart point was the smartest practically runnable 128 GB laptop model, whether AA v4.0 scores are comparable for that use, and whether mixed-Q2 quantized local runs preserve the benchmark-level utility. Treat the Moore's Law analogy as rhetoric, not a conclusion.

## Key Claims
1. A fixed 128 GB MacBook Pro memory ceiling can now run much stronger open-weight models than in 2024.
2. The chart claims AA Intelligence Index scores of 10 for Llama 3 70B, 16 for Qwen 2.5 72B, 14 for Llama 3.3 70B, 33 for gpt-oss-120B, 39 for Gemma 4 31B, 46 for Qwen3.6 27B, and 47 for DeepSeek V4 Flash.
3. Artificial Analysis corroborates several current/historical score points: DeepSeek V4 Flash 47, Qwen3.6 27B 46, Gemma 4 31B 39, gpt-oss-120B 33, Qwen2.5 72B 16, and Llama 3.3 70B 14. Llama 3 Instruct 70B currently appears as score 9 on the inspected AA page, close to but not exactly the chart's 10.
4. The exact [[antirez]] GGUF artifact does exist as `antirez/deepseek-v4-gguf`; Alpha's narrower HF search missed it because the repository name does not include all searched terms in the same way.
5. The antirez repository supports the 128 GB fit claim only at the artifact/usage-instruction level: it lists an 80.8 GiB q2 mixed quant and says to use q2 on 128 GB Mac machines. It does not provide an independent benchmark showing the quantized artifact preserves the AA score or local coding-agent usefulness.

## Notable Quotes
- Captured tweet: "Local open-weight AI on a laptop has been improving more than twice as fast as Moore's Law!"
- Captured tweet: "the smartest open-weight model from @huggingface you could actually run on it went from a score of 10 (Llama 3 70B) to 47 (DeepSeek V4 Flash on @antirez's mixed-Q2 GGUF) on the @ArtificialAnlys Intelligence Index."
- antirez GGUF README: "Use q2 on 128 GB Mac machines, q4 on machines with ≥ 256 GB RAM, pair either with MTP for optional speculative decoding."
- Artificial Analysis methodology page: "Like all evaluation metrics, it has limitations and may not apply directly to every use case."

## Entities Mentioned
- [[Artificial Analysis]]
- [[DeepSeek V4 Flash]]
- [[antirez]]
- [[Hermes Agent]]
- [[Qwen3.6]]

## Concepts Mentioned
- [[Local Open-weight Laptop Inference]]
- [[Multi-Token Prediction Local Inference]]
- [[Managed Local llama.cpp Provider]]
- [[Agent-Computer Interface Design]]

## Follow-ups
- If Overseer later approves an implementation/eval lane, test local model usefulness with explicit memory, context, throughput, quality, tool-use, and Codex/Hermes task metrics rather than adopting the Moore's Law chart as proof.
- Open evidence gap: independent benchmarks of the antirez mixed-Q2 GGUF on 128 GB Apple Silicon, especially versus the full DeepSeek V4 Flash model and current local alternatives.
