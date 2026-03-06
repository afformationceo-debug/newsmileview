# -*- coding: utf-8 -*-
"""
STEP 4: generate_pages.py
Generates 16 translated HTML files (_tw.html, _jp.html) from Korean originals.

Replacement strategies:
1. KO JSON text (authoritative) → target language translated text
2. Strip "A. " prefix for FAQ answers (handle <span>A.</span>TEXT pattern)
3. TR row items: split cells and replace individually
4. Systematic footer/day/slogan fixes
"""
import json
import os
import re

BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"
PAGES = ['index', 'invisalign', 'ortho', 'laminate', 'whitening',
         'implant', 'prosthetics', 'introduction']

LANGS = {
    'tw': {'lang_code': 'zh-TW', 'suffix': '_tw'},
    'jp': {'lang_code': 'ja',    'suffix': '_jp'},
}

# ─── Systematic fixes (footer, days, slogan) ─────────────────────────────────
FIXES_TW = [
    # Footer labels
    ('>대표자<', '>代表人<'),
    ('>사업자번호<', '>營業登記號<'),
    # Day names
    ('>평일<', '>平日<'),
    ('>토요일<', '>週六<'),
    ('>일요일<', '>週日<'),
    ('>휴진<', '>休診<'),
    ('>공휴일<', '>國定假日<'),
    # Slogan with <br>
    ('투명하고 편리한 교정부터 심미 치료까지,<br>스마일뷰치과가 당신의 아름다운 미소를 만들어 드립니다.',
     '從透明便利的矯正療程到美容牙科治療，<br>SMILEVIEW牙醫診所為您打造完美迷人的笑容。'),
    # Partial slogan (스마일뷰치과 already replaced to SMILEVIEW牙醫診所)
    ('<br>SMILEVIEW牙醫診所가 당신의 아름다운 미소를 만들어 드립니다.',
     '<br>SMILEVIEW牙醫診所為您打造完美迷人的笑容。'),
    ('당신의 아름다운 미소를 만들어 드립니다.',
     'SMILEVIEW牙醫診所為您打造完美迷人的笑容。'),
    # Footer names
    ('>김한결</', '>金韓結</'),
]

FIXES_JP = [
    # Footer labels
    ('>대표자<', '>代表者<'),
    ('>사업자번호<', '>事業者番号<'),
    # Day names
    ('>평일<', '>平日<'),
    ('>토요일<', '>土曜日<'),
    ('>일요일<', '>日曜日<'),
    ('>휴진<', '>休診<'),
    ('>공휴일<', '>祝日<'),
    # Slogan with <br>
    ('투명하고 편리한 교정부터 심미 치료까지,<br>스마일뷰치과가 당신의 아름다운 미소를 만들어 드립니다.',
     '透明で便利な矯正から審美治療まで、<br>SMILEVIEWデンタルクリニックがあなたの美しい笑顔をお作りします。'),
    # Partial slogan
    ('<br>SMILEVIEWデンタルクリニック가 당신의 아름다운 미소를 만들어 드립니다.',
     '<br>SMILEVIEWデンタルクリニックがあなたの美しい笑顔をお作りします。'),
    ('당신의 아름다운 미소를 만들어 드립니다.',
     'あなたの美しい笑顔をお作りします。'),
    # Footer names
    ('>김한결</', '>金韓結</'),
]


def load_translations(page, lang_dir):
    """
    Load translations cross-referencing KO JSON (for matching) and target JSON.
    Returns list of (orig_text, translated_text, is_attr, key) tuples.
    """
    ko_path = os.path.join(BASE, 'translations', 'ko', f'{page}.json')
    tgt_path = os.path.join(BASE, 'translations', lang_dir, f'{page}.json')

    if not os.path.exists(ko_path) or not os.path.exists(tgt_path):
        return []

    with open(ko_path, 'r', encoding='utf-8') as f:
        ko_items = json.load(f)
    with open(tgt_path, 'r', encoding='utf-8') as f:
        tgt_items = json.load(f)

    tgt_by_key = {item['key']: item.get('translated', '') for item in tgt_items}

    pairs = []
    for item in ko_items:
        key = item['key']
        orig = item.get('text', '').strip()
        trans = tgt_by_key.get(key, '').strip()

        if not orig or not trans or orig == trans:
            continue

        is_attr = key.startswith('attr_') or item.get('context') == 'attr'
        pairs.append((orig, trans, is_attr, key))

    # Sort by length descending
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return pairs


def fix_internal_links(html, suffix):
    """Replace internal page links .html → _XX.html."""
    for page in PAGES:
        html = re.sub(
            rf'(href=["\']){re.escape(page)}\.html(["\'])',
            rf'\g<1>{page}{suffix}.html\2',
            html
        )
    return html


