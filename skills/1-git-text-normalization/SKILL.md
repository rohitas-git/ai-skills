---
name: 1-git-text-normalization
description: >
  Diagnose or make one explicitly requested correction to tracked text encoding, line
  endings, or Git attributes without broad churn. Use for unexpected binary diffs, one
  UTF-8 conversion, or exact-path normalization. Not for: LFS migration, history rewrite,
  or routine commit grouping. Hub: /0-git.
disable-model-invocation: true
metadata:
  catalog:
    hub: 0-git
    role: leaf
    when:
      - "diagnose one unexpected binary diff, encoding, EOL, or exact-path attribute problem"
      - "make one explicitly requested scoped text-normalization correction"
    not_when:
      - "ordinary ignore rules or secrets → 2-security-and-hardening"
      - "LFS migration → repository-specific LFS process"
      - "history rewrite → 1-pr-repair or 1-stacked-pr-repair"
      - "routine commit grouping → 1-atomic-git-commits"
    prev: [0-git]
    next: [0-git, 1-atomic-git-commits]
    cousins: [1-atomic-git-commits, 2-security-and-hardening, 1-stacked-pr-repair]
    triggers: [git text normalization, binary diff, .gitattributes problem, normalize line endings, convert tracked file to UTF-8, exact-path renormalization]
    requires_setup: false
---
# Git Text Normalization

**Atomic job:** diagnose one bounded normalization problem, or apply its one explicitly requested local correction.

1. Select `diagnose` (read-only default) or `fix` (requires explicit edit authority). Pin caller, repo/worktree,
   branch/`HEAD`, index and working-tree state, dirty/untracked owners, exact paths, relevant attribute-file/blob hashes,
   observed symptom, intended stored/working format, allowed paths, and whether staging/commit is authorized. A linked
   worktree has its own index but still shares repository objects, attributes in history, hooks, and remote state.
2. Inspect exact working files and committed blobs for encoding, BOM, NUL bytes, EOLs, effective attributes, and LFS
   tracking. Treat NUL-containing content as binary until evidence establishes the intended replacement. Do not infer
   a repository-wide policy from one binary diff.
3. Choose the narrowest correction: one content conversion and/or exact-path `.gitattributes` rule. Diagnose mode
   stops with a proposed diff. Fix mode edits only authorized working-tree paths, preserving a recoverable original or
   hash until verification. Never stage an attribute rule merely to preview behavior.
4. Preview with read-only attribute checks, temporary copies/indexes when needed, exact-path dry runs, status, hashes,
   and semantic/textual diffs. Stop on revision drift, unexpected paths, LFS changes, or semantic changes. Broad
   renormalization and host-wide Git configuration require a separate coordinated request.
5. Return mode, candidate identity, cause, changed/protected paths, before/after format evidence, exact diff,
   verification, effects, and residual risk to `/0-git` or the actual caller. `/1-atomic-git-commits` is optional only when a
   commit was requested; this skill never pushes, rewrites history, or mutates remote state.

Detailed checklist: [evidence and preview](./references/evidence-and-preview.md).
