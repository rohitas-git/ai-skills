---
name: 1-resolving-merge-conflicts
description: >
  Use when you need to resolve an in-progress git merge/rebase conflict. Hub:
  /0-implement.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-implement
    role: soft
    when:
      - "you need to resolve an in-progress git merge/rebase conflict"
    triggers:
      - "1-resolving-merge-conflicts"
      - "resolving merge conflicts"
    requires_setup: false
---
## Process

1. Follow this skill's procedure.


1. **See the current state** of the merge/rebase. Check git history, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk.** Preserve both intents where possible. Where incompatible, pick the one matching the merge's stated goal and note the trade-off. Do **not** invent new behaviour. Always resolve; never `--abort`.

4. Discover the project's **automated checks** and run them — typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish the merge/rebase.** Stage everything and commit. If rebasing, continue the rebase process until all commits are rebased.


## Related

**Next:** `/0-implement`. Parent hub: `/0-implement`.
