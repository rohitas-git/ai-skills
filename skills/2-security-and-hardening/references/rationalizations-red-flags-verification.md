# Verification traps

Use after implementing the scoped fix, alongside [security-checklist.md](./security-checklist.md).

| Temptation | Evidence-based response |
|---|---|
| “It's internal” | Assess its actual users, trust boundaries and compromised-component paths |
| “The framework handles it” | Verify the configured control and any escape hatches on this path |
| “The test passes” | Check that it exercises the relevant threat and preserves allowed behavior |
| “The audit is green” | Identify package/advisory scope, freshness and execution limits |
| “An owner check happened earlier” | Ensure ownership/state still constrains the actual mutation |
| “The output is schema-valid” | Validate authority and allowed effect separately |
| “The path is inside the directory” | Establish ownership, alias/symlink handling and check/use safety |
| “We removed the secret line” | Report exposure; revocation/history work still needs explicit authority |
| “The checklist says disable it” | Preserve required features and use a justified, approved control |
| “A finding means fix everything nearby” | Repair only the authorized defect; separate broader follow-ups |

Report confirmed weaknesses separately from pattern-match leads. A public endpoint,
public credential-free CORS response, development-only diagnostic or deliberate
sandbox prototype is not automatically a vulnerability. Conversely, labels such
as “test fixture,” “internal,” or “prototype” do not prove sensitive data is fake
or justify removing controls needed for that environment.

Verify the original failure path plus meaningful negative/positive cases on the
actual candidate. Do not weaken a test or suppress an advisory to declare success.
Reuse applicable existing evidence and report what it cannot establish. Return
to the caller; no extra review/repair loop, deployment, commit or cleanup.
