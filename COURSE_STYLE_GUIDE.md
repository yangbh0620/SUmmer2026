# CMPSC 480 Course Style Guide

## Communication Job

By the end of each unit, upper-division computer-science students should be able to explain the governing AI concept, derive or trace the core algorithm, implement it defensively, and evaluate when it is an appropriate engineering choice.

## Voice

- Rigorous, direct, and professionally technical
- Written for capable near-graduates rather than novices
- Precise about assumptions, invariants, failure modes, and complexity
- Focused on reasoning and engineering decisions rather than memorized vocabulary

## Narrative Pattern

Lecture decks normally follow this learning progression:

1. Motivate the engineering problem.
2. State the formal model and assumptions.
3. Develop the algorithm or reasoning method.
4. Trace a concrete worked example.
5. Identify correctness, complexity, and edge cases.
6. Compare alternatives and clarify scope.
7. Check understanding.
8. Synthesize the lesson into actionable takeaways.

## Visual System

- Canvas: white
- Primary text: black
- Structural panels: pale gray
- Rules: medium gray
- Primary accent: light blue
- Strong accent: blue
- Slide size: 16:9, 1280 × 720
- Typeface: Helvetica Neue where available, with Arial as fallback
- Deck title: at least 50 pt
- Slide title: at least 35 pt
- Subheading: at least 24 pt
- Body: at least 16 pt

The system follows the Codex Grid layout language: strong typographic hierarchy, generous margins, flat compositions, restrained panels, and minimal decoration. Adjacent slides should vary their silhouette while preserving the same visual grammar.

## Slide-Writing Rules

- One primary claim or teaching job per slide
- Takeaway-style titles rather than topic labels when possible
- No production notes or agent instructions in audience-facing copy
- No dense walls of text
- No title or banner wrapping caused by avoidable wording
- Mathematical notation must remain consistent across the semester
- Code examples must be short enough to read from the back of a classroom
- Every lecture ends with synthesis and applied questions

## Source Notes

Every lecture slide must contain a speaker-notes source block. Sources may include:

- The corresponding repository prompt
- Standard course references
- Primary research papers or official standards

The required notes format is:

```text
[Sources]
- Source description
[/Sources]
```

## Assessment Rules

- Question and solution files are separate.
- Question numbering and points match exactly.
- Questions test application, derivation, tracing, debugging, or design judgment.
- Solutions show reasoning, not only final answers.
- Programming solutions address validation, edge cases, complexity, and testing.
- No solution material appears in student-facing files.

## Language and Accessibility

- All generated content, filenames, comments, labels, and metadata are in English.
- Slides use accessible contrast and readable font sizes.
- Visuals are explained in the matching script.
- Color is not the only carrier of meaning.
- Acronyms are expanded on first use.

