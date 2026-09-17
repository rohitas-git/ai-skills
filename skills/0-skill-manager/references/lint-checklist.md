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
- **warn** — runtime-specific implicit-invocation budget overrun, trigger collisions, README drift, sprawl, vault path hard-coding
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
| `claude-invocation-policy` | **critical** — only `1-coding-standards` is Claude-implicit; all others set `disable-model-invocation: true` |
| `codex-invocation-policy` | **critical** — top-level hubs plus `1-coding-standards` are Codex-implicit; all others explicitly set `allow_implicit_invocation: false` |
| `codex-manifest-policy` | **critical** — malformed/duplicate Codex policy keys; preserve other manifest fields |
| `{runtime}-invocation-budget` | independent Claude/Codex implicit-invocation context-budget warning |
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
| `hub-dir` | each domain hub has package dir `hubs/{hub}/` (flat; no bucket nesting) |
| `hub-html` | each package has `hub.html` |
| `hub-workflow-json` | each package has `workflow.json` + entry in `hubs/manifest.json` |
| `butler-hub-link` | non-butler packages parent-link 0-butler; 0-butler lists every domain hub |
| `hub-chart-link` | each `hub.html` links `flows-chart.html`; chart matrix links each package |
| `hub-member` | every live skill is listed under some hub workflow (ADR 0006); see 1-skill-linter |
| `skill-surface` | name-dir, frontmatter, ref-exists — delegated to 1-skill-linter / scripts |
| `lean` | main SKILL.md thin + progressive disclosure + chain blurb — 1-skill-linter |
| `route-top-level` | **critical** — no top-level route keys; use `metadata.catalog` only ([skill-route-surface.md](./skill-route-surface.md)) |
| `description-triggers` | warn — live skills have Use when / Triggers (butler) |
| `route-hub` | warn — `metadata.catalog.hub` is a known hub |
| `route-description-hub` | warn — description `Hub:` and `metadata.catalog.hub` disagree |
| `route-index-json` | warn — machine route projection is malformed or does not cover the live skill set |
| `gate-route` | **critical on new place/ingest** — catalog + description contract present |
| `forks` | pipeline branches document F# ask-user questions |
| `atomic-boundary` | high-collision / newly placed skills have Boundary table + one-job description ([atomic-skills.md](./atomic-skills.md)) |
| `hard-redirect` | cousin jobs redirect with ask-user fork; no silent dual-skill execution |
| `butler-no-mutate` | 0-butler SKILL.md must not own ingest/organize/lint as primary ops |

**Lint op:** load **`/1-skill-linter`** (catalog or skill mode) then merge any remaining catalog-only codes here.

Optional automation: `scripts/lint-skills` mirrors name-dir, ref-exists, hub-member, route-top-level, description-triggers, sprawl counts, and catalog checks for non-LLM CI (prints `catalog.yaml` version; `--format json` emits a schema-versioned report). After membership/frontmatter changes: `scripts/generate-route-index`, then `scripts/generate-route-index --check`.

## Organize op

**Mutations:** move, rename, deprecate (with tombstone).

1. Pin the exact old/new paths, revisions, dirty ownership, README/wiki lines, flows slots, lock entry, and tombstone text.
2. A review request returns this plan; an explicit organize/rename request authorizes the scoped reversible move.
3. Re-read targets, then apply with git-aware moves when possible.
4. Update only affected indexes, flows, and lock entries.
5. Re-run lint and report applied/unapplied items.

## Atomize op

**Mutations:** one-job descriptions, Boundary tables, hard redirects, F# forks in flows — content-overlap cleanup.

Load **`/1-skill-atomize`** (do not reimplement here). It selects assess/apply from the request, reconciles one pinned overlap cluster, then returns skill-lint evidence. Merge/split identity choices remain explicit.

Deprecate checklist:

- Move to `archive/<name>/`
- Banner + successors in SKILL.md
- `disable-model-invocation: true` preferred
- archive/README.md row
- Remove from root promoted list
- Point any live references at successor
