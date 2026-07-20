# Spec review — Skills catalog reorg

**Against:** [SPEC.md](./SPEC.md)  
**Catalog lint:** `./scripts/lint-skills` → **0 critical**, 0 warn, 1 info  
**Model-invoked promoted:** 20 (target &lt; ~25)  
**Review date:** 2026-07-19

---

## Verdict

**Structural goals of the spec are met.** Buckets, butler, setup rename, vendor park, deprecations, flows SSOT, hard deps, single tdd, vault path SSOT packaging, and lint script all landed.

**Catalog leanness is only partially met.** Routing fights are reduced (model-invoked 20, dual-router offline), but several **cousin / duplicate clusters remain intentional thin wrappers or unresolved peers**. Spec explicitly allowed some of these (grill wrappers; architecture trio) and called out **one create-skill path** as preferred if both exist — that gap is still open.

---

## Spec checklist (implementation decisions)

| Spec requirement | Status | Evidence |
|------------------|--------|----------|
| Six buckets + vendor | **Pass** | `engineering`…`deprecated` + `vendor/` |
| Root README only promoted buckets | **Pass** | personal/in-progress/deprecated/vendor excluded from promoted lists |
| Bucket READMEs with skill + blurb | **Pass** | each bucket `README.md` |
| CLAUDE.md bucket rules | **Pass** | `skills/CLAUDE.md` |
| butler @ productivity, user-invoked, 4 ops | **Pass** | `productivity/0-butler/` + references |
| butler refs: layout, flows, ingest, lint, query, hard-rules | **Pass** | all present (+ smoke-fixtures) |
| flows.md main path + on-ramps + vault + meta | **Pass** | `references/flows.md` |
| setup-rohitas-skills rename + vault SSOT | **Pass** | dir/name/lock/pointers + `vault.md` template |
| Hard deps: to-spec, to-tickets, triage | **Pass** | all mention `/0-setup-rohitas-skills` |
| Soft deps no forced setup spam | **Pass** | tdd / diagnosing-bugs / improve-… |
| agent-skills under vendor, not discovered | **Pass** | `nestedSkillRoots: []` |
| Never promote using-agent-skills | **Pass** | vendor-only; lint info |
| Single tdd (merge vendor TDD ideas) | **Pass** | one `engineering/tdd`; merge notes; no peer TDD |
| ask-matt → butler tombstone | **Pass** | `deprecated/ask-matt` |
| software-architecture deprecated | **Pass** | `deprecated/software-architecture` |
| create-skill → butler ingest handoff | **Pass** | handoff blurb present |
| writing-great-skills not replaced | **Pass** | still craft reference |
| reflect → optional butler lint/organize | **Pass** | handoff blurb |
| skills-lock paths updated | **Pass** | lock points at bucket paths |
| Install / symlink bucket discovery | **Pass** | `sync-skills-symlinks.sh` walks buckets |
| scripts/lint-skills | **Pass** | mirrors checklist; 0 critical |
| grill-me / grill-with-docs thin over grilling | **Pass** | both load `/0-grilling` |
| Model-invoked &lt; ~25 | **Pass** | 20 |
| Cousin Use/Don’t use (grill, review, learn, arch) | **Partial** | notes on grilling, code-review, learn, codebase-design, software-architect — not exhaustive on all cousins |
| Prefer one create-skill path | **Fail / open** | both `1-create-skill` and `0-skill-creator` live in productivity |
| butler SKILL.md ~80–120 lines | **Partial** | ~63 lines (thin OK; under band) |
| Selective agent-skills promotes | **Deferred (OK)** | vendor README documents deferral |
| docs/agents seeded in monorepo | **Open** | setup skill exists; this repo may still lack `docs/agents/` until setup is run |

---

## User stories scoreboard (condensed)

| Band | Stories | Notes |
|------|---------|--------|
| Done | 1–6, 8–16, 17–23, 25–28, 30–36, 37, 39–44 | Core reorg + steward + main path |
| Partial | 7, 38, 11 (confirm is documented not enforced by code) | Cousin “why not” is flows/docs, not automatic |
| Open / deferred | 29 (selective promotes), 24 residual (vault SSOT packaging done; runtime still depends on setup write) | Intentional |

---

## Duplicate & redundant skills

Legend:

- **Dup** — same job, two loadable skills (should merge or tombstone)
- **Wrapper** — intentional thin entry over an SSOT (OK if documented)
- **Cousin** — overlapping triggers; needs exclusive Use/Don’t use
- **Complement** — different job; keep

### Critical / high priority

| Cluster | Skills | Kind | Recommendation |
|---------|--------|------|----------------|
| **Skill authors** | `1-create-skill`, `0-skill-creator` | **Dup** | Spec: *prefer one path*. Keep **`1-create-skill`** (Grok/catalog local) *or* **`0-skill-creator`** (eval/improve loop); make the other a thin handoff or deprecate. Both still hand off to butler ingest — good — but dual entry confuses query. |
| **Vault steward vs generic PKM** | `0-rohitas-vault-wiki`, `obsidian-notes-manager` | **Dup / cousin** | Rohitas vault schema is the SSOT for *this* vault. `obsidian-notes-manager` is a generic PKM steward that can re-route schema. **Tombstone or demote** notes-manager for Rohitas’s Notes; keep as optional generic only if you use non-Rohitas vaults. |
| **Review main path** | `1-code-review`, `code-review-v2` | **Cousin** | Spec main path names **`1-code-review`**. v2 is two-axis Standards+Spec with sub-agents (also what implement historically closed with). **Pick one winner for implement’s exit** and document the other as optional/specialized — or make code-review a 3-line wrapper that loads v2. |
| **Find skill vs steward** | `1-discover-skills`, `0-butler` | **Cousin** | find-skills = *install from ecosystem*; butler = *route this catalog*. OK if Don’t use when is explicit on both (partially missing on find-skills). |

