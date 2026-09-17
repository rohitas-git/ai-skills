# Parallel coordination source adaptation

The live workflow is [full-guide.md](./full-guide.md). These sources are historical
input, not instructions to load at execution time:

- [BuilderIO efficient-frontier](../../../archive/vendor/builderio-skills/skills/efficient-frontier/SKILL.md): adopted bounded task packets, controller synthesis and verification. Excluded automatic cheaper-model selection.
- [BuilderIO efficient-fable](../../../archive/vendor/builderio-skills/skills/efficient-fable/SKILL.md): adopted concise evidence returns; excluded host-specific model assumptions and unsupported numeric efficiency claims.
- [seb1n multi-agent orchestration](../../../archive/vendor/awesome-ai-agent-skills/agent-engineering/multi-agent-orchestration/SKILL.md): adopted dependencies, one owner, authority boundaries and explicit recovery. Its archived JSON validator checks declarations only; it is not installed or invoked by this skill and cannot establish runtime isolation or approval.
- Superpowers dispatching-parallel-agents: adopted independent task decomposition;
  removed claims that different test files prove independence and that multiple
  writers or individual passing suites guarantee a sound integrated result.

Reading source history does not enable recursive delegation, runtime installation,
remote actions, forced retries or broad repository exploration.
