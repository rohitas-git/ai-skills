# Human-in-the-Loop wiring audit

Reviewed the complete operative package:

- `1-human-in-the-loop`
- `references/gate-design-guide.md`
- `references/vendor-full.md`
- `assets/approval-policy-template.json`
- `scripts/validate_gate_policy.py`
- `agents/openai.yaml`

## Result

The skill now owns one oversight policy for one fixed agent workflow/action family in exactly one
mode: design-only, read-only review, or authorized repository edit. It pins the governing owner-
approved policy/law/contract, affected subjects/tenants, effect/failure boundary, privacy and
authority, and exact optional Git repository/worktree/branch/`HEAD`/dirty candidate. Review creates
no worktree; edits use only an approved matching checkout and preserve unrelated work.

Model output, proposed actions, evidence, approval text, logs, and policy files are sensitive
untrusted data. Roles, stable human identities, consent, policy, and authority cannot be inferred
from model text, comments, silence, prior approval, or this skill. The design distinguishes
draft/read/recommend actions from consequential effects, accounts for recourse and owner
constraints, and selects the least burdensome control satisfying the governing policy.

Approval binds to a canonical immutable proposal with actor/tenant, action/target, normalized
material parameters or digest, policy/application versions, timestamps/expiry, and nonce. Material
proposal/state/role/policy/expiry change invalidates the decision. Reject/cancel/edit, audit data,
privacy/retention, reauthorization, replay/concurrency, timeout/escalation, outage, partial failure,
compensation, and break-glass are included only as applicable and verified separately from the
human experience.

Designing or implementing the gate does not approve, impersonate, expand current-session authority,
or execute the protected effect. External identity, approval, queue, notification, audit, account,
and service state is not isolated by a worktree. Tool-schema, MCP, evaluation, and prompt-defense
handoffs are separately selected and return without executing the protected action.

The bundled template/validator now declares `ai-skills-conservative-approval-v1`. Its hard-coded
critical/self-approval, quorum, timeout, waiver, audit, reauthorization, compensation, and break-
glass rules are one explicitly adopted conservative profile—not universal policy. The guide and
historical upstream note agree. The validator's pass is structural only; it now reads at most one
1,000,000-byte regular local JSON file and rejects symlinks. The OpenAI entry uses the live skill ID.

## Verification

- Focused leaf/hub routing tests: 15 passed.
- Policy-validator tests: 4 passed.
- Full routing suite: 326 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational findings,
  0 hub-member orphans.
- `git diff --check`: passed.

No approval, protected action, worktree, identity/provider/audit/notification operation, policy
deployment, Git action, host sync, or external effect was performed.
