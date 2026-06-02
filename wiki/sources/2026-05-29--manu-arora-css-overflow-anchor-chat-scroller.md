---
type: source
source_path: raw/sources/2026-05-29-x-mannupaaji-overflow-anchor-chat-scroller.md
title: "X post by Manu Arora: CSS overflow-anchor chat scroller"
author: "Manu Arora"
date: 2026-05-11
tags: [css, web-ui, scroll-behavior, weak-social]
created: 2026-05-29
updated: 2026-05-29
---

# X post by Manu Arora: CSS overflow-anchor chat scroller

## Summary
This weak social source claims that a chat scroller can be pinned to the bottom with CSS `overflow-anchor` by disabling scroll anchoring on all children and re-enabling it on a 1px anchor at the end of the scroller. The raw capture includes source-check notes against MDN and the CSS Scroll Anchoring Module draft: the underlying property, `auto`/`none` values, and default scroll anchoring behavior are real web-platform mechanisms. The exact chat-autoscroll recipe remains a practitioner pattern rather than a browser-documented implementation recipe. The useful Tolaria takeaway is a CSS-first autoscroll pattern with serious caveats: Safari support is absent/limited in the captured MDN compatibility view, user-intent handling must avoid forcing a reader back to the bottom, and production UIs still need fallbacks for unsupported browsers and edge cases.

## Key Claims
1. A chat or log scroller can be made to follow new content by placing a 1px anchor at the bottom and setting it as the only eligible scroll anchor.
2. The recipe is `#scroller * { overflow-anchor: none; }` plus `#anchor { overflow-anchor: auto; height: 1px; }` after the message list.
3. Browser scroll anchoring runs by default in supporting browsers to reduce layout shifts.
4. MDN and CSSWG support the underlying `overflow-anchor` mechanism, but not the full operational claim that this is sufficient for every chat UI.
5. Browser compatibility and user-scroll behavior are the main adoption risks: Safari support was not available in the captured MDN banner, and a chat UI should not override a user who intentionally scrolled upward.

## Notable Quotes
- Tweet text: "You can pin a chat scroller to the bottom with CSS `overflow-anchor`, without having to use MutationObserver or `scrollTo()` functions."
- Tweet text: "Disable it on children, re-enable it on a 1px anchor at the end and the scroll follows new content down on its own."
- Raw source-check note: "MDN marks the property as limited availability, with Chrome/Edge/Firefox support and Safari lacking support in the visible compatibility banner at capture time."
- Raw source-check note: "CSSWG draft confirms the exclusion/anchor mechanism at spec level: if a scrolling box has `overflow-anchor: none`, an anchor node is not selected for that scroller; candidate anchor nodes are chosen from viable DOM nodes unless excluded."

## Entities Mentioned
- No entity page created. The author, MDN, and CSSWG are provenance/supporting context for this source, but the knowledge payload is the web-platform pattern rather than a durable Tolaria entity.

## Concepts Mentioned
- [[CSS Scroll Anchoring Chat Autoscroll Pattern]]
- [[Adaptive UI Generation]]
- [[Artifact Review Surface]]

## Follow-ups
- Do not adopt the tweet as proof that CSS-only chat autoscroll is production-ready.
- If Hermes/Tolaria later needs chat/log autoscroll behavior, require an approved compatibility and UX check: supporting-browser behavior, Safari fallback, initial-scroll behavior, resize/image-load behavior, and a guard that respects users who scroll away from the bottom.
- The current source is useful enough for Tolaria knowledge, but not strong enough by itself to justify implementation work.
