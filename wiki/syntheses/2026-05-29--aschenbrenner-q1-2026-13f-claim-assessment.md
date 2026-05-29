---
type: synthesis
question: "Does the burrytracker social post about Leopold Aschenbrenner's Q1 2026 13F match primary SEC filings, and how should Tolaria preserve it?"
tags: [finance, market-signal, ai-infrastructure, evidence]
created: 2026-05-29
updated: 2026-05-29
---

# Aschenbrenner Q1 2026 13F Claim Assessment

## Question / Purpose
Verify whether [[burrytracker X post on Leopold Aschenbrenner Q1 2026 13F]] matches primary or more reliable filings, then decide whether Tolaria should promote the raw social source or leave it archive-only.

## Answer / Analysis
The strongest counterargument to the tweet is that it is a viral social post with a screenshot and no SEC link, and 13F options are easy to overinterpret. After checking SEC EDGAR, the core holdings table is verified: [[Situational Awareness LP]] filed a 13F-HR on 2026-05-18 for report date 2026-03-31, accession `0002045724-26-000008`, and Situational Awareness Partners LP filed a matching 13F-HR under accession `0002038540-26-000004`. Both Q1 filings expose a 42-row information table with the same top positions shown in the tweet.

The verified top rows include VanEck Semiconductor ETF put `2,042,716,860`, NVIDIA put `1,568,257,120`, Oracle put `1,072,873,230`, Broadcom put `1,006,247,961`, AMD put `969,160,863`, Bloom Energy common `878,707,930`, SanDisk common `724,363,205`, Micron put `583,686,168`, CoreWeave common `556,073,385`, TSM put `535,110,030`, and ASML put `494,122,503`. A comparison against the prior Q4 2025 Situational Awareness LP filing supports the tweet's general change claims: the major semiconductor/technology puts were new rows, CleanSpark shares increased about 648%, Riot Platforms about 86%, CoreWeave call shares fell about 83%, Bloom Energy shares fell about 36%, and Intel call, Lumentum, EQT, and Tower Semiconductor rows exited.

The social interpretation should remain caveated. The SEC table verifies reported 13F rows and values, but it does not reveal strike prices, expirations, premiums, hedge ratios, private/short offsets, manager intent, or whether the puts should be read as a directional anti-semiconductor thesis rather than hedges around AI-infrastructure longs. Tolaria should therefore promote this as a verified-filing / weak-social-interpretation note, not archive-only, and use [[13F Option Exposure Interpretation]] as the reusable caveat.

## Comparison Table
| Claim | Evidence found | Tolaria status |
|---|---|---|
| "Q1 2026 13F" | SEC EDGAR 13F-HR filings by Situational Awareness LP and Situational Awareness Partners LP, filed 2026-05-18 for report date 2026-03-31 | Verified filing fact |
| Top ten rows in tweet/screenshot | SEC XML information table matches the listed SMH/NVDA/ORCL/AVGO/AMD puts and BE/SNDK/CRWV longs among top rows | Verified table fact |
| "Opened $8.45B in new puts" | Q1-vs-Q4 table comparison shows the named put rows are new and sum to roughly the claimed scale when using reported SEC values | Mostly verified as reported 13F-value shorthand; still caveated |
| "Kept AI infrastructure longs" | Filing shows continued/common rows such as Bloom Energy, CoreWeave, IREN, Core Scientific, Applied Digital, Riot, CleanSpark, Bitfarms, and related infrastructure names | Verified as row presence/change, not as strategy/motive |
| "Leopold Aschenbrenner's filing" | Form D/A records link Aschenbrenner to related Situational Awareness entities; the 13F itself is filed by the entities | Accept as shorthand only with entity-level caveat |
| Directional bearish AI/semiconductor conclusion | No strike/expiry/premium/hedge/motive evidence in the 13F or tweet | Not verified |

## Citations
- [[burrytracker X post on Leopold Aschenbrenner Q1 2026 13F]] captures the raw social claim and the tweet/screenshot values that were checked.
- SEC EDGAR primary filings checked live: Situational Awareness LP CIK 0002045724 accession `0002045724-26-000008`; Situational Awareness Partners LP CIK 0002038540 accession `0002038540-26-000004`; prior Situational Awareness LP Q4 2025 accession `0002045724-26-000002` for change comparison.
- SEC Form D/A filings for Situational Awareness Partners LP and Situational Awareness Offshore LP identify "Aschenbrenner Leopold" as executive officer/director/promoter and general partner-related person, supporting the Aschenbrenner association but not turning the entity filing into a personal filing.

## Implications
Tolaria should preserve the source because the core claim was repeated historically and is now primary-source verified at the table level. The right knowledge value is not investment analysis; it is an example of how viral market-signal posts can be upgraded from weak social evidence to verified filing facts while keeping interpretation downgraded.

## Follow-up Questions
- If market-signal sources recur, should Tolaria create a broader synthesis for AI-infrastructure public-market positioning, or keep isolated 13F notes until multiple primary filings/sources accumulate?
- What exact wording should Tolaria standardize for 13F option rows: "reported 13F value" is safer than "notional" or "exposure" unless the filing semantics are separately normalized.
