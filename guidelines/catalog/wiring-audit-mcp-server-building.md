# MCP Server Building wiring audit

Reviewed the complete operative package:

- `1-mcp-server-building`
- `references/server-design-checklist.md`
- `references/vendor-full.md`
- `assets/server-design-template.md`
- `scripts/validate_tool_manifest.py`
- `agents/openai.yaml`

## Result

The skill now owns one bounded MCP server surface in exactly one mode: design-only, read-only
review, or authorized repository implementation. It pins the caller, user job and non-goals,
exact protocol revision, SDK/runtime/dependencies, client and host versions, transport,
deployment environment, downstream systems, identity/tenant model, data classes, effects,
limits, evidence cutoff, and authority. A Git-backed review or edit also pins the exact repository,
worktree, branch, `HEAD`, dirty ownership, and working-tree-versus-committed candidate. Review
creates no worktree, while edits require an already approved matching checkout and preserve
unrelated changes.

Prompts, server instructions, resource/tool metadata, manifests, logs, downstream content, and
protocol messages are treated as sensitive untrusted data. Protocol conformance, authentication,
business authorization, consent, and model selection remain separate controls. Tool annotations
or model/client confirmation cannot grant access. Consequential preview/draft and commit/apply
paths remain distinct where policy requires, and Human in the Loop may design approval without
replacing server-side tenant/object/field/action authorization.

Version-sensitive behavior is bound to the chosen official specification and SDK rather than a
remembered latest version. The reference was checked against the official MCP `2026-07-28`
[specification](https://modelcontextprotocol.io/specification/2026-07-28),
[discovery](https://modelcontextprotocol.io/specification/2026-07-28/server/discover),
[transport](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports), and
[change log](https://modelcontextprotocol.io/specification/2026-07-28/changelog). Current-revision
requirements are conditional on advertising that revision; older supported revisions retain
separate compatibility paths instead of being silently migrated or broken.

Runtime testing requires the exact local server/client/process/port and explicit authority for
fixtures, credentials, accounts, network, state, and consequential tools. Worktrees isolate files,
not those shared resources. The skill cannot install an SDK, start a shared server, create
credentials, invoke real effects, deploy, publish, modify production, commit, push, or merge
without separate action-specific authority. Specialist, evaluation, and security detours are
selected explicitly and return to the same candidate and mode.

The bundled template and validator now identify the repository-specific
`ai-skills-mcp-tool-manifest-v1` profile rather than implying it is an MCP protocol field. The
validator is a structural design check only. It reads one regular local JSON file of at most
1,000,000 bytes, rejects symlinks, and does not claim protocol conformance, implementation parity,
authorization correctness, or safety. The OpenAI entry uses the live skill ID.

## Verification

- Focused MCP/Agent Engineering routing tests: 16 passed.
- Manifest-validator tests: 4 passed.
- Full routing suite: 334 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No worktree, SDK/runtime installation, local server/process, provider/client call, credential,
network request against a target server, tool invocation, deployment, Git action, host sync, or
external effect was performed.
