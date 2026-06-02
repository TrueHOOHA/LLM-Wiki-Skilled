---
type: concept
aliases: ["low-level design taxonomy", "object-oriented design interview taxonomy", "LLD topic map", "OOD topic map"]
tags: [low-level-design, object-oriented-design, interviews, learning-roadmap]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# LLD/OOD Learning Taxonomy

## Definition
An LLD/OOD Learning Taxonomy is a coverage map for the object-oriented concepts, design principles, class relationships, UML artifacts, patterns, concurrency concerns, and worked interview problems used to prepare for low-level design interviews.

## Scope
In the current Tolaria source, the taxonomy covers: OOP fundamentals such as classes, objects, enums, interfaces, encapsulation, abstraction, inheritance, and polymorphism; class relationships such as association, aggregation, composition, and dependency; design principles such as DRY, YAGNI, KISS, and SOLID; GoF-style creational, structural, and behavioral design patterns; UML class/use-case/sequence/activity/state-machine diagrams; concurrency and multithreading basics; and problem tracks with local markdown requirements, diagrams, and implementations.

This concept is about class-level/object-level design and interview articulation. It does not by itself validate production architecture choices, complete language-specific implementations, or measured interview effectiveness.

## Contrasts
- Versus [[System Design Learning Taxonomy]]: LLD/OOD focuses on object models, class relationships, patterns, UML, and local implementation structure; system design focuses on services, data stores, scaling, reliability, APIs, and distributed-system tradeoffs.
- Versus [[LLD Interview Answering Method]]: the taxonomy names what to know; the method names the process for answering a specific prompt.
- Versus [[System Design Interview Answering Framework]]: the LLD method is class/entity/implementation-centered, while the system-design framework is service/API/data/deep-dive-centered.

## Evidence
- [[Awesome Low Level Design]] records the README topic map, repository structure, 33 markdown problem pages, UML class diagrams, multi-language solution links, and design-pattern implementation examples.
- [[Awesome Low Level Design Source Map]] extracts the topic taxonomy and distinguishes durable LLD/OOD learning structure from unverified interview-outcome claims.

## Related
- [[Awesome Low Level Design]]
- [[Awesome Low Level Design Source Map]]
- [[LLD Interview Answering Method]]
- [[System Design Learning Taxonomy]]
- [[System Design Interview Answering Framework]]

## Open Questions
- Which LLD problem families are most useful for future source-specific ingestion: caches, parking/booking systems, games, payments/splitting, ride-sharing/logistics, or concurrent data structures?
- Should Tolaria keep an interview-rubric synthesis separate from production OOD guidance to avoid treating interview templates as engineering doctrine?
