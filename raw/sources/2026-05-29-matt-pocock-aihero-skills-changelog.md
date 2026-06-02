---
source_url: https://x.com/mattpocockuk/status/2053789346084331569
canonical_url: https://x.com/mattpocockuk/status/2053789346084331569
ingested: 2026-05-29
ingested_by: agent-alpha
source_type: tweet
category: uncategorized
credibility_tier: social
evidence_grade: weak
context: Historical Tolaria backfill item from Alpha sessions; source-check tweet and embedded/linked material.
historical_session_refs:
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_041605_9fbc29ee.json message_index 83
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_194403_9a9f91.json message_index 83
---

# Matt Pocock tweet: AI Hero skills changelog /handoff and /prototype

## Original input context

Historical Tolaria backfill item.

URL: https://x.com/mattpocockuk/status/2053789346084331569
Source type: tweet
Category: uncategorized
Credibility tier: social
Evidence grade: weak
Context/previews from historical sessions:
- /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_041605_9fbc29ee.json message_index 83 preview: https://x.com/omarsar0/status/2052850591584383177?s=48 https://x.com/anirudhbv_ce/status/2052532004919361958?s=48 https://x.com/sudoingx/status/2052794989881753743?s=48 https://x.com/deronin_/status/2
- /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260512_194403_9a9f91.json message_index 83 preview: https://x.com/omarsar0/status/2052850591584383177?s=48 https://x.com/anirudhbv_ce/status/2052532004919361958?s=48 https://x.com/sudoingx/status/2052794989881753743?s=48 https://x.com/deronin_/status/2

## Source-check capture

### X post

Canonical URL: https://x.com/mattpocockuk/status/2053789346084331569
Author: Matt Pocock (@mattpocockuk)
Timestamp shown by X: 10:48 AM · May 11, 2026
Views shown by X at capture: 142.7K

Recovered post text from logged-out X DOM:

> Two new skills this week!
>
> - /handoff compacts your current session to a markdown file
> - /prototype helps you prototype anything - UI or backend
>
> And a bunch more updates. Here's the changelog:

X exposed two shortened links in DOM:
- https://t.co/MsINZhsocy -> https://x.com/mattpocockuk/status/2053789346084331569/video/1 (attached video, 12:43 shown in post render)
- https://t.co/5Gdat5lFfb -> https://www.aihero.dev/

Media found from browser image enumeration: only profile images; video was exposed as an X video route, not as a directly inspectable image asset.

### Linked AI Hero site

URL: https://www.aihero.dev/
Title: Become a Real AI Hero

Relevant recovered homepage text:

> Engineering fundamentals are your biggest advantage.
>
> A lot of people think the rules of software development are being rewritten by AI. They think that code is cheap. That software engineering, as a profession, is finished.
>
> Coding agents like Claude Code and Codex ship code faster than any human ever has. But without careful guidance, they make codebases worse. And the worse the codebase, the worse the AI performs. It's a vicious circle.
>
> Code isn't cheap. In fact, bad code is the most expensive it's ever been. If you can design codebases agents love, you can reap the rewards of this new era.
>
> Software fundamentals aren't obsolete. They're essential. AI Hero is for anyone who cares about the code they ship.

Relevant homepage links:
- https://www.aihero.dev/skills.md — machine-readable skills index/changelog.
- https://github.com/mattpocock/skills — source repo for the skills.
- https://www.aihero.dev/skills/skills-changelog-handoff-prototype-review-and-writing — article matching the tweet.
- https://www.aihero.dev/skills-handoff — handoff guide page.
- https://www.aihero.dev/skills-prototype — prototype guide page.

### AI Hero skills index

URL: https://www.aihero.dev/skills.md
Title/frontmatter: "AI Skills for Real Engineers"
Description: "A practical skill system for engineers who want to use AI without giving up their standards."
Install command shown by source:

```bash
npx skills add mattpocock/skills -y -g
```

Source repo listed: https://github.com/mattpocock/skills

Relevant skill entries:

```markdown
### [handoff: Move Context Between Agent Sessions](https://www.aihero.dev/skills-handoff)
A guide to the handoff skill for compacting context so another agent or session can continue cleanly.
Markdown: https://www.aihero.dev/skills-handoff.md

### [prototype: Answer Questions With Throwaway Code](https://www.aihero.dev/skills-prototype)
A guide to the prototype skill for testing UI, state, and product decisions before committing to implementation.
Markdown: https://www.aihero.dev/skills-prototype.md

### [review: Check a Diff Against Standards and Spec](https://www.aihero.dev/skills-review)
A guide to the review skill for checking agent work against both repo standards and the originating spec.
Markdown: https://www.aihero.dev/skills-review.md
```

Changelog entry from skills.md:

```markdown
### [Skills Changelog: /handoff, /prototype, /review and /writing](https://www.aihero.dev/skills/skills-changelog-handoff-prototype-review-and-writing)

_May 11, 2026_

Two new AI agent skills: /handoff for passing context between agents, and /prototype for building throwaway prototypes to test design decisions.
```

### AI Hero changelog article

URL: https://www.aihero.dev/skills/skills-changelog-handoff-prototype-review-and-writing
Title: Skills Changelog: /handoff, /prototype, /review and /writing
Author shown: Matt Pocock

Recovered article text:

