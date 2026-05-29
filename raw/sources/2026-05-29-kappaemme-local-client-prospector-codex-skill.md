---
source_url: https://x.com/kappaemme1926/status/2054981327414231173
ingested: 2026-05-29
ingested_by: agent-alpha
context: Historical Tolaria backfill item; source type tweet; category uncategorized; credibility tier social; evidence grade weak; first seen 2026-05-15T16:17:05.565935 in /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_044753_b094ad.json at message_index 186.
source_type: tweet
credibility_tier: social
evidence_grade: weak
canonical_url: https://x.com/kappaemme1926/status/2054981327414231173
---

# Kappaemme tweet: Local Client Prospector Codex skill

## Backfill context

- Original URL: https://x.com/kappaemme1926/status/2054981327414231173
- Preview URL from historical session: https://x.com/kappaemme1926/status/2054981327414231173?s=52
- First seen: 2026-05-15T16:17:05.565935
- Historical session: /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_044753_b094ad.json
- Message index: 186
- Source type: tweet
- Category: uncategorized
- Credibility tier: social
- Evidence grade: weak

## Primary X capture

Fetched via browser on 2026-05-29. X rendered the tweet body while prompting for login/signup.

Author:
- Kappaemme / @Kappaemme1926

Tweet text:

> CODEX SKILL THAT TURNS LOCAL SEARCH INTO CLIENT LEADS!
>
> I made a Codex skill that helps find local businesses that may need a website.
>
> Search nearby shops, gyms, restaurants, salons, and local activities while Codex checks who has a real website and who only has socials.
>
> -> local business prospecting
> -> website vs social-only checks
> -> lead scoring
> -> phone/contact fields
> -> chat or CSV-style output
> -> one-command install
>
> Install: npx --yes local-client-prospector-skill
>
> 100% open source.
> Repo in Bio.

Visible timestamp / engagement at fetch:
- 5:45 PM · May 14, 2026
- 320.7K views
- 28 replies, 39 reposts, 749 likes, 1.5K bookmarks shown in rendered text

Visible media:
- Profile image: https://pbs.twimg.com/profile_images/2018267726507110400/7yfnGNA2_normal.jpg
- Video thumbnail: https://pbs.twimg.com/amplify_video_thumb/2054981233252114432/img/1KbTdYDyNJ2hww7L.jpg

## Links recovered from X page

Relevant:
- https://t.co/WXAW2tpetK — bio/site link, resolved to https://kappaemmedev.vercel.app/
- https://kappaemmedev.vercel.app/ — Kappaemme Dev portfolio; includes skill library and GitHub links
- https://github.com/Kappaemme-git/local-client-prospector-skill — linked repo for the Local Client Prospector Codex skill

Other visible X links:
- https://x.com/Kappaemme1926 — profile
- https://x.com/Kappaemme1926/status/2054981327414231173 — canonical status URL
- https://x.com/Kappaemme1926/status/2054981327414231173/analytics — analytics URL; ignored as non-source

## Portfolio site capture

Resolved URL: https://kappaemmedev.vercel.app/
Title: Kappaemme Dev

Relevant site context:
- Header says: “CS STUDENT & INDIE HACKER”
- Tagline: “I design and ship digital products with a simple approach: build, test, improve, repeat.”
- Skill library includes multiple Codex skills:
  - Codex Complexity Optimizer — https://github.com/Kappaemme-git/codex-complexity-optimizer
  - Local Client Prospector — https://github.com/Kappaemme-git/local-client-prospector-skill
  - Simple Flight Search — https://github.com/Kappaemme-git/codex-simple-flight-search-skill
  - Codex Pomodoro Arena — https://github.com/Kappaemme-git/codex-pomodoro-arena
  - Codex FM — https://github.com/Kappaemme-git/codex-fm
  - Startup Pressure Test — https://github.com/Kappaemme-git/codex-startup-pressure-test-skill
  - Video Short Maker — https://github.com/Kappaemme-git/codex-video-short-maker-skill
  - Design Audit — https://github.com/Kappaemme-git/codex-design-audit-skill

## Repository capture

