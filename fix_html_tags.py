#!/usr/bin/env python3
"""
Fix non-standard HTML-like tags in markdown files that break VitePress Vue compilation.
Escapes <non-standard-tag> to &lt;non-standard-tag&gt; outside of code blocks.
"""
import re
import sys
from pathlib import Path

BASE = Path('/home/user/cc-workspace-docs/docs')

# Standard HTML5 tags that VitePress handles fine
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
    """Escape HTML tags and Vue expressions in a text line (not in code block)."""
    # Split by inline code spans to avoid modifying them
    parts = re.split(r'(`+[^`]*`+)', line)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Inside inline code — leave as-is
            result.append(part)
        else:
            # Find all < occurrences. For each, check if it's a well-formed
            # block-level HTML (starts the line with nothing before it) or inline.
            # Escape the opening < of any tag that could be parsed by Vue.
            def replace_tag(m):
                slash = m.group(1)     # "/" for closing tags
                tag = m.group(2).lower()
                rest = m.group(3)      # attributes or "/"

                # If this is a non-standard tag, always escape
                if tag not in STANDARD_TAGS:
                    return '&lt;' + (slash or '') + m.group(2) + rest + '>'

                # Standard HTML tags: escape if they appear INLINE
                # (not at start of line with only optional whitespace before)
                before_match = part[:m.start()]
                # If the tag starts at position 0 or only whitespace before it
                # AND the line appears to be a block-level HTML construct, keep it
                if re.match(r'^\s*$', before_match):
                    return m.group(0)  # block-level position — keep

                # Inline use of standard tag — escape to avoid Vue parsing issues
                return '&lt;' + (slash or '') + m.group(2) + rest + '>'

            part = re.sub(r'<(/?)([a-zA-Z][a-zA-Z0-9_-]*)([^>]*)>', replace_tag, part)
            # Escape Vue template expressions {{ ... }}
            part = re.sub(r'\{\{', '&#123;{', part)
            # Escape standalone { that would be invalid JS in Vue template context
            # (e.g. {Chinese、text} in table cells)
            # Matches { followed by non-ASCII/non-identifier content
            part = re.sub(r'\{([^}\s][^}]*[^\x00-\x7F][^}]*)\}',
                          lambda m: '&#123;' + m.group(1) + '&#125;', part)
            result.append(part)
    return ''.join(result)


def fix_file(path, dry_run=False):
    """Fix a single markdown file. Returns True if changes were made."""
    content = path.read_text(encoding='utf-8', errors='replace')
    lines = content.split('\n')
    result = []
    in_fenced_block = False
    in_frontmatter = False
    frontmatter_closed = False

    for i, line in enumerate(lines):
        # Handle YAML frontmatter
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

        # Track fenced code blocks (``` or ~~~)
        if re.match(r'^(`{3,}|~{3,})', line):
            in_fenced_block = not in_fenced_block
            result.append(line)
            continue

        if in_fenced_block:
            result.append(line)
            continue

        # Regular text line — fix non-standard tags
        result.append(fix_line(line))

    new_content = '\n'.join(result)
    if new_content != content:
        if not dry_run:
            path.write_text(new_content, encoding='utf-8')
        return True
    return False


def main(dry_run=False):
    changed = 0
    total = 0

    for md in sorted(BASE.rglob('*.md')):
        # Skip node_modules
        if 'node_modules' in md.parts:
            continue
        total += 1
        if fix_file(md, dry_run=dry_run):
            changed += 1
            mode = '[DRY]' if dry_run else '[FIXED]'
            print(f'{mode} {md.relative_to(BASE)}')

    mode = 'DRY RUN' if dry_run else 'DONE'
    print(f'\n{mode}: {changed}/{total} files fixed')


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    main(dry_run=dry)
