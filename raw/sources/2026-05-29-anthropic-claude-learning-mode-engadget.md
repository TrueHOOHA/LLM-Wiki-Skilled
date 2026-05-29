---
source_url: https://engadget.com/ai/anthropic-brings-claudes-learning-mode-to-regular-users-and-devs-170018471
ingested: 2026-05-29
ingested_by: agent-alpha
context: "Historical Tolaria backfill item from ledger; source_type=article; category=agent-engineering; mentions=4; source-check and embedded-link follow-through requested."
source_type: article
category: agent-engineering
credibility_tier: secondary
evidence_grade: medium
canonical_url: https://www.engadget.com/ai/anthropic-brings-claudes-learning-mode-to-regular-users-and-devs-170018471.html
ledger_first_seen: 2026-05-18T18:24:08.900009
---

# Engadget: Anthropic brings Claude's learning mode to regular users and devs

## Original source

- Original URL: https://engadget.com/ai/anthropic-brings-claudes-learning-mode-to-regular-users-and-devs-170018471
- Canonical/fetched URL: https://www.engadget.com/ai/anthropic-brings-claudes-learning-mode-to-regular-users-and-devs-170018471.html
- Browser title: Anthropic brings Claude's learning mode to regular users and devs
- Author: Igor Bonifacic
- Published: Aug. 14, 2025 1:00 pm EST
- Outlet: Engadget

## Ledger context supplied by Overseer

- source_type: article
- category: agent-engineering
- credibility_tier: unknown in ledger; classified here as secondary because Engadget reports on Anthropic product changes
- evidence_grade: unknown in ledger; classified here as medium after primary-source cross-checks confirmed the core Claude Code output-styles mechanism
- mentions: 4
- first_seen: 2026-05-18T18:24:08.900009
- Prior reference sessions mentioned by user:
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260518_040052_b7d0f6.json
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260518_182906_7c9791.json
  - /home/admin/.hermes/profiles/agent-alpha/sessions/session_20260518_025019_e2ea1e.json

## Captured article text

Anthropic brings Claude's learning mode to regular users and devs

For Claude Code users, it means the chatbot will explain its coding decisions.

This past spring, Anthropic introduced learning mode, a feature that changed Claude's interaction style. When enabled, the chatbot would, following a question, try to guide the user to their own solution, instead of providing them with an answer outright. Since its introduction in April, learning mode has only been available to Claude for Education users. Now, like OpenAI did with Study Mode, Anthropic is making the tool available to everyone.

Starting today, Claude.ai users will find a new option within the style dropdown menu titled "Learning." The experience here is similar to the one Anthropic offers with Claude for Education. When you turn learning mode on, the chatbot will employ a Socratic approach, trying to guide you through your question. However, unlike the real-life Socrates, who was famous for bombarding strangers with endless questions, you can turn off learning mode at any time.

Notably, Anthropic is also offering two different takes on the feature through Claude Code. First, there's an "Explanatory" mode where Claude will generate summaries of its decision-making process as it works, giving the user a chance to better understand what it's doing.

For those at the start of their coding career or hobby, there's also a more robust option, which is once again called "Learning." Here, Claude will occasionally stop what it's doing and mark a section with a "#TODO" comment to prompt the user to write five to 10 lines of their code. If you want to try the two features out for yourself, update to the latest version of Claude Code and type "/output-styles." You can then select between the two modes or Claude's default behavior.

According to Drew Bent, education lead at Anthropic, learning mode, particularly as it exists in Claude Code, is the company's attempt to make its chatbot into more of a collaborative tool. "I think it's great that there's a race between all of the AI labs to offer the best learning mode," he said. "In a similar way, I hope we can inspire something similar with coding agents."

Bent says the original learning mode came out of conversations Anthropic had with university students, who kept referring back to the concept of brain rot. "We found that they themselves realized that when they just copy and paste something directly from a chat bot, it's not good for their long-term learning," he said. When it came time to adapt the feature to Claude Code, the company wanted to balance the needs of new programmers with those like Bent who have been coding for a decade or more.

"Learning mode is designed to help all of those audiences not just complete tasks, but also help them grow and learn in the process and better understand their code base," Bent said. His hope is that the new tools will allow any coder to become a "really good engineering manager." In practice, that means those users won't necessarily write most of the code on a project, but they will develop a keen eye for how everything fits together and what sections of code might need some more work.

Looking forward, Bent says Anthropic doesn't "have all the answers, but needless to say, we're trying to think through other features we can build" that expand on what it's doing with learning mode. To that end, the company is opening up Claude Code's new Output Styles to developers, allowing them to build their own learning modes. Users too can modify how Claude communicates by creating their own custom prompts for the chatbot.

## Embedded links extracted from article

- https://www.engadget.com/ai/claudes-new-learning-mode-will-prompt-students-to-answer-questions-on-their-own-172057828.html — prior Engadget coverage of Claude Learning Mode for Education
- https://www.engadget.com/ai/chatgpts-study-mode-will-guide-students-to-an-answer-stey-by-step-180614172.html — Engadget coverage of OpenAI Study Mode comparison
- http://claude.ai/ — Claude consumer app
- https://www.anthropic.com/news/introducing-claude-for-education — Anthropic primary source for original Claude for Education / Learning Mode announcement
- https://www.anthropic.com/claude-code — Anthropic/Claude Code product page; redirects to https://claude.com/product/claude-code
- https://en.wikipedia.org/wiki/Brain_rot — contextual link for "brain rot"
- https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles — Anthropic support link; now redirects to https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills

