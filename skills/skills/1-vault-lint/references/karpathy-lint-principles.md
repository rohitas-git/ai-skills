# Karpathy lint principles (adapted)

From [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): periodically ask the LLM to health-check the wiki.

## Look for

- Contradictions between pages  
- Stale claims superseded by newer sources  
- Orphan pages with no inbound links  
- Important concepts mentioned but lacking their own page  
- Missing cross-references  
- Data gaps that could be filled with a source or web research  

Also useful: suggest new questions to investigate and sources to seek.

## This vault’s stance

- **Report first** — agent suggests; human approves fixes  
- Compiled truth lives in **Concepts**, not chat  
- Lint complements **ingest** (arrival) and **query** (use)  
- After lint, high-value follow-ups often are: `1-vault-ingest`, `1-wiki-query`, `1-vault-explain`
