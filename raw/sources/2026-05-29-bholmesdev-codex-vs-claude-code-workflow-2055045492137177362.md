---
source_url: https://x.com/bholmesdev/status/2055045492137177362
canonical_url: https://x.com/BHolmesDev/status/2055045492137177362
ingested: 2026-05-29
ingested_by: agent-alpha
source_type: tweet
category: uncategorized
credibility_tier: social
evidence_grade: weak
first_seen: 2026-05-15T14:59:38.170682
mentions_in_ledger: 7
context: Historical Tolaria backfill item; source-check tweet/video and queue only useful Tolaria information-processing work.
---

# Ben Holmes on Codex vs Claude Code workflow

## Source

- Original URL: https://x.com/bholmesdev/status/2055045492137177362
- Canonical URL: https://x.com/BHolmesDev/status/2055045492137177362
- Author shown by X: Ben Holmes / @BHolmesDev
- Posted: 10:00 PM · May 14, 2026
- Engagement visible at ingestion: 14 replies, 10 reposts, 289 likes, 444 bookmarks, 24.9K views
- Attached media: embedded video, browser reports duration about 95.5 seconds; visible X card sometimes showed 0:24 in screenshot metadata, but loaded video duration was ~1:35.
- Video poster: https://pbs.twimg.com/amplify_video_thumb/2054951436631326720/img/heiCKBcTVHimjzZZ.jpg
- Video HLS manifest observed after playback: https://video.twimg.com/amplify_video/2054951436631326720/pl/P2fqkI4Rb0ZsOeRs.m3u8?tag=27&v=bf0&variant_version=1

## User/backfill context

Historical Tolaria backfill item for ingestion. Source type: tweet. Category: uncategorized. Credibility tier: social. Evidence grade: weak. First seen: 2026-05-15T14:59:38.170682. Mentions in ledger: 7.

Preview/context examples provided by Overseer:

- https://x.com/bholmesdev/status/2055045492137177362?s=52 from /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_150009_7305a7.json message_index 56
- https://x.com/bholmesdev/status/2055045492137177362?s=52 from /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_150228_4ae84b.json message_index 56
- https://x.com/bholmesdev/status/2055045492137177362?s=52 from /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_044753_b094ad.json message_index 56

## Tweet text recovered from X

> You should use Codex differently than how you use Claude Code.
>
> I've found success with no plans and more involvement as an engineer. Here's a 1 min rundown of my process:

## Embedded links and related links inspected

The X page did not expose any outbound article, repo, paper, or documentation link. Browser anchor enumeration found only standard X links, the author profile, timestamp/analytics, signup/login/policy links, and a relevant-people link to @warpdotdev. The primary payload is the attached video.

xurl CLI was attempted for structured read access but returned a 401 Unauthorized response; browser/Camoufox extraction and video resource capture succeeded, so this was not treated as an operational blocker.

## Video thumbnail / visible UI

The video thumbnail shows a terminal-like UI running `codex --yolo` inside a project named `blank-slate`. Visible text in the terminal describes an implementation log about list item rendering, Slate schema/commands, Markdown serialization/deserialization, linting, and browser checks. A talking-head overlay appears in the lower-right.

## Machine transcript of video audio

Generated with local faster-whisper tiny model from the recovered video audio. Treat as approximate, but it is good enough for source-checking the claims.

[0.0-6.0] I would sum up the difference in how I used to prompt versus how I prompt with CodeX with this chart.

[6.0-11.0] So whenever I use Cloud Code, I would always start in planning mode, give a vague ask,

[11.0-16.0] and then let the research and discussion process drive us towards a good solution.

[16.0-20.0] Usually a step-by-step plan with different phases to implement.

[20.0-24.0] And then we might work through those step-by-step or jump to the working solution

[24.0-29.0] and work through edge cases and code quality through QA to get to something good.

[29.0-34.0] But when using CodeX, I found myself jumping to a bit more of an explicit workflow.

[34.0-36.0] First off, I don't use any modes.

[36.0-40.0] I just get a little bit more explicit with my requirements upfront.

[40.0-48.0] And then I let CodeX as bias towards research, guide us towards a pseudo plan that we get at the end of our chat discussions.

[48.0-53.0] Usually it'll go off and research the latest libraries and how my code-based works,

[53.0-58.0] so that we can reach a decision on what to build in chat without having a planning document as part of it.

[58.0-61.0] Although you could certainly ask it to write down as Markdown.

[61.0-66.0] I've also found that rather than jumping to a working solution that has edge cases,

[66.0-70.0] CodeX really thrives on just working sequentially through tasks,

[70.0-76.0] ideally with test driven development because once it knows its destination,

[76.0-79.0] it's able to get there with very high-quality code.

[79.0-83.0] So I'm a bit less ambitious with the scope of everything I ask it to build.

[83.0-86.0] I just ask it to kind of ramp through each of the steps.

[86.0-91.0] We queue a together or use playwright test or other means to test that work.

[91.0-96.0] And then we do some cleanup at the end before we pull request or merge a feature.

## Source-check notes

Claim layer:

- Codex should be used differently from Claude Code.
- The author's Codex workflow is: no special modes/planning mode, clearer requirements upfront, chat-driven research toward a pseudo-plan, sequential task execution, smaller scope, TDD when possible, Playwright/QA checks, cleanup before PR/merge.
- The author's Claude Code comparison is: planning mode, vaguer asks, research/discussion to reach a phased plan, then implementation and QA edge-case iteration.

Evidence layer:

- Evidence is a practitioner social post plus a short narrated screen recording. It is experiential and not backed by benchmark data, repo diffs, failure-rate comparisons, or reproducible metrics.
- The video does provide concrete operational heuristics rather than pure hype.
- No primary docs, repo, paper, or long-form writeup were linked from the post.

Contradiction/caveat notes:

- The transcript phrase "Cloud Code" appears to be a transcription error for "Claude Code".
- The source says "no plans" in the tweet, but the video still describes a chat-derived pseudo-plan and optionally writing it to Markdown; the stronger reading is "avoid a separate planning mode/document as the default," not "do no planning."
- Evidence grade remains weak/social. Treat this as a workflow hypothesis to compare against Overseer's Codex-local practice and Tolaria's existing Codex/agent-engineering notes, not as an adoption mandate.

## Classification

- source_type: tweet
- credibility_tier: social
- evidence_grade: weak
- actionability: useful Codex workflow hypothesis for Tolaria synthesis; not enough for implementation/prototype by itself.
- recommended route: queue one agent-beta knowledge task to promote/source-summarize the workflow hypothesis and compare it with existing Codex/Hermes practices.
