#!/usr/bin/env python3
"""Build high-quality EPUB from Steve Koh markdown articles."""

import os
import re
import glob
from ebooklib import epub
import markdown

# --- Config ---
MD_DIR = "/home/user/cc-workspace/research/substack-thestevekoh"
CSS_SRC = os.path.join(MD_DIR, "epub.css")
OUTPUT_EPUB = os.path.join(MD_DIR, "Steve_Koh_文集.epub")

# SC-only chars (Simplified Chinese)
SC_CHARS = set("这们东为时国会该实从")
# TC-only chars (Traditional Chinese)
TC_CHARS = set("這們東為時國會該實從")

PROMO_MARKERS = [
    "如果你真心想要變強",
    "P.S. 如果你還想用少過",
]


def clean_markdown(text: str) -> str:
    """Clean markdown text: remove source, promo footer, fix duplicates, normalize headings."""
    lines = text.split("\n")

    # Step 1: Remove **來源：** https?://... line and track position
    source_line_idx = None
    cleaned_lines = []
    for i, line in enumerate(lines):
        if re.match(r"^\*\*來源：\*\* https?://", line.strip()):
            source_line_idx = len(cleaned_lines)
            # Skip this line (don't add to cleaned_lines)
        else:
            cleaned_lines.append((i, line))

    # Step 2: Remove the --- separator within ~3 blank lines after source removal
    if source_line_idx is not None:
        # Look at the cleaned_lines around source_line_idx
        # We need to find a "---" that appears within a window after where the source was
        # source_line_idx is the index in cleaned_lines where the source WOULD have been
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
                # Non-blank, non-separator line before finding --- means stop
                break
            i += 1

        if remove_idx is not None:
            cleaned_lines.pop(remove_idx)

    # Rebuild lines list (discard original line numbers)
    lines = [line for _, line in cleaned_lines]
    text = "\n".join(lines)

    # Step 3: Truncate at promo footer (both variants)
    for marker in PROMO_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx].rstrip()
            break

    lines = text.split("\n")

    # Step 4 + 5: Fix bullet duplicates and ensure blank line before bullet lists
    # Pattern: "- TEXT\n\nTEXT" → keep only "- TEXT"
    # Also: ensure blank line before bullet list if preceding non-empty line isn't blank/bullet/heading
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        bullet_match = re.match(r"^(- .+)$", line)

        if bullet_match:
            # Ensure blank line before bullet list start
            # Check if previous non-empty context needs a blank line inserted
            if result_lines:
                prev_nonempty = None
                for prev in reversed(result_lines):
                    if prev.strip():
                        prev_nonempty = prev
                        break
                if prev_nonempty is not None:
                    # If last line in result is not blank, and prev_nonempty is not a bullet/heading
                    if result_lines and result_lines[-1].strip() != "":
                        if not re.match(r"^(- |\s*#)", prev_nonempty):
                            result_lines.append("")

            result_lines.append(line)
            bullet_text = line[2:].strip()  # text after "- "

            # Check if next lines have: blank line + duplicate text
            # Pattern: current "- TEXT", then "\n", then "TEXT" (stripped equal)
            if (i + 2 < len(lines)
                    and lines[i + 1].strip() == ""
                    and lines[i + 2].strip() == bullet_text):
                # Skip the blank + duplicate paragraph
                i += 3
                continue
            # Also handle: "- TITLE\nTITLE_PART\n\nTITLE_CONTENT" (multi-part bullets)
            # More complex: check if i+1 is non-blank and is a "sub-heading" then i+2 is blank and i+3 is content
            # Pattern observed: "- 超級個體會員解鎖..." -> "\n" -> "超級個體會員" -> "\n" -> "解鎖..."
            # Check for the two-part variant: "- A B\n\nA\n\nB"
            # Let's handle: after "- TEXT" if next line is blank, check if i+2 is a substring/prefix split
            # Actually looking at the data more carefully:
            # "- 超級個體會員解鎖所有高級資源..." -> blank -> "超級個體會員" -> blank -> "解鎖所有高級資源..."
            # These are harder; let's use a greedy approach: skip any paragraph immediately after
            # a bullet that matches a prefix or the full text
        else:
            result_lines.append(line)

        i += 1

    lines = result_lines

    # Step 5b: Remove any remaining standalone paragraph duplicates of bullet text
    # Re-scan: if we see "- TEXT\n\nTEXT" that wasn't caught (different spacing), handle it
    # Build new result with multi-pass regex on joined text
    text = "\n".join(lines)

    # Use regex on the full text for bullet duplicate patterns
    # Pattern: line starting with "- " followed by optional blank lines then same text as paragraph
    def remove_bullet_dups(t):
        # Match: "- TEXT\n\nTEXT\n" where TEXT is the same (stripped)
        pattern = re.compile(r"^(- (.+?))\n\n\2\n", re.MULTILINE)
        prev = None
        while prev != t:
            prev = t
            t = pattern.sub(r"\1\n", t)
        return t

    text = remove_bullet_dups(text)

    # Step 6: Remove blockquote duplicates
    # Pattern: "> TEXT\n\nTEXT" (stripped equal) → keep only "> TEXT"
    def remove_bq_dups(t):
        pattern = re.compile(r"^> (.+?)\n\n\1\n", re.MULTILINE)
        prev = None
        while prev != t:
            prev = t
            t = pattern.sub(r"> \1\n", t)
        return t

    text = remove_bq_dups(text)

    # Step 7: Normalize headings — first # stays h1, all subsequent # become ##
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
    """Detect zh-Hans vs zh-Hant based on SC/TC character counts."""
    sc_count = sum(1 for ch in text if ch in SC_CHARS)
    tc_count = sum(1 for ch in text if ch in TC_CHARS)
    if sc_count > tc_count:
        return "zh-Hans"
    return "zh-Hant"


