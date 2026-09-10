"""Generate separated CMPSC 480 Beamer question and solution decks."""

from __future__ import annotations

import argparse
import importlib.util
import re
from pathlib import Path
from typing import Any


FORBIDDEN = re.compile(r"\b(?:TODO|TBD|Lorem ipsum)\b", re.IGNORECASE)
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")


def tex_escape(value: str) -> str:
    """Escape plain text for LaTeX while preserving ASCII-only source."""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def text(item: dict[str, Any], plain_key: str, tex_key: str) -> str:
    """Return trusted TeX when supplied, otherwise escape plain text."""
    if tex_key in item:
        return str(item[tex_key])
    return tex_escape(str(item[plain_key]))


def frame(title: str, body: str, *, fragile: bool = False) -> str:
    option = "[fragile]" if fragile else ""
    return f"\\begin{{frame}}{option}{{{title}}}\n{body.rstrip()}\n\\end{{frame}}\n"


def itemize(items: list[str], *, small: bool = False) -> str:
    prefix = "\\small\n" if small else ""
    lines = "\n".join(f"  \\item {item}" for item in items)
    return f"{prefix}\\begin{{itemize}}\n{lines}\n\\end{{itemize}}"


def header(spec: dict[str, Any], document_type: str, short_title: str) -> str:
    ids = ",".join(str(problem["id"]) for problem in spec["problems"])
    style_path = spec.get("style_path", "../../../shared/cmpsc480_beamer.tex")
    return (
        "\\documentclass[aspectratio=169,11pt]{beamer}\n"
        f"\\input{{{style_path}}}\n\n"
        f"% CMPSC480_TOTAL_POINTS: {spec['total_points']}\n"
        f"% CMPSC480_ITEM_IDS: {ids}\n"
        f"\\title[{tex_escape(short_title)}]{{{tex_escape(spec['title'])}}}\n"
        f"\\subtitle{{{tex_escape(spec['subtitle'])}}}\n"
        f"\\author{{CMPSC 480 - {tex_escape(document_type)}}}\n"
        "\\date{}\n\n"
        "\\begin{document}\n\n"
    )


def title_frame(spec: dict[str, Any], solution: bool) -> str:
    warning = ""
    if solution:
        warning = (
            "\\vspace{-0.35cm}\n"
            "\\begin{center}\n"
            "\\color{coursered}\\bfseries Instructor material - "
            "do not distribute with the question deck\n"
            "\\end{center}\n"
        )
    return "\\begin{frame}\n  \\titlepage\n" + warning + "\\end{frame}\n"


def overview_frame(spec: dict[str, Any], solution: bool) -> str:
    label = "Solution overview" if solution else "Assessment overview"
    audience = (
        "This instructor deck provides a complete matched solution and grading guidance."
        if solution
        else spec["overview"]
    )
    body = (
        "\\begin{columns}[T,onlytextwidth]\n"
        "\\begin{column}{0.62\\textwidth}\n"
        f"\\Large {tex_escape(audience)}\n\n"
        "\\vspace{0.35cm}\n\\normalsize\n"
        f"Coverage: {tex_escape(spec['coverage'])}\n"
        "\\end{column}\n"
        "\\begin{column}{0.33\\textwidth}\n"
        f"\\begin{{block}}{{Points}}{spec['total_points']} total\\end{{block}}\n"
        f"\\begin{{block}}{{Expected time}}{tex_escape(spec['duration'])}\\end{{block}}\n"
        f"\\begin{{block}}{{Submission}}{tex_escape(spec['submission'])}\\end{{block}}\n"
        "\\end{column}\n"
        "\\end{columns}"
    )
    return frame(label, body)


def objectives_frame(spec: dict[str, Any]) -> str:
    return frame(
        "Learning objectives",
        itemize([tex_escape(value) for value in spec["objectives"]]),
    )


def requirements_frame(spec: dict[str, Any], solution: bool) -> str:
    title = "Instructor verification checklist" if solution else "Requirements checklist"
    return frame(
        title,
        itemize([tex_escape(value) for value in spec["requirements"]], small=True),
    )


