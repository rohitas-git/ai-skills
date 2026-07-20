# Atomic skills contract

House standard for **one-job skills** with explicit redirects. Used by place/ingest/organize and by **`/1-skill-atomize`** (catalog atomize pass).

## Rules

1. **One job** — Frontmatter `description` and the skill’s first purpose line name **exactly one primary job**. No dual claims (“tutor *and* multi-level explainer”).
2. **Boundary table** — Every placed skill lists its job and cousins:

```markdown
## Boundary

| Need | Skill |
|------|--------|
| (this job) | **this-skill** |
| (cousin job) | `/other-skill` |
```

3. **Hard redirect** — If the request matches a cousin job:
   - Do **not** do the cousin work here.
   - **Ask one question** (recommended option first).
   - Wait for the user.
   - Load only the chosen skill.
   - Never silent-load a cousin “to be helpful.”

4. **Forks** — Collision paths use F# rows (flows.md + skill body). Same shape as 0-butler forks:

| Fork | When | Question | Recommended | Branches |
|------|------|----------|-------------|----------|
| **F-…** | ambiguous trigger | one sentence? | option A | A → skill · B → skill |

5. **Lean body** — Do not re-implement a cousin’s procedure. One-line redirect + fork is enough; depth stays in `references/` for *this* job only.

## Keep both vs merge

Prefer **keep both + Boundary + forks** when jobs are distinct but triggers collide. Merge/tombstone only when the user chooses that resolution (prefer-merge hard rule still applies for *true* duplicate jobs).

## Checklist (place / atomize)

- [ ] One-job description
- [ ] Boundary table with cousins
- [ ] Hard redirect + F# if collision exists
- [ ] flows.md / hub `workflow.json` updated when forks are new
- [ ] skill-lint Gate: PASS