Repository: https://github.com/Kappaemme-git/local-client-prospector-skill
Visibility: Public
Rendered GitHub stats at fetch:
- 144 stars
- 17 forks
- Latest commit shown: 2340d02, “Add package repository metadata”, 2 weeks ago
- Files shown: bin/, local-client-prospector/, .gitignore, LICENSE, README.md, package.json

### README.md

Source: https://raw.githubusercontent.com/Kappaemme-git/local-client-prospector-skill/main/README.md

```markdown
# Local Client Prospector

Codex skill that turns local search into client leads.

Find nearby shops, gyms, restaurants, salons, clinics, and local businesses that may need a website or better online presence.

The skill uses browser-assisted research, checks whether each business has a real standalone website or only social profiles, scores the opportunity, and returns a lead sheet in chat or CSV-style rows.

## Features

- Local business prospecting
- Website vs social-only checks
- Lead scoring: Hot, Warm, Low, Skip
- Phone, website, social, source, and notes fields
- Chat table or CSV-style output
- Works with Codex's integrated spreadsheet skill for XLSX files
- One-command install

## Install

```bash
npx local-client-prospector-skill
```

This installs the skill to:

```bash
~/.codex/skills/local-client-prospector
```

Restart Codex or start a new session if the skill does not appear immediately.

## Usage

```text
Use $local-client-prospector to find gyms and shops within 20 km of Gym Exclusive Casoria, and return the result in chat.
```

With spreadsheets:

```text
Use $local-client-prospector and $spreadsheets to find businesses within 20km of Casoria that may need a website. Create an XLSX with filters, lead score, phone, website/social links, notes, and top prospects.
```

The skill answers in the same language as the user prompt.

## Compliance

This is an assisted research skill, not a bulk scraper. It asks Codex to use the browser responsibly, avoid bypassing access controls, and cross-check business details with public sources.
```

### local-client-prospector/SKILL.md

Source: https://raw.githubusercontent.com/Kappaemme-git/local-client-prospector-skill/main/local-client-prospector/SKILL.md

```markdown
---
name: local-client-prospector
description: Use this skill to find and qualify local business prospects near a location, especially shops, gyms, restaurants, clinics, salons, and local services that may need a website. It uses the integrated browser for assisted research, checks whether each business has a real website or only social profiles, and returns a concise lead sheet in chat or CSV-style rows.
---

# Local Client Prospector

Use this skill when the user wants to discover nearby local businesses that could become website or digital-marketing clients.

The default output is a compact lead sheet in chat. Create a CSV or spreadsheet only when the user asks for a file or when the result set is large enough that chat would be hard to use.

## Inputs to Collect

If missing, infer reasonable defaults and continue:

- `base_location`: address, town, landmark, or area.
- `radius_km`: default 20 km.
- `categories`: default `negozi, palestre, ristoranti, parrucchieri, estetisti, studi professionali`.
- `max_leads`: default 15.
- `language`: match the user's language.
- `output`: default `chat table`; optional `CSV`.

Ask a concise clarification only if the base location is missing and cannot be inferred.

## Compliance Guardrails

- Use the integrated browser as an assisted research tool, not as a bulk scraper.
- Do not bypass CAPTCHAs, login walls, rate limits, bot protections, or paywalls.
- Do not extract or resell Google Maps data at scale.
- Prefer public business facts and official business contact channels.
- Avoid collecting personal emails or private personal data unless the user explicitly provides a lawful basis and the source is clearly public business contact information.
- If using Google Maps manually in the browser, treat it as a discovery aid. Cross-check important details with independent public web sources such as the business website, social pages, directory listings, or search results.

## Browser Research Workflow

1. Open the browser and search for the requested category near `base_location`.
2. Build a candidate list from visible local results, search results, public directories, or business pages.
3. For each candidate, inspect enough public sources to fill the lead fields.
4. Search the exact business name plus city/town to check whether a real website exists.
5. Classify website status:
   - `No site found`: no credible standalone website after cross-check.
   - `Social only`: Facebook, Instagram, WhatsApp, Linktree, booking portal, or marketplace page only.
   - `Weak site`: standalone site exists but looks outdated, broken, very thin, non-mobile-friendly, or missing clear contact/conversion flow.
   - `Has site`: credible standalone site exists.
6. Mark confidence:
   - `High`: confirmed by at least two sources or official page.
   - `Medium`: one credible source plus consistent search evidence.
   - `Low`: incomplete or ambiguous evidence.

When the user explicitly asks for subagents or parallel verification and subagents are available, split candidates into non-overlapping batches and ask each subagent to verify only website/social/contact status. Do not use subagents for the immediate browser search if it blocks progress.

## Lead Scoring

Use this simple score:

- `Hot`: no site found or social only, phone/contact present, active business, near the target area.
- `Warm`: weak site, poor online presentation, or only marketplace/booking page.
- `Low`: good website already present or low confidence.
- `Skip`: closed, duplicate, outside radius, irrelevant category, or not a business prospect.

## Output Format

For chat output, use a concise markdown table:

| Score | Business | Category | Area | Distance | Website status | Website/Social | Phone | Why it is a prospect | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rules:

- Keep `Why it is a prospect` short and actionable.
- Use `Not found` instead of leaving blank fields.
- Include source links when possible, but do not overload the table with many URLs.
- After the table, add `Best first outreach targets` with the top 3 leads and one practical reason each.
- If confidence is low, state exactly what remains uncertain.

## CSV Columns

When returning CSV-style rows or creating a file, use these columns:

```csv
score,business,category,area,distance_km,website_status,website_url,social_urls,phone,source_urls,why_prospect,confidence,notes
```

## Quality Checks

Before finalizing:

- Remove duplicates.
- Do not label a lead `Hot` if a real standalone website was found.
- Do not claim a site is missing unless at least one exact-name web search was attempted.
- Prefer fewer verified leads over many weak guesses.
- Include the search location, radius, categories, and date in the final response.
```

