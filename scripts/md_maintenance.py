#!/usr/bin/env python3
"""
md_maintenance.py — Markdown 維護工具（frontmatter 補齊 + HTML tag 修正）

用法：
  python scripts/md_maintenance.py [--dry] [--frontmatter-only] [--html-only]

選項：
  --dry              只印出將會變更的檔案，不實際寫入
  --frontmatter-only 只執行 YAML frontmatter 補齊
  --html-only        只執行非標準 HTML tag 轉義修正
  （預設同時執行兩項）
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
RESEARCH_DIR = REPO_ROOT / "docs" / "research"
DOCS_DIR = REPO_ROOT / "docs"


# ===========================================================================
# ① YAML Frontmatter 補齊（原 add_frontmatter.py）
# ===========================================================================

def extract_h1(content):
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else None


def extract_pattern(content, *patterns):
    for pattern in patterns:
        m = re.search(pattern, content)
        if m:
            return m.group(1).strip()
    return None


def extract_date_from_filename(filename):
    m = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return m.group(1) if m else None


def yaml_val(s):
    if s is None:
        return None
    s = str(s).strip()
    if not s:
        return None
    s = re.sub(r'\s*\[.*?\]\s*$', '', s).strip()
    if not s:
        return None
    needs_quote = any(c in s for c in ('"', "'", ':', '#', '{', '}', '[', ']',
                                        ',', '&', '*', '?', '|', '>', '!', '@', '`'))
    needs_quote = needs_quote or (s and s[0] in '-?:')
    if needs_quote:
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return s


def build_frontmatter(fields):
    lines = ['---']
    for key, value in fields.items():
        formatted = yaml_val(value)
        if formatted is not None:
            lines.append(f'{key}: {formatted}')
    lines.append('---')
    lines.append('')
    return '\n'.join(lines)


# --- Per-category extractors ---

def process_tweet(content, filename):
    title = extract_h1(content)
    source = extract_pattern(
        content,
        r'\*\*來源\*\*[：:]\s*(https?://\S+)',
        r'\*\*URL\*\*[：:]\s*(https?://\S+)',
    )
    if source:
        source = source.rstrip('.,;)')
    author = extract_pattern(
        content,
        r'\*\*作者\*\*[：:]\s*([^\n]+)',
        r'\*\*by\*\*[：:]\s*([^\n]+)',
    )
    if author:
        author = re.sub(r'\s*·.*', '', author).strip()
        author = re.sub(r'\s*\*\*.*', '', author).strip()
    date = extract_pattern(
        content,
        r'\*\*發布日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*發布\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*Created\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
    ) or extract_date_from_filename(filename)
    return {'title': title, 'source': source, 'author': author,
            'date': date, 'type': 'tweet'}


def process_video(content, filename):
    title = extract_h1(content)
    source = extract_pattern(content, r'\*\*來源\*\*[：:]\s*(https?://\S+)')
    if source:
        source = source.rstrip('.,;)')
    creator = extract_pattern(
        content,
        r'\*\*作者/頻道\*\*[：:]\s*([^\n]+)',
        r'\*\*頻道\*\*[：:]\s*([^\n]+)',
        r'\*\*作者\*\*[：:]\s*([^\n]+)',
    )
    if creator:
        creator = re.sub(r'\s*[/／].*', '', creator).strip()
        creator = re.sub(r'（[^）]*）', '', creator).strip()
    date = extract_pattern(
        content,
        r'\*\*發布日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*上傳日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
    ) or extract_date_from_filename(filename)
    duration = extract_pattern(content, r'\*\*時長\*\*[：:]\s*([^\n]+)')
    fields = {'title': title, 'source': source, 'creator': creator,
              'date': date, 'type': 'video'}
    if duration:
        fields['duration'] = duration.strip()
    if source and 'youtube' in source:
        fields['platform'] = 'youtube'
    return fields


def process_report(content, filename):
    title = extract_h1(content)
    date = extract_date_from_filename(filename) or extract_pattern(
        content,
        r'\*\*日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'日期[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'date[：:]\s*(\d{4}-\d{2}-\d{2})',
    )
    return {'title': title, 'date': date, 'type': 'report'}


def process_paper(content, filename):
    title = extract_h1(content)
    arxiv_id = extract_pattern(
        content,
        r'\*\*ArXiv\*\*[：:]\s*([\d.]+)',
        r'\*\*arXiv\*\*[：:]\s*([\d.]+)',
        r'arxiv_id[：:]\s*"?([\d.]+)',
    )
    published = extract_pattern(
        content,
        r'\*\*Date\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*Published\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*發表\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*發布\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'published[：:]\s*"?(\d{4}-\d{2}-\d{2})',
    ) or extract_date_from_filename(filename)
    authors = extract_pattern(
        content,
        r'\*\*Authors\*\*[：:]\s*([^\n|]+)',
        r'\*\*作者\*\*[：:]\s*([^\n|]+)',
        r'- \*\*作者\*\*[：:]\s*([^\n]+)',
        r'authors[：:]\s*"?([^\n"]+)',
    )
    if authors:
        authors = authors.strip().rstrip('|').strip()
    if arxiv_id:
        source = f'https://arxiv.org/abs/{arxiv_id}'
    else:
        source = extract_pattern(
            content,
            r'\*\*URL\*\*[：:]\s*(https?://\S+)',
            r'\*\*來源\*\*[：:]\s*(https?://\S+)',
            r'\[.*?\]\((https://arxiv\.org/abs/[^)]+)\)',
        )
        if source:
            source = source.rstrip('.,;)')
    fields = {'title': title, 'authors': authors, 'published': published,
              'source': source, 'source_tier': 'P'}
    if arxiv_id:
        fields['arxiv_id'] = arxiv_id
    return fields


def process_article(content, filename):
    title = extract_h1(content)
    url = extract_pattern(
        content,
        r'\*\*原始 URL\*\*[：:]\s*(https?://\S+)',
        r'\*\*原始來源\*\*[：:]\s*(https?://\S+)',
        r'\*\*來源\*\*[：:]\s*(https?://\S+)',
        r'\*\*URL\*\*[：:]\s*(https?://\S+)',
        r'> Source[：:]\s*(https?://\S+)',
    )
    if url:
        url = url.rstrip('.,;)')
    return {'url': url, 'title': title,
            'date': extract_date_from_filename(filename), 'type': 'article'}


def process_scored_article(content, filename):
    title = extract_h1(content)
    url = extract_pattern(
        content,
        r'\*\*原始來源\*\*[：:]\s*(https?://\S+)',
        r'\*\*來源\*\*[：:]\s*(https?://\S+)',
        r'\*\*原始 URL\*\*[：:]\s*(https?://\S+)',
        r'\*\*URL\*\*[：:]\s*(https?://\S+)',
    )
    if url:
        url = url.rstrip('.,;)')
    return {'url': url, 'title': title,
            'date': extract_date_from_filename(filename), 'type': 'article'}


def process_index(content, filename):
    return {'title': extract_h1(content), 'type': 'index'}


def process_documentation(content, filename):
    return {'title': extract_h1(content), 'type': 'documentation'}


def process_blog(content, filename):
    return {'title': extract_h1(content),
            'date': extract_date_from_filename(filename), 'type': 'blog-index'}


def process_ai_news(content, filename):
    title = extract_h1(content)
    if title:
        title = re.sub(r'^[^\w\s一-鿿]+\s*', '', title).strip()
    date = extract_date_from_filename(filename) or extract_pattern(
        content, r'(\d{4}-\d{2}-\d{2})')
    source = extract_pattern(
        content,
        r'來源[：:]\s*\[([^\]]+)\]',
        r'來源[：:]\s*([^\n\[]+)',
    )
    return {'title': title, 'date': date, 'source': source, 'type': 'ai-news'}


def process_best_practices(content, filename):
    title = extract_h1(content)
    source = extract_pattern(
        content,
        r'來源[：:]\s*([^\n（(]+)',
        r'\*\*來源\*\*[：:]\s*([^\n]+)',
    )
    if source:
        source = source.strip().strip('*').strip()
    return {'title': title, 'source': source, 'type': 'best-practices'}


def process_prompt(content, filename):
    return {'title': extract_h1(content), 'type': 'prompt'}


def process_template(content, filename):
    return {'title': extract_h1(content), 'type': 'template'}


DOC_FILES = {
    'readme.md', 'index.md', '_sidebar.md',
    'scoring.md', 'knowledge-map.md', 'research-index.md',
    'survey.md', 'research.md', 'agents-md-research-index.md',
    'harness-articles-digest.md', 'mhf-research-digest.md',
    'llm-routing-industrial-cases.md', 'topic-index.md',
    'archive-index.md', 'latest-combined.md', 'latest-deepsrt.md',
    'latest-digest.md',
}


def get_processor(filepath, rel_path):
    parts = Path(rel_path).parts
    fname = Path(filepath).name.lower()

    if fname in DOC_FILES:
        return process_documentation if fname not in ('readme.md', 'index.md', '_sidebar.md') \
            else process_index

    top = parts[0] if parts else ''

    if top == 'tweets':
        return process_index if fname == 'readme.md' else process_tweet
    if top == 'videos':
        return process_video
    if top == 'reports':
        return process_report
    if top == 'papers':
        return process_paper
    if top == 'agent-harness':
        if len(parts) > 1 and parts[1] == 'references':
            return process_paper  # references are papers
        return process_documentation
    if top == 'ai-articles':
        if len(parts) > 1 and parts[1] == 'scored':
            return process_scored_article
        return process_article
    if top == 'claude-blog':
        return process_blog
    if top == 'ai-news':
        return process_ai_news
    if top == 'best-practices':
        return process_best_practices
    if top == 'prompts':
        return process_prompt
    if top == 'templates':
        return process_template

    return process_documentation


def run_frontmatter(dry_run=False):
    """補齊缺少 YAML frontmatter 的 markdown 檔案。"""
    processed = skipped = 0
    errors = []

    for root, dirs, files in os.walk(RESEARCH_DIR):
        dirs[:] = sorted(d for d in dirs if d != 'node_modules')
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            path = Path(root) / f
            rel = path.relative_to(RESEARCH_DIR)
            try:
                content = path.read_text(encoding='utf-8', errors='replace')
                if content.startswith('---'):
                    skipped += 1
                    continue
                processor = get_processor(str(path), str(rel))
                fields = processor(content, f)
                fm = build_frontmatter(fields)
                new_content = fm + '\n' + content
                if dry_run:
                    print(f'[DRY-FM] {rel}')
                else:
                    path.write_text(new_content, encoding='utf-8')
                    print(f'[FM] {rel}')
                processed += 1
            except Exception as e:
                errors.append((str(rel), str(e)))
                print(f'ERROR {rel}: {e}', file=sys.stderr)

    mode = 'DRY RUN' if dry_run else 'DONE'
    print(f'\nFrontmatter {mode}: {processed} 新增, {skipped} 已有, {len(errors)} 錯誤')
    return errors


# ===========================================================================
# ② HTML Tag 修正（原 fix_html_tags.py）
# ===========================================================================

STANDARD_TAGS = {
    'a', 'abbr', 'address', 'article', 'aside', 'audio', 'b', 'bdi', 'bdo',
    'blockquote', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col',
    'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog',
    'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure',
    'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header',
    'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label',
    'legend', 'li', 'link', 'main', 'map', 'mark', 'menu', 'meta', 'meter',
    'nav', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p',
    'picture', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp',
    'script', 'section', 'select', 'small', 'source', 'span', 'strong',
    'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'template',
    'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track',
    'u', 'ul', 'var', 'video', 'wbr',
}


def fix_line(line):
    """Escape non-standard HTML tags and Vue expressions outside code spans."""
    parts = re.split(r'(`+[^`]*`+)', line)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            result.append(part)
        else:
            def replace_tag(m):
                slash = m.group(1)
                tag = m.group(2).lower()
                rest = m.group(3)
                if tag not in STANDARD_TAGS:
                    return '&lt;' + (slash or '') + m.group(2) + rest + '>'
                before_match = part[:m.start()]
                if re.match(r'^\s*$', before_match):
                    return m.group(0)
                return '&lt;' + (slash or '') + m.group(2) + rest + '>'

            part = re.sub(r'<(/?)([a-zA-Z][a-zA-Z0-9_-]*)([^>]*)>', replace_tag, part)
            part = re.sub(r'\{\{', '&#123;{', part)
            part = re.sub(r'\{([^}\s][^}]*[^\x00-\x7F][^}]*)\}',
                          lambda m: '&#123;' + m.group(1) + '&#125;', part)
            result.append(part)
    return ''.join(result)


def fix_html_file(path, dry_run=False):
    """Fix a single markdown file. Returns True if changes were made."""
    content = path.read_text(encoding='utf-8', errors='replace')
    lines = content.split('\n')
    result = []
    in_fenced_block = False
    in_frontmatter = False
    frontmatter_closed = False

    for i, line in enumerate(lines):
        if i == 0 and line.rstrip() == '---':
            in_frontmatter = True
            result.append(line)
            continue
        if in_frontmatter and not frontmatter_closed:
            result.append(line)
            if line.rstrip() == '---':
                frontmatter_closed = True
                in_frontmatter = False
            continue
        if re.match(r'^(`{3,}|~{3,})', line):
            in_fenced_block = not in_fenced_block
            result.append(line)
            continue
        if in_fenced_block:
            result.append(line)
            continue
        result.append(fix_line(line))

    new_content = '\n'.join(result)
    if new_content != content:
        if not dry_run:
            path.write_text(new_content, encoding='utf-8')
        return True
    return False


def run_html_fix(dry_run=False):
    """修正 VitePress 無法解析的非標準 HTML tag 與 Vue 表達式。"""
    changed = total = 0
    for md in sorted(DOCS_DIR.rglob('*.md')):
        if 'node_modules' in md.parts:
            continue
        total += 1
        if fix_html_file(md, dry_run=dry_run):
            changed += 1
            mode = '[DRY-HTML]' if dry_run else '[HTML]'
            print(f'{mode} {md.relative_to(DOCS_DIR)}')

    mode = 'DRY RUN' if dry_run else 'DONE'
    print(f'\nHTML-fix {mode}: {changed}/{total} 檔案修正')


# ===========================================================================
# Entry point
# ===========================================================================

def main():
    args = set(sys.argv[1:])
    dry = '--dry' in args
    fm_only = '--frontmatter-only' in args
    html_only = '--html-only' in args

    if fm_only and html_only:
        print('錯誤：--frontmatter-only 與 --html-only 不能同時使用', file=sys.stderr)
        sys.exit(1)

    run_fm = not html_only
    run_html = not fm_only

    errors = []
    if run_fm:
        errors += run_frontmatter(dry_run=dry)
    if run_html:
        run_html_fix(dry_run=dry)

    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