def question_problem_frames(problem: dict[str, Any]) -> list[str]:
    chunks = [problem["parts"][i : i + 3] for i in range(0, len(problem["parts"]), 3)]
    output: list[str] = []
    for index, parts in enumerate(chunks):
        suffix = "" if len(chunks) == 1 else f" - part {index + 1}"
        title = (
            f"Task {problem['id']} - {tex_escape(problem['title'])}{suffix} "
            f"({problem['points']} points)"
        )
        prompt = text(problem, "prompt", "prompt_tex")
        entries = []
        for part in parts:
            part_text = text(part, "question", "question_tex")
            entries.append(
                f"\\item[\\textbf{{{tex_escape(part['label'])}.}}] "
                f"{part_text} \\hfill{{\\color{{courseblue}}"
                f"\\textbf{{[{part['points']} points]}}}}"
            )
        body = (
            "\\small\n"
            f"{prompt}\n\n"
            "\\vspace{0.2cm}\n"
            "\\begin{enumerate}\n"
            + "\n".join(entries)
            + "\n\\end{enumerate}"
        )
        output.append(frame(title, body))
    if problem.get("starter_code"):
        body = (
            "\\begin{lstlisting}\n"
            + problem["starter_code"].rstrip()
            + "\n\\end{lstlisting}\n"
            "\\keyidea{Complete only the specified behavior. Preserve the public interface.}"
        )
        output.append(
            frame(
                f"Task {problem['id']} - starter interface",
                body,
                fragile=True,
            )
        )
    return output


def solution_problem_frames(problem: dict[str, Any]) -> list[str]:
    output: list[str] = []
    for part in problem["parts"]:
        title = (
            f"Solution {problem['id']}.{tex_escape(part['label'])} - "
            f"{tex_escape(problem['title'])} ({part['points']} points)"
        )
        focus = text(part, "question", "question_tex")
        answer = text(part, "answer", "answer_tex")
        body = (
            "\\small\n"
            f"\\textbf{{Question focus.}} {focus}\n\n"
            "\\vspace{0.25cm}\n"
            f"\\answerlabel {answer}"
        )
        output.append(frame(title, body))
    if problem.get("solution_code"):
        body = (
            "\\begin{lstlisting}\n"
            + problem["solution_code"].rstrip()
            + "\n\\end{lstlisting}\n"
            "\\gradinglabel Equivalent implementations earn full credit when "
            "they preserve the same observable contract."
        )
        output.append(
            frame(
                f"Solution {problem['id']} - reference pseudocode",
                body,
                fragile=True,
            )
        )
    return output


def edge_frame(spec: dict[str, Any], solution: bool) -> str:
    title = "Edge-case reasoning and expected behavior" if solution else "Edge cases and defensive programming"
    values = spec["edge_solutions"] if solution else spec["edge_cases"]
    return frame(title, itemize([tex_escape(value) for value in values], small=True))


def rubric_frames(spec: dict[str, Any], solution: bool) -> list[str]:
    rows = []
    for problem in spec["problems"]:
        evidence = problem["grading"] if solution else problem["deliverable"]
        rows.append(
            f"{tex_escape(problem['title'])} & {problem['points']} & "
            f"{tex_escape(evidence)} \\\\"
        )
    midpoint = (len(rows) + 1) // 2
    chunks = [rows[:midpoint], rows[midpoint:]] if len(rows) > 4 else [rows]
    frames: list[str] = []
    for index, chunk in enumerate(chunks):
        suffix = "" if len(chunks) == 1 else f" - part {index + 1}"
        body = (
            "\\scriptsize\n"
            "\\begin{tabularx}{\\textwidth}{>{\\bfseries}p{0.28\\textwidth} "
            "p{0.08\\textwidth} X}\n"
            "\\toprule\nCategory & Points & "
            + ("Full-credit evidence" if solution else "Required evidence")
            + " \\\\\n\\midrule\n"
            + "\n".join(chunk)
            + "\n\\bottomrule\n\\end{tabularx}"
        )
        frames.append(frame(f"Grading rubric{suffix}", body))
    return frames


