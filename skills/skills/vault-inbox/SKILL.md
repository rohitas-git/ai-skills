---
name: vault-inbox
description: >
  Fast-capture notes into Rohitas's Notes Inbox while using agentic AI — no full
  ingest, no Concepts. Use when the user says add to inbox, capture this, quick
  vault note, inbox dump, save for later, or /vault-inbox. Loads rohitas-vault-wiki
  for path and naming only. Process later with vault-ingest.
---

# Vault Inbox

**Purpose:** Store information on the go. Capture only — do not classify, distill, or write Concepts.

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.
**Schema:** load **`rohitas-vault-wiki`** (`references/vault-profile.md`) for path + Title Case naming only.

## When to use

- Mid-session agent work: “save this for the vault”
- Quick dumps, quotes, URLs, meeting scraps
- Explicit `/vault-inbox`

**Do not use** for full knowledge compilation → **`vault-ingest`**.  
**Do not use** for teaching a concept → **`vault-explain`**.

## Workflow

1. Resolve vault root (default above unless user overrides).
2. Load rohitas-vault-wiki naming rules only — **skip** full ingest pipeline.
3. Choose filename:
   - User-provided title → Title Case + `.md`
   - Clear first heading/line → Title Case slug
   - Unstructured dump → `YYYY-MM-DD HHMM Capture.md` (local date/time)
4. Write **one** file under `Inbox/`:

```markdown
---
created: YYYY-MM-DD
source: chat | url | agent
tags: []
---

{body largely as provided — capture, not polish}

## Related
- {only if user named links}
```

5. Reply:

```markdown
## Captured
- Path: `Inbox/<Name>.md`
- Process later: `/vault-ingest` on this file (or “process Inbox”)
```

## Completion criterion

- File exists at `Inbox/<Name>.md`
- **No** writes to `Concepts/`, `Atlas/`, Registry, or Archives
- No takeaway debate or resource-summarizer unless user asked to process now (then hand off to `vault-ingest`)

## Hard rules

1. Friction minimal — write first.
2. Never invent Concepts or MOCs here.
3. Do not empty or “process” Inbox under this skill.
4. English optional for capture body; permanent English applies at ingest time.
5. Schema ownership stays with `rohitas-vault-wiki`.

## Related skills

| Skill | When |
|-------|------|
| `rohitas-vault-wiki` | Path, folders, naming |
| `vault-ingest` | Compile Inbox → Concepts |
| `vault-lint` | Inbox backlog health |
| `wiki-query` | Answer from vault (not capture) |

See also: `references/inbox-note-format.md`.
