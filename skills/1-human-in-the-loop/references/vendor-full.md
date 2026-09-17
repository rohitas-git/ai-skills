# Upstream Human-in-the-Loop snapshot

Historical source snapshot, not operative instructions. The live skill, active gate guide, adopted
organization policy, and exact caller authority control all work.

Source: `seb1n/awesome-ai-agent-skills`, upstream skill `human-in-the-loop`, commit
`75865a5d037a4cdaa7f409a4ec14ab9b0292920b` (MIT).

Ideas retained after adaptation:

- put judgment at the decision boundary where it changes risk;
- bind a decision to an exact immutable proposal and revalidate before execution;
- separate requester, approver role, and stable human subject;
- design rejection, expiry, retries, partial failure, recovery, and audit evidence;
- do not mistake a confirmation dialog or model text for authorization.

Not adopted as universal defaults: a mandatory seven-artifact deliverable, fixed risk tiers,
two-person control for every critical label, fixed timeouts/attempts/expiry, break-glass design,
automatic implementation, or execution of the protected action. The bundled validator enforces
one explicitly named conservative profile only when an owner adopts it.
