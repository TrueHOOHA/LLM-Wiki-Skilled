---
source_url: https://www.browserbase.com/blog/autobrowse
ingested: 2026-05-29
ingested_by: agent-alpha
context: Historical Tolaria backfill item from ingestion ledger; mentions=7; source_type=article; category=uncategorized; credibility/evidence unknown at intake.
source_type: article
credibility_tier: primary
evidence_grade: medium
contradiction_notes: Vendor-authored article with concrete workflow details and some benchmark numbers, but limited independent corroboration and no reproducible harness/results attached in the source itself.
---

# Autobrowse: The Mythos moment for Browser Agents is here

Original URL: https://www.browserbase.com/blog/autobrowse
Canonical URL: https://www.browserbase.com/blog/autobrowse

## Ingestion notes

- User requested SOUL.md / normal Alpha ingestion path for a historical Tolaria backfill item. No SOUL.md file was found in `/home/admin/.hermes/tolaria`; `/home/admin/.hermes/tolaria/AGENTS.md` was present and followed as the LLM-Wiki-Skilled schema reminder.
- Primary source fetched with browser and static HTML extraction.
- Useful embedded/adjacent links inspected: X longform article on Browserbase internal agents, Browse.sh launch article, Agent Skills overview.
- Classification: wiki-ingest / synthesis candidate. Useful for Tolaria source summary, concept/entity extraction, and a skeptical synthesis of agent-generated browser skills versus Hermes skills/Tolaria workflows.

## Related links inspected

- https://x.com/kylejeong/status/2044878529666662616 — Browserbase internal agent architecture article; provides surrounding skill/sandbox/proxy context for the Autobrowse claim.
- https://www.browserbase.com/blog/browse.sh — Browserbase launch article for a public catalog/CLI of browser skills powered by Autobrowse.
- https://agentskills.io/home — Agent Skills standard overview; corroborates broader portable SKILL.md folder format and progressive disclosure concept.

## Related: Browserbase internal agents article / X longform
URL: https://x.com/kylejeong/status/2044878529666662616

Captured via browser DOM because X direct/static fetching is unreliable. Relevant extracted substance:

- Title/body: "How we build internal agents at Browserbase". Browserbase runs one generalized internal agent named `bb` across Slack and web UI rather than a bot per task.
- Architecture: isolated ephemeral Linux sandbox per agent session; pre-warmed snapshots rebuilt every 30 minutes; key repos cloned into `/knowledge/`; OpenCode pre-installed; system tools include bun, git, gh, ripgrep, prettier, pdftotext, TypeScript LSP, Tailscale.
- Tool surface: read, write, edit, exec, safebash, skill. `exec` routes to a serverless integration proxy for CRM/logs/warehouse/support/chat.
- Credential/security model: sandbox gets references + short-lived tokens, not real secrets; proxy validates token and service.method allowlists; some egress credential brokering; domain allowlisting/request interception for sensitive APIs; RBAC plus agent-specific ABAC.
- Skill model: one OpenCode loop with lazy-loaded markdown skills and scoped permissions. Examples include data warehouse, customer intelligence, CRM, investigate-session, create-pr, write-browserbase-web-automations, log-feature-request, notion.
- Interfaces: Slack interactive mode keyed by thread ID with sandbox reuse; webhook/background mode with hard-scoped permissions; web UI showing traces/tool calls/filesystem.
- Claims/results: support-ticket/meeting-transcript scanning, feature-request coverage, faster first response, session investigation reduced from 30–60 minutes to one Slack message, engineers reviewing more PRs instead of hand-writing. These are vendor self-claims and need corroboration before adoption.
- Embedded links surfaced: https://opencode.ai/ and http://director.ai/ plus Browserbase/X profile links.


## Primary
URL: https://www.browserbase.com/blog/autobrowse
Title: Autobrowse: The Mythos moment for Browser Agents is here | Browserbase

### Extracted text

