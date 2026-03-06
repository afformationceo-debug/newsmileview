# -*- coding: utf-8 -*-
import os, re

BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"
PAGES = ['index','introduction','invisalign','whitening','ortho','laminate','implant','prosthetics']
BLOCK_RE = re.compile(
    r'<button class="lang-current"[^>]*>(.*?)</button>\s*<div class="lang-dropdown">(.*?)</div>',
    re.DOTALL
)

issues = []
ok_count = 0
for page in PAGES:
    for suffix, lang in [('', 'ko'), ('_tw', 'tw'), ('_jp', 'jp')]:
        fname = f'{page}{suffix}.html'
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        m = BLOCK_RE.search(html)
        if not m:
            issues.append(f'NO DROPDOWN: {fname}')
            continue
        btn_text = m.group(1).strip()
        body = m.group(2)
        expected_btn = {'ko': 'KO', 'tw': 'TW', 'jp': 'JP'}[lang]
        if btn_text != expected_btn:
            issues.append(f'WRONG BTN ({btn_text!r} vs {expected_btn!r}): {fname}')
        active_m = re.search(r'<a href="([^"]*)" class="active">', body)
        if not active_m:
            issues.append(f'NO ACTIVE LINK: {fname}')
        elif active_m.group(1) != '#':
            issues.append(f'WRONG ACTIVE HREF ({active_m.group(1)!r}): {fname}')
        if chr(1) in body:
            issues.append(f'HAS chr(1) CORRUPTION: {fname}')
        if lang == 'tw':
            links = re.findall(r'<a href="[^"]*"(?:\s+class="active")?>(.*?)</a>', body)
            if links and links[0] in ('繁體中文（TW）', 'KO', ''):
                issues.append(f'BAD KO TEXT ({links[0]!r}): {fname}')
        ok_count += 1

print(f'Checked {ok_count} files.')
if issues:
    print(f'{len(issues)} ISSUE(S) FOUND:')
    for i in issues:
        print(' ', i)
else:
    print('ALL FILES OK - dropdown verification passed!')
