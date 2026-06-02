---
source_url: https://x.com/adxtyahq/status/2057410759236386866
ingested: 2026-05-29
ingested_by: agent-alpha
context: Historical Tolaria backfill item from ingestion ledger; tweet; category uncategorized; credibility tier social; evidence grade weak; first seen 2026-05-21T16:33:59.973472; mentions 2.
source_type: tweet
credibility_tier: social
evidence_grade: weak
canonical_url: https://x.com/adxtyahq/status/2057410759236386866
---

# adxtyahq X post: RAG pipeline for 10M docs with zero hallucination

## Ledger context

- URL: https://x.com/adxtyahq/status/2057410759236386866
- Source type: tweet
- Category: uncategorized
- Credibility tier: social
- Evidence grade: weak
- First seen: 2026-05-21T16:33:59.973472
- Mentions: 2
- Preview/context example 1: message_index 54 preview `https://x.com/adxtyahq/status/2057410759236386866?s=52` session_file `/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260521_163522_8222f6.json`
- Preview/context example 2: message_index 54 preview `https://x.com/adxtyahq/status/2057410759236386866?s=52` session_file `/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260521_124017_ff8d5cd6.json`

## Captured X metadata

- Author: aditya (@adxtyahq), verified account
- Timestamp: 10:38 AM · May 21, 2026
- Captured engagement at fetch time: 85 replies, 336 reposts, 2.7K likes, 4.7K bookmarks, 192.8K views
- X render marker: Made with AI

## Raw post text

> “design a RAG pipeline for 10M docs with zero hallucination”
>
> apparently this was asked in a Google L5 interview round. came across it somewhere on the internet and honestly it’s a way more interesting system design problem than most classic distributed systems questions
>
> 1. ingest + normalize docs
> - remove duplicates, standardize formats, extract metadata, maintain version history
>
> 2. hybrid retrieval (BM25 + embeddings)
> - BM25 handles exact keyword matching while embeddings capture semantic meaning
> - semantic search alone usually struggles with precision at massive scale
>
> 3. ANN retrieval + reranking
> - ANN (Approximate nearest neighbor ) quickly pulls top candidate chunks from millions of docs
> - then a reranker rescoring step improves relevance by deeply comparing query vs retrieved chunks
>
> 4. source confidence scoring
> - every retrieved chunk gets scored based on freshness, trust level, overlap and retrieval consistency
> - low-confidence context should never heavily influence generation
>
> 5. constrained generation
> - the model is only allowed to answer using retrieved context (nothing new to be invented outside of the retrieved context)
>
> 6. citation-backed responses
> - every major claim links back to exact chunks, documents or timestamps
>
> 7. hallucination fallback layer
> - if retrieval confidence drops below a threshold: “insufficient evidence found”
>
> 8. continuous evals
> - run adversarial queries, retrieval recall benchmarks and hallucination tests continuously
>
> 9. caching + memory layer
> - cache high-frequency enterprise queries and retrieval paths (improves latency and output)
>
> 10. observability everywhere
> - trace retrieval paths, chunk rankings, token attribution and failure points
>
> Also at 10M docs, retrieval quality matters more than the frontier model itself.

## Embedded links inspected

No outbound technical/docs/repo/paper links were exposed in the rendered post or anchor enumeration. Exposed links were only the author/profile, photo route, analytics route, auth/legal X routes, and mentioned profile links in the sidebar/profile metadata.

Relevant exposed URLs:

- https://x.com/adxtyahq/status/2057410759236386866/photo/1 — attached image route
- https://pbs.twimg.com/media/HI1kLYjbIAAWoWx?format=jpg&name=small — attached image asset
- https://x.com/adxtyahq/status/2057410759236386866/analytics — X analytics route, not a source

## Image OCR / visual content

Attached image title: `RAG Pipeline for 10M+ Docs (Zero Hallucination)`.

The image is a hand-drawn flow diagram that restates the post as a pipeline:

1. Ingest + normalize docs from a `10M+ docs` corpus: deduplication, format standardization, metadata extraction, versioning.
2. Hybrid retrieval using BM25 + embeddings, with separate BM25 and vector indexes.
3. ANN retrieval + reranking: ANN fetches top K candidates, reranker cross-encodes/deeply scores and reorders by relevance.
4. Source confidence retrieval: score by freshness, trust, overlap, retrieval consistency; filter low-confidence chunks.
5. Constrained generation: LLM answers only from retrieved context, with no external knowledge or assumptions.
6. Citation-backed response: every claim links to source chunks/docs/timestamps, producing a final response plus citations.
7. Confidence threshold branch: if confidence fails threshold, return `insufficient evidence found (no answer)`.
8. Continuous evals: adversarial queries, retrieval recall benchmarks, hallucination-rate tracking, offline + online evaluation.
9. Caching + memory layer: cache frequent queries and retrieval results; personalize user/session memory.
10. Observability everywhere: trace retrieval paths, chunk rankings, token attribution, failure case logging, dashboards/alerts.

The image adds structure and labels (data flow, feedback/monitoring flow, support/data flow) but no independent evidence, primary references, quantitative metrics, or implementation details beyond the tweet text.

## Ingestion assessment

- Classification: research / possible wiki-ingest; not implementation.
- Claim/evidence split: The post claims a large-scale RAG design can target `zero hallucination`, but provides only a high-level interview-answer style checklist and a generated diagram. It does not provide a primary source for the Google interview claim, a reproducible architecture, datasets, benchmarks, or measured hallucination reductions.
- Contradiction/caveat notes: `zero hallucination` should be treated as an aspirational requirement or refusal/fallback policy, not as a verified achievable guarantee. The useful content is the checklist of retrieval, confidence, citation, eval, cache, and observability components for RAG design.
- Recommended action: one Tolaria information-processing card if not already covered elsewhere, focused on converting the weak social checklist into a source-backed RAG reliability/eval pattern map and explicitly grading the `zero hallucination` framing.
