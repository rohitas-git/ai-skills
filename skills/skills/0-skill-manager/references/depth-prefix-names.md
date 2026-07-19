# Depth-prefix skill names (hard rule)

Live skill **directory name**, frontmatter **`name`**, slash command, hub package dir (when applicable), and flows/workflow identifiers share one form:

```text
{depth}-{kebab-slug}
```

Examples: `0-butler`, `0-implement`, `1-to-tickets`, `1-code-review`.

## Depth meaning

| Depth | Who | Examples |
|------:|-----|----------|
| **0** | ★ **Domain hubs** (and hub-of-hubs) | `0-butler`, `0-grilling`, `0-implement`, `0-review` |
| **1** | Direct children of a domain hub, including **sub-hubs** | `1-to-spec`, `1-tdd`, `1-code-review`, `1-grill-me` |
| **2+** | Children of a depth-`(N-1)` skill/sub-hub only | `2-…` when a skill hangs only under a sub-hub |

**Dual membership:** use the **minimum** depth (shallowest attachment). Example: soft under both `0-implement` and `1-code-review` → still `1-…`, not `2-…`.

**Self-refs / ops verbs / axis labels** are not skills and stay unprefixed (`create`, `Spec`, …).

## Invariants (critical)

1. **Prefix required** — live skills under `skills/` and place-ready `inbox/` must match `^[0-9]+-[a-z0-9]+(-[a-z0-9]+)*$`.
2. **`name` == dir** — frontmatter `name` equals the directory name (including prefix).
3. **Slash == name** — agents invoke `/0-implement`, not bare `/implement`.
4. **Hub packages** — `hubs/{depth}-{slug}/` matches the hub skill name; `workflow.json` `hub` / `children[].skills` use the same strings.
5. **No bare live peers** — unprefixed live skill dirs are **forbidden** (lint critical `depth-prefix`).
6. **Vendor / archive** — `archive/vendor/` and tombstones may keep **upstream unprefixed** names; do not force-prefix third-party pack paths. When harvesting into live, **assign depth** and rename on place/ingest.

## How to assign depth (place / new-hub / ingest)

1. If the skill **is** a ★ domain hub (or butler) → **0**.
2. Else if it is a **sub-hub** under a domain (`parent_domain_hub` set) → **1**.
3. Else set depth = `min(parent_depth) + 1` over hub parents in flows / `workflow.json`.
4. If dual-attached, recompute min after place; **rename** if depth changes (organize + update all refs).

## Rename discipline

Changing depth or slug is an **organize** multi-file mutate: dir, frontmatter, hubs, flows, lock, wikis, in-skill links. Dry-run first. Never leave `name` ≠ dir.

## Lint

| Code | Sev | Check |
|------|-----|--------|
| `depth-prefix` | **critical** | live dir + `name` match `^\d+-[a-z0-9]+(-[a-z0-9]+)*$` |
| `name-dir` | critical | `name` == directory name |
| `depth-hub` | critical | ★ domain hub depth is **0**; sub-hub package depth is **1** |
| `depth-child` | warn | child depth is not parent_depth+1 (or min dual) without documented dual membership |

## Forbidden

- Live skill named `implement` instead of `0-implement`
- Frontmatter `name: to-tickets` under dir `1-to-tickets`
- Hub package `hubs/review/` when skill is `0-review`
- Prefixing vendor pack directories in place (leave archive; rename only the live winner)
