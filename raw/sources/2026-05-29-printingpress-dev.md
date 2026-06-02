---
source_url: https://printingpress.dev
ingested: 2026-05-29
ingested_by: agent-alpha
context: Historical Tolaria backfill item from ingestion ledger; first seen 2026-05-12T03:36:48.696314. Original request asked to visit printingpress.dev and summarize what it is, what problem it solves, and key features.
source_type: article
credibility_tier: primary
evidence_grade: medium
contradiction_notes: Product homepage and linked repos provide strong evidence of the project/catalog mechanics, but claims about quality, token savings, and generated tool effectiveness are not independently benchmarked here. Installation/adoption should be treated as supply-chain-sensitive.
---

# Printing Press — agent-native CLIs from a single prompt

Original URL: https://printingpress.dev
Canonical URL: https://printingpress.dev/
Browser title: Printing Press — agent-native CLIs from a single prompt

## Source text captured from homepage

Printing Press home
printingpress.dev
Search
GitHub:
CLI Printing Press · ★2.6k stars · Public Library · ★1.3k stars

NOW PRINTING · PL. A

Welcome to the Printing Press.
Print an agent-native CLI for any API, app, or site — from a single prompt. Or install one the community already made.

From an API spec, from a website with no public API, from a beloved community fan project - one prompt prints a token-efficient Go CLI, a Claude Code skill, an OpenClaw skill, and an MCP server. Peter Steinberger showed the way with discrawl and gogcli: a local SQLite mirror beats a remote API call, compound commands beat ten round trips, and an agent-native CLI beats raw HTTP. The press bakes that playbook into every binary it prints. Muscle memory for agents.

Every API has a secret identity.

Discord isn't just a chat app - it's a searchable knowledge base. Linear isn't just an issue tracker - it's a team behavior observatory. The Printing Press finds that secret and builds the CLI around it.

GET STARTED

Discover and install CLIs

Search the catalog, then install any CLI plus its agent skill — one or several at once.

npx -y @mvanhorn/printing-press-library search travel

Find tools by keyword or category. `list` shows the whole catalog.

npx -y @mvanhorn/printing-press-library install flight-goat booking-com

Install by name — one or several. Pulls the Go binary and the agent skill together. Requires Node.

npx -y @mvanhorn/printing-press-library --help

See every command — `list` for the whole catalog, `list --category travel` to filter, plus `update` and `uninstall`.

LET YOUR AGENT PICK — OPENCLAW & HERMES

Paste this to your OpenClaw or Hermes agent:

Go to printingpress.dev, follow the install instructions for the printing-press-library CLI, then — using everything you know about me and how I work — recommend which CLIs I should install, and install the ones I approve.

Build your own

Run the press to print a token-efficient CLI, agent skill, and MCP server for any API, website, or community project.

go install github.com/mvanhorn/cli-printing-press/v4/cmd/cli-printing-press@latest

Install the generator binary. Requires Go 1.26.3+, Claude Code, and Node.

npx skills add mvanhorn/cli-printing-press/skills --skill '*' -g -a claude-code -y

