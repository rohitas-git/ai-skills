# Lean SKILL.md + chaining

1-skill-linter treats **lean** skills as the house default for structure. Canonical theory: `/1-writing-great-skills`. Canonical thin examples: `/0-implement`, `/1-tdd`, `/1-to-spec`, `/1-grill-with-docs`.

**Butler routing surface** (description contract + `metadata.catalog` only — no top-level route keys): [skill-route-surface.md](../../0-skill-manager/references/skill-route-surface.md).

## Goal

Keep the **main `SKILL.md` lean**. Put depth behind **context pointers**. Wire the skill into a **chain** (domain hub + prev/next) rather than a standalone essay.

## Lean structure (required shape)

A healthy lean `SKILL.md` is a **thin router + steps**, not a book:

```text
---
name: …
description: …   # triggers for model-invoked; short human summary if user-invoked
# disable-model-invocation: true  # when user-only
---

# Title

1–3 sentence purpose (optional).

## Process | Dispatch | Steps     # ordered actions with completion criteria
…

## (optional) Rules / hard gates   # short bullets only
…

## Related / next                  # chain: prev · next · cousins · setup hard-dep
…

# Heavy material → sibling .md or references/*.md via context pointers
```

### In-skill vs disclosed

| Tier | Lives in | Examples |
|------|----------|----------|
| **In-skill steps** | `SKILL.md` | Ordered process, forks (ask user), completion criteria |
| **In-skill reference** | short bullets in `SKILL.md` | Hard rules every run needs |
| **Disclosed reference** | sibling `*.md` or `references/*` | templates, long rubrics, glossaries, axis docs |

**Progressive disclosure:** if only some branches need a blob, pointer it out of `SKILL.md`.

## Lean size gates (1-skill-linter defaults)

| Lines in SKILL.md | Code | Meaning |
|-------------------|------|---------|
| ≤ **120** | — | Lean target (lean) |
| **121–180** | `lean-soft` (info) | OK if disclosure map present |
| **181–250** | `lean` (warn) | Not lean — move reference out |
| **> 250** | `sprawl` (warn) | Fail progressive-disclosure bar |
| **> 400** | `subdomain-candidate` (warn) | Split skill or sub-domain hub |

**Lean fail (critical) for new skills:** place/ingest of a **new** skill with SKILL.md **> 180** lines and no progressive-disclosure map → `gate-lean` critical.

## Structure checks

| Code | Sev | Pass criteria |
|------|-----|----------------|
| `lean` | warn | SKILL.md ≤ 180 lines, or ≤ 250 with clear load map to refs |
| `lean-soft` | info | 121–180 without map — nudge thinner |
| `lean-shape` | warn | Has ordered Process/Dispatch/Steps **or** is intentionally all-reference with short body (like 1-writing-great-skills core is long but discloses glossary — prefer disclose) |
| `disclosure` | warn | If SKILL.md > 120 and has `references/` or sibling `.md`, SKILL.md must **link** them with when-to-load wording |
| `completion` | info | Steps imply done/not-done (completion criteria), not open-ended essay |
| `no-book` | warn | SKILL.md is not primarily long prose chapters without steps or pointers |
| `description-triggers` | warn | Model-invoked skills: description states when to use (trigger style) |

## Chaining checks (chain flow)

Skills live on a **chain**, not in isolation. Align with 0-butler `flows.md` and hub `workflow.json`.

| Code | Sev | Pass criteria |
|------|-----|----------------|
| `chain-slot` | warn | Live skill documents **parent hub** and role (pipeline / on-ramp / leaf / wrapper / hard / soft / satellite) — via flows, workflow.json, or short “Build path / Related” in SKILL.md |
| `chain-next` | warn | Pipeline skills name **next** skill(s) (e.g. 0-implement → 1-tdd → 1-code-review) |
| `chain-prev` | info | Pipeline skills name **previous** when not an entry hub |
| `hard-dep-setup` | critical | `1-to-spec`, `1-to-tickets`, `0-triage` point at `/0-setup-rohitas-skills` |
| `hub-member` | critical | Listed under a domain hub (ADR 0006) — chaining requires membership |
| `no-peer-duplicate` | warn | Does not re-implement a cousin skill’s whole job (prefer wrapper or merge) |

### Chaining patterns (good)

```text
0-setup-rohitas-skills  →  0-grilling  →  1-to-spec → 1-to-tickets → 0-implement → 1-tdd → 1-code-review
                              ↑ on-ramps: 0-triage, 0-diagnosing-bugs, 0-wayfinder, improve-arch
```

Thin hub skills only **point**:

```markdown
**Build path:** drive `/1-tdd`, then multi-axis `/1-code-review`, then commit.
```

(See `/0-implement`.)

### Bad

- Monolith that embeds setup + design + ship + 0-review in one SKILL.md
- No next/prev and not a leaf/tool under misc
- Orphan skill with no hub slot (breaks chain index)

## Remediation (report only)

1. **Thin SKILL.md** — move templates, long tables, deep theory to `references/` or sibling files; leave steps + pointers.
2. **Add chain blurb** — Build path / Related with `/prev` and `/next`.
3. **Place** under domain hub via 0-skill-manager if orphan.
4. **Split** if multi-pipeline (1-writing-great-skills: by invocation or by sequence).
5. **Sub-domain hub** only if a whole tree needs its own map (sprawl-and-subdomain.md).

Handoff rewrites to `/0-skill-creator` + place via `/0-skill-manager`. 1-skill-linter does not edit the linted skill.
