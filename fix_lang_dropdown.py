# -*- coding: utf-8 -*-
"""
Fix language dropdown links in all 24 HTML files.
- KO files: wire TW/JP hrefs
- TW files: set button=TW, KO link href, TW active, JP link href
- JP files: set button=JP, KO link href, TW link href, JP active
Also fixes the \x01 bug from the previous run.
"""
import os, re

BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"
PAGES = ['index','introduction','invisalign','whitening','ortho','laminate','implant','prosthetics']

# Regex to match the entire dropdown block (button + div)
BLOCK_RE = re.compile(
    r'(<button class="lang-current"[^>]*>)'  # group 1: button open tag
    r'[^<]*'                                  # current label (KO/TW/JP or garbage)
    r'(</button>\s*<div class="lang-dropdown">)'  # group 2: closing button + div open
    r'(.*?)'                                  # group 3: link items
    r'(</div>)',                              # group 4: div close
    re.DOTALL
)

# Regex to extract link items from the dropdown body
# Matches both <a href="x" class="active">text</a> and <a href="x">text</a>
LINK_RE = re.compile(r'<a href="([^"]*)"(?:\s+class="active")?>([^<]*)</a>')


def build_dropdown_body(indent, links):
    """links = list of (href, text, is_active)"""
    lines = []
    for href, text, active in links:
        if active:
            lines.append(f'{indent}<a href="{href}" class="active">{text}</a>')
        else:
            lines.append(f'{indent}<a href="{href}">{text}</a>')
    return '\n'.join(lines) + '\n' + indent[:-4] if indent else '\n'.join(lines)


def update_file(fpath, page, lang):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    def replacer(m):
        btn_open = m.group(1)
        btn_close_div_open = m.group(2)
        body = m.group(3)
        div_close = m.group(4)

        # Extract existing link texts (may be corrupted with \x01)
        existing = LINK_RE.findall(body)
        # existing = [(href, text), ...]
        # Reconstruct from known labels
        if lang == 'ko':
            ko_text = existing[0][1] if existing else '한국어 (KO)'
            tw_href = f'{page}_tw.html'
            jp_href = f'{page}_jp.html'
            links = [
                ('#',       ko_text,           True),
                (tw_href,   '繁體中文 (TW)',    False),
                (jp_href,   '日本語 (JP)',      False),
            ]
            label = 'KO'

        elif lang == 'tw':
            # KO label: use existing[0][1] but fix \x01 → use known TW label
            ko_text = existing[0][1].strip()
            if not ko_text or ko_text == '\x01':
                ko_text = '韓語 (KO)'
            ko_href = f'{page}.html'
            jp_href = f'{page}_jp.html'
            links = [
                (ko_href,   ko_text,            False),
                ('#',       '繁體中文 (TW)',     True),
                (jp_href,   '日本語 (JP)',       False),
            ]
            label = 'TW'

        else:  # jp
            ko_text = existing[0][1].strip()
            if not ko_text or ko_text == '\x01':
                ko_text = '韓国語 (KO)'
            ko_href = f'{page}.html'
            tw_href = f'{page}_tw.html'
            links = [
                (ko_href,   ko_text,            False),
                (tw_href,   '繁體中文 (TW)',     False),
                ('#',       '日本語 (JP)',        True),
            ]
            label = 'JP'

        # Detect indentation from existing body
        indent_m = re.search(r'\n(\s+)<a', body)
        indent = indent_m.group(1) if indent_m else '                        '

        new_body = '\n'
        for href, text, active in links:
            cls = ' class="active"' if active else ''
            new_body += f'{indent}<a href="{href}"{cls}>{text}</a>\n'
        new_body += indent[:-4]  # closing div indent

        return f'{btn_open}{label}{btn_close_div_open}{new_body}{div_close}'

    new_html = BLOCK_RE.sub(replacer, html, count=1)
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        return 'OK'
    return 'UNCHANGED'


if __name__ == '__main__':
    for page in PAGES:
        for suffix, lang in [('', 'ko'), ('_tw', 'tw'), ('_jp', 'jp')]:
            fname = f'{page}{suffix}.html'
            fpath = os.path.join(BASE, fname)
            if not os.path.exists(fpath):
                print(f'SKIP  {fname}')
                continue
            result = update_file(fpath, page, lang)
            print(f'{result}  {fname}')
    print('\nDone.')
