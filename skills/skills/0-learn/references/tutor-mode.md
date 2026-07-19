# Tutor mode (session tutoring)

**When loaded:** `/0-learn` F-L1 chose **tutor** (stuck on a problem, walk-through, quiz-me, hold-the-line practice).

**Not for:** multi-level structured explain → `/1-learning-explainer`; multi-session workspace → `/1-teach`; vault Concept → `/1-vault-explain`.

Goal: help the learner answer it themselves — this time and next time. Handing over answers and only-asking questions are both failures.

# Learn (domain hub)

**★ Hub of Domain 13.** Intellectual understanding — not Ship, Review, or Vault compile.

You **route** then load one mode. Do not invent a parallel pedagogy outside the chosen skill/refs.

## Modes

| Mode | Load | Use when |
|------|------|----------|
| **Explain** (default for “what is / explain X”) | `/1-learning-explainer` | Multi-level structured explain, mental models, progressive deep-dive |
| **Tutor** (session practice) | [tutor-mode.md](./references/tutor-mode.md) | Stuck on a problem, walk-through, quiz, hold-the-line, “won’t stick” |
| **Workspace course** | `/1-teach` | Multi-session learning in a directory (`MISSION.md`, lessons) |
| **Story** | `/1-story-teacher` | Teach via narrative / “make this a novel” |
| **Summarize source** | `/1-resource-summarizer` | Distill PDF/video/article/transcript for learning notes |
| **Vault Concept** | `/1-vault-explain` | Explain `[[Note]]` from Rohitas’s Notes (Vault on-ramp → explainer) |

## Process

1. If utterance already names a mode (slash skill, “workspace course”, “as a story”, “summarize this”, “from my vault”), go there.
2. If a **long source** is the object and they also want understanding, ask **F-L2** or default: summarize first when raw blob is huge, else explain.
3. Else ask **F-L1** (one question, recommended first):

   **What kind of learning help?**
   - **Structured explain** (`/1-learning-explainer`) — **recommended** for concepts, ELI5, levels, mental models
   - **Tutor session** (tutor-mode refs) — working a problem, quiz, practice under pressure
   - **Multi-session course** (`/1-teach`) — ongoing workspace lessons
   - **Story** (`/1-story-teacher`) — fiction that encodes the ideas
   - **Summarize a source** (`/1-resource-summarizer`) — notes from a long artifact
   - **Vault Concept** (`/1-vault-explain`) — only if the object is a vault note

4. Load **only** that mode. Optional later: offer another mode (e.g. after summarize → explain or story).

## Hard rules

- Not a product path — ship via `/0-grilling` → `/0-implement`, not here.
- Not vault compile/query — `/1-vault-ingest`, `/1-wiki-query`; teaching a compiled Concept is `/1-vault-explain`.
- **Explain SSOT** is `/1-learning-explainer` (and vault-explain always hands off there). Do not reimplement levels/CLT in the hub.
- **Tutor SSOT** is [tutor-mode.md](./references/tutor-mode.md) — Socratic practice, integrity, pressure handling.
- At every fork, ask once with recommended option; never silent branch.

## Related

- **Parent:** `/0-butler`
- **Children:** `/1-learning-explainer` · tutor-mode (refs) · `/1-teach` · `/1-story-teacher` · `/1-resource-summarizer`
- **Vault on-ramp:** `/1-vault-explain` → `/1-learning-explainer`
- **Cousins:** `/1-resource-summarizer` also soft under Vault ingest distill
