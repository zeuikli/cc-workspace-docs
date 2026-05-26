#!/usr/bin/env python3
"""
Add YAML frontmatter to research markdown files that are missing it.
Content is preserved exactly; only frontmatter is prepended.
"""
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

BASE = Path('/home/user/cc-workspace-docs/docs/research')


def extract_h1(content):
    """Extract first H1 heading from content."""
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else None


def extract_pattern(content, *patterns):
    """Try multiple regex patterns to extract a value."""
    for pattern in patterns:
        m = re.search(pattern, content)
        if m:
            return m.group(1).strip()
    return None


def extract_date_from_filename(filename):
    """Extract YYYY-MM-DD from filename."""
    m = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return m.group(1) if m else None


def yaml_val(s):
    """Format a value for a YAML line. Returns None if empty."""
    if s is None:
        return None
    s = str(s).strip()
    if not s:
        return None
    # Remove trailing markdown link artifacts
    s = re.sub(r'\s*\[.*?\]\s*$', '', s).strip()
    if not s:
        return None
    # Determine if quoting is needed
    needs_quote = any(c in s for c in ('"', "'", ':', '#', '{', '}', '[', ']',
                                        ',', '&', '*', '?', '|', '>', '!', '@', '`'))
    needs_quote = needs_quote or (s and s[0] in '-?:')
    if needs_quote:
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return s


def build_frontmatter(fields):
    """Build YAML frontmatter block from ordered dict of fields."""
    lines = ['---']
    for key, value in fields.items():
        formatted = yaml_val(value)
        if formatted is not None:
            lines.append(f'{key}: {formatted}')
    lines.append('---')
    lines.append('')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Per-category extractors
# ---------------------------------------------------------------------------

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
        # Remove " · followers · location" suffix
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
    source = extract_pattern(
        content,
        r'\*\*來源\*\*[：:]\s*(https?://\S+)',
    )
    if source:
        source = source.rstrip('.,;)')
    creator = extract_pattern(
        content,
        r'\*\*作者/頻道\*\*[：:]\s*([^\n]+)',
        r'\*\*頻道\*\*[：:]\s*([^\n]+)',
        r'\*\*作者\*\*[：:]\s*([^\n]+)',
    )
    if creator:
        # Keep only the primary name/channel
        creator = re.sub(r'\s*[/／].*', '', creator).strip()
        creator = re.sub(r'（[^）]*）', '', creator).strip()
    date = extract_pattern(
        content,
        r'\*\*發布日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
        r'\*\*上傳日期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})',
    ) or extract_date_from_filename(filename)
    duration = extract_pattern(content, r'\*\*時長\*\*[：:]\s*([^\n]+)')
    platform = 'youtube' if source and 'youtube' in source else None
    fields = {'title': title, 'source': source, 'creator': creator,
              'date': date, 'type': 'video'}
    if duration:
        fields['duration'] = duration.strip()
    if platform:
        fields['platform'] = platform
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
    # Pattern: **ArXiv**: 2603.20075 | **Date**: 2026-03-20 | **Authors**: ...
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
    source = None
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


def process_reference(content, filename):
    return process_paper(content, filename)


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
    date = extract_date_from_filename(filename)
    return {'url': url, 'title': title, 'date': date, 'type': 'article'}


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
    date = extract_date_from_filename(filename)
    return {'url': url, 'title': title, 'date': date, 'type': 'article'}


def process_index(content, filename):
    title = extract_h1(content)
    return {'title': title, 'type': 'index'}


def process_documentation(content, filename):
    title = extract_h1(content)
    return {'title': title, 'type': 'documentation'}


def process_blog(content, filename):
    title = extract_h1(content)
    date = extract_date_from_filename(filename)
    return {'title': title, 'date': date, 'type': 'blog-index'}


def process_ai_news(content, filename):
    title = extract_h1(content)
    # Strip emoji from title for cleaner frontmatter
    if title:
        title = re.sub(r'^[^\w\s一-鿿]+\s*', '', title).strip()
    date = extract_date_from_filename(filename) or extract_pattern(
        content,
        r'(\d{4}-\d{2}-\d{2})',
    )
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
    title = extract_h1(content)
    return {'title': title, 'type': 'prompt'}


def process_template(content, filename):
    title = extract_h1(content)
    return {'title': title, 'type': 'template'}


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

# Filenames that are documentation/navigation regardless of directory
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
    """Return the appropriate processor function for a file."""
    parts = Path(rel_path).parts
    fname = Path(filepath).name.lower()

    # Special index/doc files
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
            return process_reference
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(dry_run=False):
    processed = 0
    skipped = 0
    errors = []

    for root, dirs, files in os.walk(BASE):
        dirs[:] = sorted(d for d in dirs if d != 'node_modules')
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            path = Path(root) / f
            rel = path.relative_to(BASE)

            try:
                content = path.read_text(encoding='utf-8', errors='replace')

                # Skip files that already have frontmatter
                if content.startswith('---'):
                    skipped += 1
                    continue

                processor = get_processor(str(path), str(rel))
                fields = processor(content, f)
                fm = build_frontmatter(fields)
                new_content = fm + '\n' + content

                if dry_run:
                    print(f'[DRY] {rel}')
                    print(fm)
                    print()
                else:
                    path.write_text(new_content, encoding='utf-8')
                    print(f'+ {rel}')
                processed += 1

            except Exception as e:
                errors.append((str(rel), str(e)))
                print(f'ERROR {rel}: {e}', file=sys.stderr)

    mode = 'DRY RUN' if dry_run else 'DONE'
    print(f'\n{mode}: {processed} processed, {skipped} already had frontmatter, {len(errors)} errors')
    if errors:
        print('\nErrors:')
        for p, err in errors:
            print(f'  {p}: {err}')
    return len(errors) == 0


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    ok = main(dry_run=dry)
    sys.exit(0 if ok else 1)
