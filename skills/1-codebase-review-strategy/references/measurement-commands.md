# Safe measurement guidance

Use repository-local, read-only commands already available on the host. Prefer `rg --files`, manifest inspection,
existing ownership/configuration files, and targeted counts over recursive execution or installation. Exclude generated,
vendor, cache, build, and dependency trees according to the pinned scope. Record the exact command, candidate `HEAD`,
dirty-state inclusion, exit status, and truncation. Counts describe the candidate; they do not determine review quality.
