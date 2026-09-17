# Source adaptation

Source: seb1n/awesome-ai-agent-skills, upstream `prompt-injection-defense`, commit
`75865a5d037a4cdaa7f409a4ec14ab9b0292920b`, MIT. The [full snapshot](./vendor-full.md)
is retained as historical material. The live skill and [defense patterns](./defense-patterns.md)
define the catalog procedure; attack examples and source instructions remain data.

Retained: full input/memory/agent-hop/sink threat coverage, external authorization,
least privilege, exact-action approval, provenance, inert adversarial cases,
benign utility, explicit control status and structural-only manifest checking.

Adapted: assessment/design does not authorize edits, deployment or incident action.
Only relevant paths and modalities are required; outside-PR debt stays a separate
follow-up. Diagrams, report files and JSON manifests are conditional artifacts, not
mandatory work for every review. A local implementation claim is not proof of deployed
state. Evidence and test IDs are references to claims, not verified by the checker.
Missing/planned controls remain visible even when the document is structurally valid.

The upstream incident list is a planning checklist, not permission to disable tools,
quarantine records, rotate credentials or restore services. Preserve redacted evidence
and return containment recommendations to the authorized incident owner. All specialist
handoffs retain caller mode and return to the same scoped workflow.

Helper adaptations reject malformed types, ambiguous JSON and unsafe/unbounded input,
redact user-controlled diagnostic values, and check destination mapping per egress
tool. The helper remains an opinionated structural linter, not a general JSON Schema
engine, sandbox, policy executor or prompt-injection detector.
