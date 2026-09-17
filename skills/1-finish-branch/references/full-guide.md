---
name: finishing-a-development-branch
description: Complete an implemented branch through the user's selected integration outcome
---

# Finishing a Development Branch

Use after implementation and review. Receive the feature branch, exact verified SHA,
actual base branch, required-check evidence, workspace path, and ownership from the
calling workflow. An entry here is not permission to merge, push, or discard.

## 1. Verify the candidate

Inspect the current tree, branch, dirty files, and existing verification evidence.
Use the repository's required checks for this change. Run missing checks and rerun
those invalidated by subsequent changes; a green result applies only to the tree
it tested. Failing or unavailable required checks block a ready/merge claim.
Report them and preserve the work; a user can still choose to keep it.

## 2. Resolve environment and base

Inspect `git worktree list --porcelain`, the current repository root, branch or
detached HEAD, and any superproject. Use the PR's declared base, the plan, or
established branch provenance to identify the integration target. A merge-base
with main does not prove main is the intended target; ask if unresolved.

Carry creation/ownership evidence from `/1-git-worktrees`. A directory convention
does not establish ownership. Record the original worktree path before changing
directories. Resolve the destination checkout from registered worktrees rather
than deriving its location from the Git metadata directory.

## 3. Present or honor the chosen outcome

If the user already selected an outcome and granted its required authority, proceed
with that choice. Otherwise offer:

1. Merge back to the confirmed base locally.
2. Push the feature branch and create a PR.
3. Keep the branch as-is.

For detached HEAD, offer only pushing to a named feature branch and creating a PR,
or keeping the workspace as-is. Do not offer discard as a routine option.
Protected/default-branch operations still require the user's explicit permission.

## 4. Execute the selected outcome

**Local merge:** verify the destination checkout is clean and appropriate.
Refresh remote state; stop to resolve unexpected divergence rather than using an
unqualified pull that may rewrite local history. Merge the confirmed feature SHA
into the approved base. Verify the merged result before any cleanup. If merge or
verification fails, retain the branch/worktree and report the exact state.

**Push and PR:** use `/1-pr-summarizer` for the description and `/1-github-cli`
for GitHub publication, or the repository's forge tooling. Confirm head/base and
remote destination. Use a normal push; rejected pushes require investigation,
not automatic force. Detached HEAD needs an explicit feature-branch destination.
Return the PR URL. Keep the worktree for feedback.

**Keep:** report branch or detached SHA, worktree path, verification state,
remaining work, and relevant running local services.

## 5. Cleanup only the confirmed target

After a successful verified local merge, or a separately confirmed discard,
remove only a workspace whose ownership and cleanup authority are established.
Use the platform's lifecycle tools for platform-owned workspaces when authorized;
otherwise preserve them. Stop only task-owned local services when that shutdown
is included in the cleanup decision; never stop a stack shared with other work.

Inspect modified/untracked files first. If removal is refused, show the affected
paths and ask how to preserve or dispose of them; never retry with force.
Run removal from an existing directory outside the target worktree.
After successful removal, delete a merged feature branch with `git branch -d`
only when branch cleanup was selected. Do not prune unrelated registrations.

## Explicit discard request

Only after the user asks to throw the work away, show the exact branch, unique
commits, worktree path, and modified/untracked files at risk. Require the exact
word `discard` before destructive cleanup. Confirmation covers only the listed
targets. Complete authorized workspace cleanup before force-deleting that branch.
If ownership is unclear or user files remain unresolved, stop deletion.

## Return contract

Report the selected outcome, final SHA, evidence, PR URL if any, retained or
removed workspace/branch, affected local services, and outstanding blockers.
No successful integration or cleanup is implied by merely presenting options.
