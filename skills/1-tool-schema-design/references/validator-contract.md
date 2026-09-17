# Structural validator contract

From this skill directory, with Python 3.10+:

```bash
rtk python3 scripts/validate_tool_schema.py /absolute/path/to/tool.json --strict
```

The helper reads one explicit stable regular UTF-8 JSON file, maximum 1 MiB and 64
container levels. It rejects final-component symlinks, directories, FIFOs, duplicate
object members and non-standard JSON numbers. It does not follow `$ref`, fetch network
resources, install anything, import the tool, execute defaults/examples, write files,
or validate evidence. Parent-directory symlinks/races are not sandboxed; use a trusted,
task-owned location and stable input.

| Exit | Meaning |
|---|---|
| 0 | Structural subset passed; without `--strict`, warnings may remain. |
| 1 | Structural errors, or any warning under `--strict`. |
| 2 | Input unavailable/ambiguous/invalid or safe-open support unavailable. |

JSON output includes `structurally_valid`, `strict_pass`, displayed diagnostics and
full counts. At most 100 errors and 100 warnings are printed; `diagnostics_truncated`
is explicit. Property names, malformed values and parser excerpts are not echoed.
The valid tool name is returned because it is restricted to safe identifier characters.

The accepted syntax is an opinionated subset for direct function definitions or
`{"type":"function","function":{...}}` wrappers. It checks common types, object
properties/required/additionalProperties, arrays/items, enum uniqueness, selected
combinators and basic bounds. It does not implement a particular JSON Schema draft,
remote/local references, provider keyword allowlists, regex/format semantics, defaults,
cross-field invariants or branch distinguishability. Warnings use property-name
heuristics for sensitive/free-form surfaces and missing common bounds; clean output
does not prove correct selection, provider compatibility, authorization, safe execution,
SSRF/path containment, or backend conformance. Inspect the original schema privately
and validate the same candidate with the actual configured provider/runtime.
