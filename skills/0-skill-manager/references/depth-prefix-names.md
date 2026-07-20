# Depth-prefix skill names (hard rule)

Live skill **directory name**, frontmatter **`name`**, slash command, hub package dir (when applicable), and flows/workflow identifiers share one form:

```text
{depth}-{kebab-slug}
```

Examples: `0-butler`, `0-implement`, `1-to-tickets`, `1-code-review`, `2-verify-work`.

The number is **hub-tree depth** (0 … max depth of the hub tree), not an arbitrary counter. There is **no hard cap** at 2 or 3 — depths **4**, **5**, **6**, … are first-class when the tree reaches them.

## Depth from domain hub structure

### Hub packages

| Hub kind | Depth |
|----------|------:|
| ★ Domain hub / hub-of-hubs (`parent_domain_hub` absent) | **0** |
| Sub-hub (`parent_domain_hub` → parent hub) | **parent_depth + 1** (today often **1**; nested sub-hubs → **2**, **3**, …) |

### Non-hub skills

```text
depth = max over hub parents of (parent_hub_depth + 1)
```

That is the **deepest** attachment in the hub tree. Soft duals under a deeper hub **do** deepen the number when that parent is part of the membership graph.

| Depth | Who | Examples |
|------:|-----|----------|
| **0** | ★ domain hubs | `0-butler`, `0-implement`, `0-review` |
| **1** | Direct children of domain hubs; **sub-hubs** under a domain hub | `1-to-spec`, `1-tdd`, `1-code-review`, `1-grill-me` |
| **2** | Children of depth-1 hubs (e.g. under a sub-hub) | `2-verify-work`, `2-security-and-hardening` |
| **3** | Children of depth-2 parents / nested sub-hub under a depth-2 hub | `3-{slug}` when max parent depth is 2 |
| **4** | Children of depth-3 parents | `4-{slug}` when max parent depth is 3 |
| **5** | Children of depth-4 parents | `5-{slug}` when max parent depth is 4 |
| **6** | Children of depth-5 parents | `6-{slug}` when max parent depth is 5 |
| **7+** | Same recurrence | `depth = max(parent_depth + 1)` — no artificial ceiling |

### Nesting ladder (worked form)

Same formula at every level. Hypothetical nested sub-hubs illustrate depths **3–6** (catalog today tops out at **2** live skills):

```text
0-review                          # domain hub → depth 0
└─ 1-code-review                  # sub-hub (parent 0) → depth 1
   └─ 2-axis-pack                 # nested sub-hub or child of 1- → depth 2
      └─ 3-specialist             # child / sub-hub of 2- → depth 3
         └─ 4-tool                # child of 3- → depth 4
            └─ 5-leaf             # child of 4- → depth 5
               └─ 6-micro         # child of 5- → depth 6
```

| From parent depth | Child / nested sub-hub name prefix |
|------------------:|------------------------------------|
| 0 | **1-** |
| 1 | **2-** |
| 2 | **3-** |
| 3 | **4-** |
| 4 | **5-** |
| 5 | **6-** |
| N | **(N+1)-** |

**Hub identity always wins** for the skill that *is* the hub package:

- Domain hub skill → always **0** (even if also soft under another hub).
- Sub-hub skill → always that package’s hub depth (`parent_depth + 1`, often **1**; nested → **2+**).

**Self-refs / ops verbs / axis labels** are not skills (`create`, `Spec`, …).

---

## Dual domain membership

A skill may appear under **more than one** hub. One directory, one name.

| Concern | Rule |
|---------|------|
| **Depth number** | **Deepest** hub parent: `max(parent_depth + 1)` (except hub identity above) |
| **Primary hub** | Which hub “owns” the skill for routing/docs — optional `"primary": true` on the primary child group; does **not** flatten depth |
| **Adding a dual** | If the new parent is **deeper**, depth may increase → **organize rename**. If shallower only, no rename |

### Examples

| Skill | Parents (hub depth) | Name depth |
|-------|---------------------|------------|
| `0-triage` | domain hub (+ hard under setup) | **0** (identity) |
| `1-code-review` | sub-hub under Review (+ pipeline under Ship) | **1** (sub-hub identity) |
| `1-tdd` | `0-implement`, `0-diagnosing-bugs`, setup soft | **1** |
| `2-verify-work` | `0-implement` (0), `0-review` (0), `1-code-review` (1) | **2** = 1+1 |
| `2-security-and-hardening` | `0-review` (0), both Review sub-hubs (1) | **2** |
| `2-ponytail-review` | `0-ponytail` (0), `0-review` (0), `1-code-review` (1) | **2** |
| `2-software-architect` | Architecture (0), Review / code-review | **2** |
| `3-{slug}` (future) | deepest parent at depth 2 | **3** |
| `4-{slug}` (future) | deepest parent at depth 3 | **4** |
| `5-{slug}` (future) | deepest parent at depth 4 | **5** |
| `6-{slug}` (future) | deepest parent at depth 5 | **6** |

---

## Invariants (critical)

1. **Prefix required** — live `skills/` / `inbox/` match `^[0-9]+-[a-z0-9]+(-[a-z0-9]+)*$` (multi-digit depths OK: `10-…`).
2. **`name` == dir** — including the depth digit(s).
3. **Slash == name** — e.g. `/2-verify-work`, `/4-{slug}` when depth is 4.
4. **Hub packages** — `hubs/{depth}-{slug}/` matches hub skill; workflow `hub` / `children[].skills` use full names.
5. **Prefix = hub-tree depth** — lint `depth-graph` recomputes `max(parent_depth+1)` through max tree depth (hub identity special-cased). No artificial max at 2 or 3.
6. **No bare live peers**.
7. **Vendor / archive** — upstream unprefixed until place/ingest.

## Assign on place / new-hub / ingest

1. ★ domain hub → `0-{slug}` + `hubs/0-{slug}/`.
2. Sub-hub → `{parent_depth+1}-{slug}` (often `1-`; under a depth-1 hub → `2-`; under depth 2 → `3-`; … through **4- / 5- / 6-** as needed) + matching hub package + `parent_domain_hub`.
3. Child skill → compute `max(parent_depth+1)` over planned hub parents; name `{depth}-{slug}` (may be **3**, **4**, **5**, **6**, …).
4. Adding a **deeper** dual parent may require rename (organize).

## Rename discipline

Depth change → multi-file organize (dir, frontmatter, hubs, flows, lock, wikis, links) + host resync. Dry-run first. Applies equally when moving a skill from `2-` → `3-` or `3-` → `4-` / `5-` / `6-`.

## Lint

| Code | Sev | Check |
|------|-----|--------|
| `depth-prefix` | critical | `^\d+-[a-z0-9]+(-[a-z0-9]+)*$` |
| `name-dir` | critical | `name` == directory name |
| `depth-hub` | critical | domain hub packages **0-**; sub-hub package depth = parent+1 (may be **2+** when nested) |
| `depth-graph` | critical | name prefix = hub-tree depth (`max(parent+1)` / hub identity) for **any** depth 0…max |
| `depth-dual` | info | ≥2 hub parents (depth uses deepest) |

## Forbidden

- Bare live names (`implement` instead of `0-implement`)
- Leaving a sub-hub child at `1-` when max parent depth says **2** (or at `2-` when max says **3**, etc.)
- Assuming an artificial ceiling (e.g. “only 0–2 exist”) — **3–6+** are valid when the tree reaches them
- Prefixing vendor pack dirs in place