def submission_frame(spec: dict[str, Any]) -> str:
    return frame(
        "Submission instructions",
        itemize([tex_escape(value) for value in spec["submission_steps"]], small=True)
        + "\n\\vspace{0.2cm}\n"
        + "\\alert{Do not submit credentials, generated caches, or unapproved libraries.}",
    )


def reflection_frame(spec: dict[str, Any], solution: bool) -> str:
    if solution:
        body = (
            "\\answerlabel "
            + text(spec, "reflection_answer", "reflection_answer_tex")
            + "\n\n\\vspace{0.25cm}\n"
            "\\gradinglabel Award credit for a specific claim supported by "
            "technical evidence from the submitted work."
        )
        return frame("Reflection exemplar", "\\small\n" + body)
    body = (
        f"In {tex_escape(spec['reflection_length'])}:\n\n"
        + text(spec, "reflection", "reflection_tex")
    )
    return frame("Reflection prompt", body)


def build_questions(spec: dict[str, Any]) -> str:
    short = spec["short_title"] + " Questions"
    chunks = [
        header(spec, "Student Question Deck", short),
        title_frame(spec, False),
        overview_frame(spec, False),
        objectives_frame(spec),
        requirements_frame(spec, False),
    ]
    for problem in spec["problems"]:
        chunks.extend(question_problem_frames(problem))
    chunks.extend(
        [
            edge_frame(spec, False),
            submission_frame(spec),
            *rubric_frames(spec, False),
            reflection_frame(spec, False),
            "\\end{document}\n",
        ]
    )
    return "\n".join(chunks)


def build_solutions(spec: dict[str, Any]) -> str:
    short = spec["short_title"] + " Solutions"
    chunks = [
        header(spec, "Instructor Solution Deck", short),
        title_frame(spec, True),
        overview_frame(spec, True),
        requirements_frame(spec, True),
    ]
    for problem in spec["problems"]:
        chunks.extend(solution_problem_frames(problem))
    chunks.extend(
        [
            edge_frame(spec, True),
            *rubric_frames(spec, True),
            reflection_frame(spec, True),
            "\\end{document}\n",
        ]
    )
    return "\n".join(chunks)


def load_specs(path: Path) -> dict[str, dict[str, Any]]:
    module_spec = importlib.util.spec_from_file_location("assessment_specs", path)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError(f"Unable to import spec file: {path}")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module.SPECS


def validate_spec(spec: dict[str, Any]) -> None:
    points = sum(problem["points"] for problem in spec["problems"])
    if points != spec["total_points"]:
        raise ValueError(f"Task point sum {points} does not match total {spec['total_points']}")
    for problem in spec["problems"]:
        part_sum = sum(part["points"] for part in problem["parts"])
        if part_sum != problem["points"]:
            raise ValueError(
                f"Part point sum {part_sum} does not match Task {problem['id']} "
                f"total {problem['points']}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec-file", type=Path, required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--stem", required=True)
    args = parser.parse_args()

    specs = load_specs(args.spec_file.resolve())
    spec = specs[args.key]
    validate_spec(spec)
    questions = build_questions(spec)
    solutions = build_solutions(spec)

    combined = questions + "\n" + solutions
    if CJK.search(combined):
        raise ValueError("Generated LaTeX contains CJK characters")
    if FORBIDDEN.search(combined):
        raise ValueError("Generated LaTeX contains a forbidden placeholder")
    if "\\answerlabel" in questions or "\\gradinglabel" in questions:
        raise ValueError("Question deck contains instructor-only solution markers")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    question_path = args.output_dir / f"{args.stem}_questions.tex"
    solution_path = args.output_dir / f"{args.stem}_solutions.tex"
    question_path.write_text(questions, encoding="utf-8", newline="\n")
    solution_path.write_text(solutions, encoding="utf-8", newline="\n")
    print(question_path)
    print(solution_path)


if __name__ == "__main__":
    main()
