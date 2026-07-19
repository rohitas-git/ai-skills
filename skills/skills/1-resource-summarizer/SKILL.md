---
name: 1-resource-summarizer
description: >
  Distills long resources (PDF, video/transcript, article, image) into learning-focused
  notes using 80/20, Feynman, Cornell, and progressive summarization. Use for summarize,
  extract insights, study notes from a source. Soft under /0-learn; also vault-ingest distill.
  Not multi-level teach-from-scratch (/1-learning-explainer) or multi-session course (/1-teach).
disable-model-invocation: true
---

# Resource Summarizer Skill
## Boundary

| Need | Skill |
|------|--------|
| Distill long PDF/video/article for learning notes | **resource-summarizer** (this) |
| Multi-level teach-from-scratch | `/1-learning-explainer` |
| Vault compile after distill | `/1-vault-ingest` (loads this for long sources) |
| Explain vault Concept | `/1-vault-explain` |
| Code walkthrough | `/1-code-explainer` |


## Overview

This skill extracts and summarizes core information from resources (text, PDFs, videos/transcripts, images) for learning and note-taking. It applies 80/20 rule (Pareto), Feynman Technique, Cornell method, progressive summarization, mind mapping elements, and other evidence-based strategies to deliver high-value, retention-focused outputs.

## Triggers & Use Cases
- Summarize PDF, video, article, image, transcript, book chapter for learning.
- Create effective notes, key insights, action items, or study aids.
- Deep understanding, gap identification, or condensation of long resources.

## Core Principles (Evidence-Based)
- **80/20 Rule**: Focus on the 20% of content delivering 80% of value (key arguments, conclusions, data, examples).
- **Feynman Technique**: Explain concepts simply as if teaching a beginner/child; identify gaps; simplify with analogies; revisit source for accuracy.
- **Active Processing**: Paraphrase in own words, avoid passive copying. Use retrieval (recall from memory where possible).
- **Progressive Summarization**: Layered distillation — high-level → detailed → refined notes.
- **Structured Formats**: Cornell (cues/questions + notes + summary), mind maps for connections, bullets/tables for clarity.
- **Retention Focus**: Prioritize understanding over completeness; include self-test prompts, analogies, visuals descriptions.

## Standardized Summarization Workflow
1. **Scan & Structure**: Identify overall thesis, sections/headings/timestamps, visuals, length/type.
2. **Extract Core (80/20)**: Prioritize intro/conclusion, repeated ideas, data/evidence, bold/key terms, examples. Discard filler.
3. **Apply Techniques**:
   - Feynman: Draft simple explanations for main concepts; flag gaps; refine.
   - Paraphrase everything in plain language.
   - Note connections/relationships (for mind-map style).
4. **Build Output**:
   - **Executive Summary**: 1-3 paragraphs capturing essence.
   - **Key Takeaways**: Prioritized bullets (5-10), with impact/why important.
   - **Feynman Explanations**: Simple teachable versions of core ideas + analogies.
   - **Structured Notes**: Cornell-style (cues/questions for review) or outline/mind-map elements.
   - **Gaps & Questions**: Areas needing more research + self-test prompts.
   - **Visuals/Quotes**: Describe images/charts; key verbatim excerpts.
   - **Action Items/Implications**: Practical applications for learning/retention.
   - **Review Prompts**: Spaced repetition ideas or blank-sheet recall exercise.
5. **Refine**: Keep concise (10-25% original length); objective; suggest iterations for deeper dives.

## Resource-Specific Guidance
### Text/PDFs
- Leverage headings, TOC, abstracts. Use extraction tools if available.
- Focus topic sentences, data tables.

### Videos
- Use transcripts + timestamps for key moments.
- Separate verbal content from visual demonstrations/descriptions.

### Images/Visuals
- Detailed description of composition, text, data, inferred message.
- Extract readable text; note context/purpose.

## Best Practices for Learning/Note-Taking
- Ask user for focus (e.g., exam prep, conceptual understanding, actionables).
- Offer hybrid outputs (e.g., summary + Feynman notes + Cornell template).
- Encourage active recall: End with "Explain this in your own words" prompts.
- For complex topics: Iterative process — first pass summary, then targeted Feynman on weak areas.
- Combine with spaced repetition suggestions for long-term retention.
- Maintain neutrality; flag biases if evident.

## Output Guidelines
- Use markdown: Headings, bullets, tables, code blocks for clarity.
- Make self-contained and actionable.
- Offer expansions: "Want Feynman breakdown on X?" or "Cornell notes version?"

## Related

- **Parent hub (Learn):** `/0-learn` (soft; F-L2 often runs this first on huge sources)
- **After distill:** `/1-learning-explainer` or `/1-story-teacher` or `/0-learn` tutor-mode
- **Vault distill:** `1-vault-ingest` loads this for long sources (Vault domain primary ops)
- **Not for:** multi-session workspace → `/1-teach`
