# Wizard authoring constraints

- Use repository shell conventions. Never embed real credentials, enable shell tracing around
  secrets, print secret defaults, or include secret values in a closing summary.
- Resolve known official URLs. Open a stage's URL before requesting the corresponding input.
  Browser-opening commands belong in the human-run script, not the authoring session.
- Validate variable names and destinations. Treat entered values as data, never shell source.
  Never use `eval` or source a generated dotenv file to recover values.
- Prefer no credential persistence unless required by the accepted stage map. For file writes,
  check path ownership, symlinks, permissions, concurrent edits, and the consuming dotenv format.
  Preserve unrelated entries. Use restricted temporary files, cleanup traps, and atomic replacement
  where compatible. Verify special characters and failure behavior with synthetic input.
- Bind hosted writes to an explicit repository/account/environment. Show the destination and
  request default-no confirmation immediately before the write. Avoid secret values in arguments.
- Declining a stage or losing authentication must produce a skipped/failed result. A summary
  must not say setup is complete if required stages failed or were skipped.
- Re-running must preserve existing values unless replacement is deliberate. Abort safely at EOF
  or cancellation. Do not delete existing resources as an implicit retry strategy.
- Honor the caller's operational restrictions. A human-run script must not smuggle in forbidden
  production migrations, account changes, or destructive actions.
- Reuse an established safe local helper when available. Otherwise author only the helpers this
  procedure needs. Do not copy the archived upstream template unchanged: its dotenv quoting,
  file permissions/symlink behavior, implicit GitHub target, and success summary require revision.
