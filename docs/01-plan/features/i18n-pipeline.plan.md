# Plan: i18n-pipeline (다국어 번역 자동화 파이프라인)

## 1. Overview

| 항목 | 내용 |
|------|------|
| Feature | i18n-pipeline |
| 목표 | SMILEVIEW 치과 웹사이트 8개 페이지를 대만 번체(zh-TW) + 일본어(ja)로 자동 번역 |
| 대상 프로젝트 | `/c/Users/rlcks/OneDrive/Desktop/SMILEVIEW/` |
| 생성 파일 수 | 16개 (TW 8개 + JP 8개) |
| 원본 파일 보호 | 언어팩 링크 추가 외 수정 절대 금지 |

## 2. 대상 파일

| 파일 | 페이지명 | TW 출력 | JP 출력 |
|------|----------|---------|---------|
| index.html | 메인 | index_tw.html | index_jp.html |
| invisalign.html | 인비절라인 | invisalign_tw.html | invisalign_jp.html |
| ortho.html | 치아교정 | ortho_tw.html | ortho_jp.html |
| laminate.html | 라미네이트 | laminate_tw.html | laminate_jp.html |
| whitening.html | 치아미백 | whitening_tw.html | whitening_jp.html |
| implant.html | 임플란트 | implant_tw.html | implant_jp.html |
| prosthetics.html | 보철치료 | prosthetics_tw.html | prosthetics_jp.html |
| introduction.html | 병원소개 | introduction_tw.html | introduction_jp.html |

## 3. 작업 단계 (STEP 1~7)

### STEP 1: 백업
- 모든 HTML/CSS/JS 파일 → `backup/` 폴더 전체 복사
- 백업 완료 확인 후 진행

### STEP 2: 텍스트 추출 (`extract_texts.py`)
- 8개 HTML 파일에서 한국어 텍스트 자동 추출
- 추출 범위: innerText, alt/placeholder/title/aria-label 속성, CSS content, JS 문자열, data-* 속성, SVG 텍스트, 메타태그
- 결과: `translations/ko/{page}.json` (고유 키 + 위치 정보 포함)

### STEP 3: 번역 JSON 생성 (병렬 16개)
- 팀 A (zh-TW): A-1~A-8 에이전트 → `translations/tw/{page}.json`
- 팀 B (ja): B-1~B-8 에이전트 → `translations/jp/{page}.json`

**번역 규칙:**
- 스마일뷰 → SMILEVIEW / 스마일뷰치과 → TW: SMILEVIEW牙醫診所 / JP: SMILEVIEWデンタルクリニック
- 김한결 → TW: 金韓結 / JP: キム・ハンギョル
- 이소연 → TW: 李昭妍 / JP: イ・ソヨン
- 주소, 라벨 번역 규칙 적용
- 영문 타이틀 유지 (INVISALIGN, ORTHODONTICS 등)
- URL/링크/이메일 유지

### STEP 4: 번역 페이지 자동 생성 (`generate_pages.py`)
- 원본 HTML 복사 + 번역 JSON 기반 텍스트 치환
- 내부 링크 자동 치환 (`.html` → `_tw.html` / `_jp.html`)
- `<html lang>` 변경 (zh-TW / ja)
- CSS/JS 경로 공유 (복사 없음)

### STEP 5: 번역 누락 검증 + 자동 수정 (`verify_translations.py`)
- 3라운드 검증:
  - Round 1: 한국어 잔존 문자(가-힣, ㄱ-ㅎ, ㅏ-ㅣ) 전수 검출
  - Round 2: 미번역 자동 수정 → 재검증 (0건 될 때까지 반복)
  - Round 3: 최종 확인 + 인코딩 + 깨진 문자 + CDP 렌더링

### STEP 6: 언어팩 드롭다운 링크 연결
- 24개 파일(KO 8 + TW 8 + JP 8) 언어 드롭다운 업데이트
- 현재 언어 active 표시
- KO ↔ TW ↔ JP 상호 링크

### STEP 7: 최종 점검 리포트
1. 생성 파일 목록 (16개)
2. 페이지별 번역 텍스트 수
3. 한국어 잔존 수 (반드시 0)
4. 인코딩 검증
5. 언어팩 링크 상태 (24개)
6. CDP 렌더링 결과
7. 이미지 내 한국어 텍스트 목록
8. 수동 확인 필요 항목

## 4. 팀 구성 (Agent Teams)

```
팀 A (대만 번체 총괄)          팀 B (일본어 총괄)
├── A-1: index               ├── B-1: index
├── A-2: invisalign          ├── B-2: invisalign
├── A-3: ortho               ├── B-3: ortho
├── A-4: laminate            ├── B-4: laminate
├── A-5: whitening           ├── B-5: whitening
├── A-6: implant             ├── B-6: implant
├── A-7: prosthetics         ├── B-7: prosthetics
└── A-8: introduction        └── B-8: introduction
```

총 16개 작업 동시 병렬 진행

## 5. 제약 사항

| 제약 | 내용 |
|------|------|
| 원본 보호 | 한국어 파일 내용 수정 금지 (언어팩 링크만 허용) |
| 백업 필수 | 모든 작업 전 backup/ 폴더 생성 |
| 인코딩 | 모든 파일 UTF-8 |
| 한국어 잔존 | 번역 페이지에 가-힣 0건 |
| 스크립트 방식 | Python 스크립트 사용, cat >> EOF 금지 |
| 이미지 | 수정 불가 - 리포트에 목록만 정리 |
| CSS/JS | 원본 공유, 복사 금지 |

## 6. 성공 기준

- [ ] 16개 번역 페이지 생성 완료
- [ ] 모든 번역 페이지 한국어 잔존 0건
- [ ] 24개 파일 언어팩 링크 정상 연결
- [ ] CDP 렌더링 이상 없음
- [ ] 인코딩 UTF-8 확인
- [ ] 최종 점검 리포트 생성

## 7. 기술 스택

- Python 3 (BeautifulSoup4, json, re)
- Claude Agent Teams (팀 A/B 병렬)
- CDP (Chrome DevTools Protocol) - 렌더링 검증
