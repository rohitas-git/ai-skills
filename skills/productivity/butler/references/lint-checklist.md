# Lint checklist + organize

## Lint report shape

Emit a structured report:

```markdown
# Catalog lint

**Catalog root:** …
**Summary:** N critical, N warn, N info

## critical
- [code] path — message

## warn
- …

## info
- …
```

Severity:

- **critical** — broken discovery, dual router, hard-dep wrong, promotion rule violated, missing successor on deprecate
- **warn** — trigger collisions, model-invoked budget overrun, README drift, sprawl, vault path hard-coding
- **info** — style nits, optional progressive-disclosure opportunities

## Checks

| Code | Check |
|------|--------|
| `name-dir` | frontmatter `name` == directory name |
| `frontmatter` | SKILL.md has name + description |
| `bucket-readme` | every skill listed in its bucket README with one-line blurb |
| `root-promo` | root README lists only engineering + productivity + misc members |
| `model-budget` | model-invoked promoted skills target &lt; ~25; flag user-invoke candidates left model-invoked |
| `triggers` | cousin clusters have exclusive Use when / Don’t use when (grill, review, learn, architecture) |
| `hard-dep` | `to-spec`, `to-tickets`, `triage` mention `/setup-rohitas-skills` |
| `forbidden` | no discoverable `using-agent-skills`; no live `ask-matt` router; no `setup-matt-pocock-skills` name |
| `links` | relative links inside skills resolve or are noted |
| `vault-ssot` | no repeated absolute home vault paths outside setup/vault SSOT docs |
| `sprawl` | SKILL.md enormous without progressive disclosure (task-observer, hatch-pet, …) |
| `tombstone` | each deprecated skill names successor; deprecated README lists it |
| `vendor` | vendor packs not in nestedSkillRoots unless intentional |
| `lock` | skills-lock paths match on-disk locations for locked skills |

Optional automation: `scripts/lint-skills` should mirror this checklist for non-LLM CI.

## Organize op

**Mutations:** move, rename, deprecate (with tombstone).

1. Dry-run plan: old path → new path, README lines, flows.md slots, lock entry, tombstone text.
2. Confirm with human.
3. Apply with git-aware moves when possible.
4. Update indexes + flows + lock.
5. Re-run lint.

Deprecate checklist:

- Move to `deprecated/<name>/`
- Banner + successors in SKILL.md
- `disable-model-invocation: true` preferred
- deprecated/README.md row
- Remove from root promoted list
- Point any live references at successor
