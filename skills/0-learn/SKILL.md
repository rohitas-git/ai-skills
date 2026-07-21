---
name: 0-learn
description: >
  Domain hub for intellectual understanding — how/why something works, not shipping code
  or vault compile. Use for learn, teach me, explain, ELI5, walk me through, quiz me, study this.
  Not for: feature work (0-implement), vault structure/schema (0-rohitas-vault-wiki). Hub: /0-learn.
  Triggers: learn, explain, ELI5, quiz me, teach me, study this.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-learn
    role: hub
    when:
      - "learn/explain/teach routing"
      - "intellectual understanding not shipping"
    not_when:
      - "ship code → 0-implement"
      - "vault schema/ingest → 0-rohitas-vault-wiki"
    next: [1-learning-explainer, 1-code-explainer, 1-teach]
    triggers:
      - "learn"
      - "explain"
      - "ELI5"
      - "quiz me"
      - "teach me"
    requires_setup: false
---

# Learn (domain hub)

**★ Hub of Domain 13.** Intellectual understanding — not Ship, Review, or Vault compile.

You **route** then load one mode. Do not invent a parallel pedagogy outside the chosen skill/refs.

## Boundary

| Need | Skill |
|------|--------|
| Route unclear learning intent | **learn** (this hub) |
| Structured multi-level concept explain | `/1-learning-explainer` |
| Socratic problem practice / quiz | tutor-mode ([tutor-mode.md](./references/tutor-mode.md)) |
| Explain **code** in the editor | `/1-code-explainer` |
| Multi-session workspace course | `/1-teach` |
| Teach via fiction | `/1-story-teacher` |
| Distill long source for notes | `/1-resource-summarizer` |
| Explain vault `[[Note]]` | `/1-vault-explain` |

## Modes

| Mode | Load | Use when |
|------|------|----------|
| **Explain** (default for “what is / explain X”) | `/1-learning-explainer` | Multi-level structured explain, mental models, progressive deep-dive |
| **Tutor** (session practice) | [tutor-mode.md](./references/tutor-mode.md) | Stuck on a problem, walk-through, quiz, hold-the-line, “won’t stick” |
| **Code walkthrough** | `/1-code-explainer` | Explain lines/block/function/file/module of source code |
| **Workspace course** | `/1-teach` | Multi-session learning in a directory (`MISSION.md`, lessons) |
| **Story** | `/1-story-teacher` | Teach via narrative / “make this a novel” |
| **Summarize source** | `/1-resource-summarizer` | Distill PDF/video/article/transcript for learning notes |
| **Vault Concept** | `/1-vault-explain` | Explain `[[Note]]` from Rohitas’s Notes (Vault on-ramp → explainer) |

## Process

1. If utterance already names a mode (slash skill, “workspace course”, “as a story”, “summarize this”, “from my vault”, “explain this function”), go there.
2. If a **long source** is the object and they also want understanding, ask **F-L2** or default: summarize first when raw blob is huge, else explain.
3. Else ask **F-L1** (one question, recommended first) — **wait for the user**.

### Fork F-L1

**What kind of learning help?**

- **Structured explain** (`/1-learning-explainer`) — **recommended** for concepts, ELI5, levels, mental models
- **Tutor session** (tutor-mode refs) — working a problem, quiz, practice under pressure
- **Code walkthrough** (`/1-code-explainer`) — source code in the repo/editor
- **Multi-session course** (`/1-teach`) — ongoing workspace lessons
- **Story** (`/1-story-teacher`) — fiction that encodes the ideas
- **Summarize a source** (`/1-resource-summarizer`) — notes from a long artifact
- **Vault Concept** (`/1-vault-explain`) — only if the object is a vault note

### Fork F-L2

**Long source — summarize first, then explain/tutor, or go straight to understanding?**

- **Summarize first** (`/1-resource-summarizer`) — **recommended** if raw blob is huge
- Skip to explain / tutor / story

4. Load **only** that mode. Optional later: offer another mode (e.g. after summarize → explain or story).

## Hard redirect

If the user is clearly on a cousin job while this hub is open: **ask F-L1/F-L2 once**, then load that skill. Never silent dual-mode.

## Hard rules

- Not a product path — ship via `/0-grilling` → `/0-implement`, not here.
- Not vault compile/query — `/1-vault-ingest`, `/1-wiki-query`; teaching a compiled Concept is `/1-vault-explain`.
- **Explain SSOT** is `/1-learning-explainer` (and 1-vault-explain always hands off there). Do not reimplement levels/CLT in the hub.
- **Tutor SSOT** is [tutor-mode.md](./references/tutor-mode.md) — Socratic practice, integrity, pressure handling.
- **Code SSOT** is `/1-code-explainer` — do not multi-level-explain source as learning-explainer.
- At every fork, ask once with recommended option; never silent branch.

## Related

- **Parent:** `/0-butler`
- **Children:** `/1-learning-explainer` · tutor-mode (refs) · `/1-code-explainer` · `/1-teach` · `/1-story-teacher` · `/1-resource-summarizer`
- **Vault on-ramp:** `/1-vault-explain` → `/1-learning-explainer`
- **Cousins:** `/1-resource-summarizer` also soft under Vault ingest distill
