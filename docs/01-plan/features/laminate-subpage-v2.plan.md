# Plan: Laminate Subpage V2 Modifications

## Feature Name
laminate-subpage-v2

## Overview
laminate.html 서브페이지 8가지 섹션 수정. whitening.html 디자인 패턴을 벤치마크하여 배너 이미지, B&A 캐러셀, Feature 카드 확장 등 주요 UI 개선.

## Requirements

### Mod 1: One-Day Laminate 배경 섹션 수정
- **대상**: Title Band 섹션 (`.lm-title-band`, 패널 2)
- **변경**: 배경 이미지를 `images/laminate/unnamed.jpg` (치과 시술 클로즈업)으로 교체
- **파일**: `images/laminate/unnamed.jpg` (이미 존재)
- **기존 이미지**: `images/migrated/laminate/laminate_4.jpg` -> 교체

### Mod 2: 원데이 라미네이트란? 섹션 텍스트 수정
- **대상**: Definition 섹션 (`.lm-definition`, 패널 3)
- **변경 1**: 제목에서 "E MAX" 텍스트 제거 -> `원데이 라미네이트란?` (기존: `E MAX 원데이 라미네이트란?`)
- **변경 2**: 종류 텍스트 수정 -> `무삭제 라미네이트, E MAX 라미네이트, 원데이 라미네이트 등`
  - 기존: `E MAX 라미네이트, 포셀린 라미네이트, 레진 라미네이트, 무삭제 라미네이트, 미니 라미네이트, 풀 라미네이트 등`

### Mod 3: VS Comparison 섹션 개선
- **대상**: VS Comparison 섹션 (`.lm-vs`)
- **삭제 항목**: 강도, 변색 저항성, 생체 적합성 (양쪽 모두)
- **유지 항목**: 소재, 투명도, 삭제량, 제작 방식, 유지기간 (총 5개)
- **UI 개선**: 한눈에 볼 수 있게 디자인 개선
  - 좌우 카드 상단에 이미지 삽입 영역 추가
  - 일반 라미네이트 이미지: `images/migrated/benchmark/laminate/비포1.jpg`
  - E MAX 라미네이트 이미지: `images/migrated/benchmark/laminate/애프터1.jpg`
  - 비교 항목을 가로 2열 그리드 형태로 간결하게 재배치

### Mod 4: Feature 섹션 확장 (3개 -> 5개)
- **대상**: Feature Steps 섹션 (`.lm-feature-steps`)
- **변경**: 기존 3개 카드 -> 5개 카드로 확장
- **카드 내용**:
  1. **최소 삭제 스마일라미네이트** - 세부 내용 2줄 추가
  2. **정식 기공소 보유** - 세부 내용 2줄 추가
  3. **뛰어난 접착 기술** - 세부 내용 2줄 추가
  4. **즉시 일상생활 가능** - 세부 내용 2줄 추가
  5. **이보클라비바덴트사의 E-max Press2 사용** - 세부 내용 2줄 추가
- **이미지**: 임시 이미지(placeholder) 설정
- **레이아웃**: 3열 그리드 유지, 하단 2개는 중앙 정렬 또는 2열 배치

### Mod 5: Process 섹션 재설계
- **대상**: Process 섹션 (`.lm-process`)
- **변경 1**: whitening 페이지의 `lm-info-hero` 배너 이미지 패턴 적용
  - 라미네이트 전용 문구: "전문 라미네이트, 디테일이 다릅니다" (또는 적절한 문구)
  - `unnamed.jpg` 또는 기존 laminate 이미지 활용
  - whitening과 동일한 CSS (`.lm-info-hero` 스타일)
  - 하단 gradient overlay + 텍스트 오버레이
- **변경 2**: 기존 process summary 카드 유지 + sticky scroll 디테일 카드 1~4번 유지
  - 기존 구현이 이미 sticky scroll 형태이므로 유지

### Mod 6: Why Laminate? 섹션
- **대상**: Why Laminate 섹션 (`.lm-why`)
- **변경**: 기존 디자인 컬러색상에 맞춰 진행 (현재 cream 배경 유지)
- **검토**: 현재 상태 양호하면 변경 없음

### Mod 7: 추천 섹션
- **대상**: Recommendation 섹션 (`.lm-recommend`)
- **변경**: 기존 디자인과 동일하게 진행 (현재 상태 유지)
- **검토**: 현재 상태 양호하면 변경 없음

### Mod 8: 라미네이트 시술 전후 비교 (B&A) 섹션 신규 추가
- **위치**: Recommendation 섹션 이후 (Clinic 섹션 이전)
- **벤치마크**: whitening.html의 B&A 캐러셀 디자인
- **차이점**:
  - 화면에 이미지 1개만 표시 (whitening은 4-up)
  - 이미지 크기는 1개가 화면에 적절하게 보이는 크기
- **이미지 소스**:
  - `images/migrated/benchmark/laminate/비포1.jpg` + `애프터1.jpg`
  - `images/migrated/benchmark/laminate/비포2.jpg` + `애프터2.jpg`
  - 4장의 B&A 이미지 (Before/After 2세트)
- **기능**:
  - 화살표 네비게이션 (좌/우)
  - 카운터 (01 / 04)
  - 자동 슬라이드 (3초)
  - 터치 스와이프 지원
  - 다크 배경 (#252017)

## Target Files

| File | Changes |
|------|---------|
| `laminate.html` | CSS + HTML + JS 수정 |

## Available Images

| Image | Purpose |
|-------|---------|
| `images/laminate/unnamed.jpg` | Mod 1: Title Band 배경, Mod 5: Process 배너 |
| `images/laminate/unnamed (1).jpg` | Hero 배경 (기존 유지) |
| `images/migrated/benchmark/laminate/비포1.jpg` | Mod 3: VS 일반 라미네이트 이미지, Mod 8: B&A |
| `images/migrated/benchmark/laminate/애프터1.jpg` | Mod 3: VS E MAX 이미지, Mod 8: B&A |
| `images/migrated/benchmark/laminate/비포2.jpg` | Mod 8: B&A |
| `images/migrated/benchmark/laminate/애프터2.jpg` | Mod 8: B&A |
| `images/migrated/laminate/laminate_2~9` | Feature/Process 기존 이미지 |

## Implementation Order

1. **Phase A** (텍스트/삭제 수정): Mod 1 + Mod 2 + Mod 3 삭제항목
2. **Phase B** (UI 재설계): Mod 3 UI개선 + Mod 4 Feature 확장
3. **Phase C** (배너 + Process): Mod 5 배너 이미지 + Process
4. **Phase D** (B&A 신규): Mod 8 B&A 캐러셀 추가
5. **Phase E** (검증): Mod 6 + Mod 7 검토 + 전체 반응형 확인

## Risks
- B&A 이미지(비포/애프터)가 블러 처리된 상태 -> 실제 클리닉 사진으로 교체 필요할 수 있음
- Feature 5개 카드의 세부 내용은 적절한 치과 관련 텍스트로 작성 필요
- VS 섹션 이미지 삽입 시 다크 배경과의 조화 확인 필요