Install the press skills into Claude Code (Vercel's open-agent-skills CLI).

claude

Start Claude Code from any folder.

/printing-press <app or website>

Inside Claude Code — print a CLI for an API by name, or point it at a website. No spec needed.

PL. B · THE LIBRARY

The Library

Six magic moments. Browse the rest by category.

Auto-updates from the library repo when a README ships.

TRAVEL - FLIGHT-GOAT

Non-stop flights over 8 hours from SEA, Dec 24 to Jan 1, cheapest first.
$ /pp-flight-goat sea long-haul nonstop dec 24 to jan 1, 4 pax, cheapest first

Nonstop 8+ hour SEA round-trips, Dec 24 2026 to Jan 1 2027, 4 passengers, cheapest first.

Destination examples included London LHR, Amsterdam AMS, Tokyo Haneda HND, Paris CDG, Frankfurt FRA, Doha DOH, Dubai DXB, Seoul ICN, Taipei TPE, and Istanbul IST.

Two sources stitched into one query: Kayak nonstop search + sniffed Google Flights.

SPORTS + TRAVEL - ESPN X FLIGHT-GOAT

When does OKC play next, and what's the cheapest fly-in / next-morning-out?
$ /pp-espn nba okc round 2 game 1 + /pp-flight-goat sea-okc, fly-in same day

The setup: OKC just won Game 4 vs Phoenix, 131-122. Round 2 Game 1 is TBD on date and opponent. Best estimate for the next OKC home game: Sat May 9 or Sun May 10.

Pick: Wait 24-48h for ESPN to publish Round 2 Game 1, then book Southwest 1-stop for $437 RT (Wanna Get Away+ for refundable flexibility). Skip Frontier May 9 outbound; lands after tip.

Two CLIs, one Claude conversation. Live ESPN context picks the date; FlightGoat books the route.

MEDIA - MOVIE-GOAT

Kelly Van Horn's filmography, sorted by Rotten Tomatoes.
$ /pp-movie-goat person 'Kelly Van Horn' --sort rotten-tomatoes

Kelly Van Horn filmography sorted by Rotten Tomatoes - one CLI call, two source APIs (TMDb + OMDb). TMDb for the filmography, OMDb for the Rotten Tomatoes scores. One CLI joins them locally.

FOOD - RECIPE-GOAT

Find me the best chocolate cake.
$ /pp-recipe-goat find chocolate cake --rank trust --servings 8

Widget has scalable servings, ingredient links inside the steps, and timers - all from a single recipe-goat call.

Recipe-shaped output triggers Claude's cooking widget: scalable servings, in-step ingredient links, timers.

Open conversation →

PROJECT - LINEAR

Every blocked issue whose blocker has been stuck for a week.
$ /pp-linear sql 'blocked issues whose blocker hasn't moved in 7 days'
linear-pp-cli sql --compact <<SQL
SELECT i.identifier, i.title, age(now(), b.updated_at) AS stuck
FROM issues i JOIN issue_relations r ON r.issue_id = i.id
JOIN issues b ON b.id = r.related_issue_id
WHERE r.type = 'blocked_by' AND b.state = 'in_progress'
AND b.updated_at < now() - interval '7 days';
SQL
ENG-412 Crash on cold-start · blocked 11d
ENG-388 Reconnect dropped sockets · blocked 9d
ENG-301 Backfill missing rows · blocked 8d

50ms against the local SQLite mirror. Compound queries the Linear API can’t answer.

CRM - CONTACT-GOAT

Find a verified email for a person you've never met.
$ /pp-contact-goat 'Jane Doe' company:Acme --use deepline
1 Look up on LinkedIn
2 Cross-check Happenstance for warm intros
3 Pay Deepline for the verified email

Magic-moment recording in flight. The CLI ships today; the type-specimen page lands when the screen recording does.

SEARCH THE LIBRARY
Search
BROWSE BY CATEGORY

17 categories: AI, Cloud, Commerce, Developer Tools, Devices, Education, Food and Dining, Marketing, Media and Entertainment, Monitoring, Other, Payments, Productivity, Project Management, Sales and CRM, Social and Messaging, Travel.

Built by Matt Van Horn & Trevin Chow

CLI Printing Press · Public Library

## Links extracted from homepage

- https://printingpress.dev/ — Printing Press home
- https://printingpress.dev/search — Search
- https://github.com/mvanhorn/cli-printing-press — CLI Printing Press repo
- https://github.com/mvanhorn/printing-press-library — Public Library repo
- https://claude.ai/share/c7c79da5-abcf-444c-b54d-80dfb31c2fe6 — Claude share demo from recipe-goat card
- https://printingpress.dev/library/ai — AI category
- https://printingpress.dev/library/cloud — Cloud category
- https://printingpress.dev/library/commerce — Commerce category
- https://printingpress.dev/library/developer-tools — Developer Tools category
- https://printingpress.dev/library/devices — Devices category
- https://printingpress.dev/library/education — Education category
- https://printingpress.dev/library/food-and-dining — Food and Dining category
- https://printingpress.dev/library/marketing — Marketing category
- https://printingpress.dev/library/media-and-entertainment — Media and Entertainment category
- https://printingpress.dev/library/monitoring — Monitoring category
- https://printingpress.dev/library/other — Other category
- https://printingpress.dev/library/payments — Payments category
- https://printingpress.dev/library/productivity — Productivity category
- https://printingpress.dev/library/project-management — Project Management category
- https://printingpress.dev/library/sales-and-crm — Sales and CRM category
- https://printingpress.dev/library/social-and-messaging — Social and Messaging category
- https://printingpress.dev/library/travel — Travel category
- https://x.com/mvanhorn — Matt Van Horn
- https://x.com/trevin — Trevin Chow

## Linked-source inspection notes

### https://github.com/mvanhorn/cli-printing-press

What it is: Go-based generator/orchestrator for producing agent-native CLIs and MCP servers for APIs or websites. It claims to generate Go/Cobra CLIs, MCP servers, Claude Code/Open Agent skills, research/proof/score artifacts, and workflows for APIs with or without public specs.

Technical mechanism observed: Go module github.com/mvanhorn/cli-printing-press/v4; commands include cli-printing-press, printing-press, press-auth, and manifest-gen. Internal packages indicate OpenAPI/GraphQL/spec handling, browser sniffing, discovery, pipeline, CLI/MCP descriptors, auth doctor, and LLM polish. Skills exist for printing-press, reprint, polish, publish, score, catalog, import, amend, and retro. docs/PIPELINE.md documents a 9-phase managed path: preflight, research, scaffold, enrich, regenerate, review, agent-readiness, comparative, ship. Quality gates described include go mod tidy, govulncheck, go vet, go build, --help, version, doctor, dogfood, runtime verification, scorecard, MCP surface parity, and agent-readiness review.

Why it matters: Directly relevant to Hermes tool orchestration and agent-engineering because it treats CLIs/MCP servers as agent-optimized interfaces, emphasizes compact output, typed exit codes, dry-run, local SQLite/FTS5 stores, compound commands, and generated skills.

Evidence/actionability: Strong source evidence for repo existence, structure, skills, and docs; medium evidence for quality/effectiveness claims because no generator run or independent benchmark was performed. High value for knowledge ingestion; adoption/prototyping should be explicitly approved and sandboxed.

### https://github.com/mvanhorn/printing-press-library

What it is: Public catalog and installer repo for Printing Press-generated agent-oriented CLIs and focused skills. README describes it as the catalog of CLIs already printed and ready to install, with 198 CLIs across 17 categories.

Technical mechanism observed: npm package @mvanhorn/printing-press-library, Node >=20, binary printing-press-library. Default registry URL is raw GitHub registry.json. Installer fetches registry, resolves slugs/names/bundles, computes binary names, runs go install for the selected CLI, and installs matching skills using npx skills@latest add mvanhorn/printing-press-library/cli-skills/<skill> -g -y. Discovery supports list/search/category/installed/update/uninstall and --json. Repo contains library/<category>/<tool>, focused skills under cli-skills/pp-<tool>, manifests/specs/MCP metadata. Registry had 198 entries; 180/198 entries had MCP metadata, 162 full and 18 partial at inspection time.

Why it matters: More concrete source of record than the homepage for the installable catalog. Useful for Tolaria as a normalized source of agent tool/skill candidates, MCP readiness, authentication requirements, categories, install semantics, and supply-chain cautions.

Evidence/actionability: A- for catalog structure/mechanism from README, registry, npm source, and sample manifest; medium for direct installation/use because no installer or generated binaries were run. High for Tolaria catalog ingestion; avoid automatic installation without audit/pinning/sandboxing.

### https://claude.ai/share/c7c79da5-abcf-444c-b54d-80dfb31c2fe6

Direct browser access hit Cloudflare security verification. A readable rendering was available through Jina Reader during triage.

What it appears to contain: Claude shared conversation/output titled around an Ultimate Chocolate Cake, recipe-shaped answer sourced from BBC Good Food, with ingredients, steps, servings, notes/nutrition/tips, and source link https://www.bbcgoodfood.com/recipes/ultimate-chocolate-cake.

Why it matters: Supporting demo artifact for the homepage's recipe-goat claim that structured recipe output can trigger Claude's cooking widget with scalable servings, ingredient links, and timers. It is not primary evidence for Printing Press architecture.

Evidence/actionability: C+; useful only as supporting demo context, not as a standalone Tolaria workstream.

## Ingestion classification

source_type: article/product homepage with linked primary repos
credibility_tier: primary for project self-description and repos; marketing claims still require skepticism
evidence_grade: medium overall; linked library repo mechanism A-, generator repo mechanism B/B-, product efficacy claims unbenchmarked
contradiction_notes: Homepage says one prompt prints token-efficient Go CLI, Claude Code skill, OpenClaw skill, and MCP server; repos show corresponding structures and workflows but no independent proof here that output quality, token efficiency, or broad website/API coverage matches claims. Installation paths have supply-chain/security implications due to npx, go install @latest, global skill install, and third-party API wrappers.

Potential Tolaria workstream: promote this historical source into a source note and synthesize Printing Press as an agent-native CLI/MCP generation/catalog pattern for Hermes/Tolaria, with explicit supply-chain cautions and no implementation without approval.
