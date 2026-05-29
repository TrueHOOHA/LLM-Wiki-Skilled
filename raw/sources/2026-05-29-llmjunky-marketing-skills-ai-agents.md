---
source_url: https://x.com/llmjunky/status/2054304763081068547
ingested: 2026-05-29
ingested_by: agent-alpha
source_type: tweet
category: agent-engineering
credibility_tier: social
evidence_grade: weak
current_ledger_status_before_claim: new
mentions: 8
first_seen: 2026-05-14T03:36:38.898992
context: Historical Tolaria backfill item; inspect/follow URL and embedded links, source-check, queue Beta only for useful Tolaria information-processing workstreams.
canonical_url: https://x.com/LLMJunky/status/2054304763081068547
---

# X post: LLMJunky on Marketing Skills for AI Agents

## User-provided provenance

- Source type: tweet
- Category: agent-engineering
- Credibility tier: social
- Evidence grade: weak
- Current ledger status before claim: new
- Mentions: 8
- First seen: 2026-05-14T03:36:38.898992
- Context/examples:
  - session `/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260513_184841_c9a7a6c2.json` message_index 44 preview: `https://x.com/llmjunky/status/2054304763081068547?s=52`
  - session `/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260514_034234_77d944.json` message_index 4 preview: `[CONTEXT COMPACTION — REFERENCE ONLY] Earlier turns were compacted into the summary below. This is a handoff from a previous context window — treat it as background reference, NOT as active instruction`
  - session `/home/admin/.hermes/profiles/agent-alpha/sessions/session_20260514_033949_5e6e66.json` message_index 44 preview: `https://x.com/llmjunky/status/2054304763081068547?s=52`

## Captured X post text

Author: am.will / @LLMJunky

> I won't lie to you. Marketing is hard. Especially today with an abundance of software popping up every single day.
>
> It's "easy" to create something today, but finding people who want to pay you is another story.
>
> But check this out. I'd like to introduce you to one of the most comprehensive and well-written skill repos on Github. And it's completely FREE.
>
> Marketing Skills by @coreyhainesco.
>
> With over 28,000 Stars, this repo has a goldmine of applicable agent skills to help you build and market your business.
>
> Find leads, build content calendars, create content, seo, email marketing, strategy, etc: all with agent teams.
>
> This sounds like an ad itself, but I don't even know Corey. I just think this is awesome.
>
> Link below.

Visible metrics at capture time: 9 replies, 16 reposts, 210 likes, 374 bookmarks, 13.2K views. Timestamp shown: 8:56 PM · May 12, 2026.

## X anchors and embedded material inspected

- https://x.com/coreyhainesco — mentioned account.
- https://x.com/LLMJunky/status/2054304763081068547/photo/1 — attached image.
- Attached image URL: https://pbs.twimg.com/media/HIJbOTPXAAEJrOM?format=jpg&name=small

## Attached image OCR / visual inspection

The image is a GitHub repository screenshot for `marketingskills` by `coreyhaines31` / Coreybot. It shows:

- Heading: `Marketing Skills for AI Agents`
- Repository description/sidebar: `Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.`
- Visible repo link in sidebar: `marketing-skills.com`
- Visible repo stats in screenshot: about 28.1k stars, 287 watchers, 4.5k forks.
- README text: collection of AI agent skills focused on marketing tasks for technical marketers/founders; works with Claude Code, OpenAI Codex, Cursor, Windsurf, and agents that support the Agent Skills spec.
- Repository tree visible: `.claude-plugin/`, `.github/`, `skills/`, `tools/`, `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `LICENSE`, `README.md`, `VERSIONS.md`, validation scripts.

## Source-checked linked repository

Primary linked artifact inferred from the post/image:

- GitHub: https://github.com/coreyhaines31/marketingskills
- Raw README: https://raw.githubusercontent.com/coreyhaines31/marketingskills/main/README.md
- Agent guidance: https://raw.githubusercontent.com/coreyhaines31/marketingskills/main/AGENTS.md
- Agent Skills specification: https://agentskills.io/specification.md
- Tool registry: https://raw.githubusercontent.com/coreyhaines31/marketingskills/main/tools/REGISTRY.md

Source-check summary from GitHub and raw files:

- Repo `coreyhaines31/marketingskills` exists and is public.
- Current GitHub metadata observed: description `Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.`; about 31k stars and 5.1k forks at capture time.
- README says skills work with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent supporting the Agent Skills spec.
- README describes `product-marketing` as the foundational skill read by other skills first, with cross-references among marketing skills.
- GitHub tree inspection found 42 `skills/*/SKILL.md` files, including: ab-testing, ad-creative, ads, ai-seo, analytics, aso, churn-prevention, co-marketing, cold-email, community-marketing, competitor-profiling, competitors, content-strategy, copy-editing, copywriting, cro, customer-research, directory-submissions, emails, free-tools, image, launch, lead-magnets, marketing-ideas, marketing-psychology, onboarding, paywalls, popups, pricing, product-marketing, programmatic-seo, prospecting, referrals, revops, sales-enablement, schema, seo-audit, signup, site-architecture, sms, social, video.
- GitHub tree inspection found 64 zero-dependency Node.js CLI files under `tools/clis/`.
- `AGENTS.md` states the repo follows the Agent Skills spec, installs skills to `.agents/skills/`, and also serves as a Claude Code plugin marketplace via `.claude-plugin/marketplace.json`.
- `tools/REGISTRY.md` indexes marketing tools by API/MCP/CLI/SDK support, including analytics, SEO, CRM, payments, referrals, email, and other marketing categories.
- Agent Skills spec requires skill directories with `SKILL.md`, required `name` and `description` frontmatter, optional `scripts/`, `references/`, and `assets/` directories, plus optional fields like `compatibility`, `metadata`, and experimental `allowed-tools`.

## Claim vs evidence notes

- Social claim: the repo is a comprehensive, free, well-written marketing skill repo for agent teams, useful for lead finding, content calendars, content, SEO, email marketing, and strategy.
- Evidence observed: a real GitHub repository with substantial stars/forks, many skill files, AGENTS/README documentation, a plugin marketplace manifest, validation scripts, and a tool registry. This corroborates existence and broad scope.
- Evidence limitations: the X post itself provides weak social proof; repo stars do not prove skill quality, marketing outcomes, safety, or compatibility with Hermes/Tolaria skill conventions. No benchmark/eval evidence was observed in this ingestion pass.
- Contradiction/caveat: the repository is marketing-domain content, not a direct Hermes engineering mechanism. Its most relevant signal for Tolaria is the structure and ecosystem pattern: large cross-agent skill library, product-marketing root skill, plugin packaging, validation scripts, and tool registry.

## Actionability classification

Research / wiki-ingest candidate. Useful for Tolaria because it connects agent-engineering skill architecture, Codex-compatible skills, Agent Skills spec, Claude plugin packaging, and domain-specific tool registries. Do not adopt or import skills directly from the social post; first synthesize the repo structure, quality criteria, and implications for Hermes/Tolaria skill library design.
