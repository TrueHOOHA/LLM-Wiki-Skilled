---
source_url: https://x.com/garrytan/status/2053127519872614419
canonical_url: https://x.com/garrytan/status/2053127519872614419
source_type: tweet
credibility_tier: social
evidence_grade: weak
ingested: 2026-05-29
ingested_by: agent-alpha
context: "Historical Tolaria backfill item from ledger; first_seen=2026-05-12T18:31:55.856664; mentions=4; category=uncategorized."
ledger_context:
  first_seen: 2026-05-12T18:31:55.856664
  mentions: 4
  category: uncategorized
  source_type: tweet
  credibility_tier: social
  evidence_grade: weak
---

# Garry Tan X Article - Meta-Meta-Prompting: The Secret to Making AI Agents Work

Original URL: https://x.com/garrytan/status/2053127519872614419
Canonical URL: https://x.com/garrytan/status/2053127519872614419
Article URL recovered from X DOM: https://x.com/garrytan/article/2053127519872614419
Captured: 2026-05-29 by agent-alpha

## Ledger Context

- source_type: tweet
- category: uncategorized
- credibility_tier: social
- evidence_grade: weak
- first_seen: 2026-05-12T18:31:55.856664
- mentions: 4
- surrounding list included:
  - https://x.com/omarsar0/status/2052850591584383177
  - https://x.com/anirudhbv_ce/status/2052532004919361958
  - https://x.com/sudoingx/status/2052794989881753743
  - https://x.com/deronin_/status/2... (truncated in ledger context)

## Extraction Notes

X rendered the article body unauthenticated via browser snapshot/body text. No attached image URLs were recovered via browser_get_images. Embedded links were enumerated from the DOM and inspected where useful. The strongest primary/repo-linked materials were GBrain, GBrain evals, GStack, OpenClaw, Hermes Agent, Anthropic prompt caching, Karpathy LLM Wiki, and the prior X article series.

## Embedded / Related Links Recovered

- https://x.com/garrytan/article/2053127519872614419 — X article route for the same source.
- https://x.com/garrytan/status/2042925773300908103 — prior series post: Fat Skills, Fat Code, Thin Harness.
- https://x.com/garrytan/status/2044479509874020852 — prior series post: Resolvers.
- https://x.com/garrytan/status/2045404377226285538 — prior series post: LOC Controversy.
- https://x.com/garrytan/status/2045798603059548364 — prior series post: Naked models are stupider.
- https://x.com/garrytan/status/2046876981711769720 — prior series post: skillify manifesto / agents not making same mistakes.
- https://github.com/garrytan/gbrain — claimed knowledge/brain infrastructure.
- https://github.com/garrytan/gstack — claimed coding skill framework.
- https://openclaw.ai/ — linked harness/runtime site.
- https://hermes-agent.nousresearch.com/ — linked Hermes Agent site.
- https://github.com/nicobailon/hermes-agent — linked repo in rendered DOM; inspection found it 404/stale, likely should be NousResearch/hermes-agent.
- https://github.com/anthropics/anthropic-cookbook/tree/main/misc/prompt_caching — rendered as Pi/prompt caching; current equivalent appears under Anthropic/Claude cookbooks as prompt_caching.ipynb.
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f — Karpathy LLM Wiki inspiration.
- https://github.com/garrytan/gbrain-evals — linked benchmark/evals repo.

## Captured Source Text

Garry Tan @garrytan
Meta-Meta-Prompting: The Secret to Making AI Agents Work
2:58 PM · May 9, 2026
Visible engagement at capture: 134 replies, 630 reposts, 3.6K likes, 11K bookmarks, 1.4M views.

People keep asking me why I am spending my nights coding til 2AM. I have a job and a big one, as CEO of Y Combinator. We help thousands of builders a year to create their dreams of building real startups with real revenue that grow fast.

In the last 5 months, AI made me a builder again. Late last year, the tools got good enough that I went back to building. Not toy projects. Real systems that compound. I want to show you, with specific examples, what personal AI actually looks like when you stop treating it as a chat window and start treating it as an operating system. And I give it away as open source and in articles like this because I want you to speed up with me.

