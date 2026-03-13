#!/usr/bin/env python3
"""
Convert exam.md to a Word-friendly two-column HTML file.

Usage:
  python3 exam_to_word_html.py
  python3 exam_to_word_html.py --input exam.md --output exam_word.html
"""

from __future__ import annotations

import argparse
from pathlib import Path


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _is_question_line(line: str) -> bool:
    line = line.strip()
    return line[:1].isdigit() and ". " in line


def _is_option_line(line: str) -> bool:
    stripped = line.strip()
    return len(stripped) > 2 and stripped[1:3] == ". " and stripped[0] in "ABCD"


def convert_markdown_to_html(md_text: str) -> str:
    lines = md_text.splitlines()
    html_lines: list[str] = []
    in_code = False
    in_question = False

    for line in lines:
        if line.strip() == "Answer Key":
            break

        if line.startswith("```"):
            if not in_code:
                html_lines.append('<pre class="code">')
                in_code = True
            else:
                html_lines.append("</pre>")
                in_code = False
            continue

        if in_code:
            html_lines.append(_escape(line))
            continue

        if line.startswith("# "):
            html_lines.append(f"<h1>{_escape(line[2:].strip())}</h1>")
            continue

        if line.startswith("## "):
            if in_question:
                html_lines.append("</div>")
                in_question = False
            html_lines.append(f"<h2>{_escape(line[3:].strip())}</h2>")
            continue

        if _is_question_line(line):
            if in_question:
                html_lines.append("</div>")
            in_question = True
            html_lines.append(f'<div class="q"><div class="qtext">{_escape(line.strip())}</div>')
            continue

        if _is_option_line(line):
            html_lines.append(f'<div class="opt">{_escape(line.strip())}</div>')
            continue

        if line.strip() == "":
            continue

        html_lines.append(f'<div class="qtext">{_escape(line.strip())}</div>')

    if in_question:
        html_lines.append("</div>")

    body = "\n".join(html_lines)
    return f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <style>
      body {{
        font-family: Arial, Helvetica, sans-serif;
        font-size: 11pt;
        line-height: 1.3;
        color: #111;
      }}
      .columns {{
        column-count: 2;
        column-gap: 22px;
      }}
      h1, h2 {{
        column-span: all;
        margin: 0 0 8pt 0;
      }}
      h2 {{
        margin-top: 10pt;
      }}
      .q {{
        break-inside: avoid;
        margin-bottom: 6pt;
      }}
      .qtext {{
        margin-bottom: 2pt;
      }}
      .opt {{
        margin-left: 14pt;
      }}
      .code {{
        font-family: Menlo, Consolas, monospace;
        font-size: 9.5pt;
        background: #f5f5f5;
        padding: 6pt;
        border-radius: 4pt;
        white-space: pre-wrap;
      }}
    </style>
  </head>
  <body>
    <div class="columns">
{body}
    </div>
  </body>
</html>
"""


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Convert exam.md to Word HTML.")
    parser.add_argument("--input", default=str(script_dir / "exam.md"))
    parser.add_argument("--output", default=str(script_dir / "exam_word.html"))
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    md_text = input_path.read_text(encoding="utf-8")
    html = convert_markdown_to_html(md_text)
    output_path.write_text(html, encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
