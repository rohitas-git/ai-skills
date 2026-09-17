# Query workflow (0-butler)

Answer: **which domain hub / skill / flow?**

## Inputs only

1. **flows.md** — hub map, pipelines, forks (domain SSOT)
2. **route-index.md** — generated leaf skim (`when` / `not_when` / hub / next); prefer over opening every `SKILL.md`
3. Selected on-disk `SKILL.md` (authoritative validation after shortlist)
4. User utterance; pinned read-only repository evidence only if route-relevant

Skill route surface (authors): `0-skill-manager/references/skill-route-surface.md` — description contract + `metadata.catalog` only (no top-level route YAML).

**Never invent** skills. Missing skill → offer **`/0-skill-manager` ingest**.

## Algorithm

1. Strip a valid `??` prefix; never consume `???`.
2. Filter route-index rows against When, Not-for, and triggers. If one direct skill
   clearly matches, shortlist it before doing domain-level branching.
3. If several domains remain materially plausible, ask **F7** once with the best
   evidence-backed recommendation and **Agent judgment**. Otherwise do not ask.
4. Validate the shortlisted skill directory and frontmatter on disk, then read its
   complete `SKILL.md`. The live file wins over stale generated prose.
5. Name the owning **★ domain hub** for orientation and the smallest applicable
   child as **Use**. Do not invoke the hub first when the child is already clear.
6. Add one “why not” cousin only when it clarifies a real collision.
7. Return the route and first action; do not execute the selected workflow.

If route-index is missing or stale, use flows to shortlist and validate every
recommendation against the live skill file. Missing setup documents are not an
automatic Setup detour; route setup only when the request is configuration work.

## Mutation intent

If the user wants catalog CRUD, placement, lint, installation, sync, or a new hub,
return `/0-skill-manager`. Skill-body authoring returns `/0-skill-creator`. Stop
after the route; the delegated skill owns all writes and verification.

## Output template

```markdown
**Domain hub:** `/…`
**Use:** `/…`
**Why:** … (cite When / route-index when helpful)
**Why not:** `/cousin` — … (optional)
**Fork:** … (if waiting on user)
**Next:** …
```

## Smoke

| Utterance | Expected |
|-----------|----------|
| which skill / lost | 0-butler orient + F7 or hub list |
| grill me | Design hub `0-grilling` / grill-* after F2 |
| 0-implement tickets | Ship hub `0-implement` |
| add a skill to the catalog | **skill-manager** (delegate) |
| lint the catalog | **skill-manager** |
| put this in my vault | Vault hub `0-rohitas-vault-wiki` / vault-* |
| make a spreadsheet | Misc hub `0-office` → 1-xlsx (F-misc if ambiguous) |
| red-green / tdd this | `1-tdd` under `0-implement` (not 1-code-review) |
| which skill for incoming issues | `0-triage` (opt-in intake; not to-tickets) |
| direct request matching one skill | report its hub + skill; no F7 and no parent invocation |
| no reusable skill is needed | say no skill is necessary; answer through the normal task path |
