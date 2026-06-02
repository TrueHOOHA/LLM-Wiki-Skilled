---
source_url: https://x.com/mitsuhiko/status/2053228285635498149
ingested: 2026-05-29
ingested_by: agent-alpha
source_type: tweet
category: uncategorized
credibility_tier: social
evidence_grade: weak
first_seen: 2026-05-12T18:31:55.856664
context: Historical Tolaria backfill item. User asked Alpha to follow embedded links/source-check where possible and queue only useful Tolaria information-processing workstreams.
canonical_url: https://x.com/mitsuhiko/status/2053228285635498149
---

# X post by Armin Ronacher about pi-llamacpp and Qwen3.6 local llama.cpp provider

## Prior Alpha context

- `/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_041605_9fbc29ee.json` message_index 83 preview included this batch context alongside other X links.
- `/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_194403_9a9f91.json` message_index 83 preview included this batch context alongside other X links.

## Primary X source

URL: https://x.com/mitsuhiko/status/2053228285635498149
Author: Armin Ronacher ⇌, @mitsuhiko
Observed timestamp on X: 9:39 PM · May 9, 2026
Observed engagement: 20 replies, 53 reposts, 534 likes, 500 bookmarks, 37.3K views

Captured post text:

> If you don't have a 128GB mac, I also have a pi-llamacpp extension that just configures 4 versions of Qwen 3.6. https://t.co/AiIbCnpAlV — compiles and runs llama.cpp, downloads the models and sets the up correctly.

Resolved embedded link:

- t.co: https://t.co/AiIbCnpAlV
- Destination: https://github.com/mitsuhiko/pi-llamacpp

## Linked source: GitHub repository

URL: https://github.com/mitsuhiko/pi-llamacpp
Title: `mitsuhiko/pi-llamacpp`
Description: An experimental Pi extension that runs and manages Qwen with llama.cpp.
Stars/forks at capture: 143 stars, 12 forks
Latest visible commit: `66e4441` — `fix(models): pin Hugging Face revisions`, about 3 weeks before capture
Files observed: `.gitignore`, `LICENSE`, `README.md`, `index.ts`, `install-pi-extension-local.sh`, `llamacpp-watchdog.sh`, `package.json`
Package metadata: `pi-llamacpp`, MIT, Pi extension package for managed local llama.cpp inference; peer deps `@earendil-works/pi-ai` and `@earendil-works/pi-coding-agent`.

README captured claims and mechanics:

- Pi provider extension for running Pi self-managed local `llama.cpp` inference.
- Registers Qwen3.6 GGUF models under the `llamacpp` provider.
- Downloads/builds a matching llama.cpp runtime.
- Downloads selected GGUF on first use.
- Starts `llama-server` and stops it automatically when Pi shuts down.
- Registered model IDs:
  - `llamacpp/qwen-3.6-dense-2bit` (27B dense)
  - `llamacpp/qwen-3.6-dense-4bit` (27B dense)
  - `llamacpp/qwen-3.6-dense-8bit` (27B dense)
  - `llamacpp/qwen-3.6-moe-2bit` (35B-A3B MoE)
  - `llamacpp/qwen-3.6-moe-4bit` (35B-A3B MoE)
  - `llamacpp/qwen-3.6-moe-8bit` (35B-A3B MoE)
- MoE GGUF source: `havenoammo/Qwen3.6-35B-A3B-MTP-GGUF`, pinned revision `44ce525026e7e7d0e0915dc1bf83a783c813e75a`.
- Dense GGUF source: `froggeric/Qwen3.6-27B-MTP-GGUF`, pinned revision `431204640c8511573e61a7964a12cc452114a223`.
- Runtime default builds a pinned llama.cpp source snapshot from pull request #22673 for MTP/NextN support, rather than using stock binary release.
- Install command: `pi install https://github.com/mitsuhiko/pi-llamacpp`.
- Runtime state location: `~/.pi/llamacpp` with `source/`, `runtime/`, `downloads/`, `models/`, `clients/`, `server.json`, and `log`.
- Managed server binds to random localhost port by default and records endpoint in `server.json`; fixed port via `LLAMACPP_PORT`.
- Debug commands inside Pi: `/llamacpp`, `/llamacpp status`, `/llamacpp stop`.

