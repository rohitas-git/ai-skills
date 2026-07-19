# Flows — chaining SSOT

Single source of truth for how catalog skills chain. **Butler query** and agents must follow this map; do not invent competing full-graph routers.

Skill names below are slash-invokable names (`/name`). All must exist on disk under a catalog bucket (or be documented as deprecated with a successor).

---

## Precondition

**`/setup-rohitas-skills`** — run once per consumer repo before engineering flows that need an issue tracker, triage labels, domain docs, or vault root SSOT.

Hard-dep skills (`to-spec`, `to-tickets`, `triage`) **must** point at this setup skill. Soft-dep skills read `CONTEXT.md` / ADRs when present and degrade gracefully without cargo-cult setup spam.

---

## Main flow: idea → ship

Most feature work travels here.

1. **Interview**
   - **With a codebase:** `/grill-with-docs` (stateful → `CONTEXT.md` + ADRs).
   - **No codebase / pure plan:** `/grill-me`.
   - Both are thin wrappers over **`/grilling`** (interview SSOT body).
2. **Optional prototype detour** — if a question needs a runnable answer (state, UI feel):
   - `/handoff` out → fresh session → `/prototype` → `/handoff` back.
3. **Multi-session?**
   - **Yes:** `/to-spec` → `/to-tickets` → **`/implement`** per ticket (clear context between tickets).
   - **No:** `/implement` in the same window.
4. **Inside implement:** drives **`/tdd`** (red-green slices) then **`/code-review`**, then commit.

### Context hygiene

Keep grill → spec → tickets in one unbroken window when possible (smart zone ~120k). If the window fills before tickets: `/handoff`, continue fresh. Each `/implement` starts clean from the ticket.

### Single-session shortcut

After grill, if the change is small and fully specified in-thread: skip to-spec/to-tickets and go straight to `/implement`.

---

## On-ramps

Merge onto the main flow by name — do not invent ad hoc pipelines.

| Situation | Skill | Merge point |
|-----------|-------|-------------|
| Bugs/requests piling up (raw issues you didn't create) | `/triage` | agent-ready issues → `/implement` |
| Something broken / hard bug / regression | `/diagnosing-bugs` | fix with regression test; post-mortem may → `/improve-codebase-architecture` |
| Huge foggy effort (multi-session map of decisions) | `/wayfinder` | **exit only via** `/to-spec` → `/to-tickets` → `/implement` — never implement raw fog maps |
| Codebase health / deepening opportunities | `/improve-codebase-architecture` | chosen idea → main flow at `/grill-with-docs` |

### Triage rule

**Do not re-triage** tickets produced by `/to-tickets` — they are already agent-ready.

### Wayfinder rule

Wayfinder produces **decisions, not deliverables**. When the map clears: `/to-spec` collapses decisions into a buildable plan, then tickets and implement.

---

## Vocabulary (underneath)

Pulled in by main-path skills; reach for them when **words** are the problem, not process:

- `/domain-modeling` — ubiquitous language, ADRs, glossary discipline
- `/codebase-design` — deep modules, seams, interface depth
- `/coding-standards` — lean naming/modularity comments bar (with stepdown / code-comments as specialized)

These are **not** entry points competing with grill / to-spec.

---

## Vault chain (personal)

Personal knowledge is a **separate** chain from engineering. Documented here so butler query can route vault questions without inventing steps.

1. Fast capture → `/vault-inbox`
2. Process into Concepts → `/vault-ingest` (uses schema from `/rohitas-vault-wiki`)
3. Explain a Concept → `/vault-explain` (pedagogy via learning-explainer)
4. Health-check vault → `/vault-lint`
5. Answer from notes → `/wiki-query`
6. Schema / Atlas / structure SSOT → `/rohitas-vault-wiki`

**Vault root path** comes only from setup SSOT (`docs/agents/vault.md` or `## Agent skills` vault pointer) — never hard-coded home paths in skill bodies.

Project wikis (in-repo `docs/wiki/`) use `/project-wiki-manager` — not butler, not vault atoms.

---

## Meta (catalog craft)

| Intent | Path |
|--------|------|
| Scaffold a new skill | `/create-skill` (or `/skill-creator`) → **butler ingest** |
| Predictability / craft theory | `/writing-great-skills` (not replaced by butler) |
| Session learnings → skill edits | `/reflect` → optional **butler lint** / **organize** |
| Lost / which skill | **butler query** (successor of ask-matt) |

---

## Standalone (off main flow)

Useful alone; not required steps on every feature:

- `/research` — background primary-source reading → file to take into grill
- `/prototype` — throwaway design answer
- `/teach` — multi-session learning workspace
- `/handoff` — cross-session bridge
- Office/media: `/docx`, `/pptx`, `/xlsx`, `/diagram-maker`, etc. (misc bucket)

---

## Cousin clusters (exclusive winners)

When routing, pick one winner; note "why not" for cousins in query:

| Cluster | Winner(s) | Not for |
|---------|-----------|---------|
| Grill / interview | grilling via grill-me / grill-with-docs | interview-me (vendor), wayfinder (too heavy for one-session plans) |
| Review | code-review / code-review-v2 as documented | check-work only for verify-self after implement |
| Learn / teach | learn, learning-explainer, teach, story-teacher by intent | don't steal grill |
| Architecture | codebase-design + improve-codebase-architecture + software-architect | deprecated software-architecture |

---

## ASCII map

```text
setup-rohitas-skills (once)
        │
        ▼
 grill-with-docs | grill-me
        │
        ├─ optional: handoff ⇄ prototype
        │
        ├─ multi-session? ──► to-spec ──► to-tickets ──► implement*
        │                                              │
        └─ single-session ──► implement* ◄─────────────┘
                                    │
                              tdd → code-review → commit

On-ramps: triage, diagnosing-bugs, wayfinder→to-spec…, improve-codebase-architecture
```
