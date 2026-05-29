---
type: entity
aliases: ["Google NotebookLM", "Notebook LM"]
tags: [knowledge-system, notebook, retrieval]
created: 2026-05-28
updated: 2026-05-28
source_count: 1
---

# NotebookLM

## Identity
NotebookLM is presented in the source as a curated notebook store that can be queried by an agent through MCP rather than relying on open-web retrieval.

## Aliases
- Google NotebookLM
- Notebook LM

## Key Attributes
- Role in claim: backing store for personal/curated knowledge
- Claimed result: fewer hallucinations by grounding on user-selected sources
- Verification status in current evidence: unverified in this card; only social assertions are available

## Evidence
- [[2026-05-28--ibuzovskyi-hermes-notebooklm-mcp-claim|X post claim summary]] includes claims about querying notebooks and long-term knowledge accumulation.
- [[2026-05-28--hermes-notebooklm-mcp-claim-assessment|Assessment]] notes the linked article is login-gated and the GitHub target is unresolved.

## Related
- [[Hermes Agent]]
- [[Notebook-grounded Retrieval via MCP]]
- [[2026-05-28--hermes-notebooklm-mcp-claim-assessment]]

## Open Questions
- Is there a public, maintained NotebookLM MCP server/repo with install docs?
- What trust/verification controls are available for notebook ingestion and citation?