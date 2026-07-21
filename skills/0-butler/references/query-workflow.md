# Query workflow (0-butler)

Answer: **which domain hub / skill / flow?**

## Inputs only

1. **flows.md** — hub map, pipelines, forks (domain SSOT)
2. **route-index.md** — generated leaf skim (`when` / `not_when` / hub / next); prefer over opening every `SKILL.md`
3. Bucket READMEs + on-disk skills (existence check)
4. User utterance + light repo signals (docs/agents present? CONTEXT.md?)

Skill route surface (authors): `0-skill-manager/references/skill-route-surface.md` — description contract + `metadata.catalog` only (no top-level route YAML).

**Never invent** skills. Missing skill → offer **`/0-skill-manager` ingest**.

## Algorithm

1. **Classify domain** (or ask **F7**: what kind of work?) with recommended default — use flows.md domain list.
2. Name the **★ domain hub**.
3. **Filter route-index** rows for that hub (and utterance vs When / Not for / triggers). Prefer skills whose When matches; exclude clear Not-for collisions.
4. If a **fork** applies, **ask one F# question** (recommend first); wait. Options must include **Agent judgment**.
5. Resolve child skill on the chosen branch. Open that skill’s `SKILL.md` only after selection (not while browsing).
6. Optional “why not” for one cousin (from route-index Not for or Boundary in skill body).
7. If hard-dep path and no `docs/agents/`, recommend `/0-setup-rohitas-skills` first (**F1**).

If route-index is missing or stale, fall back to flows children + skill descriptions; still do not invent.

## Mutation intent

If the user wants to add/move/deprecate/lint/create a hub → **stop query** and open **`/0-skill-manager`** with a one-line brief.

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
