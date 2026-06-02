---
source_url: https://x.com/rsalimx/status/2056453084444807423
canonical_url: https://x.com/rsalimx/status/2056453084444807423
source_type: tweet
credibility_tier: social
evidence_grade: weak
ingested: 2026-05-29
ingested_by: agent-alpha
context: Historical Tolaria backfill item from ingestion ledger; first seen 2026-05-20; mentions 6; category uncategorized.
---

# rsalimx X post — TikTok slideshow growth system claim

## Source metadata

- Original URL: https://x.com/rsalimx/status/2056453084444807423
- Canonical URL: https://x.com/rsalimx/status/2056453084444807423
- Author: Salim / @rsalimx
- Created at: Mon May 18 19:13:17 +0000 2026
- Source type: tweet
- Credibility tier: social
- Evidence grade: weak
- First seen in Alpha audit: 2026-05-20T03:35:54.768167
- Mentions in ledger: 6
- Historical examples:
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260519_185958_08883d77.json message_index 15
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260519_222349_b806d9.json message_index 15
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260519_171315_d12d195d.json message_index 0

## Access notes

- Direct browser render of X showed an age-restricted/login-gated notice and did not expose the post body.
- `cdn.syndication.twimg.com/tweet-result` returned an empty JSON object.
- `api.fxtwitter.com` and `api.vxtwitter.com` exposed the public tweet metadata, text, and attached image URL.
- No external embedded links were exposed by the accessible API payloads. The only facet was the attached image/media URL.

## Captured tweet text

> Most consumer app founders are burning $4-8 CPIs on meta and praying their tiktok influencer deal pulls more than 50 installs.
>
> meanwhile, a quieter group is driving installs through tiktok slideshows at a fraction of the cost.
>
> ~$0/month stack.
>
> Here's the full system 🧵

Raw text included media facet:

> https://t.co/TMyfkxyyQN → https://x.com/rsalimx/status/2056453084444807423/photo/1

## Captured metrics from accessible mirrors

From `api.fxtwitter.com` / `api.vxtwitter.com` at ingestion time:

- Replies: 6
- Retweets: 14
- Likes: 280
- Bookmarks: 676
- Quotes: 3
- Views: approximately 23,859
- Language: English
- Media: one image
- Possibly sensitive: false in mirror payload, despite logged-out browser showing an X age-restricted notice

## Attached image

Image URL:

- https://pbs.twimg.com/media/HIn3clBXcAAPD_S.jpg?name=orig

The image is a collage of TikTok-style slideshow/video thumbnails with lifestyle/beach imagery, high-view counts, and hook-first text overlays. It appears to illustrate the type of slideshow creative the post claims can drive cheap consumer-app installs.

Visible text examples include:

- “5 bizarre life hacks my boyfriends mom taught me” / “pt 3” / “(she lived with buddhist monks for 10 years)” / “^^her in brazil at 26, 1980” — 1.8M views
- “5 of the most bizarre life hacks i stole from my mom” — 1.2M views
- “5 unhinged nervous system hacks my best friend’s mom taught me” / “(she lived with buddhist monks)” — 1.1M views
- “5 physical things you didn’t realize were symptoms of serious burnout” / “(and you need to slow down)” — 1.3M views
- “things i do to (actually) fill my cup” / “(these changed my life overnight)” — 585.5K views
- “5 unhinged ways I stayed detached during no contact” — 375.9K views
- “5 lies avoidants tell to end relationships (and what they really mean)” — 748.9K views
- “5 more unhinged ways i stay (healthily) detached in a relationship” — 329.9K views
- “5 bizarre life hacks my boyfriend’s dad taught me” / “(he lived with buddhist monks for a decade)” — 386.2K views
- “5 physical things i didn’t realize were symptoms of depression (until it was too late)” — 540.9K views
- “5 bizarre ways my mom became 95% stress free” — 189.2K views
- Additional examples reference anxiety, leaving him, signs a man is in love, and nervous-system hacks.

No URLs or tool names are visible in the image.

## Triage

- Claim: Consumer app founders can drive installs through TikTok slideshow creatives at a fraction of paid Meta CPI / influencer cost, using an approximately free stack.
- Evidence actually captured: one social post plus a collage of high-view slideshow thumbnails. No attribution, funnel screenshots, install analytics, CPI calculations, case study, reproducible stack, or full thread replies were accessible from the available sources.
- Contradiction notes / caveats: The post promises a “full system” thread, but only the root post and attached image were accessible through mirrors. The view counts shown on example slideshow thumbnails are not evidence of app installs or low CPI.
- Actionability: archive-only for Tolaria. The idea is a marketing-growth hypothesis, not a source-backed Hermes/agent-engineering workstream. Could become read-later only if Overseer wants consumer-app growth tactics synthesized separately.

## Related links inspected

- https://x.com/rsalimx/status/2056453084444807423 — primary X post; browser showed age/login gate.
- https://api.fxtwitter.com/rsalimx/status/2056453084444807423 — accessible mirror with text/metadata/media.
- https://api.vxtwitter.com/rsalimx/status/2056453084444807423 — accessible mirror with text/metadata/media.
- https://pbs.twimg.com/media/HIn3clBXcAAPD_S.jpg?name=orig — attached image inspected visually/OCR.
- https://help.twitter.com/rules-and-policies/notices-on-twitter — X “Learn more” age-restriction link from browser gate; not payload-relevant.

## Decision

Archived to Tolaria raw. No agent-beta Kanban task queued.