This is part of a series: Fat Skills, Fat Code, Thin Harness introduced the core architecture. Resolvers covered the routing table for intelligence. The LOC Controversy was about how every technical person just multiplied themselves by 100x to 1000x. Naked models are stupider argued that the model is the engine, not the car. And the skillify manifesto explained why LangChain raised $160M and gave you a squat rack and dumbell set without a workout plan, and then gave you that workout plan you needed.

## The Book That Read Me Back

Last month I was reading Pema Chödrön's When Things Fall Apart. It's 162 pages, 22 chapters on Buddhist approaches to suffering, groundlessness, and letting go. A friend recommended it during a hard period.

I asked my AI to do a book mirror.

What that means concretely: The system extracted all 22 chapters of the book, and then, for each chapter, ran a sub-agent that did two things simultaneously: summarized the author's ideas, and then mapped every idea to my actual life. Not generic "this applies to leaders" pablum. Specific mapping. It knows my family history (immigrant parents, dad from Hong Kong and Singapore, mom from Burma). It knows my professional context (running YC, building open-source tools, mentoring thousands of founders). It knows what I've been reading, what I've been thinking about at 2am, what my therapists and I are working on.

The output was a 30,000-word brain page. Each chapter rendered as two columns: what Pema says, and how it maps to what I'm actually living through. The chapter on groundlessness connected to a specific founder conversation I'd had the week before. The chapter on fear mapped to patterns my therapist had identified. The chapter on letting go referenced a late-night session where I'd written about the creative freedom I'd found this year.

The whole thing took about 40 minutes. A $300/hour therapist reading this book and applying it to my life couldn't do this in 40 hours, because they don't have the full graph of my professional context, my reading history, my meeting notes, and my founder relationships all loaded and cross-referenceable.

I've done this with over 20 books now: Amplified (Dion Lim), Autobiography of Bertrand Russell, Designing Your Life, Drama of the Gifted Child, Finite and Infinite Games, Gift from the Sea (Lindbergh), Siddhartha (Hesse), Steppenwolf (Hesse), The Art of Doing Science and Engineering (Hamming), The Dream Machine, The Book on the Taboo Against Knowing Who You Are (Alan Watts), What Do You Care What Other People Think (Feynman), When Things Fall Apart (Pema Chodron), A Brief History of Everything (Ken Wilber), and more. Each one gets richer because the brain gets richer. The second mirror knew about the first. The twentieth knew about all nineteen.

## How Book-Mirror Got Better Through Iteration

The first book mirror I did was terrible. Version 1 had three factual errors about my family. It said my parents were divorced when they weren't. Said I grew up in Hong Kong when I was born in Canada. Basic stuff that could have damaged trust if I'd shared it.

So I added a mandatory fact-check step. Every mirror now runs cross-modal evaluation against known facts in the brain before it ships. Opus 4.7 1M catches precision errors. GPT-5.5 catches missing context. DeepSeek V4-Pro catches when something reads as generic.

Then I upgraded to deep retrieval with GBrain tool use. The original version was good at synthesis but weak on specificity. Version 3 does per-section brain searches. Every right-column entry cites actual brain pages. When the book talks about dealing with difficult conversations, it doesn't just synthesize general principles. It pulls from my actual meeting notes with specific founders who were having tough conversations with co-founders. Or that idea I had on a Thursday hanging out with my brother James. Or the IM chat I had with my college roommate when I was 19. It's uncanny.

This is what skillification (using /skillify in GBrain) means in practice. I took the first manual attempt, extracted the repeatable pattern, wrote a tested skill file with triggers and edge cases, and every fix compounded across all future book mirrors.

## Skills That Build Skills

Here's where it gets recursive, and where I think the biggest insight is.

The system that runs my life didn't exist as a monolith. It was assembled from skills. And those skills were themselves created by a skill.

Skillify is a meta-skill that creates new skills. When I encounter a workflow I'm going to repeat, I say "skillify this" and it examines what just happened, extracts the repeatable pattern, writes a tested skill file with triggers and edge cases, and registers it in the resolver. The book-mirror pipeline was skillified from the first time I did it manually. The meeting-prep workflow was skillified after I noticed I was doing the same steps before every call.

Skills compose. Book-mirror calls brain-ops for storage, enrich for context, cross-modal-eval for quality, and pdf-generation for output. Each skill is focused on one thing. They chain together to create complex workflows. When I improve one skill, every workflow that uses it gets better automatically. No more "forgot to mention this edge case in my prompt." The skill remembers.

