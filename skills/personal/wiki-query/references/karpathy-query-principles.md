# Karpathy LLM Wiki — Query principles

Source: [llm-wiki.md gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and common community implementations (2026).

## Query is a core operation

Alongside **ingest** and **lint**, **query** is first-class:

> You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. … **Good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn’t disappear into chat history.

## Compiled knowledge vs RAG

| RAG-style | LLM Wiki query |
|-----------|----------------|
| Re-chunk raw docs every time | Read already-synthesized wiki pages |
| No accumulation of answers | Filed queries become part of the corpus |
| Index = embeddings of blobs | Index = human-readable catalog of pages |

The wiki is a **persistent, compounding artifact**. Cross-references and contradictions should already live on pages when possible.

## Index-first retrieval

From the gist:

- **`index.md` is content-oriented** — catalog with links + one-line summaries  
- On query, the LLM **reads the index first**, then drills into pages  
- Works well at moderate scale (~hundreds of pages) without embedding RAG  
- At larger scale, add search (e.g. hybrid BM25/vector); still start with index  

In Rohitas vault: **`README.md` + Atlas MOCs** play the index role.

## Logging

**`log.md` is chronological** — append-only record of ingests, **queries**, lint passes.

Greppable entries help both human and agent:

```text
## [YYYY-MM-DD] query | short title
```

## What “good” query behavior looks like

1. Don’t invent wiki content  
2. Cite pages with wikilinks  
3. Prefer synthesis over pasting long source text  
4. File comparisons and deep answers; skip trivial lookups  
5. Suggest new sources or open questions when the wiki is thin (lint-adjacent)

## Optional scale path

Community practice once past a few hundred pages:

- Keep a master index with one-liners  
- Add local search (FTS / hybrid) rather than pure embedding-RAG product stacks  
- Still: index/MOC first, then targeted page reads  

## Division of labor

- **Human:** sources, questions, judgment  
- **LLM:** find pages, synthesize, file, bookkeeping  
