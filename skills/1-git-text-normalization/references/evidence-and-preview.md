# Evidence and preview checklist

1. Record repo/worktree, branch/`HEAD`, index/working-tree status, exact paths, dirty owners, and relevant blob and
   attribute-file hashes.
2. Inspect working file and committed blob separately for MIME/encoding, BOM, NUL bytes, and EOLs.
3. Inspect effective attributes and LFS tracking for each exact path.
4. In diagnose mode, return a proposed exact-path change without staging or writing.
5. In fix mode, preserve source/hash, edit only authorized paths, and use temporary files or a temporary index for
   experiments. Do not stage merely to make a preview work.
6. Compare semantics plus textual diff, then verify effective attributes and status. Stop if any unexpected path,
   LFS rule, or semantic content changes.

Broad renormalization, host Git configuration, LFS migration, history rewrite, staging, commit, and push are separate
effects with separate authority.