Implementation details observed from `index.ts` / scripts:

- Provider ID: `llamacpp`; managed-by marker: `pi-llamacpp-provider`.
- Uses local state under `~/.pi/llamacpp`; client leases under `clients/`; server state in `server.json`; log file `log`.
- Runtime kind defaults to source build; release fallback exists via env.
- Default source ref: `5d5f1b46e4f56885801c86363d4677a5f72f83af` from `ggml-org/llama.cpp` unless overridden.
- Host defaults to `127.0.0.1`; port can be dynamic or env-fixed.
- Uses Qwen thinking/instruct sampling presets; default context size appears to target 262144 tokens.
- Maintains heartbeat, lease TTL, lifecycle lock, startup timeout, shutdown grace, log tail, and watchdog behavior.
- Watchdog script polls active client lease files and stops managed `llama-server` when no active leases/clients remain.
- Local dev installer symlinks the checkout into `$HOME/.pi/agent/extensions/pi-llamacpp` and instructs user to reload Pi.

## Followed linked primary/supporting sources

### llama.cpp

URL: https://github.com/ggml-org/llama.cpp
Observed API metadata: public MIT repo, description `LLM inference in C/C++`, default branch `master`, language C++, 113k+ stars, active in May 2026.
Relevance: base runtime used by pi-llamacpp.

### llama.cpp PR #22673

URL: https://github.com/ggml-org/llama.cpp/pull/22673
Title: `llama + spec: MTP Support`
State at capture: closed
Author: `am17an`
Key PR body claims:

- Adds support for MTP (Multi Token Prediction) heads.
- Tested on Qwen3.6 27B and Qwen3.6 35BA3B.
- Reports steady-state acceptance around 75% with 3 draft tokens and more than 2x speed-up over baseline.
- Notes prompt processing speed can take a negative hit when MTP is enabled due to Device-To-Host embedding transfers.
- Notes parallel decoding with MTP is supported but not fully optimized.
- Provides sample commands for `llama-server` with `--spec-type draft-mtp --spec-draft-n-max`.

Selected PR benchmark excerpt:

- Baseline Qwen3.6 Q8_0 aggregate: 1404 predicted tokens, wall_s_total 201.07, ~7 tok/s per task.
- MTP `--spec-draft-n-max 3` aggregate: 1406 predicted tokens, 1319 draft, 952 accepted, aggregate_accept_rate 0.7218, wall_s_total 83.8.
- MTP `--spec-draft-n-max 2` aggregate: 1421 predicted tokens, 1062 draft, 877 accepted, aggregate_accept_rate 0.8258, wall_s_total 90.44.

### Hugging Face: havenoammo/Qwen3.6-35B-A3B-MTP-GGUF

URL: https://huggingface.co/havenoammo/Qwen3.6-35B-A3B-MTP-GGUF
README frontmatter: Apache-2.0, base model `Qwen/Qwen3.6-35B-A3B`, tags include unsloth/qwen/qwen3_5_moe.
Key captured notes:

- GGUF files are Unsloth Dynamic 2.0 XL quantizations of Qwen3.6-35B-A3B with MTP layers grafted on top.
- MTP layers taken from `am17an/Qwen3.6-35BA3B-MTP-GGUF`, stored in Q8_0, merged into UD XL GGUFs.
- Requires custom llama.cpp build with MTP/speculative decoding support from PR #22673.
- Provides Docker image options for CUDA 13, CUDA 12, Vulkan, Intel CPU/Xe, ROCm.
- Example command uses `--spec-type mtp --spec-draft-n-max 3`, 262144 ctx, flash attention, q8_0 KV cache, and Qwen thinking-preservation chat template args.
- Model card claims Qwen3.6-35B-A3B is a 35B total / 3B activated MoE model with 262,144 native context, vision encoder, MTP trained with multi-steps, and coding-agent improvements.

