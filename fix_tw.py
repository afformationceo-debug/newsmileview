# -*- coding: utf-8 -*-
"""
TW 버전 수정 스크립트
수정 1: 네비게이션 텍스트 (ORTHODONTICS→牙齒矯正, PROSTHETICS→牙齒修復)
수정 2: 언어팩 드롭다운 type="button" 추가 + closest 방식
수정 3: 배너 이미지 제거 (prosthetics_tw.html)
수정 4: LINE 링크 삽입
수정 5: 인스타그램 링크 수정
수정 6: 이미지 경로 수정 (prosthetics_tw.html)
"""
import os, re

BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"
PAGES = ['index','introduction','invisalign','whitening','ortho','laminate','implant','prosthetics']
TW_LINE = "https://lin.ee/lHEp9er"
TW_INSTA = "https://www.instagram.com/smileview_tw/"

results = {}

for page in PAGES:
    fname = f"{page}_tw.html"
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        results[fname] = "SKIP"
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html

    # ── 수정 1: 네비게이션 텍스트 (href 포함 targeted replace) ──
    html = html.replace(
        'href="ortho_tw.html">ORTHODONTICS</a>',
        'href="ortho_tw.html">牙齒矯正</a>'
    )
    html = html.replace(
        'href="prosthetics_tw.html">PROSTHETICS</a>',
        'href="prosthetics_tw.html">牙齒修復</a>'
    )

    # ── 수정 2: 드롭다운 버튼 개선 (type="button" + closest) ──
    html = html.replace(
        '<button class="lang-current" onclick="document.getElementById(\'langSelector\').classList.toggle(\'open\')">TW</button>',
        '<button type="button" class="lang-current" onclick="this.closest(\'.lang-selector\').classList.toggle(\'open\')">TW</button>'
    )

    # ── 수정 4: LINE 링크 삽입 ──
    # 1) line-btn
    html = re.sub(
        r'<a href="#" class="line-btn"',
        f'<a href="{TW_LINE}" class="line-btn"',
        html
    )
    # 2) btn-reserve
    html = re.sub(
        r'<a href="#" class="btn-reserve">',
        f'<a href="{TW_LINE}" class="btn-reserve">',
        html
    )
    # 3) sv-float-btn--line
    html = re.sub(
        r'<a href="#" class="sv-float-btn sv-float-btn--line"',
        f'<a href="{TW_LINE}" class="sv-float-btn sv-float-btn--line"',
        html
    )

    # ── 수정 5: 인스타그램 링크 ──
    html = html.replace(
        'href="https://www.instagram.com/smileview_dental/" class="sv-float-btn sv-float-btn--instagram"',
        f'href="{TW_INSTA}" class="sv-float-btn sv-float-btn--instagram"'
    )

    # ── 수정 3 & 6: prosthetics_tw.html 전용 ──
    if page == 'prosthetics':
        # 수정 3: 배너 이미지 제거 (lm-wide-banner 내부 img만)
        html = re.sub(
            r'(<div class="lm-wide-banner">\s*)<img[^>]*e66ac7_f564524f8ac44818932c2faeb73cf5a6~mv2\.avif[^>]*>(\s*</div>)',
            r'\1\2',
            html,
            count=1
        )

        # 수정 6: 이미지 경로 수정 (TW 번역 파일명 → 한국어 원본 파일명)
        html = html.replace(
            'images/prosthodontics/탭(11)_A_蛀牙治療.avif',
            'images/prosthodontics/탭(11)_A_충치치료.avif'
        )
        html = html.replace(
            'images/prosthodontics/탭(11)_B_根管治療.avif',
            'images/prosthodontics/탭(11)_B_신경치료.avif'
        )
        html = html.replace(
            'images/prosthodontics/탭(11)_D_牙周治療.avif',
            'images/prosthodontics/탭(11)_D_잇몸치료.avif'
        )

    if html != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        results[fname] = "OK"
    else:
        results[fname] = "UNCHANGED"

print("=== TW 수정 결과 ===")
for fname, r in results.items():
    print(f"  {r}  {fname}")
print("완료.")
