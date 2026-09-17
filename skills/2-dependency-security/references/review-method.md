# Dependency review method

Follow the parent's scope, candidate, read-only authority and return target. This
guide assesses application dependencies; third-party agent packages belong to
`/2-skill-supply-chain-audit`, which inspects their instructions and capabilities.

## Comparable evidence

Record the package manager, exact resolved package identity/version/source, lockfile
and workspace paths, base/candidate revisions (including dirty inputs), advisory
source and retrieval time, scanner version/options and any excluded ecosystems.
If comparable base evidence is unavailable, report the gap; a current-head scan
alone cannot establish whether a vulnerability is new to this PR.

Use current primary advisories or publisher/security-maintainer releases for claims
about affected/fixed versions. Names, staleness or a scanner's category are leads.
Establish installed version range and reachable runtime/build/install path. A dev
dependency can affect CI or artifacts even when absent from production imports.
Never execute a suspected package to prove malicious behavior.

When permissions allow a scanner, inspect its behavior first: offline versus
network, input disclosure, lifecycle execution, disk writes and exit-code meanings.
Do not use automatic fix flags. Preserve reported findings separately from scanner
execution errors; an unavailable service or parsing failure is not zero findings.

## Ratchet by issue identity

1. Pin the actual PR base (immediate parent for a stack) and candidate.
2. Compare both against equivalent advisory data and scan options. Record any
   database/source drift that prevents a reliable introduction claim.
3. Reconcile advisory aliases, ecosystem/name/version and dependency paths. A new
   route to an already-known affected package can change exposure and needs review.
4. Classify each issue: introduced, worsened, unchanged, resolved or unknown.
   Aggregate counts are a summary, never the decision rule.
5. Apply the approved severity/reachability policy and explicit exceptions. Never
   edit baselines, thresholds or expiry dates just to pass a check. Existing debt
   remains visible even when an approved ratchet does not block on it.

Example: the base contains A; the candidate resolves A but adds B. Both have one
finding, yet B is an introduced issue. “Count did not increase” misses the regression.

## New packages and staleness

Inspect registry identity, source provenance, requested capability, license,
transitive graph and lifecycle scripts as data. Recommend reuse only when an
existing package meets the actual contract; do not impose cross-module coupling.
Release age, maintainer count and a major-version gap are maintenance signals,
not proof of insecurity. Check support policy and relevant security releases.
Do not claim an upgrade is compatible merely because it removes an advisory.

## Report and return

Return a table of issue/package → evidence → base/candidate relation → impact →
policy disposition → smallest next action, plus advisory freshness and coverage
limits. Separate proposed check design from installed/enforced CI behavior.
No findings is a bounded, point-in-time result, not proof of permanent safety.
Repairs and CI edits return to the implementation caller only when authorized;
refresh checks after changed manifests, lockfiles, configuration or build inputs.
