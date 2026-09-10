# CMPSC 480 Final Validation Report

**Validation date:** 2026-07-27  
**Controlling specification:** `goal.md`  
**Overall result:** PASS

## Acceptance Summary

| Acceptance area | Result | Evidence |
|---|:---:|---|
| Fifteen weekly units | PASS | Weeks 01-15 exist and each has lecture and assignment material |
| Indexed lessons plus Week 15 | PASS | 27 lecture packages |
| Lecture formats | PASS | 27 PPTX, 27 PDF, and 27 Markdown scripts |
| Weekly assignments | PASS | 15 separate question and solution `.tex/.pdf` pairs |
| Quizzes | PASS | 5 separate question and solution `.tex/.pdf` pairs |
| Midterm | PASS | Separate question and solution `.tex/.pdf` files |
| Comprehensive final | PASS | Separate question and solution `.tex/.pdf` files |
| English-only deliverables | PASS | Zero CJK characters in generated text and PPTX XML |
| Script-only video requirement | PASS | Zero generated video or audio files |
| Student/instructor separation | PASS | Zero instructor answer markers in 22 student sources |
| Compilation and export | PASS | 44 assessment PDFs and 27 lecture PDFs are valid |
| Point and numbering alignment | PASS | 22 paired assessments match at task and subtask level |
| Placeholder exclusion | PASS | Zero unfinished placeholder markers |
| Visual quality | PASS | All rendered lecture and assessment pages inspected |

## Artifact Counts

| Artifact class | Required | Actual | Result |
|---|---:|---:|:---:|
| Lecture PowerPoint files | 27 | 27 | PASS |
| Lecture PDF exports | 27 | 27 | PASS |
| Video-script documents | 27 | 27 | PASS |
| Assignment question LaTeX sources | 15 | 15 | PASS |
| Assignment question PDFs | 15 | 15 | PASS |
| Assignment solution LaTeX sources | 15 | 15 | PASS |
| Assignment solution PDFs | 15 | 15 | PASS |
| Quiz question LaTeX sources | 5 | 5 | PASS |
| Quiz question PDFs | 5 | 5 | PASS |
| Quiz solution LaTeX sources | 5 | 5 | PASS |
| Quiz solution PDFs | 5 | 5 | PASS |
| Exam question LaTeX sources | 2 | 2 | PASS |
| Exam question PDFs | 2 | 2 | PASS |
| Exam solution LaTeX sources | 2 | 2 | PASS |
| Exam solution PDFs | 2 | 2 | PASS |
| Generated video or audio files | 0 | 0 | PASS |

## Lecture Integrity

- All 27 PowerPoint files open with `python-pptx`.
- All 27 PowerPoint ZIP archives pass integrity checks.
- Every deck uses 16:9 slide geometry.
- Every deck has a matching PDF with the same page count.
- Every deck has a matching numbered script with the same slide count.
- Script slide numbering is contiguous from Slide 1 through the final slide.
- Every scripted slide contains a suggested pacing line and a visual cue.
- Every PowerPoint slide contains a `[Sources]` speaker-notes block.
- The 27 decks contain 491 slides in total.
- Each deck contains 18-22 slides.
- The 27 scripts contain 79,117 words in total and 2,784-3,640 words each.
- The presentation overflow tester reported
  `Test passed. No overflow detected.` for 27 of 27 decks.

## Assessment Integrity

- The assessment set contains 22 question/solution pairs:
  - 15 weekly assignments
  - 5 quizzes
  - 1 midterm
  - 1 comprehensive final
- The set contains 44 independently compilable LaTeX sources and 44 PDFs.
- A complete `latexmk` pass reported:
  `Built 44 LaTeX document(s) successfully.`
- Student-facing PDFs contain 298 pages.
- Instructor-facing PDFs contain 409 pages.
- Detailed parsing matched 251 scored task or subtask identifiers.
- Every pair has identical declared totals, item IDs, detailed point
  allocations, and PDF/source page counts.
- Every instructor source contains matched answer material.
- Student sources contain no `\answerlabel`, `\gradinglabel`, instructor
  warning, solution frame, or reflection exemplar.
- The Week 1 companion reference implementation passed all 8 `unittest`
  contract tests.
- LaTeX log scanning found zero errors, unresolved-reference warnings,
  overfull boxes, or underfull boxes.
- Every referenced LaTeX asset exists.

## Visual Inspection

The AI agent rendered PDFs to page images and assembled contact sheets for
complete-set inspection.

- All 491 lecture slides were inspected for clipping, overlap, unreadable text,
  inconsistent margins, and broken diagrams.
- All 707 assessment pages were inspected for title wrapping, content overflow,
  equation clipping, table legibility, and student/instructor separation.
- Suspected edge crops caused by the contact-sheet canvas were rechecked at
  individual-page resolution.
- The revised Week 1 Task 4 question and solution pages were re-rendered and
  inspected after point reconciliation.
- No unresolved visual defect remained.

## Revisions Closed During QA

1. Beamer frame-title spacing was made content-driven to accommodate two-line
   titles without clipping.
2. Week 1's four numbered assignment tasks were reconciled to the declared
   10-point total, and matching metadata was added to both sources.
3. The Week 1 supporting reference-solution readme was renamed to satisfy
   generated filename rules.
4. All affected documents were rebuilt and revalidated.

## Automated Validator

Command:

```powershell
python .\deliverables\build_tools\validate_deliverables.py
```

Final automated result:

```text
RESULT=PASS CHECKS=40/40
```

The complete machine-readable result, including per-deck and per-assessment
metrics, is stored in `final_validation.json`.

## Final Decision

All acceptance criteria in `goal.md` are satisfied. The package is complete,
fully English, separated correctly, buildable, visually checked, and ready for
instructor use.
