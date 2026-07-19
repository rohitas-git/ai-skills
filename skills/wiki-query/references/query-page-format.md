# Filed query page format

Path: `Queries/{Title Case}.md`  
`type: query` is only for this folder (not Concepts hubs).

```markdown
---
type: query
status: incubating
tags:
  - query
  - system-design
created: YYYY-MM-DD
updated: YYYY-MM-DD
topic: System Design
question: "Original user question in one sentence"
---

# {Title}

**Question:** {full question}

**Answered:** YYYY-MM-DD  
**Confidence:** high | medium | low

## Answer

{synthesis — short paragraphs or table}

## Sources consulted

- [[Concept A]] — …
- [[Concept B]] — …
- [[Some MOC]] — navigation

## Gaps & open questions

- …

## Related

- [[System Design MOC]]  # parent hub
- [[Write-Through Cache]]
- …
```

## Naming

- Title Case with spaces  
- Prefer outcome names: `Write-Through vs Write-Back Decision.md`  
- Avoid `Query 1.md`

## When to promote to Concepts

If the answer is the new canonical teaching on a single idea, create/update a **Concept** with `rohitas-vault-wiki` / Note Templates and leave the Query page as a trail of “how we got here,” or merge and archive the query.
