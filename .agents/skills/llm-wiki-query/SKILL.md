---
name: llm-wiki-query
description: Answer questions using the LLM Wiki knowledge base as the primary source. Use when the operator asks a question that should be answered from the wiki, such as "what do we know about X", "summarize Y", or "compare A and B". The agent reads the index, finds relevant pages, synthesizes an answer with wikilink citations, and optionally files reusable answers as synthesis pages. Trigger keywords: "query", "question", "what do we know", "summarize", "compare", "search wiki", "look up".
---

# Skill: Query

## When to Use

Use this skill when the operator asks a question that should be answered using the wiki as the primary knowledge source.

## Inputs

- The operator's question.
- Optional: preferred output format (markdown, table, slides, chart).

## Step-by-Step Process

1. **Read `wiki/index.md`**.
   - Identify relevant page categories (entities, concepts, sources, syntheses).
   - Note page names and summaries that seem relevant.

2. **Read relevant pages**.
   - Start with the most directly relevant pages.
   - Follow wikilinks to related pages as needed.
   - Read source pages for primary evidence.

3. **Synthesize an answer**.
   - Combine information from multiple pages.
   - Use wikilinks to cite sources: `[[Page Name]]` or `[[Page Name|display text]]`.
   - Note any contradictions or gaps in the wiki's coverage.
   - Choose the best output format for the question: markdown prose, comparison table, Marp slides, matplotlib chart, or canvas.

4. **Present the answer to the operator**.
   - Start with a direct answer.
   - Follow with supporting evidence and citations.
   - Mention any gaps or uncertainties.

5. **Decide whether to file the answer**.
   - If the answer is reusable or represents new synthesis, ask the operator if they want it filed.
   - If yes, create a synthesis page in `wiki/syntheses/`.
   - Filename: `YYYY-MM-DD--question-slug.md`
   - Follow the template in `wiki/templates/synthesis.md`.
   - Run `python3 scripts/rebuild_index.py`, then update `wiki/log.md`.

## Output Contract

- Answer is supported by cited wiki pages.
- Citations use wikilink syntax.
- Gaps or uncertainties are noted.
- If filed, synthesis page exists and is linked from index and log.

## Guardrails

- Do not hallucinate information not present in the wiki.
- If the wiki doesn't contain enough information, say so and suggest sources to ingest.
- Always cite sources; never make uncited claims.
- If the answer reveals a contradiction in the wiki, flag it.

## When to File an Answer

File the answer as a synthesis page if:
- The answer is likely to be useful for future queries.
- It synthesizes information from multiple sources in a novel way.
- The operator explicitly asks for it to be saved.

Do not file if:
- The answer is trivial or one-off.
- It does not add new synthesis beyond what is already in the wiki.

## Verification Checklist

- [ ] `wiki/index.md` was read.
- [ ] Relevant pages were read and cited.
- [ ] Answer is presented with citations.
- [ ] If filed, synthesis page created in `wiki/syntheses/`.
- [ ] `python3 scripts/rebuild_index.py` run (if pages changed) and `wiki/log.md` updated.