## Source-check notes from embedded links

### Anthropic: Introducing Claude for Education

- URL inspected: https://www.anthropic.com/news/introducing-claude-for-education
- Date: Apr. 2, 2025
- Confirms Anthropic introduced "Learning mode" for Claude for Education.
- Describes Learning mode as a Claude experience that guides students' reasoning rather than providing answers.
- Mechanisms described: Socratic questioning, asking how the student would approach a problem, asking what evidence supports a conclusion, emphasizing core concepts, and offering study/research templates.
- This source does not itself confirm the later general-user rollout or Claude Code output styles.

### Claude Code product page and official docs

- Product URL inspected: https://www.anthropic.com/claude-code -> https://claude.com/product/claude-code
- Relevant docs inspected by linked-source follow-through:
  - https://code.claude.com/docs/en/overview
  - https://code.claude.com/docs/en/output-styles.md
  - https://code.claude.com/docs/en/changelog.md
- Product page describes Claude Code as an agentic coding tool that reads a codebase, edits files, runs commands, integrates with GitHub/GitLab/CLI tools, and can run locally in the terminal while asking permission before file changes/commands.
- Official output-styles docs confirm the Engadget-reported Claude Code feature:
  - Output styles change how Claude responds, not what it knows, by modifying the system prompt.
  - Built-in styles include Default, Proactive, Explanatory, and Learning.
  - Explanatory provides educational "Insights" while completing software-engineering tasks.
  - Learning is a collaborative learn-by-doing mode that shares insights and asks the human to implement small strategic pieces, inserting TODO(human) markers.
  - Output style can be selected via /config -> Output style and saved in .claude/settings.local.json as outputStyle; takes effect after /clear or a new session.
  - Custom output styles are Markdown files with frontmatter and can preserve built-in coding instructions with keep-coding-instructions: true.
  - Docs warn Explanatory and Learning produce longer outputs and higher token usage.
- Changelog confirms output styles, including Explanatory and Learning, released in Claude Code v1.0.81 on Aug. 14, 2025.

### Anthropic support: styles moving to skills

- Original URL inspected: https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles
- Current redirect: https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills
- Current page states Claude consumer "styles" are moving to skills.
- Custom styles are being migrated automatically into Claude skills.
- Default styles removed include Concise, Explanatory, and Formal; Learning is preserved as an installable skill.
- Styles menu will be removed after migration; existing styles remain until then.
- Migrated custom styles activate via slash commands like /concise-pirate-style.
- Relevance: validates a broader shift from hidden/persistent style state toward explicit skill/instruction bundles, but this support page is about Claude consumer personalization, not Claude Code output-styles configuration.

## Claims vs evidence

- Claim: Claude Learning Mode moved from Claude for Education to regular Claude users.
  - Evidence: Engadget reports it; the inspected Anthropic Education page only establishes the earlier Education origin. The currently inspected support page indicates consumer Learning survives as a skill, but the source is temporally later than Engadget and not a launch announcement.
  - Confidence: medium.
- Claim: Claude Code added Explanatory and Learning modes.
  - Evidence: official Claude Code docs and changelog confirm Output Styles with Explanatory and Learning released in v1.0.81 on Aug. 14, 2025.
  - Confidence: high.
- Claim: Learning mode uses Socratic / guided learning rather than direct answers.
  - Evidence: Anthropic Education announcement plus Claude Code output-styles docs confirm this pattern.
  - Confidence: high.
- Claim: Users/developers can create custom learning modes or communication styles.
  - Evidence: Claude Code docs confirm custom output styles; consumer support docs indicate styles are migrating to skills/instructions.
  - Confidence: high for Claude Code output styles; medium for consumer-product framing because the support page has changed since the article.

## Actionability classification

- source_type: article
- credibility_tier: secondary, with primary-source corroboration for the Claude Code mechanism
- evidence_grade: medium overall; strong for Claude Code output-styles mechanics, medium for general Claude user rollout due to changed support surface
- contradiction_notes: Engadget's support-link destination has changed; current Anthropic support page says styles are moving to skills and some default styles are removed. This complicates treating the article as current product guidance.
- classification: wiki-ingest / approval-proposal candidate, not implementation.

## Agent-engineering relevance

The durable signal is not the product launch itself. The reusable pattern is mode-level behavior control for coding agents:

- Separate response policy from domain knowledge and project context.
- Offer execution, explanatory, and human-in-the-loop learning modes over the same codebase/task substrate.
- Use system-prompt-level mode files or skills to change agent behavior.
- In learning/HITL mode, insert explicit human TODO markers and require the user to implement bounded sections rather than automating everything.
- Account for token/cost overhead when switching from terse execution to explanatory/tutorial behavior.
- Track the product-design shift from "styles" to explicit skills/instructions as a relevant comparison point for Hermes skills and Codex-local workflows.

## Recommended downstream Tolaria work

Create one knowledge-processing card for agent-beta:

- Ingest this raw source and linked primary docs into Tolaria.
- Promote/update knowledge around "agent output styles", "learning mode", and "human-in-the-loop coding-agent pedagogy".
- Compare Claude Code Output Styles against Hermes skills, system prompts, memory, and Codex local workflows.
- Produce an approval proposal only if a Hermes-facing behavior-mode abstraction or evaluation checklist seems worth adopting; no code/prototype/config changes without Overseer approval.
