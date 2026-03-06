# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"
PAGES = ['index','introduction','invisalign','whitening','ortho','laminate','implant','prosthetics']

issues = []
ok_count = 0

def check(fname, condition, desc):
    if not condition:
        issues.append(f"  FAIL  {fname}: {desc}")
    else:
        global ok_count
        ok_count += 1

for page in PAGES:
    # ── TW 검증 ──
    fname = f"{page}_tw.html"
    fpath = os.path.join(BASE, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        # 수정 1: 네비 텍스트
        check(fname, 'href="ortho_tw.html">牙齒矯正</a>' in html, '수정1: ORTHODONTICS→牙齒矯正')
        check(fname, 'href="prosthetics_tw.html">牙齒修復</a>' in html, '수정1: PROSTHETICS→牙齒修復')
        check(fname, 'href="ortho_tw.html">ORTHODONTICS</a>' not in html, '수정1: 구 ORTHODONTICS 남아있음')
        check(fname, 'href="prosthetics_tw.html">PROSTHETICS</a>' not in html, '수정1: 구 PROSTHETICS 남아있음')

        # 수정 2: 드롭다운
        check(fname, 'type="button" class="lang-current"' in html, '수정2: type=button 없음')
        check(fname, "this.closest('.lang-selector')" in html, '수정2: closest 방식 없음')

        # 수정 4: LINE 링크
        check(fname, 'href="https://lin.ee/lHEp9er" class="line-btn"' in html, '수정4: line-btn href')
        check(fname, 'href="https://lin.ee/lHEp9er" class="btn-reserve"' in html, '수정4: btn-reserve href')
        check(fname, 'href="https://lin.ee/lHEp9er" class="sv-float-btn sv-float-btn--line"' in html, '수정4: float-line href')

        # 수정 5: 인스타그램
        check(fname, 'href="https://www.instagram.com/smileview_tw/"' in html, '수정5: instagram TW href')

        # 수정 3 & 6: prosthetics만
        if page == 'prosthetics':
            # 수정 3: 배너 제거 (lm-wide-banner 내 img 태그 없어야 함)
            m = re.search(r'<div class="lm-wide-banner">(.*?)</div>', html, re.DOTALL)
            if m:
                check(fname, 'e66ac7_f564524f8ac44818932c2faeb73cf5a6~mv2.avif' not in m.group(1), '수정3: 배너 이미지 아직 존재')
            else:
                check(fname, False, '수정3: lm-wide-banner div 없음')

            # 수정 6: 이미지 경로
            check(fname, 'images/prosthodontics/탭(11)_A_충치치료.avif' in html, '수정6: 충치치료 이미지 경로')
            check(fname, 'images/prosthodontics/탭(11)_B_신경치료.avif' in html, '수정6: 신경치료 이미지 경로')
            check(fname, 'images/prosthodontics/탭(11)_D_잇몸치료.avif' in html, '수정6: 잇몸치료 이미지 경로')
            check(fname, '탭(11)_A_蛀牙治療' not in html, '수정6: 구 TW 이미지명 남아있음')

    # ── JP 검증 ──
    fname = f"{page}_jp.html"
    fpath = os.path.join(BASE, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        # 수정 1: 네비 텍스트
        check(fname, 'href="invisalign_jp.html">インビザライン</a>' in html, '수정1: INVISALIGN→インビザライン')
        check(fname, 'href="invisalign_jp.html">INVISALIGN</a>' not in html, '수정1: 구 INVISALIGN 남아있음')

        # 수정 2: 드롭다운
        check(fname, 'type="button" class="lang-current"' in html, '수정2: type=button 없음')
        check(fname, "this.closest('.lang-selector')" in html, '수정2: closest 방식 없음')

        # 수정 4: LINE 링크
        check(fname, 'href="https://lin.ee/C0rBsdX" class="line-btn"' in html, '수정4: line-btn href')
        check(fname, 'href="https://lin.ee/C0rBsdX" class="btn-reserve"' in html, '수정4: btn-reserve href')
        check(fname, 'href="https://lin.ee/C0rBsdX" class="sv-float-btn sv-float-btn--line"' in html, '수정4: float-line href')

        # 수정 5: 인스타그램
        check(fname, 'href="https://www.instagram.com/smileview.dental/"' in html, '수정5: instagram JP href')

        # 수정 3 & 6: prosthetics만
        if page == 'prosthetics':
            m = re.search(r'<div class="lm-wide-banner">(.*?)</div>', html, re.DOTALL)
            if m:
                check(fname, 'e66ac7_f564524f8ac44818932c2faeb73cf5a6~mv2.avif' not in m.group(1), '수정3: 배너 이미지 아직 존재')
            else:
                check(fname, False, '수정3: lm-wide-banner div 없음')

            check(fname, 'images/prosthodontics/탭(11)_A_충치치료.avif' in html, '수정6: 충치치료 이미지 경로')
            check(fname, 'images/prosthodontics/탭(11)_B_신경치료.avif' in html, '수정6: 신경치료 이미지 경로')
            check(fname, 'images/prosthodontics/탭(11)_D_잇몸치료.avif' in html, '수정6: 잇몸치료 이미지 경로')
            check(fname, '탭(11)_A_むし歯治療' not in html, '수정6: 구 JP 이미지명 남아있음')

print(f"총 {ok_count + len(issues)}개 검사 중 {ok_count}개 통과, {len(issues)}개 실패")
if issues:
    print("\n실패 항목:")
    for i in issues:
        print(i)
else:
    print("모든 수정 검증 완료!")
