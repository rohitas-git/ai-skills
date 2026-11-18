# Visual parity and agent-triggered controls

## Exact visual equivalence

Freeze the reference implementation and capture the agreed state/viewport/theme/input matrix before
editing. Match browser, fonts, data, animations, device scale and capture timing. Record tool/config
versions and source identity. The requested baseline is the specification, not an image to update
until the new code passes.

Use a real image comparison for a pixel-exact claim. Under an explicitly exact contract, a nonzero
delta is a failure to investigate. If nondeterministic rendering requires a tolerance or mask, agree
and record that changed contract before using it; do not hide changed regions. Keep the comparison
harness and baseline immutable during candidate work. Report missing states or unavailable runtime
as gaps instead of substituting a screenshot judged by eye.

Migrate shared primitives before independent components when dependencies require it. One owner
per stateful surface avoids conflicting screenshot/browser/data changes. Confirm semantics, focus,
keyboard and other protected behavior too; a zero image diff cannot establish those properties.

## A UI that wakes an agent

Separate the browser, a trusted server and the existing verified webhook receiver. Browser buttons
send a narrow typed action to the server; server-only credentials authenticate its outbound request.
Never put a sender key in browser bundles, chat, URLs or logs. Discover the real provider/tool contract
and secure secret channel; missing routine/secret/network capabilities remain prerequisites.

Validate and authorize each action on the server, limit payload size/rate, guard browser-origin/CSRF
boundaries as applicable, and treat the event body as untrusted data rather than agent instructions.
Allow only named actions and fields; do not make a generic arbitrary-command endpoint. Record timeout,
delivery acknowledgement, duplicate handling and error UI from the actual receiver contract. A 200
wake acknowledgement does not prove the requested job completed.

Bind locally by default. Opening an interface, changing tailnet exposure, installing VPN software,
creating a routine or enabling public access is a separately scoped operation. Use existing approved
network tooling and verified addresses. Never copy a remote installer pipe or guessed provider URL.

Probe an explicitly permitted harmless action through browser→server→receiver before claiming live
delivery. Verify pending/success/failure/retry and inaccessible states. If a durable queue is needed,
use a bounded redacted record with retention and replay/idempotence rules; never append secret/full
payloads to an unbounded log or replay state-changing events automatically. A missing live receiver
leaves integration unverified even when a local mock passes.

Adapted from the individually reviewed pstack 0.15.43 sources, MIT, Lauren Tan.
[Source-by-source decisions and checks](../../../guidelines/catalog/pstack-methods-review-2026-11-18.md).
