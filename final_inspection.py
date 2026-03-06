# -*- coding: utf-8 -*-
"""
STEP 7: Final inspection report for all 24 SMILEVIEW HTML files.
Checks:
  1. No remaining Korean text in TW/JP pages
  2. Language dropdown correctness
  3. No chr(1) / corruption artifacts
  4. All inter-page links exist
"""
import os, re

BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"
PAGES = ['index','introduction','invisalign','whitening','ortho','laminate','implant','prosthetics']

BLOCK_RE = re.compile(
    r'<button class="lang-current"[^>]*>(.*?)</button>\s*<div class="lang-dropdown">(.*?)</div>',
    re.DOTALL
)

# Korean Unicode range detector (Hangul syllables + Jamo)
KO_RE = re.compile(r'[\uAC00-\uD7A3\u1100-\u11FF\u3130-\u318F]+')

# Tags/attributes to skip when checking Korean
SKIP_CONTEXTS = [
    re.compile(r'<!--.*?-->', re.DOTALL),       # HTML comments
    re.compile(r'<script.*?</script>', re.DOTALL),
    re.compile(r'<style.*?</style>', re.DOTALL),
]


def strip_skip_contexts(html):
    for pat in SKIP_CONTEXTS:
        html = pat.sub('', html)
    return html


def check_file(fpath, page, lang):
    results = {'dropdown': [], 'korean': [], 'corruption': [], 'links': []}
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # --- 1. Corruption check ---
    if chr(1) in html:
        results['corruption'].append('chr(1) found in file')
    if '\x00' in html:
        results['corruption'].append('null byte found')

    # --- 2. Dropdown check ---
    m = BLOCK_RE.search(html)
    if not m:
        results['dropdown'].append('dropdown block not found')
    else:
        btn_text = m.group(1).strip()
        body = m.group(2)
        expected_btn = {'ko': 'KO', 'tw': 'TW', 'jp': 'JP'}[lang]
        if btn_text != expected_btn:
            results['dropdown'].append(f'button text: {btn_text!r} (expected {expected_btn!r})')
        active_m = re.search(r'<a href="([^"]*)" class="active">', body)
        if not active_m:
            results['dropdown'].append('no active link found')
        elif active_m.group(1) != '#':
            results['dropdown'].append(f'active href={active_m.group(1)!r} (expected "#")')
        # Check link hrefs exist
        link_hrefs = re.findall(r'<a href="([^#"][^"]*)"', body)
        for href in link_hrefs:
            target = os.path.join(BASE, href)
            if not os.path.exists(target):
                results['links'].append(f'dropdown link missing: {href}')

    # --- 3. Korean text check (only for TW/JP) ---
    if lang in ('tw', 'jp'):
        clean = strip_skip_contexts(html)
        # Remove the dropdown block itself (already verified)
        clean = BLOCK_RE.sub('', clean)
        # Remove src/href/data attributes (image/file paths may have Korean filenames)
        clean = re.sub(r'(src|href|data-[a-z]+)="[^"]*"', '', clean)
        lines = clean.split('\n')
        for lineno, line in enumerate(lines, 1):
            ko_matches = KO_RE.findall(line)
            if ko_matches:
                stripped = line.strip()
                if stripped.startswith('<!--') or not stripped:
                    continue
                results['korean'].append(f'  L{lineno}: {stripped[:120]}')

    return results


# ─── Run ───────────────────────────────────────────────────────────────────
total_issues = 0
report_lines = []

for page in PAGES:
    for suffix, lang in [('', 'ko'), ('_tw', 'tw'), ('_jp', 'jp')]:
        fname = f'{page}{suffix}.html'
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath):
            report_lines.append(f'[SKIP]  {fname}')
            continue
        r = check_file(fpath, page, lang)
        all_issues = r['corruption'] + r['dropdown'] + r['links'] + r['korean']
        if all_issues:
            total_issues += len(all_issues)
            ko_count = len(r['korean'])
            report_lines.append(f'[FAIL]  {fname}  (dropdown:{len(r["dropdown"])} corruption:{len(r["corruption"])} links:{len(r["links"])} korean:{ko_count})')
            for cat, items in r.items():
                if items:
                    report_lines.append(f'        [{cat.upper()}]')
                    for item in items[:10]:  # cap at 10 per category
                        report_lines.append(f'          {item}')
                    if len(items) > 10:
                        report_lines.append(f'          ... and {len(items)-10} more')
        else:
            report_lines.append(f'[OK]    {fname}')

out_path = os.path.join(BASE, 'final_inspection_report.txt')
sep = '=' * 65
lines_out = [sep, 'SMILEVIEW i18n Final Inspection Report', sep] + report_lines + [sep]
if total_issues == 0:
    lines_out.append('RESULT: ALL CLEAR - 0 issues across all files.')
else:
    lines_out.append(f'RESULT: {total_issues} issue(s) found. Review FAIL entries above.')
lines_out.append(sep)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines_out))

# Print summary to console (ASCII safe)
print(f'Report saved: {out_path}')
print(f'Total issues: {total_issues}')
fails = [l for l in report_lines if l.startswith('[FAIL]')]
oks   = [l for l in report_lines if l.startswith('[OK]')]
print(f'OK: {len(oks)}  FAIL: {len(fails)}')
for l in fails:
    print(l.encode('ascii', errors='replace').decode())
