#!/usr/bin/env python3
"""Build a single combined PDF from Steve Koh markdown articles.

Each .md file becomes one chapter with a page break.
Simplified Chinese content stays in SC; Traditional Chinese stays in TC.
"""

import os
import re
import glob
import sys
import markdown
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

MD_DIR = "/home/user/cc-workspace/research/substack-thestevekoh"
OUTPUT_PDF = os.path.join(MD_DIR, "Steve_Koh_文集.pdf")

SC_CHARS = set("这们东为时国会该实从")
TC_CHARS = set("這們東為時國會該實從")

PROMO_MARKERS = [
    "如果你真心想要變強",
    "P.S. 如果你還想用少過",
]


# --- Reused from build_epub.py (clean_markdown + detect_lang) ---

def clean_markdown(text: str) -> str:
    lines = text.split("\n")

    source_line_idx = None
    cleaned_lines = []
    for i, line in enumerate(lines):
        if re.match(r"^\*\*來源：\*\* https?://", line.strip()):
            source_line_idx = len(cleaned_lines)
        else:
            cleaned_lines.append((i, line))

    if source_line_idx is not None:
        remove_idx = None
        blank_count = 0
        i = source_line_idx
        while i < min(source_line_idx + 6, len(cleaned_lines)):
            _, line = cleaned_lines[i]
            stripped = line.strip()
            if stripped == "":
                blank_count += 1
            elif stripped == "---":
                if blank_count <= 3:
                    remove_idx = i
                break
            else:
                break
            i += 1
        if remove_idx is not None:
            cleaned_lines.pop(remove_idx)

    lines = [line for _, line in cleaned_lines]
    text = "\n".join(lines)

    for marker in PROMO_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx].rstrip()
            break

    lines = text.split("\n")
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        bullet_match = re.match(r"^(- .+)$", line)
        if bullet_match:
            if result_lines:
                prev_nonempty = None
                for prev in reversed(result_lines):
                    if prev.strip():
                        prev_nonempty = prev
                        break
                if prev_nonempty is not None:
                    if result_lines and result_lines[-1].strip() != "":
                        if not re.match(r"^(- |\s*#)", prev_nonempty):
                            result_lines.append("")
            result_lines.append(line)
            bullet_text = line[2:].strip()
            if (i + 2 < len(lines)
                    and lines[i + 1].strip() == ""
                    and lines[i + 2].strip() == bullet_text):
                i += 3
                continue
        else:
            result_lines.append(line)
        i += 1

    text = "\n".join(result_lines)

    def remove_bullet_dups(t):
        pattern = re.compile(r"^(- (.+?))\n\n\2\n", re.MULTILINE)
        prev = None
        while prev != t:
            prev = t
            t = pattern.sub(r"\1\n", t)
        return t

    text = remove_bullet_dups(text)

    def remove_bq_dups(t):
        pattern = re.compile(r"^> (.+?)\n\n\1\n", re.MULTILINE)
        prev = None
        while prev != t:
            prev = t
            t = pattern.sub(r"> \1\n", t)
        return t

    text = remove_bq_dups(text)

    lines = text.split("\n")
    first_h1_seen = False
    result_lines = []
    for line in lines:
        if re.match(r"^# ", line):
            if not first_h1_seen:
                first_h1_seen = True
                result_lines.append(line)
            else:
                result_lines.append("##" + line[1:])
        else:
            result_lines.append(line)

    return "\n".join(result_lines)


def detect_lang(text: str) -> str:
    sc_count = sum(1 for ch in text if ch in SC_CHARS)
    tc_count = sum(1 for ch in text if ch in TC_CHARS)
    return "zh-Hans" if sc_count > tc_count else "zh-Hant"


def extract_title(text: str) -> str:
    for line in text.split("\n"):
        m = re.match(r"^#+ (.+)$", line)
        if m:
            return m.group(1).strip()
    return "章節"


# --- CSS ---

