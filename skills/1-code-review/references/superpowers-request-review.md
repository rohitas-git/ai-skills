# Requesting a bounded review

Use when the user or active workflow permits independent review. Otherwise run the
same review locally. Do not assume a particular host tool, model or inherited chat.

1. Record caller, requirements, exclusions, canonical repository/worktree and the
   exact review candidate. Use the shared [candidate contract](../../0-review/references/review-candidate.md).
   Do not use HEAD~1 unless it is the actual requested boundary; include task-owned
   uncommitted changes when those are under review.
2. Give the reviewer [this brief](./superpowers/code-reviewer.md), source evidence,
   allowed checks, protected paths, and the report contract. Child input is not
   permission to move branches, create worktrees, mutate files or use new systems.
3. Use the host's documented delegation API and permitted model policy. Parallel
   axes need a stable candidate and no concurrent writer; otherwise review serially.
4. Inspect returned findings against primary evidence. Resolve disagreement by
   evidence, not by author/model preference. Missing evidence remains visible.
5. Return the queue to the requesting workflow. Repair only when authorized;
   refresh affected verification and review after a fix. Do not initiate another
   whole-branch pipeline when serving a combined review or repair loop.
