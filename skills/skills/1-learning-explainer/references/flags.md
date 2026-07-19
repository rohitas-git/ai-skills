# Flags, Modes & Trigger Phrases

## Explanation Level Triggers
Use these phrases to request a specific audience level:

| Level       | Trigger Phrases                                      |
|-------------|------------------------------------------------------|
| **Child**       | child level, for kids, ELI5, very simple, explain like I'm 8, story for children |
| **Beginner**    | beginner, absolute beginner, new to this, from scratch, I know nothing |
| **Layperson**   | layperson, normal person, everyday explanation, general audience, in simple terms |
| **Specialist**  | specialist, practitioner, professional, how it works in practice, for someone who works with this |
| **Academic**    | academic, graduate, scholarly, university level, rigorous, with theory and evidence |
| **Frontier**    | frontier, cutting-edge, 1-research level, expert, state of the art, latest developments, open problems |

## Mode & Format Flags
- `--compact` or "keep it short", "compact version", "brief summary"
  → Deliver a shorter response (overview + 2–3 key levels + confidence)

- `--clt` or "with CLT", "using Cognitive Load Theory"
  → Activate CLT guidance (only on explicit request)

- `--progressive` or "deep dive", "go deeper", "continue", "next level", "expand on X"
  → Enable iterative deep-dive mode

- `--visual` or "with diagrams", "show visuals", "generate diagram"
  → Prioritize mental models and offer image generation

- `--web` or "use search", "check latest research"
  → Use web_search for verification or recent developments

- `--quiz` or "add questions", "test me"
  → Include self-assessment or 0-review questions

## Combined Usage Examples
- "Explain photosynthesis at layperson level with diagrams"
- "Beginner explanation of transformers, compact mode"
- "Frontier level on CRISPR with CLT and progressive mode"
- "Child level story about how planes fly, with visuals"

## Default Behavior (No Flags)
- Starts with knowledge probe
- Uses clear, neutral explanations
- Adapts to the level requested or inferred
- Includes one mental model + diagram description
- Ends with confidence score and offer to go deeper

## Best Practices
- You can combine multiple flags.
- When no level is specified, start with the knowledge probe and then choose an appropriate default level.
- Always respect explicit mode requests (especially CLT).