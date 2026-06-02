---
type: entity
aliases: ["llama.cpp", "llama-server", "ggml-org/llama.cpp"]
tags: [local-inference, llama-cpp, open-source]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# llama.cpp

## Identity
llama.cpp is the open-source C/C++ local LLM inference runtime used by pi-llamacpp to run Qwen3.6 GGUF models through `llama-server`.

## Aliases
- llama.cpp
- llama-server
- ggml-org/llama.cpp

## Key Attributes
- Category: local LLM inference runtime
- Repository observed in source: `ggml-org/llama.cpp`, public MIT C++ project
- Role in source: base runtime that pi-llamacpp builds or downloads and launches behind a managed provider endpoint
- MTP relevance: PR #22673 is cited for Multi Token Prediction/speculative decoding support and benchmark claims on Qwen3.6 models
- Evidence caveat: runtime mechanics are primary-source-backed, but source-specific speed claims need independent target-machine verification

## Evidence
- [[Armin Ronacher X post on pi-llamacpp Qwen3.6 local provider]] records that pi-llamacpp uses llama.cpp, defaults to a pinned source snapshot for MTP/NextN support, and exposes `llama-server` through a managed localhost endpoint.
- [[pi-llamacpp Managed Local Provider Pattern Assessment]] frames llama.cpp as the runtime layer in a possible future Hermes-managed local provider evaluation.

## Related
- [[pi-llamacpp]]
- [[Qwen3.6]]
- [[Managed Local llama.cpp Provider]]
- [[Multi-Token Prediction Local Inference]]
- [[Hermes Agent]]

## Open Questions
- Which llama.cpp release first includes the relevant MTP support without needing the pinned PR snapshot?
- Which server flags, KV-cache settings, context sizes, and chat templates are stable enough for any future managed-provider evaluation?
- How should a Hermes-managed provider detect and report llama.cpp build/runtime incompatibilities?
