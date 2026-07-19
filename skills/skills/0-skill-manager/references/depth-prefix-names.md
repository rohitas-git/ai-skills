# Depth-prefix skill names (hard rule)

Live skill **directory name**, frontmatter **`name`**, slash command, hub package dir (when applicable), and flows/workflow identifiers share one form:

```text
{depth}-{kebab-slug}
```

Examples: `0-butler`, `0-implement`, `1-to-tickets`, `1-code-review`.

The number is **hub-tree depth**, not an arbitrary counter.

## Depth from domain hub structure

| Depth | Who | Examples |
|------:|-----|----------|
| **0** | ★ **Domain hubs** (and hub-of-hubs) | `0-butler`, `0-grilling`, `0-implement`, `0-review` |
| **1** | Direct children of a domain hub, including **sub-hubs** | `1-to-spec`, `1-tdd`, `1-code-review`, `1-grill-me` |
| **2+** | Children whose **primary** parent is depth `(N-1)` only | `2-…` when primary parent is a sub-hub |

**Self-refs / ops verbs / axis labels** are not skills and stay unprefixed (`create`, `Spec`, …).

---

## Dual domain membership (adjusted rule)

A skill may appear under **more than one** hub (soft dual, on-ramp, cousin, pipeline cross-link). That is **logical dual membership** only — one directory, one name.

### Rules

1. **One primary, zero or more duals**  
   Exactly one hub attachment is **primary** for naming. All other attachments are **dual** (secondary). Dual listings **must not** change `{depth}-`.

2. **Hub identity always wins**  
   - If the skill **is** a ★ domain hub → depth is always **0**, even when also soft/hard under another hub (e.g. `0-triage` hard-dep of setup, `0-implement` on-ramp from triage).  
   - If the skill **is** a **sub-hub** (`parent_domain_hub` set) → depth is always **1**, even when also pipeline-linked under another domain (e.g. `1-code-review` under Ship pipeline **and** Review sub-hub).

3. **Primary for non-hub skills** (first match wins):  
   a. Workflow edge with `"primary": true` on the child group (or skill entry), if present.  
   b. Else highest **link-type strength** among parents:  
      `pipeline` > `hard` > `wrapper` > `sub-hub` > `leaf` / `satellite` > `on-ramp` / `pull-in` / `detour` > `persona` / `vocab` > `cousin` > `soft` / `handoff` / `delegate` / `routing`  
   c. Else among remaining, **shallower parent hub** (domain hub depth 0 beats sub-hub depth 1).  
   d. Else stable tie-break: lexicographic parent hub name.

4. **Depth formula (non-hub)**  
   `depth = primary_parent_hub_depth + 1`  
   Soft duals under deeper hubs (e.g. under `1-code-review` only as secondary) **do not** push the skill to `2-`.

5. **Rename only when primary changes**  
   Adding/removing a dual soft under another domain is **not** a rename. Changing primary hub (or promoting to domain/sub-hub) **is** an organize rename if depth changes.

### Examples

| Skill | Primary | Duals | Name depth |
|-------|---------|-------|------------|
| `0-triage` | domain hub | hard under setup | **0** (hub identity) |
| `1-code-review` | sub-hub under Review | pipeline under Ship | **1** (sub-hub identity) |
| `1-tdd` | pipeline under Ship or Diagnose | soft under setup | **1** |
| `1-verify-work` | cousin under Ship (`0-implement`) | cousin under Review / code-review | **1** (not 2) |
| `1-software-architect` | persona under Architecture | soft under Review | **1** |
| `1-handoff` | detour under Design | soft session meta under butler | **1** |
| `1-security-and-hardening` | soft under `0-review` (shallowest primary soft) | soft under both Review sub-hubs | **1** (not 2) |

---

## Invariants (critical)

1. **Prefix required** — live `skills/` and place-ready `inbox/` match `^[0-9]+-[a-z0-9]+(-[a-z0-9]+)*$`.
2. **`name` == dir** — frontmatter `name` equals the directory name (including prefix).
3. **Slash == name** — agents invoke `/0-implement`, not bare `/implement`.
4. **Hub packages** — `hubs/{depth}-{slug}/` matches the hub skill name; `workflow.json` `hub` / `children[].skills` use the same strings.
5. **Prefix matches primary depth** — name prefix equals hub-graph primary depth (this file’s algorithm). Lint: `depth-graph`.
6. **No bare live peers** — unprefixed live skill dirs are **forbidden** (`depth-prefix`).
7. **Vendor / archive** — may keep upstream unprefixed names until place/ingest assigns depth.

## How to assign depth (place / new-hub / ingest)

1. If new ★ domain hub → **`0-{slug}`** + `hubs/0-{slug}/`.
2. If new sub-hub → **`1-{slug}`** + `hubs/1-{slug}/` with `parent_domain_hub`.
3. Else attach to primary parent hub; depth = parent_depth + 1; name = `{depth}-{slug}`.
4. When adding a **dual** listing only: update the secondary hub’s `workflow.json` / flows — **do not** rename.
5. Optional: set `"primary": true` on the primary child group when dual membership would be ambiguous (all soft, etc.).

## Rename discipline

Changing primary hub or hub identity (domain/sub-hub) may change depth → **organize** multi-file mutate (dir, frontmatter, hubs, flows, lock, wikis, links). Dry-run first. Dual soft add/remove → no rename.

## Lint

| Code | Sev | Check |
|------|-----|--------|
| `depth-prefix` | **critical** | live dir + `name` match `^\d+-[a-z0-9]+(-[a-z0-9]+)*$` |
| `name-dir` | critical | `name` == directory name |
| `depth-hub` | critical | ★ domain hub packages/skills are **0-**; sub-hubs are **1-** |
| `depth-graph` | **critical** | name prefix equals **primary** hub-tree depth (duals ignored) |
| `depth-dual` | info | skill has ≥2 hub parents; primary parent recorded in report |

## Forbidden

- Live skill named `implement` instead of `0-implement`
- Renaming a skill to `2-…` only because it is **soft dual** under a sub-hub
- Frontmatter `name` without matching dir prefix
- Hub package `hubs/review/` when skill is `0-review`
- Prefixing vendor pack directories in place (leave archive; rename only the live winner)
