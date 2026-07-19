# Explain from Concept (binding for 1-learning-explainer)

## Resolve path

```
Concepts/{Title Case}.md
```

If missing, search:

```bash
rg -n -i 'title-or-keywords' Concepts --glob '*.md'
```

Prefer exact Title Case filename match.

## Context pack for 1-learning-explainer

Pass as the “resource” to explain:

1. Full body of the Concept (after frontmatter)  
2. Title + `topic` + tags from frontmatter  
3. Optional: 5–15 lines from parent MOC describing this node  
4. Optional: titles of `## Related` links (not full dump of all neighbors)

Do **not** dump the entire Atlas or vault.

## Prompt pattern to self

> Using **learning-explainer**, explain the vault Concept below. Ground in this note first. Label any expansion as not in vault. Resource:

```markdown
# {Title}
topic: …
{body}
```

## After explanation

If user says “add that analogy to the note” → switch to **vault-ingest** / schema skill with a small update plan.  
If user says “I still don’t get X” → progressive deep-dive inside 1-learning-explainer, still grounded.  
If the vault note is thin → say so; offer ROOT deepen or new source ingest.
