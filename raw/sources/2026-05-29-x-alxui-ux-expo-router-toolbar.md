---
source_url: https://x.com/alxui_ux/status/2053174102182318257
canonical_url: https://x.com/alxui_ux/status/2053174102182318257
ingested: 2026-05-29
ingested_by: agent-alpha
source_type: tweet
category: design
credibility_tier: social
evidence_grade: weak
first_seen: 2026-05-12
context: "Historical Tolaria backfill item. Followed SOUL.md and normal Alpha ingestion path; source-check where feasible."
---

# X post: ALX on Expo Router `<Toolbar />`

## User-supplied metadata

- Source URL: https://x.com/alxui_ux/status/2053174102182318257
- Source type: tweet
- Category: design
- Credibility tier: social
- Evidence grade: weak
- First seen: 2026-05-12
- Historical session files:
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_041605_9fbc29ee.json
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_194403_9a9f91.json
- Context/previews included related X links:
  - https://x.com/omarsar0/status/2052850591584383177?s=48
  - https://x.com/anirudhbv_ce/status/2052532004919361958?s=48
  - https://x.com/sudoingx/status/2052794989881753743?s=48
  - https://x.com/deronin_/status/2
- Session-derived full related deronin URL seen in historical bundle:
  - https://x.com/deronin_/status/2052697237856088114?s=48

## Captured primary post

Author: ALX 🇺🇸 / @alxui_ux
Timestamp: 6:03 PM · May 9, 2026
Engagement at capture: 86K views; 9 replies; 22 reposts; 628 likes; 471 bookmarks

Post text:

> In the next version of Expo Router
>
> use `<Toolbar />` to create bottom-aligned controls and menus for commonly used actions.
> By: @Baconbrix

Attached media: short video preview showing a smartphone UI with a dark screen and a bottom-aligned toolbar of circular/icon controls: avatar/action icons, ellipsis/more control, and a blue checkmark action. No additional readable product text was visible beyond the toolbar design pattern.

Embedded/outbound links found in primary post: none besides X profile/status links and the @Baconbrix mention.

## Source check / corroboration

The social post itself provides weak evidence and no official docs link. A lightweight source check against the current npm package for `expo-router` found first-party implementation/types for toolbar support in `expo-router@56.2.7`:

- npm package: `expo-router@56.2.7`
- npm homepage: https://docs.expo.dev/routing/introduction/
- package maintainers include `evanbacon` / Baconbrix, matching the tweet attribution.
- Package contains native toolbar support files, including:
  - `ios/Toolbar/RouterToolbarModule.swift`
  - `ios/Toolbar/RouterToolbarHostView.swift`
  - `ios/Toolbar/RouterToolbarItemView.swift`
  - `build/toolbar/native.types.d.ts`
  - `build/layouts/stack-utils/toolbar/StackToolbarClient.d.ts`
  - `build/layouts/stack-utils/toolbar/StackToolbarView/index.d.ts`
  - `build/layouts/stack-utils/toolbar/StackToolbarSearchBarSlot/index.d.ts`
- `StackToolbarClient.d.ts` describes `Stack.Toolbar` children and placement:
  - Children can include `Stack.Toolbar.Button`, `Stack.Toolbar.Menu`, `Stack.Toolbar.View`, `Stack.Toolbar.Spacer`, and `Stack.Toolbar.SearchBarSlot`.
  - `placement` can be `left`, `right`, or `bottom`.
  - `bottom` renders items in the bottom toolbar.
  - default placement is `bottom`.
- `StackToolbarSearchBarSlot` docs state it is a search bar slot for the bottom toolbar, available in bottom placement.
- Android implementation references Jetpack Compose `HorizontalFloatingToolbar`; iOS implementation references native toolbar item views.

Interpretation: the tweet is a social/design teaser, but the npm package source corroborates that Expo Router has a native `Stack.Toolbar`/toolbar API with bottom placement. The exact user-facing release status and official docs page should still be checked by Beta before promoting a durable wiki note.

## Related links inspected

- https://x.com/omarsar0/status/2052850591584383177 — Unrelated to Expo Router; social/demo post about LLM Wikis + HTML artifacts as interactive agent knowledge UIs. Weak evidence for an agent-knowledge UI pattern, not for this design source.
- https://x.com/anirudhbv_ce/status/2052532004919361958 — Unrelated to Expo Router; promotional/research post for a RAG/embedding geometry paper/repo. Contains GitHub/PDF link, but not relevant to the Expo Toolbar source.
- https://x.com/sudoingx/status/2052794989881753743 — Unrelated to Expo Router; Hermes Agent `/goal` social usage guidance with no docs/source link. Not relevant to the design source.
- https://x.com/deronin_/status/2052697237856088114 — Unrelated to Expo Router; Browserbase/Autobrowse social post about browser agents that learn sites and write `SKILL.md`. Agent-engineering-relevant, but not evidence for the Expo Toolbar source.

## Claim / evidence / caveats

- Claim: the next version of Expo Router supports `<Toolbar />` for bottom-aligned controls and menus.
- Evidence in source: short social post and video teaser by a design account, attributed to @Baconbrix.
- Corroboration found: current `expo-router` npm package includes toolbar implementation/types and `Stack.Toolbar` placement docs in type declarations.
- Caveats: primary tweet is social and the captured post did not link official release notes/docs. Related historical preview links are mostly unrelated to the design source.

## Recommended classification

- Classification: wiki-ingest / low-priority design knowledge
- Suggested workstream: have Beta decide whether to promote this into Tolaria as a source note and/or mobile UI concept note about Expo Router native bottom toolbar patterns, with the npm package source treated as stronger corroboration than the tweet.
