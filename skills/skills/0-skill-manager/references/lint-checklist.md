# Lint checklist + organize

**Per-skill / hub-membership / sprawl:** load **`/1-skill-linter`** (ADR 0006). This file is the **catalog + hub package** checklist 0-skill-manager still owns; 1-skill-linter owns SKILL.md + references + membership report format.

## Lint report shape

Prefer 1-skill-linter [report-format.md](../../1-skill-linter/references/report-format.md). Catalog-only runs may still use:

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

- **critical** — broken discovery, dual router, hard-dep wrong, promotion rule violated, missing successor on deprecate, **hub-member orphan**, broken skill refs
- **warn** — trigger collisions, model-invoked budget overrun, README drift, sprawl, vault path hard-coding
- **info** — style nits, optional progressive-disclosure opportunities

## Checks

| Code | Check |
|------|--------|
| `depth-prefix` | **critical** — live skill dir + `name` = `{depth}-{kebab-slug}`; no bare unprefixed live skills ([depth-prefix-names.md](./depth-prefix-names.md)) |
| `depth-hub` | **critical** — ★ domain hubs are `0-*`; sub-hub package depth = parent+1 (often `1-*`; nested `2-*`+); hub package dir matches hub skill name |
| `depth-graph` | **critical** — name prefix = hub-tree depth `max(parent+1)` / hub identity for any depth 0…max (incl. **3–6+**); duals use deepest parent |
| `name-dir` | frontmatter `name` == directory name |
| `frontmatter` | SKILL.md has name + description |
| `bucket-readme` | every skill listed in its bucket README with one-line blurb |
| `root-promo` | root README lists only engineering + productivity + misc members |
| `model-budget` | model-invoked promoted skills target &lt; ~25; flag user-invoke candidates left model-invoked |
| `triggers` | cousin clusters have exclusive Use when / Don’t use when (grill, 0-review, 0-learn, architecture) |
| `hard-dep` | `1-to-spec`, `1-to-tickets`, `0-triage` mention `/0-setup-rohitas-skills` |
| `forbidden` | no discoverable `using-agent-skills`; no live `ask-matt` router; no `setup-matt-pocock-skills` name |
| `links` | relative links inside skills resolve or are noted |
| `vault-ssot` | no repeated absolute home vault paths outside setup/vault SSOT docs |
| `sprawl` | SKILL.md enormous without progressive disclosure (task-observer, 1-hatch-pet, …) |
| `tombstone` | each deprecated skill names successor; deprecated README lists it |
| `vendor` | vendor packs not in nestedSkillRoots unless intentional |
| `lock` | skills-lock paths match on-disk locations for locked skills |
| `hub-integrity` | each flows.md domain has exactly one ★ hub skill on disk |
| `hub-children` | children listed under a hub exist on disk (or are axes/docs) |
| `hub-dir` | each domain hub has package dir `hubs/{hub}/` (flat; no Matt-bucket nesting) |
| `hub-html` | each package has `hub.html` |
| `hub-workflow-json` | each package has `workflow.json` + entry in `hubs/manifest.json` |
| `butler-hub-link` | non-butler packages parent-link 0-butler; 0-butler lists every domain hub |
| `hub-chart-link` | each `hub.html` links `flows-chart.html`; chart matrix links each package |
| `hub-member` | every live skill is listed under some hub workflow (ADR 0006); see 1-skill-linter |
| `skill-surface` | name-dir, frontmatter, ref-exists — delegated to 1-skill-linter / scripts |
| `matt-lean` | main SKILL.md thin + progressive disclosure + chain blurb — 1-skill-linter |
| `forks` | pipeline branches document F# ask-user questions |
| `atomic-boundary` | high-collision / newly placed skills have Boundary table + one-job description ([atomic-skills.md](./atomic-skills.md)) |
| `hard-redirect` | cousin jobs redirect with ask-user fork; no silent dual-skill execution |
| `butler-no-mutate` | 0-butler SKILL.md must not own ingest/organize/lint as primary ops |

**Lint op:** load **`/1-skill-linter`** (catalog or skill mode) then merge any remaining catalog-only codes here.

Optional automation: `scripts/lint-skills` mirrors name-dir, ref-exists, hub-member, sprawl counts, and catalog checks for non-LLM CI.

## Organize op

**Mutations:** move, rename, deprecate (with tombstone).

1. Dry-run plan: old path → new path, README lines, flows.md slots, lock entry, tombstone text.
2. Confirm with human.
3. Apply with git-aware moves when possible.
4. Update indexes + flows + lock.
5. Re-run lint.

## Atomize op

**Mutations:** one-job descriptions, Boundary tables, hard redirects, F# forks in flows — content-overlap cleanup.

Load **`/1-skill-atomize`** (do not reimplement here). Dry-run → confirm → apply → skill-lint. Default: keep both peers + forks, not silent merge.

Deprecate checklist:

- Move to `archive/<name>/`
- Banner + successors in SKILL.md
- `disable-model-invocation: true` preferred
- archive/README.md row
- Remove from root promoted list
- Point any live references at successor
