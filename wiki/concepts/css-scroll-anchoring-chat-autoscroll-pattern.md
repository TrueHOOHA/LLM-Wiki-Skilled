---
type: concept
aliases: ["overflow-anchor chat autoscroll", "CSS-only chat autoscroll", "scroll anchoring bottom sentinel", "chat scroller bottom anchor"]
tags: [css, web-ui, scroll-behavior, design-pattern]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# CSS Scroll Anchoring Chat Autoscroll Pattern

## Definition
CSS Scroll Anchoring Chat Autoscroll Pattern is a CSS-first technique for keeping a chat, console, or append-only log viewport near its bottom by making a tiny end-of-list element the only eligible scroll anchor. The captured recipe disables `overflow-anchor` for scroller descendants and re-enables it on a 1px bottom sentinel, so supporting browsers may preserve the bottom anchor as new content is inserted.

## Scope
This concept covers append-only message/log surfaces where new content arrives below existing content and the intended default behavior is to remain at the latest item. It is most relevant when the user is already at or near the bottom and the UI wants to avoid JavaScript-only `MutationObserver` or `scrollTo()` loops. It does not cover virtualized lists, reverse-column layouts, pagination above the viewport, unread markers, media that changes height after load, or accessibility announcements by itself.

## Contrasts
- Versus imperative autoscroll: JavaScript `scrollTo()` or observer loops can explicitly detect bottom proximity, unsupported browsers, and user intent, but add code paths and timing bugs.
- Versus CSS scroll anchoring: the pattern repurposes the browser's layout-shift mitigation mechanism; it is not a chat-specific API.
- Versus forced-bottom chat: a good chat UI should respect a reader who intentionally scrolled upward, whereas an unconditional bottom-follow behavior can make older messages unreadable.
- Versus virtualization/windowing: virtualized chat lists may need explicit list-state management because DOM node recycling and dynamic heights can change anchor selection.

## Evidence
- [[X post by Manu Arora: CSS overflow-anchor chat scroller]] provides the weak social recipe and the raw source-check summary.
- MDN and the CSS Scroll Anchoring Module draft, as captured in the raw source, support the underlying `overflow-anchor: auto | none` property and anchor-exclusion mechanism, but not the whole chat-autoscroll UX recipe as production guidance.

## Related
- [[X post by Manu Arora: CSS overflow-anchor chat scroller]]
- [[CSS Overflow-anchor Chat Autoscroll Assessment]]
- [[Adaptive UI Generation]]
- [[Artifact Review Surface]]

## Open Questions
- In current browser versions, what exact behavior occurs for initial render, appended messages, images that load after insertion, user scroll-away, container resize, and reverse-direction layouts?
- What Safari fallback should be preferred if a Hermes/Tolaria surface later uses this pattern?
- Should chat/log UIs combine the CSS anchor with explicit bottom-proximity detection and an unread/new-message affordance rather than treating CSS anchoring as the whole behavior?