Autobrowse: The Mythos moment for Browser Agents is here | BrowserbaseSkip to contentBrowserbaseNavigation
Platform
Primitives
BrowsersReal browsers for your agent to use the web, without the headaches
Web Data APIsSearch and fetch APIs to efficiently retrieve web data
RuntimeScalable, sandboxed environments for agent deployments
IdentityAuthenticate your agent to navigate the web like a human
ModelsUse any model with a single API key
ObservabilityUnified debugging your agent across replays, logs, and prompts
Open Source
Browse CLIGive your agent browsing skills with a single command
StagehandThe most popular AI browser automation framework
DirectorA complete UI for building useful browser agents
Solutions
All Use Cases
Browser Agent
Automated Testing
Workflow Automation
Web Data Extraction
Resources
Resources
Blog
Customers
Enterprise
Templates
Pricing
Docs
Log in
Log inSign upGet a demo
May 06, 2026
Autobrowse: The Mythos moment for Browser Agents is here
Kyle Jeong
Shubhankar Srivastava
Engineering
10 minread
TL;DRBrowser agents have an amnesia problem. They re-discover every site from scratch on every run, paying the full discovery tax forever. Autobrowse fixes that by letting an agent iterate on a real task until it converges, then graduating the winning approach into a durable, reusable skill. That skill is memory the next agent, teammate, or customer can pick up and run without “re-learning” what's already been learned.
The genius without a hippocampus
If you've shipped a browser agent into production, you already know the shape of this problem.
The first run on a new site is exciting. The agent wanders around, figures out the page, eventually completes the task. The second run looks almost identical. The hundredth run is depressing. By then you've paid for the same exploration a hundred times, the cost graph is a straight line going up, and you still don't have a clean artifact you can hand to a teammate to say "this is how we do this job."
Real sites are messy. They render differently for different user agents, gate content behind JavaScript, hide the data you actually want behind an undocumented JSON endpoint, throw captchas when they don't recognize the session, and sometimes redesign their flow on a Tuesday. A generic agent loop copes with all of that fluently in the moment, then forgets everything once the session closes. The reasoning that solved Monday's problem evaporates along with the session.
The real bottleneck for browser agents in production is memory, in a form humans and agents can both read and trust. Reasoning has stopped being the constraint.
What is Autobrowse?
Autobrowse is a workflow that uses AI to improve AI. You give an agent a real task on a real site. It runs the task end to end, studies the trace it produced, iterates on its strategy, and keeps going until the workflow becomes reliable rather than lucky. Once it converges, it graduates the winning approach into a reusable skill: a markdown file plus the deterministic glue (CLI calls, fetches, selectors, helper scripts) needed to repeat the job.
This is similar to Karpathy's autoresearch harness, but for learning faster and cheaper browser skills. The first run is expensive on purpose, it's the run that pays for everything that comes after.
The artifact is the point. Every Autobrowse run produces a durable markdown file any future agent can load and execute, on top of whatever value you got from the run itself.
How it works:
The learning loop:
The core loop is simple:
Objective. Hand the agent a real task on a real site ("book a 7pm dinner reservation at this restaurant on OpenTable").
Run. Let the agent attempt the task end to end against a live browser.
Study. The agent reads its own trace. Where did it stall? Where did it guess? Where did it spend tokens it didn't need to?
Strategy. The run’s “outer loop” maintains a strategy.md file, basically a scratchpad where the agent dumps observations after each iteration (what worked, what broke, what to try next, what to stop doing). On the next iteration, the agent reads strategy.md first and uses it as context, so improvements compound instead of resetting every run.
Iterate. Refine the strategy based on those notes. Drop steps that didn't pull weight. Lean on deterministic helpers (browse fetch, browse search, custom Python) wherever possible.
Converge. Once consecutive iterations stop yielding meaningful improvements in cost or turn count, short-circuit.
Graduate. Write out a SKILL.md plus any helper files into the public skills repo.
In practice, we cap iterations low (~ 3 to 5) and short-circuit aggressively. The goal is a reliable, cheap path that's good enough to be reused, (technically short of any theoretical global optimum).
The output?
What comes out the other side is a small, readable file. No transcript, no vector of embeddings, no screenshot reel. Just markdown (just skim this):
markdown
--- name: "craigslist-search-listings" title: "Craigslist Search Listings" description: "Search Craigslist in a given city and category for listings matching a query, returning each listing's title, price, location, posting date, and listing URL." website: "craigslist.org" category: "marketplace" tags: ["craigslist", "marketplace", "listings", "search"] status: "autobrowsed-run-004 + prod-validated-002" source: "autobrowse + browser-trace · 4 iters · converged 2026-04-30 · cross-region prod validation 2026-05-01 (NY/SF/Boston, cta+apa) · postal-override discovery 2026-05-01 (Chicago/NYC, mca+apa)" updated: "2026-05-01" recommended_method: "api" alternative_methods:  - method: "browser"  rationale: "When the JSON API is rate-limited or blocked (rare — no auth or anti-bot today), fall back to browsing the city subdomain's /search/{category} page and extracting listings from the rendered text + anchor hrefs." ---
# Craigslist Search Listings — Browser Skill
## Purpose
Return a list of Craigslist postings matching a query in a given city and category — title, price, location, posting time, lat/lon, posting ID, and canonical listing URL. Read-only; never posts or edits.
## When to Use
- Daily / hourly monitoring of new listings matching a query. - Bulk extraction across multiple cities or categories. - Anywhere you'd otherwise scrape Craigslist HTML — the API is faster, cheaper, and structurally more reliable.
## Workflow
The Craigslist web UI is a thin client over a public JSON API at `https://sapi.craigslist.org` — no auth, cookies, session state, or anti-bot stealth. Send a `Referer` header matching the target city subdomain; if your outbound IP is in a different region than the target city, add `postal=<zip>&search_distance=<mi>` to the query — the API geo-scopes by IP only when no `postal` is supplied (see the gotcha below). **A residential proxy is not required.** Lead with the API path; the browser path works as a fallback but pays a ~100× cost premium because the search page is fully JS-rendered (`browse snapshot` returns 0 a11y refs and harvesting per-listing URLs costs ~3 turns each).
1. **Pick city + category** (and optionally subarea). City is the Craigslist subdomain (`sfbay`, `newyork`, `losangeles`, `seattle`, ...). Category is the search-path abbreviation (`sss` for-sale-all, `cta` cars+trucks, `apa` apartments, `ggg` for-sale-by-owner, etc.). To scope to a specific subarea (city-within-region), prefix the category in `searchPath` — e.g. `searchPath=sfc/apa` for SF-proper apartments, `searchPath=eby/cta` for East Bay cars. Subarea codes are listed in each response's `data.decode.locations[i][2]`. Subarea-scoping is significantly more efficient than fetching region-wide and filtering client-side (e.g. `apa` returns 9,798 bay-wide vs. 253 for `sfc/apa`).
2. **First page**:
GET https://sapi.craigslist.org/web/v8/postings/search/full
?searchPath={cat}
&query={q}
&sort={date|rel|priceasc|pricedsc}
&batch=1-0-360-1-0
&lang=en&cc=us
Referer: https://{city}.[craigslist.org/](http://craigslist.org/)
Returns JSON with `data.totalResultCount`, `data.items[]`, and decode tables under `data.decode`. Confirm the response is scoped to the right region via `data.areas` (e.g. `{"1": {"name": "newyork"}}`) — if it shows the wrong city, add `postal=<zip>&search_distance=<mi>` (any ZIP in the target metro) to override the IP-based geo-scope.
**Common filter params** (append as query args; check `data.humanReadableParams` to confirm acceptance): `min_price`, `max_price`, `min_bedrooms`, `max_bedrooms`, `min_bathrooms`, `bundleDuplicates=1`, `hasPic=1`, `postal=<zip>`, `search_distance=<mi>`, `availabilityMode=available`, `auto_make_model=<text>`, `min_auto_year`/`max_auto_year`, `min_auto_miles`/`max_auto_miles`. Unrecognized params are silently dropped.
3. **Decode each item**. `data.items[]` is an array of positional arrays. **Critical: many fields are offsets / lookup keys, not absolute values** — always read against `data.decode.*`:  - `item[0]` — `postingIdOffset`. Absolute id = `data.decode.minPostingId + item[0]`.  - `item[1]` — `postedDateOffset` (seconds). Absolute epoch = `data.decode.minPostedDate + item[1]`.  - `item[2]` — `categoryId` (integer). Maps to a 3-letter sub-category abbreviation (`cat3`) used in canonical URLs. The mapping is **not** in the response — it's a fixed Craigslist enum. Observed during iter-2 verification: `68 → bik` (bicycles), `93 → spo` (sporting goods), `122 → pts` (parts), `197 → bop` (bicycle parts/accessories). Other categories will need to be back-derived from the `data.decode` block or a click-through verification.  - `item[3]` — price as integer (0 or missing for free items).  - `item[4]` — `"locIdx:hoodDescIdx:hoodIdx~lat~lon"`. Look up `data.decode.locations[locIdx]` → `[1, city, subareaAbbr]`; `data.decode.locationDescriptions[hoodDescIdx]` → display location string; parse `lat~lon` for coordinates.  - **Title** — last array element that is a plain string (i.e. not a tagged `[code, ...]` block). For `cta` (cars+trucks) this is `item[-1]`. For `apa` (apartments) and other housing categories, a trailing `[5, beds, sqft]` housing-meta block pushes the title earlier — iterate from the end and take the first plain string.  - Tagged blocks `[code, value]` mid-array: `code === 5` is `[beds, sqft]` (housing categories); `code === 6` is the URL slug; `code === 10` is the formatted price string ("$1,350"); other codes carry image refs and metadata.
4. **Construct canonical post URL**:
https://{city}.[craigslist.org/{subareaAbbr}/{cat3}/d/{slug}/{postingId}.html](http://craigslist.org/{subareaAbbr}/{cat3}/d/{slug}/{postingId}.html)
- `postingId` from step 3 (offset + minPostingId)  - `subareaAbbr` from `data.decode.locations[locIdx][2]` (e.g. `nby`, `sby`, `sfc`, `eby`, `pen`)  - `cat3` from the categoryId enum (step 3)  - `slug` from the `[6, ...]` tagged block
**Wrong `cat3` will 404**. If you don't know the mapping for a categoryId, fall back to `https://{city}.craigslist.org/search/{cat}?postingId={postingId}` which redirects to the canonical URL.
5. **Paginate** (only if results > 360):
GET https://sapi.craigslist.org/web/v8/postings/search/batch
?batch=1-{OFFSET}-1080-1-0-{startTs}-{endTs}
&cacheId={cacheId from step 2}
Referer: https://{city}.[craigslist.org/](http://craigslist.org/)
Increment `OFFSET` in steps of 1080. `startTs`/`endTs` are the `data.cacheTs` and current epoch.
## Site-Specific Gotchas
- **Geo-redirect on bare domain**: `https://www.craigslist.org/` redirects to a city based on the request IP (in our trace, `provo.craigslist.org`). Always open `{city}.craigslist.org` directly. - **API geolocates by request IP — `postal=<zip>&search_distance=<mi>` overrides it**: No auth, no cookies, no anti-bot — but if no `postal` is supplied, the API scopes results to the city corresponding to the request's source IP, not the `Referer` header (e.g. a NY query from an SF IP silently returns `{"1": {"name": "sfbay"}}` results). Adding `postal=<zip>` for any ZIP in the target metro plus `search_distance=<mi>` forces the result set to that region. Verified 2026-05-01 with direct curl from an SF IP returning correct Chicago (`postal=60601&search_distance=50`, 0.21s, 41 results) and NYC (`postal=10001&search_distance=10`, 2.19s, 475 results) listings. **A residential proxy is not required** — `bb fetch --proxies` *without* `postal` is also geo-locked to sfbay (proxy doesn't change the source-IP region for this API), and adding `postal` to a direct curl is ~8× faster than the proxy path (0.21s vs 1.63s on the same Chicago query). Always verify scope via `data.areas` in the response. - **Snapshot returns 0 refs on `/search/`**: The search page is fully JS-rendered. Don't use `browse snapshot`/`click` to enumerate listings. - **Compact response format**: `data.items[]` uses positional arrays + `data.decode.*` lookup tables to keep the response small. Don't expect named fields per item — decode by position. - **Pagination batch sizes**: First page is ~360 (`batch=1-0-360-1-0`); subsequent batches are 1080 each (`batch=1-OFFSET-1080-1-0`). - **Free items have no price**: `item[3]` may be `0` or absent. - **Posting time precision**: The rendered page shows relative ("< 1 hr ago"); absolute epoch = `data.decode.minPostedDate + item[1]`. - **`item[0]` is NOT the postingId** — it's an offset from `data.decode.minPostingId`. Naïvely treating `item[0]` as the postingId produces 404s. - **`data.decode.locations` indexing is per-response, not stable.** Iter-3 saw `locations[1] → ["sfbay","sfc"]`; iter-4 saw `locations[1] → ["sfbay","eby"]` for the same city/query. The decode block is rebuilt per cache TTL — **always look up `locations[locIdx]` from the response in hand**, never cache or hardcode the table. - **Neighborhood labels are unreliable**: `data.decode.locationDescriptions` varies per response and per category. The same neighborhood may appear under different label-table indices across responses, may be missing in some categories (e.g. "Russian Hill" shows up in `apa` but is absent from `cta` decode tables), and is sometimes replaced by a generic city-level label by the poster. For neighborhood-scoped searches, use **lat/lon bounding-box matching** on `item[4]`'s coordinates as a fallback or supplement to label-string matching. Example bbox for North Beach + Russian Hill: `lat 37.794–37.810, lon -122.425 to -122.404`. - **Categories are an undocumented enum** — the response decode tables don't include the `categoryId → cat3` mapping; observed values across iters: `68→bik, 93→spo, 101→foa, 122→pts, 197→bop, 5→fua` (and likely many more for non-bicycle queries). The redirect URL `https://{city}.craigslist.org/search/{cat}?postingId={id}` is the safest fallback when an unknown categoryId is encountered. - **Rate-limit self-imposed**: No formal block but Craigslist throttles aggre
If the agent discovered an undocumented JSON endpoint, that endpoint is in there. If a particular form needs a small wait before submission, that's in there too. If a domain-specific helper (`helpers/amazon.py`, `helpers/opentable.py`, `helpers/sf-portal.py`) is worth keeping around, it gets checked in next to the skill.
This is the same shape we use inside `bb`, our internal generalist agent. In our post onhow we build agents at Browserbase, we wrote about how every internal workflow (feature requests, session investigations, PRs, sales triage) runs through one agent that loads small markdown skills on demand. The general loop stays simple. The domain knowledge lives in skills, where it can be read, edited, versioned, and reused.
Autobrowse pushes that idea one layer further: the agent writes its own skill, learned by actually doing the task.
The hand-written skills inside `browse` and the Autobrowse-graduated skills inside the public Browse CLI ecosystem are, importantly, the same kind of artifact. Once a skill exists, nothing about how an agent loads or runs it cares whether a human or another agent wrote it.
What is it good at?
Autobrowse shines on sites that genuinely require exploration.
Hidden or undocumented APIs that aren't visible from the rendered page but show up in network traffic.
Heavy client-side rendering, where the "real" content only appears after a sequence of interactions.
Multi-step login or wizard flows, where the right path isn't obvious from the first screen.
Any UI where the shortest reliable path is non-trivial enough that a human reverse-engineering it would take a couple of hours.
Token-saving opportunities where parts of the loop are redundant (e.g. skipping `browse screenshot` when the UI isn’t changing meaningfully).
For example, we used Autobrowse to play around with a federal grants portal and surface an undocumented JSON endpoint that returned every current grant in a single call. What looked like a 28-page scrape collapsed into a single `browse fetch`, and that discovery is now baked into the graduated skill so we never have to re-find it.
This is the recurring pattern that makes the whole approach worth investing in:an agent tries something a person never would, and finds something a person would never see.
A concrete benchmark: Craigslist
A clear internal benchmark we've shared so far is Craigslist.
Traditional Claude Code loop
: ~$0.22, ~71s
Graduated Autobrowse skill
: ~$0.12, 27s
The shape matters more than the absolute numbers. The first run on the site costs about what you'd expect from a generic agent loop. The end skill changes the unit economics of every subsequent run by an order of magnitude or more, because it encodes the shortest reliable path the agent could find and reuses it instead of re-deriving it.
We see the same shape on smaller tasks. On an early form-fill experiment, cost dropped from $1.40/run to $0.24/run in four iterations, just by letting the agent notice and remove the parts of its own approach that weren't pulling weight.
Where Autobrowse breaks
It would be easy to oversell this. Autobrowse is genuinely strong on a specific shape of problem and genuinely the wrong tool on another. The discipline of not using Autobrowse is part of using it well.
Autobrowse is not the right tool when the task is deterministic parsing. We learned this the hard way against a 167-row static HTML state catalog. The data was right there in the markup. No JavaScript, no auth, no anti-bot, just rows.
We threw Autobrowse at it anyway, because the framing of "let the agent figure it out" is seductive. Four iterations and ~$24 later, the loop still hadn't returned all 167 rows in a single output. The model's per-turn output cap kept truncating its reasoning, and the iteration loop kept trying to be clever about a problem that didn't reward cleverness.
Once we recognized the regime mismatch, the agent pivoted to ~200 lines of deterministic Python with `browse fetch` and BeautifulSoup. Sub-second runtime, zero inference cost, all 167 rows surfaced.
The lesson got written into the skill itself:
# Step 1: probe with fetch first.
browse fetch "<https://example.gov/programs>"
# If the data comes back cleanly in the response, write the parser.
# If the response is empty / dynamic / gated, escalate to Autobrowse.
Browser agents come in different agency levels, from a static script with no LLM in the loop, through router-style and tool-using agents, all the way up to fully autonomous loops that can spawn other agents and define their own tools. Choosing the right level is a real engineering decision.
Autobrowse sits at the high-agency end of that spectrum, and like any high-agency tool, you reach for it once the cheaper, more deterministic options have given up.
Why this changes workflows
A skill operates as a customer handoff, with all the weight that implies.
Today, when an agent succeeds at a job, the customer's engineering team gets a trace, maybe a session replay, maybe a paragraph of natural-language reasoning. None of those are legible to the people who actually own the workflow.
A skill is legible. It's durable, debuggable, human-auditable, and ownable. An engineer can read it, edit it, and commit it. A non-engineer (a technical PM, a VP of technology, a grants manager who knows their portal inside out) can also read it and roughly understand what the agent is doing without ever touching code.
We go from "just trust the agent's output" to "read the agent's playbook." That, in our view, is the thing that makes browser agents robust enough to live inside a serious enterprise workflow rather than awkwardly next to it.
The compounding effect matters too. Each new site an agent encounters yields one more durable skill. The library grows. The agent gets cheaper and faster on the long tail of repetitive workflows because it stops paying the discovery tax.
Autobrowse already functions as a factory for browser-agent capabilities, well beyond what any single agent could ship on its own. A single Autobrowse skill is useful. A growing public directory of them, accessible to anyone running a browser agent, is the actual prize.
What we're working on next
Smarter stopping
Right now we cap iterations at a small number and short-circuit when consecutive runs converge in cost and turn count. It's a reasonable heuristic, but a blunt one. We're letting the agent reason about its own convergence more explicitly, comparing not just cost and turns but the structure of its trace across runs.
Some of Autobrowse's most useful wins (like the federal-portal JSON endpoint) come from the agent randomly varying its approach and stumbling onto a much shorter path. We don't want to optimize that variance away too aggressively.
Better priors about how to explore
We want to make sure the agent reaches for our `fetch` and `search` primitives before spawning a full browser session. A lot of what looks like exploration can be answered with one fetch. For more advanced tasks, it’s reasonable to let the agent inspect browser traces, network events, and CDP logs so it can discover internal APIs by watching network requests rather than guessing at them from the rendered DOM.
Recursive Autobrowse
The most exciting direction is recursive: Autobrowse improving Autobrowse. Today the iteration loop, the convergence heuristic, and the skill template are mostly hand-crafted. The same way we use Autobrowse to graduate skills for individual sites, we can use it to graduate improvements to its own harness. Better prompts for the iteration step. Better priors for which primitives to reach for first. Better templates for what the final skill should look like for a given class of task.
The bigger picture
A dominant story about browser agents right now is that they'll get good when the underlying models get good. We're one Anthropic or OpenAI release away from agents that just work on the web. We don't entirely buy that.
Even a perfect model still has to discover (on every new site) what a perfect model would already know if it had been there before. Without a place to put what the agent learns, every run is a fresh start.
The real bottleneck is memory, in a form humans and agents can both understand and trust.
→ Kyle
Keep reading
Adding Foreground Tab Tracking to the Chrome Devtools Protocol
AuthorsNick SweetingPublished onMay 20, 2026TopicEngineering
Browse.sh, a catalog of browser skills for the agentic future
AuthorsKyle Jeong, Shubhankar Srivastava, Alex Qiu & Shrey PandyaPublished onMay 18, 2026TopicEngineering
Introducing the Session Replay API: Stream browser session replays
AuthorsKyle Jeong & Mike MoranPublished onMay 14, 2026TopicEngineering
What is Firecracker?
AuthorsKyle JeongPublished onMay 11, 2026TopicEngineeringView all blog postsBrowserbase
Primitives
Browsers
Web APIs
Runtime
Identity
Model Gateway
Observability
Stagehand
MCP
Industries
AI
Healthcare
Supply Chain
GTM
Tax
Legal
Developers
Docs
Templates
APIs & SDKs
Changelog
Status
Github
Company
Careers
Customers
Partner with Us
Trust & Security
Community
TwitterLinkedinYoutubeInstagram
Privacy Policy
Terms of Service
Community
TwitterLinkedinYoutubeInstagram
Privacy Policy
Terms of Service

