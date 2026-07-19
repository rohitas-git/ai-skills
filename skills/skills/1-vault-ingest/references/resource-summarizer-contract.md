# 1-resource-summarizer contract (1-vault-ingest)

**Do not reimplement** summarizer techniques in this skill. **Load and follow** the **`1-resource-summarizer`** skill.

## Gate

| Material | Action |
|----------|--------|
| \>~40 lines **or** multi-heading dump **or** long URL body | **Mandatory:** load `1-resource-summarizer` |
| ~15–40 lines | Light Feynman rewrite + bullets (summarizer techniques OK without full skill dump) |
| \<~15 lines, one idea | Place + frontmatter only — skip full summarizer |
| Hub / MOC gloss only | No body rewrite |

## Mapping summarizer → vault Concept

From summarizer output, keep:

| Summarizer product | Vault placement |
|--------------------|-----------------|
| Executive summary | Concept lead / overview |
| Key takeaways | Bullets under main sections |
| Feynman explanations | Own-words concept body |
| Gaps & questions | `## Open questions` or incubating stubs |
| Action items | Only if durable strategy — else skip |
| Full Cornell cues / 0-review prompts | **Drop** from permanent notes |

## Ownership

- **resource-summarizer** — prose quality of the distill  
- **rohitas-vault-wiki / vault-ingest** — path, Title Case name, frontmatter, MOC links, archive, log  

## Invocation language (for the agent)

> Load skill **resource-summarizer**. Distill this source with 80/20 + Feynman own-words + 5–10 takeaways + gaps. I will map the result into Rohitas Concepts (no Cornell template).
