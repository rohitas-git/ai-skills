# Query workflow (0-butler)

Answer: **which domain hub / skill / flow?**

## Inputs only

1. **flows.md** — hub map, pipelines, forks  
2. Bucket READMEs + on-disk skills  
3. User utterance + light repo signals (docs/agents present? CONTEXT.md?)

**Never invent** skills. Missing skill → offer **`/0-skill-manager` ingest**.

## Algorithm

1. **Classify domain** (or ask **F7**: what kind of work?) with recommended default.
2. Name the **★ domain hub**.
3. If a **fork** applies, **ask one F# question** (recommend first); wait.
4. Resolve child skill on the chosen branch.
5. Optional “why not” for one cousin.
6. If hard-dep path and no `docs/agents/`, recommend `/0-setup-rohitas-skills` first (**F1**).

## Mutation intent

If the user wants to add/move/deprecate/lint/create a hub → **stop query** and open **`/0-skill-manager`** with a one-line brief.

## Output template

```markdown
**Domain hub:** `/…`
**Use:** `/…`
**Why:** …
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