### Extracted links
- Browserbase — /
- Browsers Real browsers for your agent to use the web, without the headaches — /browsers
- Web Data APIs Search and fetch APIs to efficiently retrieve web data — /search
- Runtime Scalable, sandboxed environments for agent deployments — /runtime
- Identity Authenticate your agent to navigate the web like a human — /identity
- Models Use any model with a single API key — /models
- Observability Unified debugging your agent across replays, logs, and prompts — /observability
- Browse CLI Give your agent browsing skills with a single command — /browse-cli
- Stagehand The most popular AI browser automation framework — /stagehand
- Director A complete UI for building useful browser agents — /director
- All Use Cases — /use-cases
- Browser Agent — /solutions/browser-agents
- Automated Testing — /solutions/testing
- Workflow Automation — /solutions/workflow-automation
- Web Data Extraction — /solutions/accessing-web-data
- Blog — /blog
- Customers — /customer-stories
- Enterprise — /enterprise
- Templates — /templates
- Pricing — /pricing
- Docs — https://docs.browserbase.com
- Log in — /sign-in
- Log in — /sign-in
- Sign up — /sign-up
- Get a demo — /contact
- Engineering — /blog/engineering/
- how we build agents at Browserbase — https://x.com/kylejeong/status/2044878529666662616
- Adding Foreground Tab Tracking to the Chrome Devtools Protocol — /blog/cdp-foreground-tab-tracking
- Browse.sh, a catalog of browser skills for the agentic future — /blog/browse.sh
- Introducing the Session Replay API: Stream browser session replays — /blog/session-replay
- What is Firecracker? — /blog/what-is-firecracker
- View all blog posts — /blog
- Browserbase — /
- Browsers — /browsers
- Web APIs — /search
- Runtime — /runtime
- Identity — /identity
- Model Gateway — /models
- Observability — /observability
- Stagehand — /stagehand
- MCP — /mcp
- AI — /industry/ai
- Healthcare — /industry/healthcare
- Supply Chain — /industry/supply-chain
- GTM — /industry/gtm
- Tax — /industry/fintech
- Legal — /industry/legal
- Docs — https://docs.browserbase.com
- Templates — /templates
- APIs & SDKs — https://docs.browserbase.com/reference/introduction
- Changelog — /changelog
- Status — https://status.browserbase.com/
- Github — https://github.com/browserbase
- Careers — /careers
- Customers — /customer-stories
- Partner with Us — /partner
- Trust & Security — https://trust.browserbase.com
- Twitter — https://x.com/browserbase
- Linkedin — https://www.linkedin.com/company/browserbasehq/
- Youtube — https://www.youtube.com/@browserbase
- Instagram — https://www.instagram.com/browserbase
- Privacy Policy — /privacy-policy
- Terms of Service — /terms-of-service
- Twitter — https://x.com/browserbase
- Linkedin — https://www.linkedin.com/company/browserbasehq/
- Youtube — https://www.youtube.com/@browserbase
- Instagram — https://www.instagram.com/browserbase
- Privacy Policy — /privacy-policy
- Terms of Service — /terms-of-service

