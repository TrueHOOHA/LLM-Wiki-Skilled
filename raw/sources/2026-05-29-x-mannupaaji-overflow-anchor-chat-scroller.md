---
source_url: https://x.com/mannupaaji/status/2053829832757407907
original_url: https://x.com/mannupaaji/status/2053829832757407907
source_type: tweet
ingested: 2026-05-29
ingested_by: agent-alpha
category: uncategorized
credibility_tier: social
evidence_grade: weak
first_seen: 2026-05-20T03:35:54.768167
mentions: 2
context: Historical Tolaria backfill from ingestion ledger; source-check tweet claim and embedded media/links when accessible.
---

# X post by Manu Arora: CSS overflow-anchor chat scroller

Canonical source: https://x.com/mannupaaji/status/2053829832757407907

Historical ledger previews:
- session /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260519_185958_08883d77.json message_index 73 preview: https://x.com/mannupaaji/status/2053829832757407907?s=52
- session /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260519_222349_b806d9.json message_index 73 preview: https://x.com/mannupaaji/status/2053829832757407907?s=52

## Captured tweet text

Author: Manu Arora (@mannupaaji)
Posted: 1:29 PM · May 11, 2026
Visible metrics at capture: 65.3K views; 11 replies; 93 reposts; 1.4K likes; 1.8K bookmarks.

> You can pin a chat scroller to the bottom with CSS `overflow-anchor`, without having to use MutationObserver or `scrollTo()` functions
>
> ```html
> <div id="scroller">
>   ...
>   ...
>   <div id="anchor"></div>
> </div>
> ```
>
> ```css
> #scroller * { overflow-anchor: none; }
> #anchor    { overflow-anchor: auto; height: 1px; }
> ```
>
> Browsers run scroll anchoring by default to prevent layout shifts
>
> Disable it on children, re-enable it on a 1px anchor at the end and the scroll follows new content down on its own

## Captured media

Video thumbnail URL discovered in page DOM:
- https://pbs.twimg.com/amplify_video_thumb/2053829781968625664/img/JuaXs7NNDN0yGvqu.jpg

Visible thumbnail content: a black demo slide comparing two chat scrollers. Left panel is labeled with a red X, "w/o overflow-anchor"; right panel is labeled with a green check, "w/ overflow-anchor". Both show the same small chat message list ("Hey! Are you free for a quick call?", "Sure, give me 5 minutes!", "Sounds good 👍"). This appears to demonstrate the claimed chat-scroll behavior, but the video itself was not downloaded in this ingestion pass.

## Embedded / adjacent links inspected

The tweet body exposed no outbound links beyond X-internal status/profile/hashtag links. The page's sidebar/profile bio exposed these adjacent links, but they are not evidence for the tweet's CSS claim:
- https://t.co/4eCBc4SSJt — profile bio link text `ui.aceternity.com`; not part of tweet body.
- https://t.co/NPJalHkrux — profile bio link text `aceternity.com`; not part of tweet body.
- https://x.com/aceternitylabs — profile bio mention; not part of tweet body.
- https://t.co/3OQiOSxJvC — profile bio link text `manuarora.link/yt`; not part of tweet body.

## Source-check notes

Primary/secondary references checked:
- MDN: https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-anchor
- CSS Scroll Anchoring Module Level 1 draft: https://drafts.csswg.org/css-scroll-anchoring-1/

MDN confirms:
- `overflow-anchor` lets authors opt out of browser scroll anchoring behavior, which adjusts scroll position to minimize content shifts.
- Scroll anchoring is enabled by default in supporting browsers.
- Syntax includes `overflow-anchor: auto;` and `overflow-anchor: none;`.
- `auto`: the element becomes a potential anchor when adjusting scroll position.
- `none`: the element will not be selected as a potential anchor.
- MDN marks the property as limited availability, with Chrome/Edge/Firefox support and Safari lacking support in the visible compatibility banner at capture time.

CSSWG draft confirms the exclusion/anchor mechanism at spec level: if a scrolling box has `overflow-anchor: none`, an anchor node is not selected for that scroller; candidate anchor nodes are chosen from viable DOM nodes unless excluded.

## Classification

source_type: tweet
credibility_tier: social
evidence_grade: weak for the tweet as evidence; medium/primary for the underlying CSS property documentation.
contradiction_notes: The general property behavior is supported by MDN/CSSWG, but the exact "chat scroller follows new content down" recipe is an undocumented social-practitioner pattern and may fail or require fallback in Safari and in edge cases where the user scrolls away from the bottom.

Actionability: useful Tolaria knowledge item / possible UI implementation proposal. Best downstream workstream is source-backed synthesis of the `overflow-anchor` chat-autoscroll pattern, browser-support caveats, and whether it should be proposed for Hermes/Tolaria chat/log UI surfaces. No direct implementation was performed by Alpha.