### Medium — intentional wrappers / specialized family

| Cluster | Skills | Kind | Recommendation |
|---------|--------|------|----------------|
| **Grill** | `0-grilling`, `1-grill-me`, `1-grill-with-docs` | **Wrapper** | Spec-compliant. Keep; ensure grill-me / grill-with-docs stay thin. |
| **Architecture** | `1-codebase-design`, `0-improve-codebase-architecture`, `2-software-architect` + deprecated `software-architecture` | **Complement + cousin** | design = vocabulary; improve = survey; architect = persona. Keep three; **software-architect** already user-invoked. Don’t re-promote deprecated. |
| **Comment family** | `1-coding-standards`, `1-code-comments`, `1-inline-comments`, `1-execution-flow-comments`, `1-stepdown-rule` | **Complement** | Well-boundaried table in coding-standards. Keep; not true dups. |
| **Ponytail family** | `0-ponytail` + 5 satellites | **Complement** | Spec: satellites user-invoked. Keep; only `0-ponytail` model-invoked. |
| **Vault ops** | `1-vault-inbox`, `1-vault-ingest`, `1-vault-lint`, `1-vault-explain`, `1-wiki-query` | **Complement** | Chain ops — good. |
| **Obsidian primitives** | `1-obsidian-markdown`, `1-obsidian-cli`, `1-obsidian-bases` | **Complement** | Syntax/CLI/Bases tools under schema steward — keep. |

### Medium — learning / docs sprawl

| Cluster | Skills | Kind | Recommendation |
|---------|--------|------|----------------|
| **Learn stack** | `0-learn`, `1-learning-explainer`, `1-teach`, `1-story-teacher`, `1-resource-summarizer`, `1-vault-explain` | **Cousin** | Distinct modes (tutor / multi-level explain / multi-session course / narrative / summarize / vault-bound). Keep but add exclusive Don’t use when on each; consider **story-teacher** and **resource-summarizer** as pull-ins from learning-explainer only. |
| **Living docs** | `1-living-documentation-governor`, `1-project-wiki-manager`, `1-domain-modeling` | **Cousin** | domain-modeling = CONTEXT/ADR glossary; project-wiki = in-repo wiki atoms; living-doc-governor = code↔docs sync. Overlap on “where does knowledge go?” — document in flows as three different targets. |
| **Session meta** | `1-handoff`, `1-strategic-compact`, `1-context-monitor`, `task-observer`, `continuous-learning-v2`, `1-session-skill-reflect` | **Cousin** | handoff vs compact is clear in flows. observer / continuous-learning / reflect all “improve skills from sessions” — highest meta-redundancy after create-skill pair. Prefer **reflect** as post-session, **butler** as catalog, demote or progressive-disclose the rest. |

### Low / clean

| Cluster | Status |
|---------|--------|
| TDD | Single `1-tdd`; vendor TDD not co-routed |
| Router | `ask-matt` dead; butler sole steward |
| Setup naming | `0-setup-rohitas-skills` only |
| Vendor dual-router | offline |

### Vendor pack vs catalog (not duplicates on disk discovery, but conceptual cousins)

| Vendor skill | Catalog cousin | Policy (spec) |
|--------------|----------------|---------------|
| `interview-me` | grilling / grill-* | Do **not** promote as peer |
| `spec-driven-development` | to-spec | Do **not** promote as peer |
| `planning-and-task-breakdown` | to-tickets | Do **not** promote as peer |
| `test-driven-development` | tdd | Merged ideas only |
| `debugging-and-error-recovery` | diagnosing-bugs | Promote only via ingest if gap |
| `code-review-and-quality` | code-review / v2 | Prefer merge, not second skill |
| `using-agent-skills` | butler | **Never** promote |

---

## Gaps vs “craft bar” (not structural failures)

1. **~79 discoverable skills** still (including personal + deprecated tombstones). Promotion list is shorter, but symlink sync still flattens personal + deprecated into agent dirs — hosts may still see many descriptions if they scan all links.
2. **Cousin Don’t use when** incomplete on find-skills, learn stack, living-doc pair, create-skill pair, code-review vs v2.
3. **Butler line count** under 80 — fine functionally; optional expand with examples.
4. **This monorepo** may not have run setup yet → no `docs/agents/*` until you do.

---

## Recommended cleanup order (optional follow-ups)

1. **One create path** — deprecate or wrap `0-skill-creator` ↔ `1-create-skill`.
2. **One implement review exit** — align implement + flows on `1-code-review` *or* `code-review-v2`.
3. **Vault: rohitas-vault-wiki wins** — demote `obsidian-notes-manager` for this vault (tombstone or personal/in-progress with note).
4. **Meta skill diet** — progressive-disclose or deprecate continuous-learning-v2 / task-observer if reflect+butler cover the job.
5. **Optional:** stop symlink-discovering `deprecated/` (tombstones offline) to shrink agent skill lists.

---

## Flowchart

Interactive HTML diagram:

**[flows-chart.html](./flows-chart.html)** — open in a browser.

Covers: setup precondition, main engineering flow, on-ramps, vocabulary layer, vault chain, catalog meta, standalone, and deprecation edges.
