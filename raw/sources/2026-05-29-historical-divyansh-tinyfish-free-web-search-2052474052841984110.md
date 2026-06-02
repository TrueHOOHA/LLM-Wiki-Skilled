---
source_url: https://x.com/divyansht91162/status/2052474052841984110
ingested: 2026-05-29
ingested_by: agent-alpha
context: "Historical Tolaria backfill item from prior Alpha sessions; tweet/social source about TinyFish making Search/Fetch free for AI agents."
source_type: tweet
category: uncategorized
credibility_tier: social
evidence_grade: weak
current_ledger_status_before_claim: new
mentions: 2
canonical_url: https://x.com/divyansht91162/status/2052474052841984110
---

# Historical X source: Divyansh Tiwari on TinyFish free web search/fetch for agents

## User/backfill context

Historical Tolaria backfill item, not a new user DM.

Original URL to ingest: https://x.com/divyansht91162/status/2052474052841984110
Source type: tweet
Category: uncategorized
Credibility tier: social
Evidence grade: weak
Ledger status before claim: new
Mentions: 2

Original session previews:
- /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_041605_9fbc29ee.json message_index 83 preview included batches beginning with https://x.com/omarsar0/status/2052850591584383177?s=48, https://x.com/anirudhbv_ce/status/2052532004919361958?s=48, https://x.com/sudoingx/status/2052794989881753743?s=48, https://x.com/deronin_/status/2...
- /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_194403_9a9f91.json message_index 83 preview included the same batch pattern.

## Primary X post capture

Browser/body text was recoverable unauthenticated on 2026-05-29.

Author: divyansh tiwari / @DivyanshT91162
Post URL: https://x.com/DivyanshT91162/status/2052474052841984110
Posted: 7:42 PM · May 7, 2026
Visible metrics at capture: 30.6K views; 20 replies; 34 reposts; 366 likes; 661 bookmarks/engagement count as rendered.

Post text:

> Crazy how fast this changed.
>
> Web search is basically free now for AI agents.
>
> I switched my OpenClaw and Hermes agents to TinyFish, and suddenly my agents could browse, research, and retrieve live info at scale…
>
> for $0.
>
> This is the kind of shift that quietly changes the entire AI agent ecosystem.

No outbound t.co links were exposed in the X DOM. The post appears to be a claim/endorsement, not a link thread. Profile image URLs only were exposed by browser_get_images; no attached media payload was recovered.

## Links and related sources inspected

Because the tweet itself names TinyFish, OpenClaw, and Hermes but exposes no links, Alpha inspected TinyFish's official site/docs and integration surfaces as related linked material.

- https://www.tinyfish.ai/ — official TinyFish homepage. Claims Search and Fetch APIs are free on every plan, with Search/Fetch/Agent/Browser as one web layer for agents.
- https://docs.tinyfish.ai/search-api — Search API docs. Search returns structured ranked web results; endpoint GET https://api.search.tinyfish.ai; requires X-API-Key; docs/pricing say 0 credits/request.
- https://docs.tinyfish.ai/fetch-api — Fetch API docs. Fetch renders URLs and extracts clean markdown/html/json; endpoint POST https://api.fetch.tinyfish.ai; max 10 URLs/request; docs/pricing say 0 credits/URL.
- https://www.tinyfish.ai/pricing — Pricing page. States Search and Fetch are 0 credits; Agent consumes 1 credit/step; Browser consumes 1 credit/4 min; PAYG listed as $0.015/credit with 500 free credits to start.
- https://registry.modelcontextprotocol.io/?q=tinyfish — MCP Registry search. TinyFish Web Agent server exposed as streamable-http at https://agent.tinyfish.ai/mcp.
- https://github.com/tinyfish-io/tinyfish-cookbook — official cookbook/examples. Describes TinyFish as web layer for AI agents and includes MCP/config examples.
- https://www.clawhub.ai/simantak-dabhade/tinyfish-web-agent — OpenClaw skill page. Shows install command `openclaw skills install tinyfish-web-agent`, plus prerequisites such as `npm install -g @tiny-fish/cli`, `tinyfish auth login`, or `TINYFISH_API_KEY`.
- https://pypi.org/project/tinyfish/ — official Python SDK, package `tinyfish`, Python >=3.11.
- https://www.npmjs.com/package/@tiny-fish/cli — TinyFish CLI package, checked via registry metadata because npm web UI was bot-gated.
- https://docs.tinyfish.ai/agent-api — Agent API docs; agent/browser automation is metered, not free.
- https://docs.tinyfish.ai/browser-api — Browser API docs; browser sessions are metered and have startup/session caveats.
- https://www.tinyfish.ai/customers — first-party customer/case-study surface; useful but marketing evidence.

## Extracted facts from inspected sources

### Search API

