---
name: learn
description: >
  Domain hub for intellectual understanding — how/why something works, not shipping
  code or vault compile. Use for learn, teach me, explain, ELI5, walk me through,
  quiz me, study this, rusty on, confusion signals, or terse concept names. Routes
  to the right Learn mode (explain, tutor, code walkthrough, multi-session course,
  story, summarize). Not for tasks, feature work, or Claude opinion/verdict prompts.
disable-model-invocation: true
---

# Learn (domain hub)

**★ Hub of Domain 13.** Intellectual understanding — not Ship, Review, or Vault compile.

You **route** then load one mode. Do not invent a parallel pedagogy outside the chosen skill/refs.

## Boundary

| Need | Skill |
|------|--------|
| Route unclear learning intent | **learn** (this hub) |
| Structured multi-level concept explain | `/learning-explainer` |
| Socratic problem practice / quiz | tutor-mode ([tutor-mode.md](./references/tutor-mode.md)) |
| Explain **code** in the editor | `/code-explainer` |
| Multi-session workspace course | `/teach` |
| Teach via fiction | `/story-teacher` |
| Distill long source for notes | `/resource-summarizer` |
| Explain vault `[[Note]]` | `/vault-explain` |

## Modes

| Mode | Load | Use when |
|------|------|----------|
| **Explain** (default for “what is / explain X”) | `/learning-explainer` | Multi-level structured explain, mental models, progressive deep-dive |
| **Tutor** (session practice) | [tutor-mode.md](./references/tutor-mode.md) | Stuck on a problem, walk-through, quiz, hold-the-line, “won’t stick” |
| **Code walkthrough** | `/code-explainer` | Explain lines/block/function/file/module of source code |
| **Workspace course** | `/teach` | Multi-session learning in a directory (`MISSION.md`, lessons) |
| **Story** | `/story-teacher` | Teach via narrative / “make this a novel” |
| **Summarize source** | `/resource-summarizer` | Distill PDF/video/article/transcript for learning notes |
| **Vault Concept** | `/vault-explain` | Explain `[[Note]]` from Rohitas’s Notes (Vault on-ramp → explainer) |

## Process

1. If utterance already names a mode (slash skill, “workspace course”, “as a story”, “summarize this”, “from my vault”, “explain this function”), go there.
2. If a **long source** is the object and they also want understanding, ask **F-L2** or default: summarize first when raw blob is huge, else explain.
3. Else ask **F-L1** (one question, recommended first) — **wait for the user**.

### Fork F-L1

**What kind of learning help?**

- **Structured explain** (`/learning-explainer`) — **recommended** for concepts, ELI5, levels, mental models
- **Tutor session** (tutor-mode refs) — working a problem, quiz, practice under pressure
- **Code walkthrough** (`/code-explainer`) — source code in the repo/editor
- **Multi-session course** (`/teach`) — ongoing workspace lessons
- **Story** (`/story-teacher`) — fiction that encodes the ideas
- **Summarize a source** (`/resource-summarizer`) — notes from a long artifact
- **Vault Concept** (`/vault-explain`) — only if the object is a vault note

### Fork F-L2

**Long source — summarize first, then explain/tutor, or go straight to understanding?**

- **Summarize first** (`/resource-summarizer`) — **recommended** if raw blob is huge
- Skip to explain / tutor / story

4. Load **only** that mode. Optional later: offer another mode (e.g. after summarize → explain or story).

## Hard redirect

If the user is clearly on a cousin job while this hub is open: **ask F-L1/F-L2 once**, then load that skill. Never silent dual-mode.

## Hard rules

- Not a product path — ship via `/grilling` → `/implement`, not here.
- Not vault compile/query — `/vault-ingest`, `/wiki-query`; teaching a compiled Concept is `/vault-explain`.
- **Explain SSOT** is `/learning-explainer` (and vault-explain always hands off there). Do not reimplement levels/CLT in the hub.
- **Tutor SSOT** is [tutor-mode.md](./references/tutor-mode.md) — Socratic practice, integrity, pressure handling.
- **Code SSOT** is `/code-explainer` — do not multi-level-explain source as learning-explainer.
- At every fork, ask once with recommended option; never silent branch.

## Related

- **Parent:** `/butler`
- **Children:** `/learning-explainer` · tutor-mode (refs) · `/code-explainer` · `/teach` · `/story-teacher` · `/resource-summarizer`
- **Vault on-ramp:** `/vault-explain` → `/learning-explainer`
- **Cousins:** `/resource-summarizer` also soft under Vault ingest distill