> I've added two brand new skills to my skills repo: /handoff and /prototype. Both have been great upgrades to how I work with agents, especially during planning.
>
> The repo has been growing like crazy - the response has been incredible.
>
> I've also fixed some bugs in /grill-with-docs, /to-prd, and /to-issues. And I'm sharing a sneak peek at some in-progress skills for writing and code review.
>
> /handoff
>
> The new /handoff skill compacts your current conversation into a handoff document for another agent to pick up. It creates a temporary file that summarizes the context, captures the vibe and intent of the session, and suggests which skills the next agent should use.
>
> This solves a common problem: you're deep into a grilling session at 60K tokens, and you need to prototype something or fix a bug. Instead of cramming that work into your remaining context window, you can hand off to a fresh agent with full context. You can even hand back to the original session afterward with what you learned.
>
> There are two main patterns: fire and forget (spin up an agent to fix a bug mid-session) and DIY sub-agent (hand off during planning, do some work, then hand back). The skill lives in the productivity section because it's useful beyond just engineering work.
>
> /prototype
>
> The new /prototype skill builds throwaway prototypes to flush out design decisions before committing to them. It's critical for AI engineering because you need to use prototypes as research and spikes to answer unknown unknowns that you can only figure out by looking at code.
>
> While UI prototypes are the obvious use case, the skill also handles business logic prototypes. When you have complex state machines or entities that change over time, you can build a tiny interactive terminal app that pushes the state through edge cases that are hard to reason about on paper.
>
> For UI work, it generates several radically different variations with a floating button to toggle between them. You can walk down the design tree, combining elements from different variations and discarding others. This is essential for making AFK agents good at front-end - you need a human in the loop to apply taste, because AI often can't see what it's building.
>
> Bug Fixes
>
> The /grill-with-docs skill was sometimes too eager to implement instead of asking questions. The fix was wrapping the supporting information in XML tags to reduce its "loudness" compared to the core instructions. This signals to the LLM that the content inside <supporting-info> should be slightly less prioritized.
>
> Both /to-prd and /to-issues now apply the ready-for-agent-triage label instead of needs-triage. Once you've created issues with these skills, they're ready for agents - no additional triage needed.
>
> In-Progress Preview
>
> There's a tri-part writing skill in development: fragments, beats, and shape. The theory is based on how authors keep journals of ideas that eventually work their way into stories. You dictate fragments (ideas), then write beats (a path through the story), then do a final shaping pass to make sure it doesn't sound AI-generated.
>
> There's also a review skill coming that will kick off two parallel sub-agents: one checking if the diff follows the repo's coding standards, and another checking if it faithfully implements the original issue or PRD. A separate skill will extract coding standards from your repo to make the standards check more effective.

### GitHub repository

URL: https://github.com/mattpocock/skills
Title: GitHub - mattpocock/skills: Skills for Real Engineers. Straight from my .claude directory.
Stars shown at capture: 110k
Forks shown at capture: 9.7k
Latest commit shown at capture: e3b90b5, "Refine rules in CONTEXT-FORMAT.md for clarity and consistency", 11 hours ago.

README recovered from raw.githubusercontent.com:

> My agent skills that I use every day to do real engineering - not vibe coding.
>
> Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.
>
> These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience.

README frames common failure modes and corresponding skills:
- Misalignment -> /grill-me and /grill-with-docs.
- Agent verbosity/domain jargon -> shared language and CONTEXT.md via /grill-with-docs.
- Code doesn't work -> feedback loops, tests, /tdd, /diagnose.
- Ball of mud -> PRD/module awareness, /zoom-out, /improve-codebase-architecture.

Relevant README reference entries:

```markdown
- prototype — Build a throwaway prototype to flesh out a design — either a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route.
- handoff — Compact the current conversation into a handoff document so another agent can continue the work.
```

### Raw skill source excerpts

URL: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/handoff/SKILL.md

```markdown
---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
```

URL: https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/prototype/SKILL.md

```markdown
---
name: prototype
description: Build a throwaway prototype to flesh out a design before committing to it. Routes between two branches — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route. Use when the user wants to prototype, sanity-check a data model or state machine, mock up a UI, explore design options, or says "prototype this", "let me play with it", "try a few designs".
---

# Prototype

A prototype is **throwaway code that answers a question**. The question decides the shape.

## Pick a branch

- "Does this logic / state model feel right?" -> LOGIC.md. Build a tiny interactive terminal app that pushes the state machine through cases that are hard to reason about on paper.
- "What should this look like?" -> UI.md. Generate several radically different UI variations on a single route, switchable via a URL search param and a floating bottom bar.

## Rules that apply to both

1. Throwaway from day one, and clearly marked as such.
2. One command to run.
3. No persistence by default.
4. Skip the polish.
5. Surface the state.
6. Delete or absorb when done.

## When done

The answer is the only thing worth keeping from a prototype. Capture it somewhere durable (commit message, ADR, issue, or a NOTES.md next to the prototype) along with the question it was answering.
```

## Initial classification

- Tweet layer: social, weak evidence, points to more useful primary-ish repo/docs.
- AI Hero changelog: practitioner/secondary, medium evidence for the author's own skill design, weak evidence for general effectiveness.
- GitHub repo skill files: primary for the concrete skill prompts/mechanisms, medium evidence for implementable workflow primitives, not evidence that they outperform alternatives.

Potential Tolaria workstream: synthesize the skills-repo mechanisms as agent-engineering workflow patterns relevant to Hermes/Tolaria: session handoff artifacts, throwaway prototypes as question-answering spikes, XML/supporting-info loudness control, ready-for-agent-triage labeling, and two-lane review (standards vs spec fidelity). Any operational adoption should be proposal-only, not direct implementation.
