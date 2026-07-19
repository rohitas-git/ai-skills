---
name: vault-lint
description: >
  Health-check Rohitas's Notes vault: broken wikilinks, orphans, misplaced hubs,
  frontmatter, contradictions, duplicates, Registry drift. Report-only by default.
  Use when the user says lint vault, health check notes, find contradictions,
  orphan notes, wiki audit, or /vault-lint. Loads rohitas-vault-wiki for schema.
---

# Vault Lint

LLM Wiki **Lint** op: periodic health check of the compiled vault.

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.
**Schema:** load **`rohitas-vault-wiki`**.  
**Default:** **report only** — no auto-fix unless user says “fix”.

## When to use

- After large ingests  
- Weekly GC / Sunday maintenance  
- Explicit `/vault-lint` or “audit the vault”

## Workflow

1. Confirm vault path; load vault-profile + hard rules.  
2. Run checklist in `references/lint-checklist.md` (sample smartly if vault is large — prioritize Registry areas + recent Ingest Log).  
3. Produce report (template below).  
4. Suggest next actions: fix (with confirm), re-ingest, `wiki-query`, `vault-explain`.  
5. Optional: append one line to Ingest Log or `Archives/Lint Log.md` only if user wants logging.

## Report format

```markdown
## Vault lint — YYYY-MM-DD

### Critical
1. …

### Hygiene
1. …

### Knowledge gaps / contradictions
1. …

### Suggested next actions
- Fix: …
- Ingest: …
- Query: …
- Explain: …
```

Each finding: **what** + **where** + **suggested fix**. Do not apply fixes unless asked.

## Fix pass (only if requested)

1. Show planned edits  
2. Confirm  
3. Apply using `rohitas-vault-wiki` rules  
4. Log  

## Completion criterion

- Numbered findings with suggestions  
- Zero silent vault mutations unless user requested and approved a fix pass  

## References

- `references/lint-checklist.md`
- `references/karpathy-lint-principles.md`
- Schema: `rohitas-vault-wiki`
