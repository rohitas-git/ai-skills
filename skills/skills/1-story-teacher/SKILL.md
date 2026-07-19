---
name: 1-story-teacher
description: Use to turn any summary, lesson, educational text, article, book notes, video transcript, URL content, or raw document into an original, engaging short novel or story that teaches the core ideas invisibly through narrative, character decisions, plot consequences, and high-stakes situations — never as direct instruction or tutorial. Triggered by requests like turn this into a novel, teach this through a story, make a fiction version of this lesson, create an adventure that explains, or story that makes this memorable.
disable-model-invocation: true
---

# Story Teacher

## Overview

This skill transforms dry, complex, or abstract educational content into memorable, emotionally engaging short novels or stories. The concepts are not explained — they are *experienced* by characters who succeed or fail based on whether they apply (or violate) the underlying principles. The result feels like pure fiction (thriller, fantasy, heist, adventure, sci-fi, mystery) while faithfully preserving the source material's 80/20 essence.

## Core Principles for Every Story

- **Invisible Teaching**: Never name the concepts, quote the source, or break the fourth wall with explanations. The reader discovers the power of the ideas only through story outcomes.
- **High Stakes + Emotional Payoff**: Every major concept must have a dramatic "trial" moment where violating it causes visible, painful failure and applying it creates a turning point or victory.
- **Fidelity with Creativity**: Stay true to the source concepts without distortion, but freely invent characters, world, plot, and metaphors that make the ideas feel native to the fiction.
- **80/20 Focus**: Identify the few ideas that deliver most of the value. Structure the story so these become the emotional and plot backbone.
- **Engaging Prose First**: Prioritize readability, tension, character voice, twists, and pacing over "educational completeness." A gripping story that teaches 70% well beats a complete but boring one.
- **User Collaboration**: For anything longer than a short story, propose the premise and chapter outline first. Write chapter-by-chapter on confirmation. This keeps responses manageable and allows iteration.
- **Optional Mapping**: Only provide a "What Each Chapter Taught" appendix if the user explicitly asks after reading. The novel itself must stand alone as pure fiction.

## Workflow (Follow This Order)

1. **Understand the Input**
   - If the input is long, raw text, a URL, or video, first recommend or internally use the `1-resource-summarizer` skill to create a clean 80/20 + Feynman distillation.
   - Extract the 5–10 core concepts/principles that matter most. Ignore filler, examples that don't generalize, and low-impact details.
   - Ask clarifying questions if needed: preferred genre(s), tone (gritty/dark, hopeful, humorous, epic), target length (short story vs 6–12 chapter novella), audience (general, technical, young adult), any elements to include or avoid.

2. **Design the Story Premise**
   - Invent a fictional world and situation where the core concepts are *necessary survival or success tools*.
   - Good patterns that work well:
     - Heist / infiltration where bad architecture = system collapse or capture.
     - Fantasy where magic systems literally follow the principles (spells as functions, grimoires as modules, ancient runes as legacy code).
     - Sci-fi or cyberpunk where characters are "refactoring" a failing AI, city infrastructure, or spaceship.
     - Thriller / mystery where misunderstanding a principle leads to disaster and understanding it solves the case.
     - Adventure where the hero must "draw boundaries," "invert dependencies," or "make the system scream its purpose" to win.
   - The protagonist(s) should start with flawed or missing understanding and grow through painful experience.

3. **Map Concepts to Dramatic Moments (Invisible Integration)**
   - For each major concept, create at least one scene where:
     - Violating it causes immediate, visible, costly failure (chase goes wrong, ally dies, plan collapses, betrayal succeeds).
     - Applying it creates a clever reversal, narrow escape, or emotional win.
   - Weave multiple concepts together naturally instead of one-per-chapter in a rigid way.
   - Use character dialogue and internal thought during action to surface the idea without naming it ("We can't have one person doing the job of three teams — that's why the eastern sector just went dark!").

4. **Structure & Output**
   - Default to a short novel of 6–12 chapters (roughly 1,200–2,000 words per chapter).
   - Chapter titles should be atmospheric and story-driven only (e.g., "The Tangled Web", "One Job Too Many", "Arrows Pointing the Wrong Way").
   - Write in vivid, novelistic prose with strong character voice, sensory detail, tension, and emotional stakes.
   - End with a satisfying resolution that shows the transformed world/characters because the principles were applied.
   - After the story (only if requested): Provide a clean, spoiler-aware mapping of which concepts each chapter embodied.

5. **Quality Checks Before Delivering**
   - Does the story feel like fiction first and teaching second?
   - Would a reader who knows nothing about the source topic still enjoy it as entertainment?
   - Are the concepts accurately represented through consequences rather than exposition?
   - Is the prose engaging and professional (no tutorial tone, no lists, no "remember that..." asides)?

## Handling Different Inputs

- **Already-distilled summary** (like the clean-books-summary.md): Excellent starting point. Move quickly to premise design.
- **Raw long text or book**: Route through `1-resource-summarizer` first.
- **URL or article**: Use `browse_page` tool with instructions focused on extracting core lessons.
- **Video**: Note that a transcript is usually required first; offer to summarize key points if transcript is provided.
- **Single concept or short lesson**: Can become a tight short story or novella instead of full novel.

## Tone & Genre Guidance

Default to high-engagement genres unless user specifies: cyberpunk thriller/heist, epic fantasy (magic-as-system), sci-fi adventure, mystery, or near-future dystopian. Mix tension with hope and clever problem-solving. Use dark humor sparingly and only when it fits character voice.

Always offer 2–3 genre/premise options and let the user choose or refine before writing the full story.

## Limitations & Honesty

- This skill creates *original fiction inspired by* the source material. It does not reproduce copyrighted text, characters, or plots from existing works.
- Very technical or highly mathematical topics may need stronger metaphors; be transparent if a pure story format would lose critical precision.
- Extremely long or dense source material is best handled chapter-by-chapter with user feedback between sections.

## References

- Detailed workflow, examples of strong premise design, and chapter mapping templates: `references/workflow-and-examples.md`
- Example of excellent input distillation: `references/clean-books-summary.md` (the Clean Code + Clean Architecture distillation used to create the original "Clean Break" novel concept)

Use this skill whenever someone wants dry knowledge turned into something they will actually remember and enjoy reading. The goal is transformation, not just translation.

## Related

- **Parent hub:** `/0-learn` (leaf)
- **Before long raw input:** `/1-resource-summarizer` (80/20 distill)
- **Direct explain instead:** `/1-learning-explainer`
- **Multi-session course:** `/1-teach`