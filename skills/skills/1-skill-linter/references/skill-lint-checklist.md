# Skill lint checklist (SSOT for per-skill checks)

Severity: **critical** · **warn** · **info**

**Matt lean + chaining** is the default quality bar. See [matt-lean-structure.md](./matt-lean-structure.md) and `/1-writing-great-skills`.

## A. SKILL.md surface

| Code | Sev | Check |
|------|-----|--------|
| `depth-prefix` | **critical** | live dir + frontmatter `name` match `^\d+-[a-z0-9]+(-[a-z0-9]+)*$` (depth-prefix hard rule; see 0-skill-manager `depth-prefix-names.md`) |
| `name-dir` | critical | frontmatter `name` == directory name (includes prefix) |
| `depth-hub` | critical | ★ domain hub skills use depth **0**; sub-hub package skills use depth **1** |
| `frontmatter` | critical | `name` and `description` present |
| `description-quality` | warn | description ≥ ~40 chars; signals when-to-use / triggers |
| `description-triggers` | warn | model-invoked (no `disable-model-invocation`): description has trigger phrasing (“Use when…”) |
| `body-structure` | warn | non-empty body; has Process/Dispatch/Steps **or** short intentional all-reference |
| `matt-shape` | warn | follows Matt lean shape (thin router + steps + pointers), not a book (matt-lean-structure.md) |
| `disable-model` | info | large (>180 lines) or steward skills: prefer `disable-model-invocation: true` |

## B. Lean main SKILL.md (Matt progressive disclosure)

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
| `ref-orphan` | warn | files under `references/` never linked from SKILL.md |
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

## Catalog-level (delegate / include)

Catalog promotion, dual-router, lock, tombstones remain in 0-skill-manager [lint-checklist.md](../../0-skill-manager/references/lint-checklist.md) and `scripts/lint-skills`. 1-skill-linter **catalog** mode includes hub-member + lean + chain checks for all live skills.
