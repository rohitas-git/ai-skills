# Merge and contradiction handling

## Prefer merge over duplicate

When an existing Concept covers the same idea:

1. Read the full existing note  
2. List **additive** facts (new, non-conflicting)  
3. List **conflicts** (cannot both be true without context)  
4. Propose merge of additive content only after plan confirm  
5. Preserve the note’s voice; do not wholesale replace  

Bump `updated` on every edit.

## Additive merge pattern

```markdown
## {existing section}
{keep existing}

{new bullets clearly integrated, own-words}

## Sources
- [[Prior Source]]
- [[New Source (Source)]]  ; or URL in frontmatter
```

Optional callout for evolution:

```markdown
> [!note] Updated YYYY-MM-DD
> Added: {one-line delta from latest source}
```

## Contradiction table

When claims disagree:

```markdown
## Inconsistencies
| Claim (new) | Existing note | Existing claim | Options |
|-------------|----------------|----------------|---------|
| "X is always Y" | [[Concept]] | "X is usually Z" | keep old / prefer new / both with context |
```

### Resolution options

| User choice | Write |
|-------------|--------|
| keep old | Do not apply conflicting claim; log that new source was considered |
| prefer new | Replace/annotate old claim; note supersession + source |
| both with context | Keep both under conditions (when/domain); never leave bare contradiction |

Never pick silently.

## Near-duplicates

If two Concepts overlap heavily, prefer:

1. Merge into the stronger title  
2. Leave redirect-style note or aliases  
3. Or link both with explicit scope boundaries  

Do not create a third overlapping atom.

## Multi-source concepts

Concept page is the compiled truth. Note differing viewpoints with citations to Source archives. See hard rules: no invention.