PDF_CSS = """
@page {
    size: A4;
    margin: 2.2cm 2.5cm;
}

body {
    font-family: "Noto Sans CJK TC", "Noto Sans CJK SC",
                 "WenQuanYi Zen Hei", sans-serif;
    font-size: 11pt;
    line-height: 1.8;
    color: #1a1a1a;
}

/* SC sections override to SC-priority font */
section[lang="zh-Hans"],
section[lang="zh-Hans"] * {
    font-family: "Noto Sans CJK SC", "Noto Sans CJK TC",
                 "WenQuanYi Zen Hei", sans-serif;
}

h1 {
    font-size: 1.6em;
    font-weight: bold;
    line-height: 1.4;
    margin-top: 0;
    margin-bottom: 0.6em;
    color: #111;
}

h2 {
    font-size: 1.2em;
    font-weight: bold;
    line-height: 1.4;
    margin-top: 1.4em;
    margin-bottom: 0.4em;
    color: #222;
}

h3 {
    font-size: 1.05em;
    font-weight: bold;
    margin-top: 1em;
    margin-bottom: 0.3em;
}

p {
    margin: 0 0 0.8em 0;
    overflow-wrap: anywhere;
}

blockquote {
    border-left: 3px solid #bbb;
    margin: 0.8em 0 0.8em 0.5em;
    padding-left: 1em;
    color: #555;
}

blockquote p {
    margin-bottom: 0.4em;
}

ul, ol {
    padding-left: 1.5em;
    margin: 0.5em 0 0.8em 0;
}

li {
    margin-bottom: 0.3em;
    line-height: 1.8;
}

li p {
    margin-bottom: 0.2em;
}

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 1.2em 0;
}

a {
    color: #2c5f8a;
    word-break: break-all;
}

strong { font-weight: bold; }
em     { font-style: italic; }

/* Chapter page break — applied to all sections except the first */
section.page-break {
    break-before: page;
    page-break-before: always;
}

.article-date {
    font-size: 9pt;
    color: #888;
    margin-bottom: 1.2em;
}

/* TOC page */
.toc-section {
    break-after: page;
    page-break-after: always;
}

.toc-title {
    font-size: 1.5em;
    font-weight: bold;
    margin-bottom: 1em;
}

.toc-entry {
    font-size: 9.5pt;
    line-height: 1.6;
}

.toc-entry a {
    text-decoration: none;
    color: #1a1a1a;
}

/* Cover page */
.cover-section {
    break-after: page;
    page-break-after: always;
    text-align: center;
    padding-top: 6cm;
}

.cover-title {
    font-size: 2em;
    font-weight: bold;
    line-height: 1.5;
    margin-bottom: 1em;
}

.cover-subtitle {
    font-size: 1em;
    color: #555;
}
"""


def escape_html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_html(chapters: list, test_mode: bool = False) -> str:
    # Cover
    cover = """<section class="cover-section" lang="zh-Hant">
  <div class="cover-title">Steve Koh 文集<br/>超級個體與一人公司</div>
  <div class="cover-subtitle">Steve Koh 著</div>
</section>"""

    # TOC
    toc_rows = []
    for i, ch in enumerate(chapters):
        num = i + 1
        title_esc = escape_html(ch["title"])
        toc_rows.append(
            f'<div class="toc-entry">{num}. <a href="#{ch["anchor"]}">{title_esc}</a></div>'
        )
    toc = (
        '<section class="toc-section page-break" lang="zh-Hant">'
        '<div class="toc-title">目錄</div>'
        + "".join(toc_rows)
        + "</section>"
    )

    # Chapters
    chapter_parts = []
    for i, ch in enumerate(chapters):
        break_class = " page-break" if i > 0 else ""
        date_html = (
            f'<div class="article-date">{escape_html(ch["date"])}</div>'
            if ch["date"]
            else ""
        )
        chapter_parts.append(
            f'<section class="chapter{break_class}" lang="{ch["lang"]}" id="{ch["anchor"]}">'
            f"{ch['html']}"
            f"{date_html}"
            f"</section>"
        )

    body = cover + toc + "".join(chapter_parts)

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8"/>
<title>Steve Koh 文集：超級個體與一人公司</title>
<style>{PDF_CSS}</style>
</head>
<body>
{body}
</body>
</html>"""


def main():
    test_mode = "--test" in sys.argv

    md_files = sorted(glob.glob(os.path.join(MD_DIR, "*.md")))
    print(f"Found {len(md_files)} markdown files")

    if test_mode:
        # Pick first TC file and first SC file only
        test_files = []
        found_tc = found_sc = False
        for f in md_files:
            with open(f, "r", encoding="utf-8") as fh:
                raw = fh.read()
            cleaned = clean_markdown(raw)
            lang = detect_lang(cleaned)
            if lang == "zh-Hant" and not found_tc:
                test_files.append(f)
                found_tc = True
            elif lang == "zh-Hans" and not found_sc:
                test_files.append(f)
                found_sc = True
            if found_tc and found_sc:
                break
        md_files = test_files
        print(f"TEST MODE: processing {len(md_files)} files")

    chapters = []
    for md_path in md_files:
        filename = os.path.basename(md_path)
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})_", filename)
        date_str = date_match.group(1) if date_match else ""

        with open(md_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned = clean_markdown(raw_text)
        lang = detect_lang(cleaned)
        title = extract_title(cleaned)
        body_html = markdown.markdown(cleaned, extensions=["extra"])
        anchor = f"ch-{len(chapters)+1:03d}"

        chapters.append(
            {"title": title, "date": date_str, "lang": lang, "html": body_html, "anchor": anchor}
        )
        print(f"  [{lang}] {title[:50]}")

    print(f"\nRendering PDF…")
    output_path = OUTPUT_PDF if not test_mode else OUTPUT_PDF.replace(".pdf", "_test.pdf")
    font_config = FontConfiguration()
    html_doc = build_html(chapters, test_mode=test_mode)
    HTML(string=html_doc, base_url=MD_DIR).write_pdf(output_path, font_config=font_config)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\nPDF written: {output_path} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
