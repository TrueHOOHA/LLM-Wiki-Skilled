---
source_url: https://x.com/clementdelangue/status/2053825719587815711
ingested: 2026-05-29
ingested_by: agent-alpha
context: Historical Tolaria backfill item from social source; category uncategorized; first seen 2026-05-12T20:32:25.254532; mentions 6.
source_type: tweet
credibility_tier: social
evidence_grade: weak
---

# Clement Delangue tweet: local open-weight AI on laptops improving faster than Moore's Law

## Original source

- URL: https://x.com/clementdelangue/status/2053825719587815711
- Author: clem / @ClementDelangue
- Posted: 1:13 PM · May 11, 2026
- Source type: tweet
- Credibility tier: social
- Evidence grade: weak

## Historical context/previews

- /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_203225_3fd38c.json message_index=4 preview="[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instructio"
- /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_041605_9fbc29ee.json message_index=83 preview="https://x.com/omarsar0/status/2052850591584383177?s=48 https://x.com/anirudhbv_ce/status/2052532004919361958?s=48 https://x.com/sudoingx/status/2052794989881753743?s=48 https://x.com/deronin_/status/2"
- /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_194403_9a9f91.json message_index=83 preview="https://x.com/omarsar0/status/2052850591584383177?s=48 https://x.com/anirudhbv_ce/status/2052532004919361958?s=48 https://x.com/sudoingx/status/2052794989881753743?s=48 https://x.com/deronin_/status/2"

## Captured tweet text

Local open-weight AI on a laptop has been improving more than twice as fast as Moore's Law!

Between May 2024 and May 2026, the most expensive MacBook Pro you could buy stayed at 128 GB of unified memory. The hardware ceiling barely moved.

But the smartest open-weight model from @huggingface you could actually run on it went from a score of 10 (Llama 3 70B) to 47 (DeepSeek V4 Flash on @antirez's mixed-Q2 GGUF) on the @ArtificialAnlys Intelligence Index.

That is 4.7× in 24 months, or a doubling of intelligence every 10.7 months. Moore's Law (transistor count) doubles every 24 months. Local open-weight AI on a laptop has been improving more than twice as fast as Moore's Law, on completely unchanged hardware.

## Image OCR / chart content

Attached image URL:
- https://pbs.twimg.com/media/HICmz2QXYAAROFH?format=jpg&name=small

Chart title/text:
- "Smartest open-weight model on a 128 GB MacBook Pro"
- "Artificial Analysis Intelligence Index v4.0 (higher score better)"

Rows shown:
- May 2024 — Llama 3 70B — score 10
- Oct 2024 — Qwen 2.5 72B — score 16
- Mar 2025 — Llama 3.3 70B — score 14
- Oct 2025 — gpt-oss-120B — score 33
- May 2026 — Gemma 4 31B — score 39
- May 2026 — Qwen3.6 27B — score 46
- May 2026 — DeepSeek V4 Flash — score 47

Chart annotation:
- "Moore's Law would predict a score of ≈ 20 here (starting at 10, doubling every 24 months)."

## Links and source-check notes

Links exposed in the X render:
- https://x.com/ClementDelangue — author profile
- https://x.com/huggingface — Hugging Face mention
- https://x.com/antirez — antirez mention, cited for mixed-Q2 GGUF
- https://x.com/ArtificialAnlys — Artificial Analysis mention
- https://x.com/ClementDelangue/status/2053825719587815711/photo/1 — attached chart image

Related primary/near-primary pages inspected during backfill:
- https://artificialanalysis.ai/ — Artificial Analysis homepage currently exposes an Intelligence leaderboard and links to model pages/methodology.
- https://artificialanalysis.ai/models/deepseek-v4-flash — confirms DeepSeek V4 Flash is listed as open weights, released April 2026, 47 Artificial Analysis Intelligence Index, 102 output tokens/sec, 284B total / 13B active parameters, MIT license, 1M context window, Hugging Face weights link.
- https://artificialanalysis.ai/methodology/intelligence-benchmarking — methodology link exposed from Artificial Analysis pages; not fully extracted in this Alpha pass.
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash — model card confirms model availability, MIT license, DeepSeek V4 series description, 284B total / 13B active parameters, 1M context, FP4+FP8 mixed precision, local deployment references, and evaluation tables.
- https://huggingface.co/models?search=antirez%20DeepSeek%20V4%20Flash%20GGUF — inspected for the claimed antirez mixed-Q2 GGUF artifact; search returned 0 models in this render, so the exact quantized artifact was not corroborated in this pass.

## Key claims extracted

- Claim: A fixed 128 GB MacBook Pro hardware ceiling can run much stronger open-weight models in 2026 than in 2024.
  - Evidence: Social claim plus chart; Artificial Analysis corroborates the DeepSeek V4 Flash score and open-weight model page, but not the full historical laptop-runnable sequence.
- Claim: Artificial Analysis score rose from 10 for Llama 3 70B in May 2024 to 47 for DeepSeek V4 Flash in May 2026.
  - Evidence: Tweet/chart; DeepSeek V4 Flash current AA score of 47 corroborated; earlier chart points not independently checked in this pass.
- Claim: This is 4.7x in 24 months / intelligence doubling every 10.7 months, faster than Moore's Law's 24-month transistor doubling.
  - Evidence: Arithmetic follows from 10 to 47 if the underlying scores and comparability are accepted; methodology comparability and laptop-runnable assumptions need review.
- Claim: DeepSeek V4 Flash can run on a laptop via antirez mixed-Q2 GGUF.
  - Evidence: Not corroborated here; exact antirez GGUF artifact was not found by HF model search during this pass.

## Contradiction notes / caveats

- Social post is a weak evidence source and compresses several assumptions: benchmark comparability across time, what "smartest" means, what "actually run" means, quantization quality, context length, speed/latency, and usability on laptop hardware.
- Artificial Analysis confirms the 47 score for DeepSeek V4 Flash on its current page, but the complete historical series and the laptop-runnable quantized artifact need stronger source-checking.
- HF confirms model availability and specs, but not that a specific mixed-Q2 GGUF by antirez preserves the claimed score or is usable on a 128 GB MacBook Pro.
- The Moore's Law comparison is rhetorically useful but potentially misleading because benchmark scores are not transistor counts and may not scale linearly with real task utility.

## Actionability

Classification: Research / wiki-ingest.

Recommended Beta workstream: create a Tolaria source page and, if useful, a synthesis note on the local open-weight laptop inference trend: distinguish validated facts from social extrapolation, check Artificial Analysis methodology/historical scores, verify the GGUF/laptop-run claim, and extract implications for local Codex/Hermes model strategy without recommending implementation yet.
