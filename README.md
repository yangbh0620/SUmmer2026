# CMPSC 480 Course Package

This directory is the completed AI-agent-produced instructional package for
**CMPSC 480 - AI Curriculum Engineering**. It covers a fifteen-week,
upper-division computer-science course and preserves the source prompts outside
`deliverables/`.

## Completion Summary

- 15 weekly units
- 27 editable lecture decks (`.pptx`)
- 27 matching lecture PDF exports
- 27 slide-synchronized video scripts (`.md`)
- 15 weekly assignment question/solution pairs as LaTeX Beamer and PDF
- 5 quiz question/solution pairs as LaTeX Beamer and PDF
- 1 cumulative midterm question/solution pair as LaTeX Beamer and PDF
- 1 comprehensive final question/solution pair as LaTeX Beamer and PDF
- 44 independently compilable LaTeX sources and 44 matching assessment PDFs
- No generated video or audio files

All instructional and instructor-facing content is in English. Student question
decks and instructor solution decks are separate files.

## Intended Audience and Prerequisites

The package targets upper-division computer-science students. It assumes
proficiency in Python, NumPy, object-oriented programming, data structures,
linear algebra, calculus, and probability.

## Directory Map

```text
deliverables/
├── README.md
├── MANIFEST.md
├── COVERAGE_MATRIX.md
├── AI_AGENT_LOG.md
├── COURSE_STYLE_GUIDE.md
├── NOTATION_GUIDE.md
├── ASSESSMENT_BLUEPRINT.md
├── shared/
│   └── cmpsc480_beamer.tex
├── build_tools/
│   ├── build_latex.ps1
│   ├── export_pptx_to_pdf.ps1
│   └── validate_deliverables.py
├── validation/
│   ├── final_validation.json
│   └── final_validation.md
├── units/
│   ├── week_01/
│   │   ├── lectures/
│   │   ├── scripts/
│   │   ├── assignment/
│   │   └── quiz/
│   ├── ...
│   └── week_15/
└── exams/
    ├── midterm/
    └── final/
```

A `quiz/` directory appears only in the week where a quiz is administered.

## Using the Lecture Packages

Each lecture has three matching files:

1. Open the `.pptx` file to edit or present the lecture.
2. Use the `.pdf` file for distribution or a stable classroom rendering.
3. Use the `_video_script.md` file as the narration script. Script headings
   match slide numbers and provide pacing and visual cues.

Every PowerPoint slide contains a `[Sources]` block in speaker notes. The
scripts are documents only; this package intentionally contains no video,
audio, animation, or voice-over output.

## Using the Assessments

- Files ending in `_questions` are student-facing.
- Files ending in `_solutions` are instructor-facing and must not be
  distributed with the question decks.
- Each `.tex` source has a compiled `.pdf` beside it.
- Question and solution sources contain matching machine-readable point and
  item metadata.
- Programming assignments emphasize reproducibility, defensive validation,
  tests, and evidence rather than output alone.

## Building the LaTeX Documents

Requirements:

- PowerShell
- MiKTeX with `latexmk`
- Perl, such as Strawberry Perl

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File `
  .\deliverables\build_tools\build_latex.ps1
```

The build script recursively compiles every assessment `.tex` file while
excluding shared style and build-tool directories.

## Exporting a Lecture PDF

The provided exporter uses the locally installed Microsoft PowerPoint COM
interface:

```powershell
powershell -ExecutionPolicy Bypass -File `
  .\deliverables\build_tools\export_pptx_to_pdf.ps1 `
  -PptxPath .\deliverables\units\week_01\lectures\week_01_lesson_01_ai_engineering_mindset.pptx
```

If `-PdfPath` is omitted, the PDF is written beside the PowerPoint file.

## Running Acceptance Validation

Requirements:

- Python 3.11 or newer
- `pypdf`
- `python-pptx`

Run:

```powershell
python .\deliverables\build_tools\validate_deliverables.py
```

The validator checks required counts, all fifteen weeks, PPTX archive integrity,
16:9 dimensions, source notes, lecture PDF and script synchronization,
assessment pairing, detailed point alignment, student/instructor separation,
PDF validity, English-only compliance, filename rules, placeholders, media
exclusions, LaTeX logs, and referenced assets. Its machine-readable result is
written to `validation/final_validation.json`; the reviewed summary is
`validation/final_validation.md`.

## Course-Level References

- `MANIFEST.md` is the artifact-level completion record.
- `COVERAGE_MATRIX.md` maps topics and learning outcomes to instruction and
  assessment.
- `COURSE_STYLE_GUIDE.md` defines voice and visual rules.
- `NOTATION_GUIDE.md` defines course-wide mathematical conventions.
- `ASSESSMENT_BLUEPRINT.md` defines assessment purpose, coverage, points, and
  exam balance.
- `AI_AGENT_LOG.md` records the observable AI-agent production and validation
  workflow.

## Final Status

The package is complete and validated. The authoritative validation evidence is
recorded in `validation/final_validation.md` and
`validation/final_validation.json`.
