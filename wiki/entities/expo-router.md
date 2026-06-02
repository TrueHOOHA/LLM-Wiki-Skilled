---
type: entity
aliases: ["expo-router", "Expo Router", "Stack.Toolbar", "Expo Router Stack.Toolbar"]
tags: [mobile-framework, react-native, navigation, expo]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# Expo Router

## Identity
Expo Router is Expo's file-based routing and navigation layer for React Native and Expo apps. In the current Tolaria evidence, it matters because the `expo-router@56.2.7` package includes an experimental `Stack.Toolbar` API that can render native toolbar items, including a default bottom placement, while the originating social post only weakly announces the design direction.

## Aliases
- expo-router
- Expo Router
- Stack.Toolbar
- Expo Router Stack.Toolbar

## Key Attributes
| Attribute | Current Tolaria evidence |
|---|---|
| Ecosystem | Expo / React Native navigation |
| Relevant API | `Stack.Toolbar` with `Button`, `Menu`, `MenuAction`, `View`, `Spacer`, `SearchBarSlot`, `Label`, `Icon`, and `Badge` composition components |
| Placement support | Package declarations list `left`, `right`, and `bottom`; `bottom` is documented in the type comments as the default placement |
| Platform notes | Package comments mark Android and iOS support for the toolbar; `SearchBarSlot` is bottom-placement-only and marked iOS 26+ |
| Maturity caveat | Package declarations mark the API experimental; official docs text captured during ingestion is thinner than the package comments for bottom placement |

## Evidence
- [[ALX X post on Expo Router Stack.Toolbar bottom controls]] preserves the weak social teaser and the stronger package-source corroboration for toolbar API existence.

## Related
- [[Native Bottom Toolbar Pattern]]
- [[ALX X post on Expo Router Stack.Toolbar bottom controls]]

## Open Questions
- Which Expo SDK/release note first treats `Stack.Toolbar` as stable rather than experimental?
- Will the official Expo Router docs document bottom placement, platform differences, and production guidance as clearly as the npm package type comments?
- How should this native toolbar pattern coexist with tab bars, safe-area insets, Android IME behavior, and iOS Liquid Glass navigation affordances in real app designs?
