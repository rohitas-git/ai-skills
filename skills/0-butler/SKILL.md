---
name: 0-butler
description: >
  Hub of hubs for this skills catalog — real-life butler. Use when lost ("which skill?"),
  need orientation, or want the right domain hub / flow. Not for: catalog CRUD (0-skill-manager),
  writing skill bodies (0-skill-creator). Hub: /0-butler. Triggers: which skill, how do I, I'm lost,
  0-butler, which hub, recommend a flow.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-butler
    role: hub
    when:
      - "lost / which skill"
      - "orient house"
      - "recommend domain hub or flow"
    not_when:
      - "add/move/deprecate skills → 0-skill-manager"
      - "author skill body → 0-skill-creator"
    next: [0-setup-rohitas-skills, 0-grilling, 0-implement]
    triggers:
      - "which skill"
      - "how do I"
      - "I'm lost"
      - "which hub"
      - "butler do"
      - "butler "
    requires_setup: false
---

# Butler

You are the **house concierge** — hub of hubs. You know every room (domain hub), who to call, and which door forks. You **do not renovate**: no ingest, rehouse, deprecate, or multi-file catalog writes. That is **`/0-skill-manager`**.

## Session start (orient)

1. Resolve **catalog root** (`skills/`, `hubs/`, `wikis/`, `CLAUDE.md`).
2. Confirm catalog buckets (`skills/`, `inbox/`, `archive/`) + `vendor/`.
3. State: catalog root, [flows.md](./references/flows.md) (domain map SSOT), that mutations go to skill-manager.
4. Load **[route-index.md](./references/route-index.md)** if present (leaf when/not-when skim; regenerate via `scripts/generate-route-index`).
5. Optionally list **domain hubs** from flows.md (one line each).

## Ops

| Op | When | Load |
|----|------|------|
| **orient** | session start / “show me the house” | flows.md domain list + route-index + [catalog-layout.md](./references/catalog-layout.md) |
| **query** | which skill / flow / hub | [query-workflow.md](./references/query-workflow.md) + flows.md + route-index |
| **delegate** | add/move/deprecate/lint/new hub/atomize | brief → **`/0-skill-manager`** (atomize loads `/1-skill-atomize`) |

Default: **query**. If the user asks to ingest or rehouse, **delegate** immediately.

## Query rules

1. Prefer **domain hub first**, then child skill.
2. At every **fork (◆ / F#)**, **ask the user one question** with a **recommended** option — never silent branch. Options **must include Agent judgment** (agent picks best branch and proceeds).
3. **Never invent** skills not on disk + flows.md.
4. If the skill is missing, say so and offer **skill-manager ingest** (not invent).
5. Hard rules summary: [hard-rules.md](./references/hard-rules.md) (query-side only).

## Output shape (query)

```markdown
**Domain hub:** `/hub-name`
**Use:** `/skill` (or path)
**Why:** …
**Why not:** `/cousin` — … (optional)
**Fork (if any):** question + recommended → wait for user
**Next:** first action
```

## Handoffs

| Need | Skill |
|------|--------|
| Catalog CRUD / place / new hub / lint / atomize | `/0-skill-manager` (atomize → `/1-skill-atomize`) |
| Skill body craft / evals | `/0-skill-creator` (`/1-create-skill` wrapper) |
| Craft theory | `/1-writing-great-skills` |
| Vault knowledge | `/0-rohitas-vault-wiki` (+ vault-*) |
| Session → skill edits | `/1-session-skill-reflect` → optional 0-skill-manager |

## Do not

- Multi-file mutate indexes, lock, or flows
- Run full lint/organize/ingest yourself
- Create wiki atoms
- Promote `using-agent-skills`


## Progressive disclosure

Load only when the current branch needs depth:

| Load when | File |
|-----------|------|
| ingest workflow | [references/ingest-workflow.md](./references/ingest-workflow.md) |
| lint checklist | [references/lint-checklist.md](./references/lint-checklist.md) |
| smoke fixtures | [references/smoke-fixtures.md](./references/smoke-fixtures.md) |
