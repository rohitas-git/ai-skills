# Supply-Chain & Dependency Auditing Guidance

Load this during Phase 1 (Recon) and Phase 2 (Hunting) for any project that has external dependencies, build scripts, container images, or CI/CD pipelines.

## Inventory & Visibility
- Identify all package manifests and lockfiles (package.json + package-lock/yarn.lock/pnpm-lock, requirements.txt / poetry.lock / Pipfile.lock, go.mod + go.sum, Cargo.toml + Cargo.lock, pom.xml / build.gradle, etc.).
- Note whether lockfiles are present and committed.
- Identify transitive dependency depth and any “phantom” or unused direct dependencies.
- Check for private/internal registries and how authentication to them is handled.

## Vulnerability & Freshness
- Look for known vulnerable versions (even without running an external scanner — note patterns of very old packages, packages with recent critical CVEs that are unpinned, etc.).
- Unmaintained or abandoned packages (last release years ago, single maintainer, etc.).
- Overly broad version ranges (`*` or `latest`) that allow unexpected major upgrades.
- Missing or ignored security advisories in CI.

## Integrity & Provenance
- Absence of lockfiles or integrity hashes (e.g., no `package-lock.json`, no `go.sum`, no Cargo.lock).
- Install scripts (`postinstall`, `preinstall`) that run arbitrary code.
- Dependencies that download additional code at install or runtime without verification.
- Use of `curl | bash` or equivalent in Dockerfiles, Makefiles, or CI scripts.
- Unsigned or unverified container base images and packages.

## Confusion & Typosquatting Risks
- Package names that closely resemble popular packages (typosquatting).
- Dependency confusion potential (public package with same name as internal one, or missing scope).
- Unexpected maintainers or sudden ownership changes (harder to detect statically, but note if documentation mentions it).

## Build & CI/CD Pipeline Risks
- Secrets available to build jobs that should not need them.
- Build scripts that pull code from untrusted branches, PRs, or user-controlled sources.
- Lack of pinning for actions, Docker images, or third-party orbs.
- Overly permissive GitHub Actions / GitLab CI permissions (`write-all`, etc.).
- Artifacts published without signing or attestation.
- Cache poisoning vectors.

## Runtime & Deployment
- Container images that run as root or with excessive capabilities.
- Secrets baked into images or environment variables visible in process lists.
- Dynamic loading of remote code or plugins at runtime without integrity checks.
- Auto-update mechanisms that do not verify signatures.

## Finding Quality Rules
- Prefer findings with clear impact (e.g., “Known RCE in dependency X version Y used by critical path Z”).
- Distinguish between direct and transitive issues; note whether the vulnerable function is actually reachable.
- For missing lockfiles or unpinned versions, explain the practical risk (reproducible builds broken, silent major upgrades, etc.).
- When possible, suggest concrete remediation (pin version, replace package, add integrity check, move secret out of build, etc.).

## Positive Patterns Worth Noting
- Consistent use of lockfiles + integrity verification.
- Dependabot / Renovate or equivalent automated updates with review.
- Minimal dependency sets and regular pruning.
- Signed commits, signed releases, or SLSA-style provenance.

Map supply-chain findings primarily to OWASP A03 (Software Supply Chain Failures) or A08 (Software and Data Integrity Failures).