def md_to_xhtml(body_html: str, lang: str, title: str) -> str:
    """Wrap HTML body in a full XHTML document with proper lang attributes."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"
      xml:lang="{lang}" lang="{lang}">
<head>
  <meta charset="UTF-8"/>
  <title>{title}</title>
  <link rel="stylesheet" type="text/css" href="../style/main.css"/>
</head>
<body>
{body_html}
</body>
</html>"""


def build_css() -> str:
    """Read epub.css and remove break-before/page-break-before from h1 rule."""
    with open(CSS_SRC, "r", encoding="utf-8") as f:
        css = f.read()

    # Remove the two page-break lines from h1 block
    css = re.sub(r"\s*break-before:\s*page;\n?", "\n", css)
    css = re.sub(r"\s*page-break-before:\s*always;\n?", "\n", css)

    # Clean up any double blank lines that result
    css = re.sub(r"\n{3,}", "\n\n", css)
    return css


def extract_title(text: str) -> str:
    """Extract title from first # heading."""
    for line in text.split("\n"):
        m = re.match(r"^#+ (.+)$", line)
        if m:
            return m.group(1).strip()
    return "章節"


def main():
    # Get sorted list of markdown files
    md_files = sorted(glob.glob(os.path.join(MD_DIR, "*.md")))
    print(f"Found {len(md_files)} markdown files")

    # Build EPUB
    book = epub.EpubBook()
    book.set_identifier("stevekoh-collection-2024")
    book.set_title("Steve Koh 文集：超級個體與一人公司")
    book.add_author("Steve Koh")
    book.set_language("zh")

    # Add CSS
    css_content = build_css()
    css_item = epub.EpubItem(
        uid="style_main",
        file_name="style/main.css",
        media_type="text/css",
        content=css_content.encode("utf-8"),
    )
    book.add_item(css_item)

    chapters = []
    toc_entries = []

    for idx, md_path in enumerate(md_files):
        chapter_num = idx + 1
        chapter_id = f"ch{chapter_num:03d}"
        chapter_file = f"ch/{chapter_id}.xhtml"

        with open(md_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        # Clean the markdown
        cleaned = clean_markdown(raw_text)

        # Detect language
        lang = detect_lang(cleaned)

        # Extract title
        title = extract_title(cleaned)

        # Convert to HTML
        body_html = markdown.markdown(cleaned, extensions=["extra"])

        # Build full XHTML
        xhtml = md_to_xhtml(body_html, lang, title)

        # Create chapter item
        chapter = epub.EpubHtml(
            uid=chapter_id,
            file_name=chapter_file,
            media_type="application/xhtml+xml",
        )
        chapter.content = xhtml.encode("utf-8")
        chapter.lang = lang
        chapter.title = title

        book.add_item(chapter)
        chapters.append(chapter)
        toc_entries.append(epub.Link(chapter_file, title, chapter_id))

        if chapter_num <= 3 or chapter_num == 12 or chapter_num == len(md_files):
            print(f"  ch{chapter_num:03d}: [{lang}] {title[:40]}")

    # Set spine and TOC
    book.spine = ["nav"] + chapters
    book.toc = toc_entries

    # Add required NCX and Nav items
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Write EPUB
    epub.write_epub(OUTPUT_EPUB, book, {})
    print(f"\nEPUB written: {OUTPUT_EPUB}")
    size_mb = os.path.getsize(OUTPUT_EPUB) / (1024 * 1024)
    print(f"File size: {size_mb:.2f} MB")


if __name__ == "__main__":
    main()
