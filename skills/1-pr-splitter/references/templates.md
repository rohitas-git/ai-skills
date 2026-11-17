# Templates and release notes

## Local scratchpad

Prefer `.notes/pr-split.md`; keep it ignored locally or untracked. Check repository ignore rules and status. If local exclusion is needed, inspect the repository's actual Git exclude path rather than assuming `.git` is a directory. Do not add a tracked ignore rule just to hide scratch notes. Preserve any existing notes and never include them in a split commit unless explicitly requested.

```markdown
# PR split scratchpad

Original branch / source PR:
Original tip SHA:
Backup ref: backup/original-large-pr
Backup SHA:
Base branch / pinned SHA:
Mode / authorized effects:
Topology / dependency reason:

## Planned PRs

1. branch-name
   - Immediate base / SHA:
   - Scope:
   - Files/hunks extracted:
   - Candidate SHA (or uncommitted diff identity):
   - Verification checklist and results:
     - Relevant build/typecheck/lint/tests:
     - PR-scoped changeset: packages, bump type, scoped message (or policy-based N/A)
   - Status:

## Remaining original intent

- Unit / evidence / extracted, remaining, superseded, or deferred:

## Drift notes

- Date / branch / reviewed decision / reason / replacement:
- Old parent + child SHAs / new parent + child SHAs:
- Range-diff summary / verification:
```

## PR description

```markdown
## Summary

This is PR N of M split from a larger change.

## Scope

- ...

## Intentionally excluded

- Follow-up PR will handle ...

## Verification

- ...
```

Name each PR's immediate base and dependent follow-ups where helpful. Keep full extraction notes local; a reviewer needs purpose, boundaries, dependencies, and evidence. When N/M changes, update the description rather than leave a stale sequence.

## Changesets

First inspect the target repository's release policy and installed tooling. Where Changesets is used and policy requires an entry, each applicable split PR carries its own scoped changeset. Do not copy the source branch's combined changeset into a split PR unchanged. If policy exempts a PR, record the exemption; repositories without Changesets use their own release-note process.

1. Identify exact changeset files introduced by the source PR. Exclude those combined entries during extraction; if already carried over into a task-owned split branch, remove only those identified files. Preserve unrelated and immediate-parent changesets.
2. Create a replacement using the repository's existing CLI and documented command. The supplied source used `.mastracode/commands/changeset.md` and this shorthand:

   ```bash
   pnpm changeset -s -m "scoped message" --patch pkg-name
   ```

   Use that shorthand only when the target repository documents/supports it. Otherwise use its supported Changesets workflow. Do not install a CLI or assume a Mastra-specific file exists.
3. Name only packages changed by this PR and describe only this PR's behavior. A combined entry listing five packages must not survive in a PR touching only `@mastra/core`.
4. Choose patch/minor/major from repository policy and the actual public contract. A releasable refactor is commonly patch, new compatible API commonly minor, and breaking API commonly major; a prep-only PR may be exempt. Do not infer a major bump from PR size or blindly assign patch to every refactor.
5. Inspect generated entries against the immediate-base diff, include them with the appropriate candidate, and record packages, bump types, scoped message, and verification in the scratchpad. Confirm no combined source entry was duplicated across descendants.
