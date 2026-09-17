# Bases procedure and minimal examples

The installed Obsidian version and current official schema are authoritative. Load this only for
the exact `.base` operation selected by the main skill. Do not copy a full example by default.

## Build the smallest object

1. Define the intended population in plain language, including exclusions and sensitive fields.
2. Inspect the existing file and active vault property names/types; do not invent them.
3. Add or change only the required global/view filter, formula, display property, summary, or
   named view. A Base defaults to a broad population when filters are absent, so assess exposure.
4. Parse as YAML. Resolve every referenced property/formula/view against the candidate and active
   version. Preserve unknown fields instead of treating this note as an exhaustive schema.
5. Preview representative matching paths/fields when possible without exposing unrelated note
   content. Runtime-check the named view/query only through the separately authorized CLI handoff.

## Minimal shape

```yaml
filters:
  and:
    - 'file.inFolder("Projects")'
    - 'status == "active"'

formulas:
  age_days: '(today() - file.ctime).days'

views:
  - type: table
    name: "Active projects"
    order:
      - file.name
      - status
      - formula.age_days
```

This is syntax illustration only. Folder, property, formula, function, view-type, and summary
support are version-sensitive. Confirm them against `https://help.obsidian.md/bases/syntax`,
`https://help.obsidian.md/bases/functions`, and local runtime/help evidence.

## Static checks

- exact target is a contained `.base` file and a create does not collide;
- YAML parses without rewriting unrelated formatting;
- filter nesting and quoting match the installed schema;
- every `formula.X` use has a fitting definition and expected output type;
- view name is unique where required and every ordered/grouped/summarized field exists;
- intended population is not accidentally vault-wide or privacy-invasive;
- plugin-dependent view/function behavior is labeled and not installed automatically;
- dynamic date/time formulas are tested with representative boundary values when material.

## Result contract

Return the exact hunk and static results. If runtime validation was authorized, include exact
vault/path/view, command, result shape/count, redactions, and observed version. A rendered view
does not prove every note matches the intended semantics; state the sampled/queried coverage.
