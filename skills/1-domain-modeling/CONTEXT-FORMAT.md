# Context-language format

Use only for the `context-language` mode of `/1-domain-modeling` after the relevant meaning or
relationship is accepted.

## Placement

- Preserve existing repository conventions and generated-file ownership.
- If `CONTEXT-MAP.md` exists, use its explicit context paths; do not infer ownership across contexts.
- If one root `CONTEXT.md` exists, update only the accepted context entry.
- If neither exists, propose a root `CONTEXT.md`; create it only in explicitly authorized apply mode.

## Term entry

```md
**<Canonical term>**:
<One or two sentences defining its domain meaning and boundary.>
_Avoid_: <only evidenced ambiguous aliases>
```

Context relationships may be recorded in the repository's existing map format. Keep implementation
details, framework terms, speculative scenarios, and unresolved meanings out of the accepted glossary.
Preserve conflicting stakeholder meanings as unresolved rather than choosing one silently.

Verify the exact target and diff after an apply. Do not stage, commit, publish, or update a second artifact.