- Purpose: web search returning structured ranked results: title, snippet, URL, site_name, position, total_results.
- Endpoint: GET https://api.search.tinyfish.ai.
- Required parameter: query. Optional parameters include location, language, page.
- Docs/pricing say Search does not consume credits / 0 credits per request.
- Rate limits captured by delegate inspection: Free/PAYG 30 req/min, Starter 60 req/min, Pro 120 req/min, Enterprise custom.
- Auth: X-API-Key header required; SDK can read TINYFISH_API_KEY.
- Caveat: docs/reference still list possible 402 payment-required and 403 access-not-enabled errors despite zero-credit pricing.

### Fetch API

- Purpose: render URLs with a real browser, including JavaScript-heavy pages, and extract clean content.
- Endpoint: POST https://api.fetch.tinyfish.ai.
- Request: `urls` required, max 10 per request; optional `format` markdown/html/json, `links`, `image_links`, `ttl`.
- Docs/pricing say Fetch does not consume credits / 0 credits per URL.
- Rate limits captured by delegate inspection: Free/PAYG 150 URLs/min, Starter 300 URLs/min, Pro 600 URLs/min, Enterprise custom.
- Operational caveats: http/https only; localhost/private IP/cloud metadata endpoints rejected; per-URL failures appear in errors[]; per-URL backend timeout 110s; full batch CDN ceiling 120s; bot blocks can return bot_blocked; default may serve cached content unless `ttl=0` forces live fetch; unsupported content includes images/video/binary.

### Integration surfaces

- MCP Registry server: `ai.tinyfish.agent/web-agent`, version 1.0.1, remote `streamable-http` URL https://agent.tinyfish.ai/mcp.
- TinyFish cookbook shows a different MCP config URL in one place: `https://mcp.tinyfish.ai`, creating a URL inconsistency to verify before use.
- OpenClaw skill: `openclaw skills install tinyfish-web-agent`, current page version v1.0.3.
- Python SDK: package `tinyfish`, latest inspected 0.2.5, Python >=3.11, supports TinyFish and AsyncTinyFish; methods include agent.run(), agent.queue(), agent.stream(), runs.get(), runs.list().
- CLI: npm package `@tiny-fish/cli`, latest inspected 0.1.6, bin `tinyfish`.
- TypeScript SDK: npm package `@tiny-fish/sdk`, latest inspected 0.0.8.
- Docs/cookbook support generic MCP/coding-agent/OpenClaw integration. No TinyFish page explicitly naming Hermes was found; Hermes fit would depend on Hermes MCP/CLI integration patterns.

### Homepage/customer/benchmark claims

- Homepage claims Search is fresh/live and Fetch/Browser/Agent support production web workflows.
- Homepage claims "highest publicly benchmarked web agent" and "Mind2Web · 89.9%" but the accessible pages did not expose benchmark methodology or an independent leaderboard link.
- Homepage claims `<250ms` browser cold start, 85% anti-bot pass rate, and 99.3% detection coverage. These were not independently substantiated in inspected pages.
- Customer pages provide first-party case-study metrics and named quotes, but no independent measurement methodology was visible.

## Skeptical classification

Source claim: TinyFish makes web search essentially free for AI agents and made OpenClaw/Hermes agents able to browse, research, and retrieve live info at scale for $0.

Evidence actually found:
- Official TinyFish docs/pricing support the narrower claim that Search and Fetch are zero-credit/free-on-plan APIs with rate limits and API-key access.
- Official integrations support a general agent/MCP/OpenClaw integration story.
- Agent and Browser automation are not free; they are metered by credits.
- No direct evidence was found that this specific author switched Hermes agents successfully, or that Hermes has an official TinyFish integration.

Concepts worth preserving:
- Free/zero-credit Search+Fetch as an ingestion/research layer for agents.
- Separation between discovery/fetch (cheap/free) and browser/agent automation (metered).
- MCP/OpenClaw/CLI/SDK web-access surfaces as possible agent integration pathways.
- Need to validate freshness, caching behavior, failure modes, and real rate limits before relying on the service for Tolaria/Alpha/Beta workflows.

Contradiction notes/caveats:
- The social claim overstates the free aspect if interpreted as all web browsing/agent work; only Search and Fetch are zero-credit.
- "Live" needs qualification: Search is marketed as live/never cached, but Fetch can serve cached content unless `ttl=0` is used.
- Homepage browser cold-start claim conflicts with Browser API docs reporting typical session creation around 10-30 seconds.
- MCP URL appears inconsistent between registry (`https://agent.tinyfish.ai/mcp`) and cookbook (`https://mcp.tinyfish.ai`).
- Benchmark, anti-bot, and customer metrics are first-party/marketing-grade from inspected evidence.

Recommended disposition: queue one Tolaria knowledge-processing task, not implementation. Ask Beta to promote this source cluster into Tolaria with evidence grading and a proposal/approval question for any future Hermes/Tolaria integration validation.
