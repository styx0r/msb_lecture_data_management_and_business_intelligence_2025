#!/usr/bin/env python3
"""
Convert mock_exam.md to a two-column PDF.

Usage:
  python3 mock_exam_to_pdf.py
  python3 mock_exam_to_pdf.py --interactive
  python3 mock_exam_to_pdf.py --input mock_exam.md --output mock_exam.pdf

If dependencies are missing, install with:
  python3 -m pip install markdown weasyprint
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _require_dependencies():
    try:
        from markdown import markdown  # noqa: F401
        from weasyprint import HTML  # noqa: F401
    except Exception:
        print(
            "Missing dependencies. Install with:\n"
            "  python3 -m pip install markdown weasyprint",
            file=sys.stderr,
        )
        sys.exit(1)


def _split_answer_key(text: str) -> tuple[str, str]:
    marker = "Answer Key"
    if marker in text:
        before, after = text.split(marker, 1)
        return before.strip(), (marker + after).strip()
    return text.strip(), ""


def _build_html(questions_md: str, answer_md: str, base_url: str) -> str:
    from markdown import markdown

    questions_html = markdown(questions_md, extensions=["extra"])
    answer_html = markdown(answer_md, extensions=["extra"]) if answer_md else ""

    return f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <style>
      @page {{
        size: A4;
        margin: 12mm;
      }}
      body {{
        font-family: "Helvetica", "Arial", sans-serif;
        font-size: 10.5pt;
        line-height: 1.25;
        color: #111;
      }}
      h1, h2 {{
        margin: 0 0 6pt 0;
      }}
      h1, h2 {{
        column-span: all;
      }}
      .questions {{
        column-count: 2;
        column-gap: 18px;
      }}
      ol, ul {{
        margin: 0 0 6pt 18pt;
        padding: 0;
      }}
      li {{
        margin: 0 0 4pt 0;
        break-inside: avoid;
        page-break-inside: avoid;
      }}
      .answer-key {{
        margin-top: 12pt;
        column-count: 1;
      }}
    </style>
  </head>
  <body>
    <div class="questions">
      {questions_html}
    </div>
    {"<div class=\"answer-key\">" + answer_html + "</div>" if answer_html else ""}
  </body>
</html>
"""


def _prompt_with_default(label: str, default_value: str) -> str:
    prompt = f"{label} [{default_value}]: "
    value = input(prompt).strip()
    return value or default_value


def main() -> int:
    _require_dependencies()

    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Convert mock exam markdown to two-column PDF."
    )
    parser.add_argument(
        "--input",
        default=str(script_dir / "mock_exam.md"),
        help="Path to input markdown file.",
    )
    parser.add_argument(
        "--output",
        default=str(script_dir / "mock_exam.pdf"),
        help="Path to output PDF file.",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Prompt for input/output paths.",
    )
    args = parser.parse_args()

    run_interactive = args.interactive or len(sys.argv) == 1
    if run_interactive:
        print("Mock exam PDF generator (two-column layout)")
        input_value = _prompt_with_default("Input markdown", args.input)
        output_value = _prompt_with_default("Output PDF", args.output)
    else:
        input_value = args.input
        output_value = args.output

    input_path = Path(input_value).expanduser().resolve()
    output_path = Path(output_value).expanduser().resolve()

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    text = input_path.read_text(encoding="utf-8")
    questions_md, answer_md = _split_answer_key(text)
    html = _build_html(questions_md, answer_md, base_url=str(input_path.parent))

    from weasyprint import HTML

    HTML(string=html, base_url=str(input_path.parent)).write_pdf(str(output_path))
    print(f"PDF created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
