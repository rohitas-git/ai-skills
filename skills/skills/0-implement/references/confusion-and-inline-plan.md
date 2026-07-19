# Confusion surfacing + inline plan (harvested)

Source: archive vendor `context-engineering` — implementation-facing pieces only.  
Session packing / hierarchy → [`strategic-compact/references/context-hierarchy.md`](../../1-strategic-compact/references/context-hierarchy.md).

## When context conflicts

Spec and codebase disagree → **do not silently pick**. Surface:

```text
CONFUSION:
Spec says X; code does Y (path).

Options:
A) Follow the spec …
B) Follow existing patterns …
C) Ask — likely intentional; don't override

→ Which approach?
```

## When requirements are incomplete

1. Check code for precedent.
2. If none, **stop and ask** with 2–3 concrete options.
3. Do not invent product requirements.

## Inline plan (multi-step slice)

Before executing a multi-step implement slice, emit a short plan:

```text
PLAN:
1. …
2. …
3. …
→ Executing unless you redirect.
```

Cheap redirect before sunk cost. Not a substitute for `/1-to-tickets` on multi-session work.