## The Meeting That Prepped Itself

Demis Hassabis came to YC for a fireside chat. Sebastian Mallaby's biography of him had just come out.

I asked the system to prep me.

In under two minutes it pulled: Demis's full brain page (which had been accumulating for months from articles, podcast transcripts, and my own notes). His published beliefs about AGI timelines ("50% scaling, 50% innovation," thinks AGI is 5-10 years away). The Mallaby biography highlights. His stated research priorities (continual learning, world models, long-term memory). Cross-references to things I've said publicly about AI. Three demo scripts for showing the brain's multi-hop reasoning capability during the conversation. And a set of conversation hooks based on where our worldviews overlap and diverge.

This wasn't just a better Google search. This was preparation that used my accumulated context about Demis, my own positions, and the strategic goals for the conversation. The system prepped not just facts, but angles.

## What 100,000 Pages of Brain Looks Like

I maintain a structured knowledge base with about 100,000 pages. Every person I meet gets a page with a timeline, a state section (what's currently true), open threads, and a score. Every meeting gets a transcript, a structured summary, and something I call entity propagation: after every meeting, the system walks through every person and company mentioned and updates their brain pages with what was discussed. Every book I read gets a chapter-by-chapter mirror. Every article, podcast, and video I engage with gets ingested, tagged, and cross-referenced.

The schema is simple. Each page has: compiled truth at the top (the current best understanding), an append-only timeline below (events in chronological order), and raw data sidecars for source material. Think of it as a personal Wikipedia where every page is continuously updated by an AI that was at the meeting, read the email, watched the talk, and ingested the PDF.

Here's an example of how this compounds. I meet a founder at office hours. The system creates or updates their person page, their company page, cross-references the meeting notes, checks if I've met them before (and surfaces what we discussed last time), checks their application data, pulls their latest metrics, and identifies if any of my portfolio companies or contacts are relevant to their problem. By the time I walk into the next meeting with them, the system has a full context pack ready.

This is the difference between having a filing cabinet and having a nervous system. The filing cabinet stores things. The nervous system connects them, flags what's changed, and surfaces what's relevant to right now.

## The Architecture

Here's how it works. I think this is the right way to build personal AI, and I open-sourced the whole thing so you can build it yourself.

The harness is thin. OpenClaw is the runtime. It receives my messages, figures out which skill applies, and dispatches. A few thousand lines of routing logic. It doesn't know anything about books or meetings or founders. It just routes.

The skills are fat. Over 100 of them now, each a self-contained markdown file with detailed instructions for one specific task. You've already seen book-mirror and meeting-prep above. Here are a few more that ship with GBrain:

meeting-ingestion: After every meeting, it pulls the transcript, creates a structured summary, and then walks through every person and company mentioned and updates their brain pages with what was discussed. The meeting page is not the end product. The entity propagation back to every person and company page is the real value.

enrich: Give it a person's name. It pulls from five different sources, merges everything into a single brain page with career arc, contact info, meeting history, and relationship context. Cited sources on every claim.

media-ingest: Handles video, audio, PDF, screenshots, GitHub repos. Transcribes, extracts entities, files to the right brain location. I use this constantly for YouTube videos, podcasts, and voice memos.

perplexity-research: Brain-augmented web research. Searches the web via Perplexity, but before synthesizing, checks what the brain already knows so it can tell you what's actually new vs. what you've already captured.

I have dozens more I've built for my own work that I'll probably open source: email-triage, investor-update-ingest that detects portfolio updates in my email and extracts metrics into company pages, calendar-check for conflict detection and travel impossibility, and a whole journalistic research stack I use for civic work. Each skill encodes operational knowledge that would take a new human assistant months to learn. When someone asks how I "prompt" my AI, the answer is: I don't. The skills are the prompts.

The data is fat. 100,000 pages of structured knowledge in the brain repo. Every person, company, meeting, book, article, and idea I've engaged with, all linked, all searchable, all growing every day.

The code is fat. The code that feeds it (scripts for transcription, OCR, social media archival, calendar sync, API integrations) matters too, but the data is where the compound value lives. I run more than 100 crons per day that check all the things: social media, Slack, email, whatever I pay attention to, my OpenClaw/Hermes Agents look at for me too.

The models are interchangeable. I run Opus 4.7 1M for precision. GPT-5.5 for recall and exhaustive extraction. DeepSeek V4-Pro for creative work and third perspectives. Groq with Llamma for speed. The skill decides which model to call for which task. The harness doesn't care. When someone asks "which AI model is best," the answer is: wrong question. The model is just the engine. Everything else is the car.

## The 2am Builder and the Compounding System

People ask me about productivity. I don't think about it that way. What I think about is compounding.

Every meeting I take adds to the brain. Every book I read enriches the context for the next book. Every skill I build makes the next workflow faster. Every person page I update makes the next meeting prep sharper. The system today is 10x what it was two months ago, and two months from now it'll be 10x again.

When I'm still up at 2am coding (and I am, regularly, because AI gave me back the joy of building), I'm not just writing software. I'm adding to a system that gets better every hour. 100 cronjobs 24/7. The meeting ingestion runs automatically. The email triage runs every 10 minutes. The knowledge graph enriches itself from every conversation. The system processes daily transcripts and extracts patterns I missed in real time.

This is not a writing tool. It's not a search engine. It's not a chatbot. It's a second brain that actually works, not as a metaphor, but as a running system with 100,000 pages, 100+ skills, 15 cron jobs, and the accumulated context of every professional relationship, meeting, book, and idea I've engaged with in the last year.

I open-sourced the whole stack. GStack is the coding skill framework (87,000+ stars) that I used to build it. I still use it as a skill inside OpenClaw/Hermes Agent when the agent needs to code. There's a great programmable browser (both headed and headless) in there. GBrain is the knowledge infrastructure. OpenClaw and Hermes Agent are the harnesses, you should choose but I usually do both. The data repos are on GitHub.

The thesis is simple: the future belongs to individuals who build compounding AI systems, not to individuals who use corporate-owned centralized AI tools. The difference is the difference between keeping a journal and having a nervous system.

## How to Start

If you want to build this:

Pick a harness. OpenClaw, Hermes Agent, or build your own from scratch with Pi. Keep it thin. The harness is just the router. Host it on your spare computer at home with Tailscale, or use Render or Railway in the cloud.

Start a brain with GBrain. I got inspired by Karpathy's LLM Wiki, implemented it in OpenClaw, and extended it into GBrain. It's the best retrieval system I've benchmarked (97.6% recall on LongMemEval, beating MemPalace with no LLM in the retrieval loop) and it ships 39 installable skills including everything described in this article. One command to install. A git repo where every person, meeting, article, and idea gets a page.

Do something interesting. Don't start by planning your skill architecture. Start by doing a thing. Write a report. Research a person. Download a season of NBA scores and build a prediction model for your sports bets. Analyze your portfolio. Whatever you actually care about. Do it with your agent, iterate until it's good, and then run Skillify (the meta-skill from earlier) to extract the pattern into a reusable skill. Then run check_resolvable to verify the new skill is wired into the resolver. That loop turns one-off work into compounding infrastructure.

Keep using it and look at the output. The skill will be mediocre at first. That's the point. Use it, read what it produces, and when something is off, run cross-modal eval: send the output through multiple models and have them score each other on the dimensions you care about. That's how I caught the factual errors in book-mirror. The fix got baked into the skill, and every mirror since has been clean. In six months you'll have something no chatbot can replicate, because the value isn't in the model. It's in what you've taught the system about your specific life, work, and judgment.

The first thing I built with this system was terrible. The hundredth was something I'd trust with my calendar, my inbox, my meeting prep, and my reading list. The system learned. I learned. The compound curve is real.

Fat skills. Fat code. Thin harness. The LLM on its own is just an engine. You can build your own car.

Everything I described here, all the skills, the book mirror pipeline, the cross-modal eval framework, the skillify loop, the resolver architecture, plus 30+ installable skillpacks, is open source and free on GitHub: github.com/garrytan/gbrain. Go build.

## Linked-source Inspection Summary

### GBrain / GBrain evals

- GBrain is a TypeScript/Bun markdown-backed personal/company brain layer with PGLite/Postgres indexing, hybrid retrieval, graph/backlink boosts, MCP tools, skills, ingestion recipes, cron/dream-cycle maintenance, and synthesis commands.
- Public docs strongly support the thin-harness/fat-skills/fat-data philosophy, markdown SKILL.md usage, skillify, book-mirror, meeting-ingestion, entity propagation, and a benchmark/eval culture.
- Production scale claims such as 100k+ pages are self-reported; private production brain is not independently verifiable from the public repo.
- GBrain-evals provides benchmark artifacts. Reported examples include gbrain-hybrid 97.60% R@5 on LongMemEval_s and BrainBench hybrid+graph R@5 near 97.9%; caveat: retrieval recall, synthetic/rich-prose datasets, not end-to-end QA proof.
- Actionable Tolaria idea: use GBrain as a reference architecture for compiled-truth + append-only timeline, entity propagation, skill contracts, retrieval evals, brain-first lookup, cross-model review receipts, and graph-aware retrieval tests.

### GStack / OpenClaw / Hermes Agent

- GStack is a prompt/skill framework for coding agents with host adapters for Claude, Codex, OpenCode, OpenClaw, Hermes, GBrain, etc. Hermes/OpenClaw integration is largely generated methodology/prompt artifacts rather than deep runtime code.
- OpenClaw is a local-first assistant/gateway with provider/model/runtime/channel separation, WebSocket/HTTP gateway, messaging integrations, agent runtimes, skills, and ACP-style harness support. It supports the architecture comparison but is not literally “thin” as a full platform.
- The linked GitHub repo `github.com/nicobailon/hermes-agent` returned 404/stale during inspection. Correct active Hermes Agent repo appears to be NousResearch/hermes-agent, with docs at https://hermes-agent.nousresearch.com/.
- Parent claims that models are interchangeable and skills can be routed by harnesses are directionally supported. The “thin harness” phrasing is better interpreted as model-agnostic orchestration over providers/tools/skills, not a tiny codebase.

### Anthropic prompt caching / Karpathy LLM Wiki / prior series posts

- Anthropic prompt caching is a primary-source, high-evidence mechanism for repeated large contexts: cache writes, cache reads, explicit breakpoints, 5-minute default TTL, optional 1-hour TTL, and speculative cache warming. Useful for repeated Tolaria/project context operations.
- Karpathy LLM Wiki is a medium-evidence design pattern: raw immutable sources, LLM-maintained wiki, schema file, ingest/query/lint workflows, index/log, entity/concept/source/synthesis pages.
- The prior series posts add concrete concepts:
  - Thin Harness, Fat Skills: skill files, harness, resolvers, deterministic code, subagents/structured memory, context minimization.
  - Resolvers: routing tables for skills/filing/context; trigger evals, reachability audits, dark-skill prevention, filing rules.
  - LOC controversy: quality-adjusted productivity metrics instead of raw volume metrics.
  - Naked models are stupider: evaluate the full system (model + harness + tools + skills + verification), route deterministic work out of latent space.
  - Skillify manifesto: every repeated failure becomes a skill contract, tests, resolver trigger/eval, smoke test, and filing rule.

## Actionability Classification

Classification: wiki-ingest / synthesis-proposal.

Rationale:
- This is directly relevant to Overseer's current interests: Hermes, Alpha/Beta, skills, memory, kanban/tool orchestration, Tolaria, LLM-Wiki-Skilled, Codex/GPT/harness workflows.
- The primary X source is social/weak and includes large self-reported productivity claims, but many linked artifacts provide concrete repositories/docs/evals that deserve source-backed Tolaria synthesis.
- Recommended action is not implementation. Recommended action is Beta information-processing: promote this source and linked evidence into Tolaria, separate claims from evidence, and prepare a knowledge note / approval proposal around a Tolaria compounding-knowledge pilot and evaluation plan.

## Contradictions / Caveats

- Social headline claims are evidence-weak; repo docs/evals support mechanisms, not all production-scale claims.
- GBrain production page counts and personal workflow outcomes are self-reported.
- GBrain-evals support retrieval recall claims more than end-to-end answer quality.
- OpenClaw/Hermes are model/runtime/tool orchestration platforms; calling them “thin” is conceptually useful but technically imprecise.
- The rendered Hermes GitHub link `github.com/nicobailon/hermes-agent` was stale/404; docs and local origin indicate NousResearch/hermes-agent is the active source.
- Anthropic prompt-caching docs are primary and high-confidence, but benchmark/cost effects must be measured on Tolaria workloads.
