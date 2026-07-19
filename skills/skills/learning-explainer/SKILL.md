---
name: learning-explainer
description: >
  Structured multi-level explanations (child through frontier) with knowledge
  probe, mental models, diagrams, progressive deep-dive, and optional CLT.
  Use for "explain X", ELI5, audience-level teaching, or vault-explain pedagogy.
  Default explain mode under /learn. Not code walkthroughs (/code-explainer),
  multi-session courses (/teach), Socratic problem practice (learn tutor-mode),
  or raw summarization alone (/resource-summarizer).
disable-model-invocation: true
---

# Learning Explainer

**Structured explain SSOT** under domain hub `/learn`. Also loaded hard by `/vault-explain`.

## Boundary

| Need | Skill |
|------|--------|
| Multi-level concept explain + probe | **learning-explainer** (this) |
| Route unclear learning intent | `/learn` (F-L1) |
| Explain **source code** | `/code-explainer` |
| Socratic problem practice / quiz | `/learn` tutor-mode |
| Multi-session workspace course | `/teach` |
| Distill long artifact only | `/resource-summarizer` |
| Story teaching | `/story-teacher` |
| Vault Concept explain | `/vault-explain` → this skill |

## Hard redirect

If the object is **code in a file/repo** (not a concept about programming in the abstract): ask **F-L1** with recommended `/code-explainer`, wait, then load that skill — do not run multi-level explain on the code here.

If the user wants to **work a problem** under pressure (quiz, “won’t stick”, hold-the-line): ask once → `/learn` tutor-mode.

## Process

0. **Brief plain-English override** — If user wants simple/short/ELI5-brief, answer in 1 short paragraph or 3–4 bullets. Skip probe, mental-model mandate, confidence, progressive structure unless they ask.

1. **Knowledge probe** — Assess familiarity and goals ([knowledge-probe.md](./references/knowledge-probe.md)).

2. **CLT only if requested** — Default = no CLT ([clt-clarification.md](./references/clt-clarification.md)).

3. **Long input** — Distill first via `/resource-summarizer` (or its techniques), then explain at the right level(s). If only notes are wanted, redirect with F-L2 → summarizer.

4. **Always include** (unless brief override): mental model(s) + diagram description ([mental-models.md](./references/mental-models.md)); level-adapted structure; confidence + justification; offer deeper/redirect.

5. **Progressive deep-dive** — On “go deeper” / `--progressive` ([progressive-deep-dive.md](./references/progressive-deep-dive.md)).

## Audience levels (load matching ref)

| Level | Ref |
|-------|-----|
| Child | [level-child.md](./references/level-child.md) |
| Layperson | [level-layperson.md](./references/level-layperson.md) |
| Beginner | [level-beginner.md](./references/level-beginner.md) |
| Academic | [level-academic.md](./references/level-academic.md) |
| Specialist | [level-specialist.md](./references/level-specialist.md) |
| Frontier | [level-frontier.md](./references/level-frontier.md) |

Also: [flags.md](./references/flags.md) · [examples.md](./references/examples.md) · [templates.md](./references/templates.md).

## Hard rules

- Modular: keep this file thin; load level/ref only when needed.
- Brief/simple wording beats the rich template.
- End with a clear next-step invitation (deeper, quiz, different level).
- At forks: ask once (recommended first); never silent branch.

## Related

- **Parent hub:** `/learn` (leaf — default F-L1 for concepts)
- **Vault on-ramp:** `/vault-explain` → this skill
- **Before long sources:** `/resource-summarizer`
- **Code:** `/code-explainer`
- **Not for:** multi-session workspace → `/teach`; Socratic practice → `/learn` tutor-mode; story → `/story-teacher`
