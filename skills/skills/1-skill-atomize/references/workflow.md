# 1-skill-atomize — detection & apply detail

Load from SKILL.md when scanning or applying a pass.

## What “overlap” means

**Content overlap** = two skills that would both reasonably claim the same user utterance **and** re-implement similar procedures.

**Not overlap** (exclude from “fix” clusters):

- Intentional hub relationships in flows.md: wrapper, hard, soft, pipeline, on-ramp, leaf, axis, satellite, sub-hub
- Explicit cousins already documented with a clean Boundary (e.g. comment family)
- Deprecated tombstones (mention successor only)

Examples of intentional (do not “fix” by merging):

- `/0-grilling` ↔ `1-grill-me` / `1-grill-with-docs`
- `/0-skill-manager` ↔ `1-skill-linter` / 1-create-skill path
- Vault ops under `/0-rohitas-vault-wiki`
- Ship pipeline `1-to-spec` → `1-to-tickets` → `0-implement`

## Detection recipe

1. Inventory live skills under `skills/`, `productivity/`, `misc/`, `personal/` (name + description + first ~400 body chars).
2. Cluster by theme keywords (0-review, learn/explain, wiki/docs, architecture, security, context, etc.).
3. For each pair in a cluster, score:
   - Shared triggers in descriptions
   - Shared procedure (not just shared domain word)
   - Missing Boundary / hard redirect
4. Drop pairs already linked as hub children of the same parent with distinct link roles.
5. Rank High / Medium / Low.

### High (typical)

- Same job, different packaging (two full “explain” systems)
- Two living-knowledge systems for the same repo class
- Doctrine Q&A vs always-on enforcer with no F-fork

### Medium

- Adjacent jobs, fuzzy trigger (verify vs 0-review closer)
- Shared vocabulary, different artifact

### Low

- Complementary leaves with explicit Boundary already

## Apply checklist (per skill in scope)

1. Rewrite **description** → one job (+ “not X → /cousin”).
2. Add **Boundary** table (self + cousins).
3. Add **Hard redirect** + **Forks** matching flows F# IDs.
4. Strip re-implemented cousin procedures (one-line pointer only).
5. Keep Matt-lean SKILL.md; depth in `references/`.
6. Update flows.md children + fork tables.
7. Update hub `workflow.json` if domain hub package exists.
8. README one-liners if description changed materially.
9. skill-lint Gate: PASS.

## Contract SSOT

Always enforce [atomic-skills.md](../../0-skill-manager/references/atomic-skills.md). If the contract is missing, create/update it under 0-skill-manager references first (Phase 0).

## Resolution modes (F-A2)

| Mode | Actions |
|------|---------|
| **keep-both** (default) | Boundary + forks only; no tombstones |
| **merge** | Winner keeps job; loser → `deprecated/` + successor; flows remove loser |
| **split** | Extract thinner leaves; hub becomes router; new skills need place + skill-lint |

## Phases (large pass)

| Phase | Work |
|-------|------|
| 0 | Ensure atomic-skills contract + lint checklist codes |
| 1…N | One cluster at a time (Learn, Docs, Clean-code, …) |
| last | Integration: skill-lint catalog, hub-member, forks present |

## Non-goals

- Butler query routing redesign
- Full 0-skill-creator eval loop for every body
- Vendor pack rewrites
- Promoting `using-agent-skills`

**Agent judgment:** every user-facing fork must offer **Agent judgment** (agent chooses best branch and proceeds without more questions on that fork).
