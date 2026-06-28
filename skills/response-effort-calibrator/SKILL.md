---
name: response-effort-calibrator
description: Guides the AI on response effort, depth, and style (brief, concise, balanced, detailed, exhaustive) based on prompt cues. Use for requests specifying length, detail level, quick answer, in-depth analysis, or similar effort/verbosity controls.
---

# Response Effort Calibrator

## Overview

This skill standardizes how the agent interprets user instructions about response effort, length, and depth. It prevents over- or under-responding by mapping common phrases to consistent behaviors.

## Common Effort Levels (use these mappings)

- **Ultra-brief / Quick / Short answer**: 1-3 sentences max. Key facts only. No examples unless asked.
- **Brief / Concise**: 1 paragraph or bullet list. Essential info, minimal elaboration.
- **Balanced / Standard**: Normal helpful response — context, explanation, pros/cons if relevant. ~200-400 words.
- **Detailed / In-depth**: Comprehensive coverage with examples, reasoning steps, alternatives, potential edge cases. Structured (headings, lists).
- **Exhaustive / Thorough / Full analysis**: Leave no stone unturned — deep research (use tools), multiple angles, comparisons, long-term implications, references. Can be multi-section.

## Instructions

1. **Scan the user query** for effort cues:
   - Keywords/phrases: "briefly", "quickly", "in short", "concise", "detailed", "in-depth", "thoroughly", "comprehensive", "full breakdown", "explain like I'm 5", "expert level", "TL;DR", "step-by-step", etc.
   - Context clues: "just the answer", "summarize", "deep dive", "everything you know", "short response".

2. **Default behavior**: Balanced unless cues present.

3. **Adjust accordingly**:
   - Match the requested level exactly.
   - If conflicting cues, ask for clarification or default to balanced + note the choice.
   - Structure output to match: Use bullets/headings for higher effort; keep dense for lower.
   - For tool use: Scale research depth (e.g., brief = 1-2 searches; detailed = multiple tools + synthesis).

4. **Tone & Quality Controls** (always maintain):
   - Stay helpful, truthful, and clear regardless of length.
   - Prioritize accuracy and usefulness over filler.
   - End with offer for more details if appropriate (especially in brief modes).

## Examples

**User**: "Briefly explain quantum computing."
→ Response: Short definition + 1-2 key principles.

**User**: "Give a detailed comparison of React vs Vue."
→ Response: Sections on pros/cons, performance, ecosystem, learning curve, code examples.

**User**: "Quick answer — what's the weather like?"
→ Ultra-brief: Direct answer only.

This skill ensures consistent, user-aligned response calibration across sessions. Combine with other skills as needed.