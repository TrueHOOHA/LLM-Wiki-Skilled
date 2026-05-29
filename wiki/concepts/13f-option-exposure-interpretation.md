---
type: concept
aliases: ["13F options interpretation", "13F put exposure", "13F call exposure", "13F derivative caveats"]
tags: [finance, market-signal, evidence]
created: 2026-05-29
updated: 2026-05-29
source_count: 1
---

# 13F Option Exposure Interpretation

## Definition
13F Option Exposure Interpretation is the evidence discipline of separating what a Form 13F information table reports from what observers infer about a manager's economic bet. A 13F can verify that a reporting manager disclosed put or call rows, issuers, share/principal amounts, and reported values; it usually cannot by itself prove strike, expiry, premium, hedge ratio, net exposure, motive, private offsets, or future trade intent.

## Scope
This concept covers how Tolaria should treat social claims about 13F puts, calls, and market themes: use SEC EDGAR filings as primary evidence for table facts, then downgrade social interpretations unless they are independently supported. It applies especially when a viral post converts large reported option rows into claims such as "opened billions in puts," "kept AI-infrastructure longs," or "is betting against semiconductors."

## Contrasts
- Versus raw 13F table verification: table verification can be high-confidence when EDGAR rows match the claim.
- Versus portfolio-thesis interpretation: inferring directional intent, risk, or conviction from 13F options is lower-confidence without strike, expiry, premium, short/long offsets, and contemporaneous manager commentary.
- Versus investment advice: Tolaria preserves evidence quality and source context, not trading recommendations.

## Evidence
- [[burrytracker X post on Leopold Aschenbrenner Q1 2026 13F]] is a concrete example: SEC filings verify the Q1 2026 Situational Awareness top holdings and option rows, but the social framing remains weaker than the filing facts.
- [[Aschenbrenner Q1 2026 13F Claim Assessment]] applies this concept by splitting verified EDGAR rows from unverified social interpretation of AI-infrastructure and semiconductor exposure.

## Related
- [[Situational Awareness LP]]
- [[Leopold Aschenbrenner]]
- [[Aschenbrenner Q1 2026 13F Claim Assessment]]

## Open Questions
- What exact 13F option-value field semantics should Tolaria use for future filings: raw reported value, notional shorthand, underlying share count, or a safer "reported 13F value" label?
- When should a 13F social-source cluster deserve a dedicated market-signal synthesis versus remaining a source-only note?
