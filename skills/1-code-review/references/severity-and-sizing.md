# Severity and sizing

Apply labels inside each axis; preserve axis statuses when summarizing blockers.

| Label | Meaning |
|---|---|
| Critical | Evidence-backed severe correctness, security, data-loss or availability impact |
| Major / Important | Material defect or required contract/policy gap that needs resolution |
| Nit | Optional local clarity/style suggestion |
| Optional | Nonblocking alternative or future improvement |

Severity follows consequence and likelihood, not keyword matches, model confidence
or file length. Missing evidence is a coverage limitation; explain whether it blocks
the requested completion claim without inventing a code defect.

Recommend splitting incoherent changes along meaningful, verifiable boundaries.
Line counts are review-effort signals unless the project sets a hard limit.
Dependency/lockfile changes need compatibility and relevant risk evidence; do not
require an unrelated upgrade or cleanup to complete a scoped review.
