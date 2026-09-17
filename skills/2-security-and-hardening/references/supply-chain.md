# Scoped dependency hardening

For evidence collection and base/candidate vulnerability classification, use
/2-dependency-security and return its result to the implementation caller. A
scanner severity or lower aggregate count is not by itself a remediation plan.

## Decide before changing

Confirm the approved package/issue, affected runtime/build/install paths, compatible
fixed versions and project policy. Dev-only dependencies can affect shipped artifacts
or privileged CI. A workaround, replacement or exception needs its own evidence;
an allowlist entry or deadline does not constitute approval.

Choose the smallest compatible change and inspect manifest, lockfile and script-
policy diffs together. No automatic forced audit fixes, cross-project upgrades,
new service integration or widened exception baseline. Preserve unrelated user work.

## Installation boundary

Resolve the package manager and exact version from the repository, authoritative
lockfile, workspace ownership and CI. A package may belong to an ancestor workspace;
the nearest manifest is not always an independent install root. Independent projects
may legitimately use different managers. Resolve conflicts before changing a lock.

When installation is an authorized implementation step, determine the pinned client's
actual frozen/immutable and lifecycle-script controls from official documentation.
Do not discover untrusted scripts by running them first. Disable unreviewed dependency
scripts or use a proven fail-closed policy, inspect exact package/script sources, and
approve only what is explicitly required and authorized. Never blanket-approve.

Verify root/workspace scripts, optional/platform packages and later build commands
too; blocking dependency lifecycle hooks does not sandbox arbitrary project commands.
Avoid changing a global package-manager policy or wiping an existing install to test
a branch. Use an appropriate task-owned workspace for clean-install verification.

Package-manager defaults change. Consult the applicable version's documentation:
[npm](https://docs.npmjs.com/cli/), [pnpm](https://pnpm.io/),
[Yarn](https://yarnpkg.com/). Do not use a static version matrix as proof of current
behavior, substitute another manager, or claim script approval support without
checking it. External audits may disclose private inventory; verify that authority.

## Verify and return

Run relevant build/tests and dependency checks for the actual changed candidate;
verify script policy before any permitted execution. Signature/provenance support
is ecosystem-specific; absence alone is not proof of compromise. Record package
identity, advisory sources/dates, effective policy and residual risk.

Return the scoped diff and evidence. Commit or publish only through the caller's
authorized Git/release path; this reference never commits an approval policy itself.
