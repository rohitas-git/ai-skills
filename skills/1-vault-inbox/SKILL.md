---
name: 1-vault-inbox
description: >
  Fast-capture into vault Inbox — no full ingest. Use for add to inbox, capture this,
  save for later. Not for: compile into Concepts (1-vault-ingest). Hub: /0-rohitas-vault-wiki.
  Triggers: add to inbox, capture this, quick vault note.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-rohitas-vault-wiki
    role: pipeline
    when:
      - "fast capture to Inbox"
      - "no Concept compile yet"
    not_when:
      - "full ingest to Concepts → 1-vault-ingest"
    next: [1-vault-ingest]
    triggers:
      - "add to inbox"
      - "capture this"
      - "quick vault note"
      - "1-vault-inbox"
    requires_setup: false
---

# Vault Inbox

**Purpose:** Store information on the go. Capture only — do not classify, distill, or write Concepts.

**Vault root:** resolve from SSOT only — consumer repo `docs/agents/vault.md` (written by `/0-setup-rohitas-skills`), or the `## Agent skills` vault pointer. Do **not** hard-code a home path in this skill. If unset, ask once and offer to write the SSOT.
**Schema:** load **`0-rohitas-vault-wiki`** (`references/vault-profile.md`) for path + Title Case naming only.

## When to use

- Mid-session agent work: “save this for the vault”
- Quick dumps, quotes, URLs, meeting scraps
- Explicit `/1-vault-inbox`

**Do not use** for full knowledge compilation → **`1-vault-ingest`**.  
**Do not use** for teaching a concept → **`1-vault-explain`**.

## Workflow

1. Resolve vault root (default above unless user overrides).
2. Load 0-rohitas-vault-wiki naming rules only — **skip** full ingest pipeline.
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
- Process later: `/1-vault-ingest` on this file (or “process Inbox”)
```

## Completion criterion

- File exists at `Inbox/<Name>.md`
- **No** writes to `Concepts/`, `Atlas/`, Registry, or Archives
- No takeaway debate or 1-resource-summarizer unless user asked to process now (then hand off to `1-vault-ingest`)

## Hard rules

1. Friction minimal — write first.
2. Never invent Concepts or MOCs here.
3. Do not empty or “process” Inbox under this skill.
4. English optional for capture body; permanent English applies at ingest time.
5. Schema ownership stays with `0-rohitas-vault-wiki`.

## Related skills

| Skill | When |
|-------|------|
| `0-rohitas-vault-wiki` | Path, folders, naming |
| `1-vault-ingest` | Compile Inbox → Concepts |
| `1-vault-lint` | Inbox backlog health |
| `1-wiki-query` | Answer from vault (not capture) |

See also: `references/inbox-note-format.md`.
