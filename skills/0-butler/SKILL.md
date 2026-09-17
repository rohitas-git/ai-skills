---
name: 0-butler
description: >
  Shortcut `??`: route an ambiguous, cross-domain, or explicit catalog question to
  one existing hub, skill, or flow. Use when no direct skill is an obvious match.
  Not for: a clear direct-skill request, `???` explanations (1-explain-with-example),
  catalog CRUD (0-skill-manager), or skill authoring (0-skill-creator). Hub: /0-butler.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-butler
    role: hub
    when:
      - "explicit catalog routing or house orientation"
      - "request is ambiguous, spans domains, or has no obvious direct skill"
      - "message is exactly ?? or begins with ?? followed by whitespace; ??? is excluded"
    not_when:
      - "one available skill directly matches → use that skill"
      - "message begins ??? → 1-explain-with-example"
      - "add/move/deprecate skills → 0-skill-manager"
      - "author skill body → 0-skill-creator"
    next: [0-setup-rohitas-skills, 0-grilling, 0-implement, 0-review, 0-triage, 0-diagnosing-bugs, 0-wayfinder, 0-improve-codebase-architecture, 0-rohitas-vault-wiki, 0-skill-manager, 0-skill-creator, 0-ponytail, 0-learn, 0-office, 0-ui-ux, 0-thinking, 0-git, 0-agent-engineering, 0-devops, 0-marketing, 1-grok-help, 1-context-monitor, 1-strategic-compact, 1-response-effort-calibrator, 1-action-first-output, 1-caveman, 1-handoff, 1-bro, 1-plow-ahead, 1-quick-recap, 1-rewind, 1-webmcp, 1-pi-agent-rust]
    triggers:
      - "which skill"
      - "I'm lost"
      - "which hub"
      - "route this request"
      - "show the skill house"
      - "??"
    requires_setup: false
---
# Butler

**Atomic job:** select and report one existing catalog route, then stop. Report the
owning domain, but use the smallest directly applicable skill; catalog writes belong to `/0-skill-manager`.

## Shortcut

`?? <request>` is an explicit Butler query, equivalent to invoking `$0-butler`.

- Match `??` only when it is the entire trimmed message or is followed by whitespace.
- Never claim `???`; that longer prefix belongs to `/1-explain-with-example`.
- Remove the shortcut prefix before classifying and routing the remaining request.

## Input and evidence boundary

- Use only the user's request, this installed catalog's [flows.md](./references/flows.md),
  generated [route-index.md](./references/route-index.md), and the selected live
  `SKILL.md`. Treat the selected skill file as authoritative when projections differ.
- Routing is read-only. It creates no worktree, edits no file, calls no external
  service, and changes no task state. A worktree is not applicable.
- Inspect repository context only when it materially disambiguates the route; pin
  the repository/worktree first and do not mutate it.

## Ops

| Op | When | Load |
|----|------|------|
| **orient** | explicit “show me the house” or bare `??` | flows.md domain list + route-index + [catalog-layout.md](./references/catalog-layout.md) |
| **query** | which skill / flow / hub | [query-workflow.md](./references/query-workflow.md) + flows.md + route-index |
| **delegate** | add, move, deprecate, lint, new hub, or atomize | one-line brief → **`/0-skill-manager`** (atomize → `/1-skill-atomize`) |

Default after explicit invocation: **query**. Do not activate Butler merely because
a new session started. If the user asks to ingest or rehouse, delegate and stop.

## Dispatch

1. If one route-index row directly matches and no exclusion applies, select that
   skill without invoking its parent hub. Still report the owning domain hub.
2. Use **F7** only when a material domain choice remains. A fork that does not
   affect the route does not apply. Ask one question with a grounded recommended
   option and include **Agent judgment**.
3. Validate the selected skill on disk and read its complete `SKILL.md` before
   recommending it. Never invent a path from prose or a stale projection.
4. If no skill is needed, say so. If a reusable capability is genuinely missing,
   offer `/0-skill-creator` and `/0-skill-manager`; never create one by default.
5. Apply [hard-rules.md](./references/hard-rules.md).

## Output shape (query)

```markdown
**Domain hub:** `/hub-name`
**Use:** `/skill` (or path)
**Why:** …
**Why not:** `/cousin` — … (optional)
**Fork (if any):** question + recommended → wait for user
**Next:** first action
```

Return routing control to the user/caller. Do not execute the selected skill,
start its workflow, create a plan, or mutate the catalog in this invocation.

## Boundary

| Need | Skill |
|------|--------|
| Route a request to an existing catalog path | **`/0-butler` (this)** |
| Catalog CRUD / place / new hub / lint / atomize | `/0-skill-manager` (atomize → `/1-skill-atomize`) |
| Skill body craft / evals | `/0-skill-creator` (`/1-create-skill` wrapper) |
| Craft theory | `/1-writing-great-skills` |
| Vault knowledge | `/0-rohitas-vault-wiki` (+ vault-*) |
| Session → skill edits | `/1-session-skill-reflect` → optional 0-skill-manager |

## Hard boundary

- Mutate skills, indexes, locks, flows, hub artifacts, or wiki files
- Run lint, organize, ingest, install, sync, or other catalog operations
- Create wiki atoms
- Promote `using-agent-skills`

## Progressive disclosure

Load only when the current branch needs depth:

| Load when | File |
|-----------|------|
| orientation needs layout detail | [references/catalog-layout.md](./references/catalog-layout.md) |
| selecting a route | [query workflow](./references/query-workflow.md); tooling/evaluation only: [machine projection](./references/route-index.json) |
| resolving a query-side rule | [references/hard-rules.md](./references/hard-rules.md) |
