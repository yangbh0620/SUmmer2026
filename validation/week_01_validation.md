# Week 1 Validation Report

**Validation date:** 2026-07-27  
**Scope:** two lecture packages and one separated assignment package

## Lecture 1.1

| Check | Result |
|---|---|
| PowerPoint file | Present and readable |
| PDF export | 19 pages |
| Video script | Present; synchronized to 19 slides |
| Narration | 2,693 words |
| Speaker-note source blocks | 19 |
| Automated overflow test | Passed |
| Visual inspection | All slides and PDF pages inspected; no clipping or overlap |
| Language and placeholder scan | 0 CJK characters; 0 forbidden placeholders |

## Lecture 1.2

| Check | Result |
|---|---|
| PowerPoint file | Present and readable |
| PDF export | 22 pages |
| Video script | Present; synchronized to 22 slides |
| Narration | 3,057 words |
| Speaker-note source blocks | 22 |
| Automated overflow test | Passed |
| Visual inspection | All slides and PDF pages inspected; no clipping or overlap |
| Language and placeholder scan | 0 CJK characters; 0 forbidden placeholders |

## Week 1 Assignment

| Check | Questions | Solutions |
|---|---:|---:|
| LaTeX source | Present | Present |
| Compiled PDF | 19 pages | 27 pages |
| LaTeX errors | 0 | 0 |
| Overfull boxes | 0 | 0 |
| Underfull boxes | 0 | 0 |
| Visual inspection | All pages passed | All pages passed |
| CJK characters | 0 | 0 |
| Forbidden placeholders | 0 | 0 |

## Separation and Alignment

- The student-facing deck contains no `Answer.`, `Instructor material`,
  `Complete Solutions`, or `Grading guidance.` markers.
- The question and solution decks both state a 10-point total.
- The question deck contains Tasks 1-4.
- The solution deck contains matching Solutions 1-4.
- The instructor deck contains complete code, expected behavior, edge-case
  reasoning, grading guidance, and a rubric.

## Executable Reference Solution

The companion source under `assignment/reference_solution/` was copied into a
clean temporary Git repository with one commit.

Observed environment-check output:

```text
PYTHON=3.11.0
NUMPY=2.4.6
JUPYTER=4.6.2
GIT_COMMITS=1
```

Observed test result:

```text
Ran 8 tests
OK
```

The implementation intentionally contains no search algorithm; it establishes
the validated agent and problem abstractions that Week 2 will extend.

## Media Check

No video or audio file was generated. The required video component is delivered
only as Markdown narration scripts.
