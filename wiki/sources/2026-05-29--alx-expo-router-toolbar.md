---
type: source
source_path: raw/sources/2026-05-29-x-alxui-ux-expo-router-toolbar.md
title: "ALX X post on Expo Router Stack.Toolbar bottom controls"
author: "ALX / @alxui_ux; package corroboration from expo-router maintainers"
date: 2026-05-09
tags: [mobile-ui, expo-router, social-claim, design]
created: 2026-05-29
updated: 2026-05-29
source_count: 0
---

# ALX X post on Expo Router Stack.Toolbar bottom controls

## Summary
This source is a weak-evidence X design teaser claiming that the next version of [[Expo Router]] supports `<Toolbar />` for bottom-aligned controls and menus for commonly used actions. The captured post has no official docs or release-note link, but the raw source records a source check against `expo-router@56.2.7` showing first-party package files and type declarations for `Stack.Toolbar`, `placement="bottom"`, toolbar buttons, menus, views, spacers, labels, icons, badges, and a bottom toolbar search slot. Expo's public Stack docs also expose a "Stack Toolbar" section, but in the captured docs text it is framed as an iOS header toolbar with Liquid Glass support and does not by itself prove mature bottom-toolbar documentation. Treat the tweet as discovery evidence and the npm package source/types as stronger evidence for API existence, while keeping adoption readiness medium/uncertain until official release notes and complete docs catch up.

## Key Claims
1. The X post claims that Expo Router will support `<Toolbar />` for bottom-aligned controls and menus.
2. The raw source's npm package check found toolbar implementation/type files in `expo-router@56.2.7`, including iOS Swift toolbar files, Android/native package artifacts, `build/toolbar/native.types.d.ts`, and stack toolbar declaration files.
3. `StackToolbarClient.d.ts` says `Stack.Toolbar` children can include `Button`, `Menu`, `View`, `Spacer`, and `SearchBarSlot`, and that `placement` supports `left`, `right`, and `bottom`, with `bottom` as the default.
4. The package type comments mark `Stack.Toolbar` as experimental and note that `placement="bottom"` can only be used inside page components, not layout components.
5. `StackToolbarSearchBarSlot` is described as a bottom-toolbar-only slot and marked for iOS 26+ in the package types.
6. Official docs currently provide some `Stack Toolbar` surface area, but the captured docs text emphasizes iOS header toolbar/Liquid Glass and is thinner than the package type comments for bottom placement.

## Notable Quotes
- X post: "In the next version of Expo Router use `<Toolbar />` to create bottom-aligned controls and menus for commonly used actions. By: @Baconbrix"
- Raw source note: "current `expo-router@56.2.7` includes toolbar files and type declarations for `Stack.Toolbar`, bottom placement, toolbar buttons/menus/views/spacers/search slot."
- Package type comment: "Use `placement=\"bottom\"` (default) to show a bottom toolbar."
- Package caveat: "`Stack.Toolbar` with `placement=\"bottom\"` can only be used inside **page** components, not in layout components."

## Entities Mentioned
- [[Expo Router]]

## Concepts Mentioned
- [[Native Bottom Toolbar Pattern]]

## Evidence Notes
- Social layer: weak. The X post is a teaser with a video preview and no linked docs.
- Package/source layer: medium. The npm package is first-party and contains concrete implementation/type evidence for the toolbar API, but the feature is marked experimental in the declarations.
- Documentation layer: medium-low. Public Expo docs expose a Stack Toolbar heading, but the captured docs text did not clearly document the bottom-placement pattern as fully as the package types.

## Follow-ups
- Check Expo release notes and final docs before treating this as stable adoption guidance for production apps.
- If designing a mobile UI with Expo Router, evaluate platform constraints first: experimental API status, page-only bottom placement, Android IME padding behavior, iOS 26+ search slot support, and how the toolbar coexists with tabs, safe areas, and native navigation headers.
