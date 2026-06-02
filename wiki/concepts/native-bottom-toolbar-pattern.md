---
type: concept
aliases: ["bottom-aligned native toolbar", "native bottom toolbar", "Expo Router bottom toolbar", "Stack.Toolbar bottom placement"]
tags: [mobile-ui, navigation, react-native, design-pattern]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Native Bottom Toolbar Pattern

## Definition
Native Bottom Toolbar Pattern is a mobile UI pattern where high-frequency contextual actions are placed in a native bottom toolbar rather than only in a top navigation header, tab bar, floating action button, or custom overlay. In the current Tolaria evidence, [[Expo Router]]'s experimental `Stack.Toolbar` bottom placement is an example of this pattern for React Native/Expo apps.

## Scope
This concept covers contextual action controls such as icon buttons, overflow menus, search slots, spacers, badges, labels, and custom toolbar views that sit at the bottom edge of a screen. It does not imply that every app should replace a tab bar or bottom navigation; the pattern is most relevant when actions belong to the current screen context and should remain reachable near the thumb zone without becoming global navigation.

## Contrasts
- Versus tab bars: tab bars switch between primary app destinations; bottom toolbars expose actions for the current screen.
- Versus floating action buttons: a bottom toolbar can group multiple actions, menus, and search affordances instead of emphasizing one primary action.
- Versus custom overlays: native toolbars can inherit platform behavior and styling, but may also carry platform/version constraints.
- Versus top header buttons: bottom placement favors reachability and action grouping, while header placement favors conventional navigation/header affordances.

## Evidence
- [[ALX X post on Expo Router Stack.Toolbar bottom controls]] records the social design claim and package-source corroboration that `Stack.Toolbar` supports bottom placement, toolbar composition components, and a bottom toolbar search slot.

## Related
- [[Expo Router]]
- [[ALX X post on Expo Router Stack.Toolbar bottom controls]]

## Open Questions
- What are the practical design guidelines for deciding between bottom toolbar, tab bar, FAB, and header actions in Expo Router apps?
- Does `Stack.Toolbar` bottom placement remain experimental in the first broadly documented release, and what limitations appear in production use?
- How do Android IME padding, iOS 26+ search slot availability, safe areas, and Liquid Glass styling affect cross-platform designs?
