[中文](./README.zh-CN.md)

# LLM Wiki

A personal knowledge base maintained by LLM agents, following the pattern described in [Karpathy's LLM Wiki](https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md). The `wiki/` tree conforms to the [Open Knowledge Format (OKF)](./SPEC.md) v0.1.

**The core metaphor:** Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase. You browse the results in real time — following links, checking the graph view, reading updated pages. The LLM does all the grunt work: summarizing, cross-referencing, filing, and bookkeeping.

## Use Cases

This pattern applies anywhere you're accumulating knowledge over time and want it organized rather than scattered:

- **Personal**: tracking goals, health, psychology — filing journal entries, articles, podcast notes, building a structured picture of yourself over time.
- **Research**: going deep on a topic over weeks — reading papers, articles, reports, incrementally building a comprehensive wiki with an evolving thesis.
- **Reading a book**: filing each chapter, building pages for characters, themes, plot threads. By the end you have a rich companion wiki (think [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page)).
- **Business/team**: internal wiki fed by Slack threads, meeting transcripts, project docs, customer calls. The LLM does the maintenance no one wants to do.
- **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives** — anything where knowledge compounds.

## Quick Start

### 1. Add a Source

Drop a file into `raw/sources/` (e.g., an article, paper, or transcript). Then tell your LLM agent:

> "Ingest the source `raw/sources/my-article.md`."

The agent will:
- Read the source
- Discuss key takeaways with you
- Create a summary in `wiki/sources/`
- Update relevant entity and concept pages
- Update the index and log

### 2. Ask a Question

> "What do we know about [topic] so far?"

The agent will:
- Search `wiki/index.md` for relevant pages
- Read and synthesize information from multiple pages
- Cite sources using Obsidian wikilinks
- Offer to file the answer as a new synthesis page if it's reusable

### 3. Health Check

> "Lint the wiki."

The agent will:
- Scan for contradictions, stale claims, orphan pages, and missing cross-references
- Produce a report with severity ratings
- Discuss and apply fixes with you

## Project Structure

```
LLM-wiki/
├── AGENTS.md          # Schema and conventions (the "system prompt")
├── SPEC.md            # Open Knowledge Format (OKF) v0.1 spec the wiki conforms to.
├── README.md          # This file
├── raw/               # Your immutable source documents
│   ├── sources/       # Text sources
│   └── assets/        # Images, data files
├── wiki/              # LLM-maintained knowledge base
│   ├── index.md       # Content catalog
│   ├── log.md         # Timeline of all operations
│   ├── entities/      # Concrete things
│   ├── concepts/      # Abstract ideas
│   ├── sources/       # Source summaries
│   ├── syntheses/     # Cross-source analysis
│   └── templates/     # Reusable page templates
└── .agents/            # Project-level skill definitions
    └── skills/
        ├── llm-wiki-ingest/   # Ingest workflow skill
        ├── llm-wiki-query/    # Query workflow skill
        └── llm-wiki-lint/     # Lint workflow skill
```

## Workflows

The three core workflows are documented as skills in `.agents/skills/`:

- **`.agents/skills/llm-wiki-ingest/SKILL.md`** — How to add a new source to the wiki
- **`.agents/skills/llm-wiki-query/SKILL.md`** — How to answer questions using the wiki
- **`.agents/skills/llm-wiki-lint/SKILL.md`** — How to health-check the wiki

The skills enforce the schema defined in `AGENTS.md` and maintain `wiki/index.md` / `wiki/log.md` on every operation — there are no helper scripts to run.

## Tips

### Obsidian Setup

- **Open `wiki/` in Obsidian** for the best browsing experience. The graph view shows connections between pages — what's connected, which pages are hubs, which are orphans.
- **Graph View**: The best way to see the shape of your wiki. Enable it in the left sidebar.
- **Web Clipper**: Install the [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension to save web articles directly to `raw/sources/` as markdown.
- **Download images locally**: In Obsidian Settings → Files and links, set "Attachment folder path" to `raw/assets/`. Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey — all images get downloaded to local disk so the LLM can view them directly instead of relying on URLs that may break.
- **Dataview plugin**: Install [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) to query page frontmatter. Since the LLM adds YAML frontmatter (tags, dates, source counts) to every page, Dataview can generate dynamic tables and lists across the wiki.
- **Marp plugin**: Install [Marp](https://marp.app/) for Obsidian to render markdown slide decks. Useful for generating presentations directly from wiki content — answers to queries can be output as slides.

### Query Output Formats

Answers can take different forms depending on the question:
- **Markdown page** — standard prose with citations
- **Comparison table** — side-by-side analysis
- **Slide deck (Marp)** — for presentations or sharing
- **Chart (matplotlib)** — for data visualization
- **Canvas** — for visual relationship mapping

The important insight: **good answers can be filed back into the wiki as new synthesis pages.** A comparison, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. Your explorations compound in the knowledge base just like ingested sources do.

### Version Control

This is just a git repo of markdown files. You get version history, branching, and collaboration for free. Commit regularly. The wiki is code — treat it like one.

### General

- **Templates**: Use the templates in `wiki/templates/` as starting points for new pages.
- **Ingestion style**: Work interactively. Read summaries, check updates, guide the LLM on what to emphasize. You can also batch-ingest with less supervision — develop the workflow that fits your style.

## Tools

- **[qmd](https://github.com/tobi/qmd)** (optional): Local search engine for markdown with hybrid BM25/vector search and LLM re-ranking, all on-device. Has both a CLI (so the LLM can shell out to it) and an MCP server (native tool integration). At small scale the index file is enough; as the wiki grows, qmd becomes valuable.

## Philosophy

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting contradictions, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.

The human curates sources, directs the analysis, asks good questions, and thinks about what it all means. The LLM does everything else.
