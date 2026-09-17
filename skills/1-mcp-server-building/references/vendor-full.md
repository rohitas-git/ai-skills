# Upstream MCP Server Building snapshot

Historical source snapshot, not operative instructions. The live skill, pinned official MCP
revision, selected SDK/client documentation, repository rules, and caller authority control.

Source: `seb1n/awesome-ai-agent-skills`, upstream skill `mcp-server-building`, commit
`75865a5d037a4cdaa7f409a4ec14ab9b0292920b` (MIT).

Ideas retained after adaptation:

- minimize capabilities and enumerate data/effects explicitly;
- separate protocol conformance, authorization, consent, and model behavior;
- constrain tool schemas and caller-safe errors;
- test negative authorization, malformed calls, cancellation, retries, and data leakage;
- report exact clients/revisions actually exercised and residual risk.

Not adopted as defaults: one mandatory seven-artifact delivery, automatic current-revision
migration, a specific SDK/transport, blanket feature flags, deployment/rollback operations,
credential rotation, production testing, or automatic specialist chains.