### Hugging Face: froggeric/Qwen3.6-27B-MTP-GGUF

URL: https://huggingface.co/froggeric/Qwen3.6-27B-MTP-GGUF
README frontmatter: Apache-2.0, library `llama.cpp`, base model `Qwen/Qwen3.6-27B`, tags include gguf, qwen3.6, vision, multimodal, speculative-decoding, mtp.
Key captured notes:

- Claims Qwen3.6-27B with MTP is up to 2.7x faster, 262K context on 48 GB, fixed chat template.
- Example server command requires llama.cpp b9180 or newer and uses `--spec-type draft-mtp --spec-draft-n-max 3`, 262144 context, temp/top-p/top-k coding sampling, and optional mmproj for vision.
- Recommendation matrix says coding/debugging benefits from MTP across quants; creative writing can be slower on Q4_K_M–Q6_K.
- Claimed task acceptance ranges: code 79–89%, factual 62–70%, analysis 48–56%, creative 39–48%.
- Claims Apple Silicon memory table: 16 GB Mac can run IQ2_M at 65K context without vision; 32 GB Mac Q4_K_M at 77K/128K depending KV; 48 GB Mac Q6_K or Q5_K_M at 262K; 64 GB Mac Q8_0 at 262K; 96+ GB F16 at 262K.
- Provides OpenAI-compatible `/v1/chat/completions`, Anthropic-compatible `/v1/messages`, Claude Code usage via `ANTHROPIC_BASE_URL=http://127.0.0.1:8081 claude`, tool use, and vision examples.

## Source-check / skepticism notes

- The X post itself is social and weak evidence; it mainly points to a concrete repo.
- The repo is primary for the Pi extension implementation and exposes useful mechanism-level patterns: provider registration, model registry, first-use runtime/model download, dynamic localhost endpoint, server state file, lease files, watchdog shutdown, pinned upstream revisions.
- The performance claims are not fully independently verified here. They come from PR/model-card benchmarks and should be treated as hypotheses until tested on the target machine/harness.
- The linked model cards and PR indicate MTP support has been evolving; pi-llamacpp pins a specific PR snapshot/revisions, while the dense model card says b9180+ includes MTP support. This version drift should be checked before adopting any runtime instructions.
- The useful Tolaria angle is not “install this now”; it is a reusable pattern for managed local model providers and a source-backed note on Qwen3.6/MTP/llama.cpp local coding-agent runtime options.

## URLs captured

- https://x.com/mitsuhiko/status/2053228285635498149
- https://t.co/AiIbCnpAlV
- https://github.com/mitsuhiko/pi-llamacpp
- https://raw.githubusercontent.com/mitsuhiko/pi-llamacpp/main/README.md
- https://raw.githubusercontent.com/mitsuhiko/pi-llamacpp/main/index.ts
- https://raw.githubusercontent.com/mitsuhiko/pi-llamacpp/main/package.json
- https://raw.githubusercontent.com/mitsuhiko/pi-llamacpp/main/install-pi-extension-local.sh
- https://raw.githubusercontent.com/mitsuhiko/pi-llamacpp/main/llamacpp-watchdog.sh
- https://github.com/ggml-org/llama.cpp
- https://github.com/ggml-org/llama.cpp/pull/22673
- https://huggingface.co/havenoammo/Qwen3.6-35B-A3B-MTP-GGUF
- https://huggingface.co/froggeric/Qwen3.6-27B-MTP-GGUF
- https://huggingface.co/am17an/Qwen3.6-27B-MTP-GGUF/
- https://huggingface.co/am17an/Qwen3.6-35BA3B-MTP-GGUF
- https://unsloth.ai/docs/basics/unsloth-dynamic-v2.0-gguf
- https://docs.unsloth.ai/models/qwen3.6
- https://qwen.ai/blog?id=qwen3.6-35b-a3b
