---
name: 0-thinking
description: >
  Domain hub for structured mental models — diagnose, decide, create, risk, compose frames.
  Use when: which thinking skill / mental model / reasoning frame; first-principles, pre-mortem,
  systems, reversibility, OODA, steel-man route when unclear.
  Not for: house routing (0-butler), plan interview (0-grilling), live bug pipeline
  (0-diagnosing-bugs), security audit product path (1-security-auditor), simplify mode (0-ponytail).
  Hub: /0-thinking. Triggers: thinking, mental model, which frame, model router, reasoning skill.
disable-model-invocation: true
license: MIT
metadata:
  catalog:
    hub: 0-thinking
    role: hub
    when:
      - "which mental model / thinking frame"
      - "structured reasoning skill catalog"
    not_when:
      - "house domain routing → 0-butler"
      - "plan interview → 0-grilling"
      - "live bug pipeline → 0-diagnosing-bugs"
      - "security product audit → 1-security-auditor"
      - "simplify/delete code → 0-ponytail"
    next:
      - 1-thinking-scientific-method
      - 1-thinking-pre-mortem
      - 1-thinking-reversibility
      - 1-thinking-first-principles
    cousins:
      - 0-butler
      - 0-grilling
      - 0-diagnosing-bugs
      - 0-ponytail
      - 1-security-auditor
    triggers:
      - "thinking"
      - "mental model"
      - "which frame"
      - "reasoning skill"
      - "model router"
    requires_setup: false
  vendor:
    source: tjboudreaux/cc-thinking-skills
    upstream_id: thinking-model-router
    commit: 7b8fece345dfaa11773be7152ccd194589cb5437
---

# Thinking (domain hub)

**★ Hub of Domain 16.** Structured mental-model frames — not Ship, Grill interview, or house routing.

You **route** then load one leaf (or NONE / reason directly). Prefer one primary frame; multi only via `/1-thinking-model-combination` when roles are distinct.

Vendor origin: `tjboudreaux/cc-thinking-skills` (MIT). Router procedure adapted from `thinking-model-router`.

## Boundary

| Need | Skill |
|------|--------|
| Mental-model / which frame (this hub) | **0-thinking** (this) |
| House “which domain?” | `/0-butler` |
| Plan interview / grill | `/0-grilling` |
| Live bug localization pipeline | `/0-diagnosing-bugs` |
| Security audit product path | `/1-security-auditor` |
| Simplify / YAGNI delete mode | `/0-ponytail` |
| Compose multiple frames | `/1-thinking-model-combination` |
| Steel-man only | `/1-thinking-steel-manning` |

## Process

1. **Short-circuit.** If the user names a frame (slash skill or clear mechanism), load that leaf. If no frame improves the work, reason directly (NONE) — do not force a model.
2. If frame is unclear, ask **F-T1** (or use Agent judgment).
3. If category is unclear, ask **F-T2** with recommended default from problem type.
4. Load **one** leaf. Multi-frame only after primary leaves a blind spot → `/1-thinking-model-combination`.

### Fork F-T1

**Is the right thinking frame already clear?**

- **Yes — invoke leaf** — recommended when user named a model or mechanism
- **No — route via this hub (F-T2)** — recommended when fit is unclear
- **NONE — reason without a catalog frame** — routine implementation, no analytical unknown
- **Agent judgment**

### Fork F-T2

**What kind of thinking help?**

- **Diagnose** — scientific-method, five-whys-plus, kepner-tregoe, systems, map-territory, cynefin, socratic
- **Decide** — reversibility, opportunity-cost, probabilistic, second-order, steel-manning, bounded-rationality, circle-of-competence, lindy-effect
- **Create** — first-principles, triz, via-negativa, thought-experiment, jobs-to-be-done, effectuation
- **Risk / execution** — pre-mortem, red-team, margin-of-safety, theory-of-constraints, ooda
- **Compose** — model-combination (after one primary)
- **Agent judgment**

**Type defaults (override when constraints demand):**

| Problem type | Prefer |
|--------------|--------|
| Diagnose | five-whys-plus or scientific-method (kepner-tregoe if IS/IS-NOT) |
| Decide | reversibility first; then opportunity-cost or probabilistic |
| Understand | systems (map-territory if model≠reality; cynefin if domain unclear) |
| Create | first-principles (triz for contradictions; via-negativa for remove-first) |
| Evaluate | steel-manning (socratic if definitions are the unknown) |
| Predict | probabilistic |
| Optimize | theory-of-constraints (ooda under time pressure; bounded-rationality for stop) |
| Risk / what fails? | pre-mortem or red-team; margin-of-safety for buffers |
| Product what to build? | jobs-to-be-done |

## Hard rules

- Not a second house meta-router — house domain pick is always `/0-butler`.
- Prefer **NONE or one** primary leaf; cap multi at three distinct roles via model-combination.
- Leaf skills are soft — no forced setup.
- At every fork, ask once with recommended option; always offer **Agent judgment**.
- Dual: `1-thinking-steel-manning` primary remains `/0-grilling`; soft here for catalog completeness.

## Children (by category)

### Diagnose
`/1-thinking-scientific-method` · `/1-thinking-five-whys-plus` · `/1-thinking-kepner-tregoe` · `/1-thinking-systems` · `/1-thinking-map-territory` · `/1-thinking-cynefin` · `/1-thinking-socratic`

### Decide
`/1-thinking-reversibility` · `/1-thinking-opportunity-cost` · `/1-thinking-probabilistic` · `/1-thinking-second-order` · `/1-thinking-steel-manning` · `/1-thinking-bounded-rationality` · `/1-thinking-circle-of-competence` · `/1-thinking-lindy-effect`

### Create
`/1-thinking-first-principles` · `/1-thinking-triz` · `/1-thinking-via-negativa` · `/1-thinking-thought-experiment` · `/1-thinking-jobs-to-be-done` · `/1-thinking-effectuation`

### Risk / execution
`/1-thinking-pre-mortem` · `/1-thinking-red-team` · `/1-thinking-margin-of-safety` · `/1-thinking-theory-of-constraints` · `/1-thinking-ooda`

### Compose
`/1-thinking-model-combination`

## Related

- **Parent:** `/0-butler`
- **Vendor:** `archive/vendor/cc-thinking-skills/`
- **Cousins:** `/0-grilling` · `/0-diagnosing-bugs` · `/0-ponytail` · `/1-security-auditor`