## Related: Browse.sh
URL: https://www.browserbase.com/blog/browse.sh
Title: Browse.sh, a catalog of browser skills for the agentic future | Browserbase

### Extracted text

Browse.sh, a catalog of browser skills for the agentic future | BrowserbaseSkip to contentBrowserbaseNavigation
Platform
Primitives
BrowsersReal browsers for your agent to use the web, without the headaches
Web Data APIsSearch and fetch APIs to efficiently retrieve web data
RuntimeScalable, sandboxed environments for agent deployments
IdentityAuthenticate your agent to navigate the web like a human
ModelsUse any model with a single API key
ObservabilityUnified debugging your agent across replays, logs, and prompts
Open Source
Browse CLIGive your agent browsing skills with a single command
StagehandThe most popular AI browser automation framework
DirectorA complete UI for building useful browser agents
Solutions
All Use Cases
Browser Agent
Automated Testing
Workflow Automation
Web Data Extraction
Resources
Resources
Blog
Customers
Enterprise
Templates
Pricing
Docs
Log in
Log inSign upGet a demo
May 18, 2026
Browse.sh, a catalog of browser skills for the agentic future
Kyle Jeong
Shubhankar Srivastava
Alex Qiu
Shrey Pandya
Engineering
7 minread
TL;DRWe builtBrowse.sh, an open catalog of 100+ curated browser skills that any agent can install with one CLI command. Our Skills are durable, reusable playbooks that capture how to navigate real websites, so your agents stop re-discovering every site from scratch on every run. All of this is powered by Autobrowse, our system that uses AI to iterate on real tasks until it converges on the cheapest, fastest path. Open source, free, and ready to use today atbrowse.sh.
Over 100 skills. Zero re-learning. Your agent’s brain grew some grooves.
Browser Agents are everywhere right now, living in Claude Code, Cursor, and Codex. AI products are now shipping some version of "let the model drive a browser." And yet, every single one of these agents does the same dumb thing: it re-discovers every website from scratch, every time it runs.
Open a browser. Poke around. Find the button. Click it. Parse the response. Close the session. Forget everything, then do it all again tomorrow.
We've been building browser agents and infra at Browserbase for a while now. We've watched agents burn through tokens re-learning sites they've already conquered. We've watched customers painstakingly hand-write Playwright scripts for workflows an agent already solved last Tuesday. We've watched the same discovery tax get paid over and over, across thousands of sessions, by thousands of teams.
Today we're launchingBrowse.sh: an open catalog of browser skills that any agent can install and use immediately. 100 curated skills at launch and one CLI command to install.
What isBrowse.sh?
Browse.shis two things:
A catalog of browser skills atbrowse.sh, where you can search, preview, and install curated skills for navigating real websites.
The Browse CLI (npm i -g browse), the open-source command-line tool your agents use to actually drive browsers, fetch pages, search the web, and load skills on demand.
A "skill" is a markdown file (SKILL.md) plus any helper scripts needed to repeat a browser workflow reliably. It contains the exact steps, gotchas, API endpoints, selectors, and fallback strategies an agent needs to complete a task on a specific site. No vector embeddings or screenshot reels. Just plain text that humans can read and agents can execute.
It’s just like a playbook. An agent that loads the Craigslist skill doesn't need to spend 30 turns figuring out that the search page is fully JS-rendered and that there's a hidden JSON API atsapi.craigslist.org. That knowledge is already in the skill. The agent reads it, runs it, and moves on.
Why this exists
If you've shipped a browser agent into production, you know this shape intimately.
The first run on a new site is exciting. The agent wanders around, figures out the page, eventually completes the task. The second run looks almost identical. The hundredth run is depressing. By then you've paid for the same exploration a hundred times, the cost graph is a straight line going up, and you still don't have a clean artifact you can hand to a teammate and say "this is how we do this job."
Reasoning has stopped being the constraint. Memory has become the bottleneck, in a form that humans and agents can both read and trust.
The unit economics are brutal
We benchmarked this on Craigslist. A generic agent loop searching listings costs ~$0.22 per run. The agent has to discover that the search page is fully JS-rendered, stumble onto the hidden JSON API atsapi.craigslist.org, figure out the positional array decoding, learn that item[0] is an offset (not the posting ID), and work around IP-based geo-scoping. Every run pays that discovery tax from scratch.
After four Autobrowse iterations, the graduatedBrowse.shskill does the same job for ~$0.12 per run. The 45% cost reduction comes from better memory.
Every subsequent run after the first is fundamentally cheaper because the skill encodes the shortest reliable path the agent could find (the undocumented endpoint, the decode tables, the geo-override hack) and reuses it instead of re-deriving it. At scale, this is the difference between a cost curve that flatlines and one that compounds against you.
Skills are the new primitives
The industry is converging on this. Claude Code ships with skills. OpenAI Codex supports them. TheAgentSkills standardis gaining traction. Every major agent framework is adding some version of "load a markdown file that tells the agent how to do a specific thing."
Browser skills are the natural next step. The web is messy: sites render differently for different user agents, gate content behind JavaScript, hide data behind undocumented endpoints, throw CAPTCHAs on a whim, and redesign their flows on a Tuesday. A generic agent loop copes with all of that in the moment, then forgets everything once the session closes.
Browse.shcaptures what the agent learned, so the next agent (or the next teammate, or the next customer) doesn't have to learn it again.
How it works
Install the CLI
npm i -g browse
That's it.
Browse a skill
Head tobrowse.shand search for the site or task you need. Each skill page shows what the skill does, how it works, site-specific gotchas, and the install command.
Install a skill
browse skills add zillow.com/extract-listings
This pulls the skill into your local skills directory. Your agent can now load it on demand.
Use it in your agent
Point your agent at the skill and let it run. The skill provides the playbook; the agent provides the reasoning. A typical prompt looks like:
Use /extract-listings to find apartments under $3,000 in SF with 2+ bedrooms.
The agent reads the SKILL.md, follows the workflow, handles edge cases using the documented gotchas, and returns structured results.
Verify it yourself
Quick check: does the CLI see your installed skills?
browse skills list
What's inside a skill?
Every skill graduates fromAutobrowse, our system that uses AI to improve AI. You give an agent a real task on a real site. It runs the task end to end, studies its own trace, iterates on its strategy, and keeps going until the workflow becomes reliable rather than lucky. Once it converges, it writes out a durable skill.
Here's what that looks like in practice. This is a real excerpt from our Craigslist skill:
## Site-Specific Gotchas
- Snapshot returns 0 refs on `/search/`: The search page  is fully JS-rendered. Don't use `browse snapshot`. - `item[0]` is NOT the postingId - it's an offset from  `data.decode.minPostingId`. Treating it as the ID produces 404s. - API geolocates by request IP. Add `postal=<zip>` to   override. A residential proxy is not required.
- Rate-limit: keep ≤ 1 req/s sustained.
This is the kind of knowledge that takes a human engineer a couple of hours to reverse-engineer, and an agent dozens of dollars in tokens to discover from scratch. Once it's in a skill, it's free forever.
If the agent discovered an undocumented JSON endpoint, that endpoint is in there. If a particular form needs a small wait before submission, that's in there too. If a domain-specific helper script is worth keeping around, it gets checked in next to the skill.
What shipped?
We're launching with 100 skills spanning:
Marketplaces: Craigslist, Zillow, Amazon, eBay
Food & dining: OpenTable, DoorDash, McDonald's online ordering
Travel: flight search, hotel booking, Airbnb
Government: federal grants portals, state program catalogs
Developer tools: GitHub, npm, documentation sites
Enterprise SaaS: via partner integrations
Each skill is tagged with a category, verified status, and the site it targets. Partner skills from companies like Ramp, Lovable, Poke, and Reducto ship with a verified badge.
Generate your own
Don't see the skill you need? Type any domain and task intobrowse.sh, and Autobrowse will generate a skill for you. It runs the task against the live site, iterates until it converges, and publishes the result to the public catalog for anyone to use.
Every new skill makes the catalog more valuable, which brings more users, who generate more skills.
Who is this for?
Do you build agents that need the web? ├── Yes
│   ├── Are you tired of re-writing browser logic?
│   │   ├── Yes → install browse, load skills, ship
│   │   └── No → you will be. bookmark this
│   └── Do you want your agents to get cheaper over time?
│       ├── Yes → browse.sh skills compound
│       └── No → keep paying the discovery tax
└── No → browse.sh isn't for you (yet)
More specifically:
AI engineers building agents that automate web workflows (QA, data extraction, form filling, monitoring).
Product teams shipping browser-based features who want deterministic, auditable playbooks instead of black-box agent runs.
Platform teams looking to reduce token spend and latency across their agent fleet.
Anyone using Claude Code, Cursor, or Codex who wants their coding agent to browse the web with pre-built expertise.
The Vision
A dominant story about browser agents right now is that they'll get good when the underlying models get good. We're one Anthropic or OpenAI release away from agents that just work on the web.
We don't entirely buy that.
Even a perfect model still has to discover, on every new site, what a perfect model would already know if it had been there before. Without a place to put what the agent learns, every run is a fresh start. The models will keep getting better. The web will keep getting messier. The gap between "can reason about a page" and "knows the fastest path through this specific site" will persist.
Browse.shis that place. One CLI. A growing catalog of skills. Memory that compounds.
We built this because we believe the real unlock for browser agents isn't better reasoning. It's better memory, in a form that humans can audit and agents can execute.
Install our CLI with:
npm i -g browse
And find or create the skill you need atbrowse.sh.
The bottleneck for browser agents was never intelligence. It was amnesia.Browse.shis the cure.
Keep reading
Adding Foreground Tab Tracking to the Chrome Devtools Protocol
AuthorsNick SweetingPublished onMay 20, 2026TopicEngineering
Introducing the Session Replay API: Stream browser session replays
AuthorsKyle Jeong & Mike MoranPublished onMay 14, 2026TopicEngineering
What is Firecracker?
AuthorsKyle JeongPublished onMay 11, 2026TopicEngineering
Autobrowse: The Mythos moment for Browser Agents is here
AuthorsKyle Jeong & Shubhankar SrivastavaPublished onMay 06, 2026TopicEngineeringView all blog postsBrowserbase
Primitives
Browsers
Web APIs
Runtime
Identity
Model Gateway
Observability
Stagehand
MCP
Industries
AI
Healthcare
Supply Chain
GTM
Tax
Legal
Developers
Docs
Templates
APIs & SDKs
Changelog
Status
Github
Company
Careers
Customers
Partner with Us
Trust & Security
Community
TwitterLinkedinYoutubeInstagram
Privacy Policy
Terms of Service
Community
TwitterLinkedinYoutubeInstagram
Privacy Policy
Terms of Service