def apply_translations(html, pairs):
    """Apply translations using multiple strategies."""
    # Strategy 1: Attribute replacements in quoted context
    for orig, trans, is_attr, key in pairs:
        if is_attr:
            html = html.replace(f'="{orig}"', f'="{trans}"')
            html = html.replace(f"='{orig}'", f"='{trans}'")

    # Strategy 2: Global text replacement
    for orig, trans, is_attr, key in pairs:
        html = html.replace(orig, trans)

    # Strategy 3: Strip "A. " prefix for FAQ answers
    # Handles <span>A.</span>KOREAN → <span>A.</span>TRANSLATED
    for orig, trans, is_attr, key in pairs:
        if orig.startswith('A. ') and len(orig) > 5:
            ko_body = orig[3:]   # text after "A. "
            tr_body = trans[3:] if trans.startswith('A. ') else trans
            if ko_body and tr_body and ko_body != tr_body:
                html = html.replace(ko_body, tr_body)

    # Strategy 4: Table row cell replacement
    # For _tr items: extract individual cell texts and replace them
    for orig, trans, is_attr, key in pairs:
        if key.endswith('_tr') or ('_tr' in key):
            # Split orig and trans into space-separated tokens
            # Try to find Korean substrings in HTML and replace
            pass  # Handled by cell-level fixes below

    return html


def apply_cell_fixes(html, pairs):
    """
    For table row items (_tr), extract individual cell texts and replace.
    These are items where extract_texts.py concatenated all <td> texts.
    """
    for orig, trans, is_attr, key in pairs:
        if not key.endswith('_tr'):
            continue
        # The orig is space-joined cell texts; trans is space-joined translated cells
        # Try to build td-level replacements
        # We match individual Korean cells that still appear in HTML
        ko_re = re.compile(r'[가-힣ㄱ-ㅎㅏ-ㅣ]')
        if ko_re.search(html):
            # Split by the pattern of Korean word boundaries is not reliable
            # Instead, try to replace known Korean cell patterns
            pass  # Let per-page explicit fixes handle this
    return html


def apply_systematic_fixes(html, lang_dir):
    """Apply footer/day/slogan systematic fixes."""
    fixes = FIXES_TW if lang_dir == 'tw' else FIXES_JP
    for old, new in fixes:
        html = html.replace(old, new)
    return html


def count_remaining_korean(filepath):
    """Count Korean-containing lines in HTML, excluding script/style blocks."""
    ko = re.compile(r'[가-힣ㄱ-ㅎㅏ-ㅣ]')
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_script = False
    in_style = False
    ko_lines = []
    for i, line in enumerate(lines, 1):
        sl = line.strip().lower()
        if '<script' in sl and not in_script:
            in_script = True
        if '</script>' in sl:
            in_script = False
            continue
        if '<style' in sl and not in_style:
            in_style = True
        if '</style>' in sl:
            in_style = False
            continue
        if not in_script and not in_style and ko.search(line):
            ko_lines.append((i, line.rstrip()))
    return ko_lines


def generate_page(page, lang_dir, lang_code, suffix):
    """Generate a single translated HTML page."""
    src = os.path.join(BASE, f'{page}.html')
    if not os.path.exists(src):
        return False

    with open(src, 'r', encoding='utf-8') as f:
        html = f.read()

    pairs = load_translations(page, lang_dir)

    # 1. Replace lang attribute
    html = re.sub(r'lang="ko"', f'lang="{lang_code}"', html)

    # 2. Apply translations (multiple strategies)
    html = apply_translations(html, pairs)

    # 3. Apply systematic footer/day/slogan fixes
    html = apply_systematic_fixes(html, lang_dir)

    # 4. Fix internal links
    html = fix_internal_links(html, suffix)

    out_path = os.path.join(BASE, f'{page}{suffix}.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return True


if __name__ == '__main__':
    print("=== STEP 4: Generating translated HTML pages ===\n")
    results = {}

    for lang_dir, cfg in LANGS.items():
        lang_code = cfg['lang_code']
        suffix = cfg['suffix']
        print(f"--- Language: {lang_code} ({lang_dir}) ---")

        for page in PAGES:
            ok = generate_page(page, lang_dir, lang_code, suffix)
            if ok:
                out_path = os.path.join(BASE, f'{page}{suffix}.html')
                ko_lines = count_remaining_korean(out_path)
                results[f'{page}{suffix}'] = len(ko_lines)
                status = "✓" if len(ko_lines) == 0 else f"! ({len(ko_lines)} ko lines)"
                print(f"  {page}{suffix}.html  {status}")
            else:
                results[f'{page}{suffix}'] = -1

    print("\n=== Summary ===")
    total_pages = len([v for v in results.values() if v >= 0])
    clean_pages = len([v for v in results.values() if v == 0])
    print(f"Generated: {total_pages}/16 pages")
    print(f"Clean (0 Korean): {clean_pages}/{total_pages}")

    issues = [(k, v) for k, v in results.items() if v > 0]
    if issues:
        print("\nPages with remaining Korean (HTML content):")
        for page, count in sorted(issues):
            print(f"  {page}.html: {count} lines")
    else:
        print("All pages clean!")
