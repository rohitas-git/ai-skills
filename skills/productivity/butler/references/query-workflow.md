# Query workflow

Answer: **which skill or flow should I use?**

## Inputs (only)

1. **`flows.md`** — chaining SSOT
2. **Bucket README indexes** — engineering, productivity, misc, personal, in-progress, deprecated
3. **On-disk skills** — directories with `SKILL.md` under discoverable buckets
4. User utterance + optional repo signals (has CONTEXT.md? issue tracker?)

**Never invent** a skill name that is not on disk. If the right skill is missing, say so and offer **ingest** or a documented vendor candidate path.

## Algorithm

1. Classify intent: main-flow feature, bug, triage, vault, catalog meta, office tool, learning, architecture, unknown.
2. Map to flows.md row or standalone list.
3. Resolve concrete skill directory; read frontmatter `description` only if needed to disambiguate cousins.
4. Recommend **one primary** skill (or ordered path of 2–4 skills).
5. Optionally list **why not** for 1–2 cousins in the same cluster.
6. If setup never run and hard-dep path chosen, mention `/setup-rohitas-skills` first.

## Output template

```markdown
**Use:** `/skill-name` (or path: a → b → c)
**Why:** one sentence
**Why not:** `/cousin` — one sentence (optional)
**Next:** concrete first action
```

## Manual smoke fixtures

| # | Utterance | Expected primary |
|---|-----------|------------------|
| 1 | "which skill should I use?" / "I'm lost in the catalog" | `butler` (query self) or present flows overview then ask one clarifying Q |
| 2 | "stress-test this plan" / "grill me" | `grill-with-docs` (if codebase) or `grill-me` |
| 3 | "turn this into a spec / tickets" | `to-spec` then `to-tickets` |
| 4 | "this bug is weird / diagnose this" | `diagnosing-bugs` |
| 5 | "put this in my vault" / "query my notes" | `vault-ingest` / `wiki-query` (vault chain) |
| 6 | "implement these tickets" | `implement` |

Run these after catalog moves; failures mean flows.md or indexes drifted.

## ask-matt succession

`ask-matt` is **deprecated**. Its graph lives here + `flows.md`. Tombstone points to **butler**.
