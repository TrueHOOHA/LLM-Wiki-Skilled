---
source_url: https://x.com/coreyhainesco/status/2055011827600572668
canonical_url: https://x.com/coreyhainesco/status/2055011827600572668
source_type: tweet
category: agent-engineering
credibility_tier: social
evidence_grade: weak
ingested: 2026-05-29
ingested_by: agent-alpha
context: "Historical Tolaria backfill item from ledger; first seen 2026-05-15T14:59:38.170682; mentions: 3; preview repeated in agent-alpha session files."
ledger_examples:
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_150228_4ae84b.json
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_044753_b094ad.json
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_150343_b40e0d.json
---

# Corey Haines X post: Marketing Skills v2.0

## Original / preview context from ledger

Historical Tolaria backfill item. Source type: tweet. Category: agent-engineering. Credibility tier: social. Evidence grade: weak. URL: https://x.com/coreyhainesco/status/2055011827600572668 . Original/preview context from ledger examples: repeated preview https://x.com/coreyhainesco/status/2055011827600572668?s=20 from agent-alpha session files /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_150228_4ae84b.json, /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_044753_b094ad.json, /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260515_150343_b40e0d.json. First seen 2026-05-15T14:59:38.170682; mentions: 3.

## Captured X post text

Author: Corey Haines (@coreyhainesco)
Post URL: https://x.com/coreyhainesco/status/2055011827600572668
Timestamp shown by X: 7:46 PM · May 14, 2026
Engagement shown at capture: 64 replies, 96 reposts, 1.4K likes, 2.8K bookmarks, 136.5K views.

Text:

> Marketing Skills v2.0 is finally here! 🎉
>
> I've been working on this for over a month.
>
> The biggest release yet. Shorter names, one unified CRO skill, and a foundation built to scale.
>
> What's new:
>
> ✨ Cleaner, faster skill names
> → /paid-ads → /ads
> → /email-sequence → /emails
> → /social-content → /social
> → /launch-strategy → /launch
> → /pricing-strategy → /pricing
> → /referral-program → /referrals
> → + 11 more
>
> 🔗 /cro is now one skill
> Page CRO + Form CRO merged. One mental model for every conversion optimization workflow.
>
> 📦 100+ refinements across the entire skill set
>
> 40 skills. 52 tool integrations. 100% evals coverage.
>
> Free and open source.
>
> 🚨 Heads up — v2.0 is a breaking change, so reinstall to get the new names:
>
> npx skills add coreyhaines31/marketingskills

The post includes an embedded video, but the visible post text and linked repo/website carry the reusable technical payload.

## Links discovered and inspected

- https://github.com/coreyhaines31/marketingskills — inferred from `npx skills add coreyhaines31/marketingskills`; inspected as primary source of truth.
- https://marketing-skills.com/ — profile/site link and project landing page; inspected. It points to GitHub and describes "Marketing Skills for AI Agents."
- https://conversionfactory.co — author agency profile link; not directly relevant to the skill-pack mechanism.
- https://swipefiles.com — author newsletter/product link; not directly relevant to the skill-pack mechanism.
- https://magistermarketing.com — author product link; not directly relevant to the skill-pack mechanism.
- https://agentskills.io — referenced by the repo README as the Agent Skills specification.

## GitHub repo capture

Repository: coreyhaines31/marketingskills
Description from GitHub/API: "Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering."
Stars shown by browser/API page at capture: about 31k.
License: MIT.
Recent browser snapshot showed 40 skills, 52+ tool integrations/CLIs, eval JSON files for each skill, and Claude Code plugin marketplace files.

README excerpts captured:

> A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want AI coding agents to help with conversion optimization, copywriting, SEO, analytics, and growth engineering. Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports the Agent Skills spec.

> Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, your agent can recognize when you're working on a marketing task and apply the right frameworks and best practices.

> Skills reference each other and build on shared context. The `product-marketing` skill is the foundation — every other skill checks it first to understand your product, audience, and positioning before doing anything.

Installation options captured:

```bash
npx skills add coreyhaines31/marketingskills
npx skills add coreyhaines31/marketingskills --skill cro copywriting
npx skills add coreyhaines31/marketingskills --list
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

AGENTS.md excerpts captured:

- Repository follows the Agent Skills specification and installs to `.agents/skills/`, with Claude Code plugin support through `.claude-plugin/marketplace.json`.
- Structure includes `skills/<skill-name>/SKILL.md`, optional `references/`, `scripts/`, `assets/`, per-skill `evals/evals.json`, and `tools/` registries/integrations.
- Validation guidance: frontmatter name/description constraints, skill names match directory names, SKILL.md under 500 lines, zero-dependency Node CLI tools syntax-checkable with `node --check tools/clis/<name>.js`.
- Tool registry includes many marketing API integrations and CLI wrappers; README and AGENTS.md position tools as implementation supports referenced by skills.

Partial repo tree evidence:

- `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`
- `.github/workflows/validate-skill.yml`, `.github/workflows/sync-skills.yml`
- `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, `VERSIONS.md`
- `skills/*/SKILL.md` for 40 marketing skills
- `skills/*/evals/evals.json` for each listed skill in the captured tree
- many `skills/*/references/*.md` support files
- `tools/REGISTRY.md`
- `tools/clis/*.js` zero-dependency Node CLI wrappers
- `tools/integrations/*.md`
- `tools/composio/marketing-tools.md`

## Capture notes / skeptical assessment

- Social claim is weak evidence by itself and promotional in tone.
- The linked GitHub repo is the stronger source; it supports the claims that this is a skill-pack repo with structured skill directories, plugin marketplace files, many integration docs/CLIs, and per-skill eval files.
- The exact "100% evals coverage" claim was not independently executed or verified; only repo tree evidence of per-skill `evals/evals.json` files was captured.
- Main reusable concept is not the marketing content itself; it is the large domain-specific skill-pack architecture: short names, shared foundation skill, cross-skill references, optional references/scripts/assets, tool registry, plugin marketplace metadata, and eval coverage.

## Initial classification

Useful for Tolaria information processing as an agent-engineering case study. Recommended downstream work: have Beta promote/synthesize the repo-backed mechanisms into Tolaria, separating social claims from repo evidence and extracting implications for Hermes/Tolaria skill architecture and evaluation loops. Do not implement or install this pack without explicit approval.
