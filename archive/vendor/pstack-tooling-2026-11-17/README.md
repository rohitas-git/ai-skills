# Pstack entry-point provenance

These three upstream entry points are retained as source evidence only. Do not execute them or add
this directory to host discovery. Adapted live tools have existing catalog owners and are documented
in [pstack tooling](../../../guidelines/catalog/pstack-tooling.md).

Source: cursor/plugins `e1cc03121a0e71129a4fb730d7c5528a0a3e43c8`, pstack 0.15.43, MIT, Lauren Tan.
The bootstrap performs dependency installation; the worktree audit fetches refs and reads Cursor
transcripts. Their live adaptations intentionally have different effects. The log adapter adds
locking, file checks, and leading-whitespace formula escaping.

The [manifest](../../../guidelines/catalog/pstack-tooling-manifest.json) records source paths and hashes
for these originals and the live CLI/test corpus. No complete plugin or automation pack is promoted.
