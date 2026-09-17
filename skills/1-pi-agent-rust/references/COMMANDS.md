# Candidate command recipes

Snapshot guidance only. Before using a command, verify the file, script, test target,
tool, environment variable, and side effects against the current checkout and its
rules. These examples grant no install, uninstall, network, release, shared-cache, or
host-state authority.

## 1) Optional resource isolation

```bash
# Choose unique, writable paths for this exact worktree when isolation is needed.
# Do not copy a shared absolute path from this snapshot.
```

## 2) Fast Recon

```bash
git status --short
rg -n "TODO|FIXME|install|uninstall|skill|checksum|sigstore|completion|provider|session|extension" \
  install.sh uninstall.sh README.md tests/installer_regression.sh src/
```

## 3) Skill Integrity and Sync Guard

```bash
bash scripts/skill-smoke.sh
```

## 4) Installer and Shell Safety Gates

```bash
bash -n install.sh uninstall.sh tests/installer_regression.sh
shellcheck -x install.sh uninstall.sh tests/installer_regression.sh
bash tests/installer_regression.sh
```

## 5) Rust Quality Gates

```bash
# Use only when `rch` is installed and repository instructions prefer it.
rch exec -- cargo check --all-targets
rch exec -- cargo clippy --all-targets -- -D warnings

# Formatting can run locally
cargo fmt --check
```

## 6) Targeted Test Slices

```bash
# Tool behavior
cargo test tools

# Provider streaming/protocol
cargo test provider_streaming

# Session persistence/index
cargo test session

# Extension runtime/policy
cargo test extension

# RPC surface
cargo test e2e_rpc

# Broader safety net after targeted slices
cargo test conformance
```

## 7) Installer interfaces (read-only discovery first)

```bash
# Help/flag visibility
bash install.sh --help

# Do not run installer/uninstaller commands from this snapshot. Inspect help and the
# regression harness, then use only an already-authorized disposable test fixture.
```

## 8) Status and Safety Tracing

```bash
# Installer status flow
rg -n "AGENT_SKILL_STATUS|CHECKSUM_STATUS|SIGSTORE_STATUS|COMPLETIONS_STATUS" install.sh

# Skill install safety + replacement
rg -n "install_skill_to_destination|is_installer_managed_skill_file|is_expected_skill_destination" install.sh

# Uninstall safety guards
rg -n "remove_installed_skills|is_managed_skill_file|is_expected_skill_directory|PIAR_AGENT_SKILL" uninstall.sh
```

## 9) Docs Drift Checks

```bash
rg -n "no-agent-skills|completions|checksum|sigstore|artifact-url|skill" README.md install.sh uninstall.sh
```

For symptom-driven step-by-step root-cause flows, use `DEBUGGING-PLAYBOOKS.md`.
