# Source adaptation: agent-watchdog

Historical source: [BuilderIO agent-watchdog](../../../archive/vendor/builderio-skills/skills/agent-watchdog/SKILL.md).

Adopted: reconstruct the current request, inspect the other agent's actual artifacts,
form independent hypotheses, seek counterevidence and distinguish gaps, defects,
scope drift and verification misses.

Not adopted as automatic behavior: monitoring a live agent, relaying messages,
accessing production data, spawning workers, changing branches or making fixes.
The source is historical context; the local verification guide governs execution.

For a supplied completed run, verify only the scoped claims using available primary
evidence and report missing transcript/source access. For explicit monitoring, use
the host's documented recurring/wait mechanism against a confirmed live handle;
an observation timeout does not prove the run stopped. Do not silently convert
one verification pass into a watcher.

Process-improvement recommendations belong to /1-agent-workflow-observer, not this
outcome-verification pass. Any handoff is conditional on that separate request.