### Extracted links
- Browserbase — /
- Browsers Real browsers for your agent to use the web, without the headaches — /browsers
- Web Data APIs Search and fetch APIs to efficiently retrieve web data — /search
- Runtime Scalable, sandboxed environments for agent deployments — /runtime
- Identity Authenticate your agent to navigate the web like a human — /identity
- Models Use any model with a single API key — /models
- Observability Unified debugging your agent across replays, logs, and prompts — /observability
- Browse CLI Give your agent browsing skills with a single command — /browse-cli
- Stagehand The most popular AI browser automation framework — /stagehand
- Director A complete UI for building useful browser agents — /director
- All Use Cases — /use-cases
- Browser Agent — /solutions/browser-agents
- Automated Testing — /solutions/testing
- Workflow Automation — /solutions/workflow-automation
- Web Data Extraction — /solutions/accessing-web-data
- Blog — /blog
- Customers — /customer-stories
- Enterprise — /enterprise
- Templates — /templates
- Pricing — /pricing
- Docs — https://docs.browserbase.com
- Log in — /sign-in
- Log in — /sign-in
- Sign up — /sign-up
- Get a demo — /contact
- Engineering — /blog/engineering/
- Browse.sh — http://browse.sh/
- browse.sh — http://browse.sh/
- Browse.sh — http://browse.sh/
- Browse.sh — http://browse.sh/
- Browse.sh — http://browse.sh/
- browse.sh — http://browse.sh/
- sapi.craigslist.org — https://sapi.craigslist.org/
- sapi.craigslist.org — https://sapi.craigslist.org/
- Browse.sh — http://browse.sh/
- AgentSkills standard — https://agentskills.io/
- Browse.sh — http://browse.sh/
- browse.sh — http://browse.sh/
- Autobrowse — https://www.browserbase.com/blog/autobrowse
- browse.sh — http://browse.sh/
- Browse.sh — http://browse.sh/
- browse.sh — http://browse.sh/
- Browse.sh — http://browse.sh/
- Adding Foreground Tab Tracking to the Chrome Devtools Protocol — /blog/cdp-foreground-tab-tracking
- Introducing the Session Replay API: Stream browser session replays — /blog/session-replay
- What is Firecracker? — /blog/what-is-firecracker
- Autobrowse: The Mythos moment for Browser Agents is here — /blog/autobrowse
- View all blog posts — /blog
- Browserbase — /
- Browsers — /browsers
- Web APIs — /search
- Runtime — /runtime
- Identity — /identity
- Model Gateway — /models
- Observability — /observability
- Stagehand — /stagehand
- MCP — /mcp
- AI — /industry/ai
- Healthcare — /industry/healthcare
- Supply Chain — /industry/supply-chain
- GTM — /industry/gtm
- Tax — /industry/fintech
- Legal — /industry/legal
- Docs — https://docs.browserbase.com
- Templates — /templates
- APIs & SDKs — https://docs.browserbase.com/reference/introduction
- Changelog — /changelog
- Status — https://status.browserbase.com/
- Github — https://github.com/browserbase
- Careers — /careers
- Customers — /customer-stories
- Partner with Us — /partner
- Trust & Security — https://trust.browserbase.com
- Twitter — https://x.com/browserbase
- Linkedin — https://www.linkedin.com/company/browserbasehq/
- Youtube — https://www.youtube.com/@browserbase
- Instagram — https://www.instagram.com/browserbase
- Privacy Policy — /privacy-policy
- Terms of Service — /terms-of-service
- Twitter — https://x.com/browserbase
- Linkedin — https://www.linkedin.com/company/browserbasehq/
- Youtube — https://www.youtube.com/@browserbase
- Instagram — https://www.instagram.com/browserbase
- Privacy Policy — /privacy-policy
- Terms of Service — /terms-of-service

