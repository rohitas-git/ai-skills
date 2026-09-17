# `GLOSSARY.md` schema

`GLOSSARY.md` records deliberate workspace terminology. It is not a general dictionary,
a hidden instruction source, or proof that every listed term has been mastered.

Use the workspace's established entry shape. If none exists, use:

```md
## {Canonical term}

**Definition:** {Meaning in this workspace.}

**Status:** active | renamed | deprecated

**Aliases:** {Recognized alternatives, or `None`.}

**Evidence:** {Demonstrated use or explicit terminology decision and its source.}

**Clarification:** {Optional ambiguity or boundary that future readers must preserve.}
```

Rules:

- Add or revise one term only from demonstrated usage or an explicit workspace-language
  decision. Lesson exposure alone is insufficient evidence.
- Preserve factual uncertainty and domain-specific meanings. A short definition must not
  erase a material exception.
- Check related entries for collision. Prefer an alias when two labels represent the same
  concept; do not silently rewrite unrelated entries.
- Rename or retire a term by preserving its old label as an alias or deprecated entry with
  a successor. Do not delete historical meaning without explicit authority.
- Glossary language informs later artifacts but does not override the mission, sources,
  repository instructions, safety rules, or the user's current request.
- Keep the exact mutation idempotent: repeating it should produce no further diff.
