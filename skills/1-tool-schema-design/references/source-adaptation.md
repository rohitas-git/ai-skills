# Source adaptation

Source: seb1n/awesome-ai-agent-skills, upstream `tool-schema-design`, commit
`75865a5d037a4cdaa7f409a4ec14ab9b0292920b`, MIT. The [full snapshot](./vendor-full.md)
is historical. Live procedure and [validator contract](./validator-contract.md) govern use.

Retained: one coherent intent per tool, contrastive selection descriptions, bounded
arguments, trusted server-side identity and authorization, explicit effect/confirmation/
idempotency/error contracts, provider validation and both denied-effect and utility tests.

Adapted: design/review does not authorize source edits, provider calls, dependency
installs or consequential tool execution. Specialist calls preserve the caller's mode
and return. A matching worktree isolates source state only when needed; it is not a
security sandbox or permission to reset services. JSON Schema describes input shape,
not authorization, runtime destination policy, output trust or implementation fidelity.

The existing validator remains a conservative partial checker, not a general JSON
Schema implementation. It now bounds and safely opens one explicit file, rejects
ambiguous/non-standard JSON, handles hostile shapes without crashing, redacts
user-controlled diagnostic values, caps output and states its supported contract.
Provider/runtime testing remains independent evidence.