## Related: Agent Skills
URL: https://agentskills.io/home
Title: Agent Skills Overview - Agent Skills

### Extracted text

Agent Skills Overview - Agent SkillsSkip to main content
Agent Skills now has an officialDiscord server. See theannouncementfor details.
Agent Skillshome pageAgent SkillsSearch...⌘KAsk Assistant
agentskills/agentskills
agentskills/agentskills
Search...NavigationAgent Skills Overview
Overview
Specification
Client Showcase
For skill creators
Quickstart
Best practices
Optimizing descriptions
Evaluating skills
Using scripts
For client implementors
Adding skills support
On this page
What are Agent Skills?
Why Agent Skills?
How do Agent Skills work?
Where can I use Agent Skills?
Open development
Get started with Agent Skills
Agent Skills Overview
Copy page
A standardized way to give AI agents new capabilities and expertise.
Copy page
Documentation Index
Fetch the complete documentation index at:https://agentskills.io/llms.txt
Use this file to discover all available pages before exploring further.
​What are Agent Skills?
Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.At its core, a skill is a folder containing a
SKILL.md
file. This file includes metadata (
name
and
description
, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.
my-skill/├── SKILL.md          # Required: metadata + instructions├── scripts/          # Optional: executable code├── references/       # Optional: documentation├── assets/           # Optional: templates, resources└── ...               # Any additional files or directories
​Why Agent Skills?
Agents are increasingly capable, but often don’t have the context they need to do real work reliably. Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders that agents load on demand. This gives agents:
Domain expertise: Capture specialized knowledge — from legal review processes to data analysis pipelines to presentation formatting — as reusable instructions and resources.
Repeatable workflows: Turn multi-step tasks into consistent, auditable procedures.
Cross-product reuse: Build a skill once and use it across any skills-compatible agent.
​How do Agent Skills work?
Agents load skills throughprogressive disclosure, in three stages:
Discovery: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
Activation: When a task matches a skill’s description, the agent reads the full
SKILL.md
instructions into context.
Execution: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.
Full instructions load only when a task calls for them, so agents can keep many skills on hand with only a small context footprint.
​Where can I use Agent Skills?
Agent Skills are supported by a large number of AI tools and agentic clients — see theClient Showcaseto explore some of them!
​Open development
The Agent Skills format was originally developed byAnthropic, released as an open standard, and has been adopted by a growing number of agent products. The standard is open to contributions from the broader ecosystem.Come join the discussion onGitHuborDiscord!
​Get started with Agent Skills
Quickstart
Create your first Agent Skill and see it in action.
Specification
The complete format specification for Agent Skills.Specification⌘IAssistantResponses are generated using AI and may contain mistakes.

### Extracted links
- Discord server — https://discord.gg/MKPE9g8aUy
- announcement — https://github.com/agentskills/agentskills/discussions/273
- Agent Skills home page Agent Skills — /
- agentskills/agentskills — https://github.com/agentskills/agentskills
- agentskills/agentskills — https://github.com/agentskills/agentskills
- Overview — /home
- Specification — /specification
- Client Showcase — /clients
- Quickstart — /skill-creation/quickstart
- Best practices — /skill-creation/best-practices
- Optimizing descriptions — /skill-creation/optimizing-descriptions
- Evaluating skills — /skill-creation/evaluating-skills
- Using scripts — /skill-creation/using-scripts
- Adding skills support — /client-implementation/adding-skills-support
- https://agentskills.io/llms.txt — https://agentskills.io/llms.txt
- Client Showcase — /clients
- Anthropic — https://www.anthropic.com/
- GitHub — https://github.com/agentskills/agentskills
- Discord — https://discord.gg/MKPE9g8aUy
- Specification — /specification