### package.json

Source: https://raw.githubusercontent.com/Kappaemme-git/local-client-prospector-skill/main/package.json

```json
{
  "name": "local-client-prospector-skill",
  "version": "0.1.0",
  "description": "Codex skill for assisted local business prospecting and lead qualification.",
  "homepage": "https://github.com/Kappaemme-git/local-client-prospector-skill#readme",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Kappaemme-git/local-client-prospector-skill.git"
  },
  "bugs": {
    "url": "https://github.com/Kappaemme-git/local-client-prospector-skill/issues"
  },
  "bin": {
    "local-client-prospector-skill": "bin/install.js"
  },
  "scripts": {
    "check": "node --check bin/install.js",
    "pack:dry-run": "npm pack --dry-run"
  },
  "files": [
    "bin",
    "local-client-prospector"
  ],
  "keywords": [
    "codex",
    "skill",
    "local-business",
    "prospecting",
    "leads"
  ],
  "license": "MIT",
  "publishConfig": {
    "access": "public"
  },
  "engines": {
    "node": ">=18"
  }
}
```

### bin/install.js

Source: https://raw.githubusercontent.com/Kappaemme-git/local-client-prospector-skill/main/bin/install.js

```javascript
#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const root = path.resolve(__dirname, "..");
const source = path.join(root, "local-client-prospector");
const targetRoot = path.join(os.homedir(), ".codex", "skills");
const target = path.join(targetRoot, "local-client-prospector");

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else if (entry.isFile()) {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

if (!fs.existsSync(source)) {
  console.error(`Skill source not found: ${source}`);
  process.exit(1);
}

fs.rmSync(target, { recursive: true, force: true });
copyDir(source, target);

console.log(`Installed Codex skill: ${target}`);
console.log("Restart Codex or start a new session if the skill does not appear immediately.");
```

## Initial Alpha assessment

- The X post itself is a social/marketing announcement and weak evidence.
- The linked GitHub repository is the primary artifact for the actual mechanism.
- The reusable mechanism is not “adopt this prospecting skill blindly”; it is a compact pattern for Codex skill packaging, one-command npm installation into `~/.codex/skills`, browser-assisted lead qualification, quality checks, and compliance guardrails.
- Risks/caveats: local-business prospecting may run into platform ToS, privacy, rate-limit, and lead-quality issues; the skill’s claims are not backed by benchmark/eval evidence; it relies on manual/browser-assisted research rather than an auditable API-backed pipeline.
- Possible Tolaria workstream: promote a source-backed note about Codex skill distribution/guardrails and assess whether any packaging or quality-check patterns should inform Overseer’s local Codex workflow, without implementing anything yet.
