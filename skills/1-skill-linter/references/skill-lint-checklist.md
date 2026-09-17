# Skill lint checklist (SSOT for per-skill checks)

Severity: **critical** · **warn** · **info**

**lean + chaining** is the default quality bar. See [lean-structure.md](./lean-structure.md) and `/1-writing-great-skills`.

## A. SKILL.md surface

| Code | Sev | Check |
|------|-----|--------|
| `depth-prefix` | **critical** | promoted live (`skills/`) dir + frontmatter `name` match `^\d+-[a-z0-9]+(-[a-z0-9]+)*$`; **inbox/ exempt until place** (see 0-skill-manager `depth-prefix-names.md`) |
| `name-dir` | critical | frontmatter `name` == directory name (includes prefix) |
| `depth-hub` | critical | ★ domain hub skills use depth **0**; sub-hub package depth = parent+1 (often **1**; nested → **2+**; hub identity over dual edges) |
| `depth-graph` | **critical** | name prefix equals hub-tree depth: hub identity or `max(parent_depth+1)` for **any** depth 0…max (incl. **3–6+**) |
| `depth-dual` | info | skill has ≥2 hub parents — depth uses deepest parent |
| `frontmatter` | critical | `name` and `description` present |
| `description-quality` | warn | description ≥ ~40 chars; signals when-to-use / triggers |
| `description-triggers` | warn | **all live** skills: description has Use when / Use for / Triggers / Trigger on (butler route surface; not only model-invoked) |
| `route-top-level` | **critical** | no top-level `hub`/`when`/`not_when`/`next`/`prev`/`cousins`/`triggers`/`role` — use `metadata.catalog` only ([skill-route-surface.md](../../0-skill-manager/references/skill-route-surface.md)) |
| `route-hub` | warn | `metadata.catalog.hub` must be a known hub and actually own this skill; membership under a different hub does not count |
| `route-cousin` | warn | dual-member or high-collision cluster lacks `not_when` / `## Boundary` |
| `route-index-stale` | info | missing or older than skills/workflows — run `scripts/generate-route-index` |
| `body-structure` | warn | non-empty body; has Process/Dispatch/Steps **or** short intentional all-reference |
| `lean-shape` | warn | follows lean shape (thin router + steps + pointers), not a book (lean-structure.md) |
| `claude-invocation-policy` | critical | Claude implicit only for `1-coding-standards`; every other live skill sets `disable-model-invocation: true` |
| `codex-invocation-policy` | critical | Codex implicit only for top-level `role: hub` skills plus `1-coding-standards`; every other live skill explicitly sets `agents/openai.yaml` policy false |
| `codex-manifest-policy` | critical | `agents/openai.yaml` policy is well formed; preserve interface, dependency, and metadata fields |
| `{runtime}-invocation-budget` | warn | Claude and Codex implicit counts receive independent context-budget checks |

## B. Lean main SKILL.md (progressive disclosure)

| Code | Sev | Check |
|------|-----|--------|
| `lean-soft` | info | 121–180 lines — OK but prefer thinner |
| `lean` | warn | > 180 lines without progressive-disclosure map (links to refs/siblings with when-to-load) |
| `disclosure` | warn | if `references/` or sibling `.md` exist, SKILL.md must link them (no silent dumps) |
| `no-book` | warn | long prose chapters without steps or context pointers |
| `completion` | info | steps imply checkable completion criteria |

## C. References & links

| Code | Sev | Check |
|------|-----|--------|
| `ref-exists` | critical | relative markdown links from SKILL.md resolve on disk |
| `handoff-target` | critical | every depth-prefixed skill handoff in a live skill, `flows.md`, or a hub workflow names a live skill |
| `ref-orphan` | warn | files under `references/` not reachable from SKILL.md through package-local Markdown links or explicit backticked file pointers; follow chains/cycles by path, not basename, without executing assets or fetching remote links |
| `ref-empty` | warn | linked file empty or trivial stub |
| `scripts-exec` | info | `scripts/` present but never mentioned (or opposite) |

## D. Hub membership + chaining

| Code | Sev | Check |
|------|-----|--------|
| `hub-member` | critical | live skill listed in hub `workflow.json` and/or flows.md (hub-membership.md) |
| `hub-type` | warn | link type known (wrapper/hard/soft/pipeline/on-ramp/leaf/axis/satellite/sub-hub) |
| `hub-package` | critical | ★ domain hubs have `hubs/{hub}/hub.html` + `workflow.json` (ADR 0005) |
| `chain-slot` | warn | parent hub + role visible (flows / workflow / Related section in SKILL.md) |
| `chain-next` | warn | pipeline skills name next skill(s); hubs name children or build path |
| `chain-prev` | info | non-entry pipeline skills name previous when useful |
| `hard-dep-setup` | critical | `1-to-spec`, `1-to-tickets`, `0-triage` mention `/0-setup-rohitas-skills` |
| `no-peer-duplicate` | warn | does not re-own a cousin skill’s full job |

Exempt membership: `archive/`, `vendor/`. `inbox/` → warn only.

## E. Sprawl / sub-domain

| Code | Sev | Check |
|------|-----|--------|
| `sprawl` | warn | SKILL.md > 250 lines without progressive disclosure |
| `subdomain-candidate` | warn | > 400 lines **or** > 5 substantial refs **or** multiple independent pipelines |
| `subdomain-procedure` | info | when candidate: sprawl-and-subdomain.md |

Prefer **thin + chain** over new domain hubs. Sub-domain only for whole trees.

## F. New-skill gate

| Code | Sev | Check |
|------|-----|--------|
| `gate-place` | critical | place/ingest target fails any critical (A–D) |
| `gate-hub-slot` | critical | new skill has no planned parent hub + link type |
| `gate-depth-prefix` | critical | **new** skill lacks `{depth}-{slug}` name/dir or hub package name mismatch |
| `gate-lean` | critical | **new** skill SKILL.md > 180 lines and no disclosure map — must thin before place |
| `gate-route` | critical | **new** skill: description contract + hub membership + `metadata.catalog` (`hub`, `role`, `when` or `triggers`) — see skill-route-surface.md |

## Catalog-level (delegate / include)

Catalog promotion, dual-router, lock, tombstones remain in 0-skill-manager [lint-checklist.md](../../0-skill-manager/references/lint-checklist.md) and `scripts/lint-skills`. 1-skill-linter **catalog** mode includes hub-member + lean + chain checks for all live skills.
