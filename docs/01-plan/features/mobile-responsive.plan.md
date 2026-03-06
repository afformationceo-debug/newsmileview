# Plan: Mobile Responsive Optimization

> SMILEVIEW 전체 페이지 모바일 반응형 최적화

## 1. Overview

| 항목 | 내용 |
|------|------|
| Feature | mobile-responsive |
| 목표 | PC 전용으로 제작된 전체 22개 페이지를 모바일/태블릿에서도 최적화된 UX로 제공 |
| 대상 페이지 | 메인(index.html) + 서브페이지 17개 |
| Breakpoints | 1024px (태블릿), 768px (모바일), 480px (소형 모바일) |
| 현재 커버리지 | 약 60% (Footer/Review/B&A만 양호, 나머지 미흡) |
| 목표 커버리지 | 95%+ 모든 섹션 모바일 최적화 |

## 2. Current State Analysis (현황 분석)

### 2.1 페이지 목록 (22개)

**메인 페이지:**
- `index.html` - 메인 홈페이지 (Hero, Philosophy, B&A, Solutions, Shorts, TV, Indoor, Reviews, Footer)

**서브 페이지 (11개):**
- `introduction.html` - 병원소개
- `invisalign.html` - 인비절라인
- `whitening.html` - 치아미백
- `laminate.html` - 라미네이트
- `ortho.html` - 치아교정
- `implant.html` - 수면 임플란트
- `prosthetics.html` - 보철치료
- `treatment.html` - 진료안내
- `brand.html` - 브랜드
- `staff.html` - 의료진
- `location_guide.html` - 오시는길

**소스 페이지 (10개):**
- `source_invisalign.html`
- `source_whitening.html`
- `source_laminate.html`
- `source_implant.html`
- `source_prosthetics.html`
- `source_ortho_conventional.html`
- `source_ortho_lingual.html`
- `source_ortho_nonsurgical.html`
- `source_ortho_partial.html`
- `source_ortho_surgeryfirst.html`

### 2.2 CSS 구조

| 파일 | 라인 수 | 역할 |
|------|---------|------|
| `css/style.css` | 3,739줄 | 메인 스타일시트 (모든 페이지 공유) |
| `css/animations.css` | 58줄 | 애니메이션 유틸리티 |
| 각 페이지 inline `<style>` | 200~400줄 | 페이지별 고유 스타일 |

### 2.3 기존 반응형 커버리지

| 섹션 | Desktop | Tablet (1024px) | Mobile (768px) | 상태 |
|------|---------|-----------------|----------------|------|
| Header/Nav | Good | Good | Partial | 모바일 메뉴 동작 불확실 |
| Hero | Good | Poor | Poor | 반응형 없음 |
| Philosophy | Good | Fair | Fair | 400vh 높이 미조정 |
| B&A Slider | Good | Good | Fair | 양호 |
| **SOLUTIONS** | Good | Good | **NONE** | 수평 스크롤 모바일 미대응 |
| **SHORTS** | Good | Fair | **NONE** | 타이틀 4rem, 카드 사이징 없음 |
| **TV (YouTube)** | Good | Fair | **NONE** | 타이틀 4rem, 모바일 규칙 없음 |
| Indoor | Good | Fair | Minimal | 높이 고정, 패딩 미조정 |
| Reviews | Good | Good | Good | 양호 |
| Footer | Good | Good | Good | 양호 |
| **서브페이지 공통** | Good | Partial | **POOR** | 960px 고정 너비 패널, overflow |

## 3. Implementation Strategy (구현 전략)

### 3.1 Phase 순서 (우선순위 기반)

```
Phase 1: 공통 기반 (Header, Footer, 공유 컴포넌트)
    ↓
Phase 2: 메인 홈페이지 (index.html - 9개 섹션)
    ↓
Phase 3: 주요 서브페이지 (invisalign, laminate, ortho 등 7개)
    ↓
Phase 4: 나머지 서브페이지 (소개, 의료진, 오시는길 등)
    ↓
Phase 5: Source 페이지 (10개 - 공통 패턴 적용)
    ↓
Phase 6: 크로스 디바이스 테스트 & 미세 조정
```

### 3.2 Phase 1: 공통 기반 (영향 범위: 전체 22개 페이지)

**목표:** 모든 페이지에 공통 적용되는 반응형 기반 구축

| # | 작업 | 파일 | 상세 |
|---|------|------|------|
| 1-1 | viewport meta 확인 | 모든 HTML | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| 1-2 | 모바일 햄버거 메뉴 완성 | style.css, main.js | 1024px 이하에서 메뉴 토글 동작 구현 |
| 1-3 | 공통 breakpoint 변수화 | style.css | CSS custom property 기반 breakpoint 관리 |
| 1-4 | 기본 타이포그래피 스케일링 | style.css | `clamp()` 활용 유동 폰트 크기 |
| 1-5 | 컨테이너 패딩 조정 | style.css | `40px → 20px → 16px` 단계적 축소 |
| 1-6 | 플로팅 SNS 버튼 모바일 최적화 | style.css | 크기/위치 조정 |

### 3.3 Phase 2: 메인 홈페이지 (index.html)

**목표:** 9개 섹션 모두 모바일 최적화

| # | 섹션 | 핵심 변경 | 난이도 |
|---|------|-----------|--------|
| 2-1 | Hero | 높이 150vh→100vh, 폰트 스케일링, 스크롤 인디케이터 조정 | 중 |
| 2-2 | Philosophy | 400vh→200vh, 3-col→1-col, 폰트 축소, 이미지 비율 조정 | 상 |
| 2-3 | B&A Slider | 기존 768px 보완, 탭 버튼 wrap, 네비게이션 터치 최적화 | 하 |
| 2-4 | **SOLUTIONS** | **수평→수직 전환**, 카드 100% 너비, 타이틀 축소, JS 분기 | **상** |
| 2-5 | **SHORTS** | 카드 200px 축소, 타이틀 2.5rem, 네비 버튼 크기 조정 | 중 |
| 2-6 | **TV (YouTube)** | 3열→1열, 타이틀 2.5rem, 슬라이더→스와이프, 버튼 조정 | 중 |
| 2-7 | Indoor | 아이템 250px→200px, 패딩 조정, 커서 비활성화(터치) | 중 |
| 2-8 | Reviews | 기존 양호 - 미세 조정만 | 하 |
| 2-9 | Footer | 기존 양호 - 확인만 | 하 |

**SOLUTIONS 섹션 모바일 전환 전략:**
```
Desktop (1025px+): 수평 스크롤 (현재 동작 유지)
Tablet (769~1024px): 수평 스크롤 유지, 카드 크기 축소
Mobile (≤768px): 수직 스택 레이아웃으로 전환
  - height: 400vh → auto
  - horizontal-track: flex-direction: column
  - h-item: width: 100%, margin: 0 0 40px 0
  - JS: 수평 스크롤 로직 비활성화 (window.innerWidth > 1024 조건 이미 존재)
```

### 3.4 Phase 3: 주요 서브페이지 (7개)

| 페이지 | 핵심 이슈 | 작업 내용 |
|--------|-----------|-----------|
| invisalign.html | 고정 너비 패널, 인라인 스타일 | 반응형 그리드, 폰트 스케일링 |
| laminate.html | 960px 패널, 수평 스크롤 | 모바일 수직 전환 |
| ortho.html | 복잡한 레이아웃 | 그리드→단일 컬럼 |
| whitening.html | 고정 너비 | 유동 너비 전환 |
| implant.html | 고정 너비 | 유동 너비 전환 |
| prosthetics.html | 고정 너비 | 유동 너비 전환 |
| treatment.html | 레이아웃 | 모바일 적응 |

**공통 패턴:**
- `--lm-max-w: 1200px` → `max-width: 100%` at 768px
- `padding: 0 50px` → `padding: 0 20px` at 768px
- 수평 스크롤 패널 `960px` → `100vw` at 768px

### 3.5 Phase 4: 나머지 서브페이지 (4개)

| 페이지 | 작업 |
|--------|------|
| introduction.html | 인라인 반응형 보완 (이미 부분 구현) |
| staff.html | 의료진 카드 그리드 조정 |
| brand.html | 브랜드 섹션 레이아웃 |
| location_guide.html | 지도 높이 축소 (600px→350px), 정보 레이아웃 |

### 3.6 Phase 5: Source 페이지 (10개)

- 공통 템플릿 기반으로 일괄 반응형 적용
- 인라인 스타일 패턴이 유사하므로 한 번에 처리 가능

### 3.7 Phase 6: 크로스 디바이스 테스트

| 디바이스 | 해상도 | 테스트 항목 |
|----------|--------|-------------|
| iPhone SE | 375x667 | 최소 너비 레이아웃 |
| iPhone 14 | 390x844 | 표준 모바일 |
| iPad | 768x1024 | 태블릿 세로 |
| iPad 가로 | 1024x768 | 태블릿 가로 |
| Galaxy S21 | 360x800 | Android 표준 |

## 4. Technical Approach (기술 방침)

### 4.1 CSS 전략

```css
/* Mobile-First 접근은 아닌 Desktop-First (기존 유지) */
/* Breakpoint 체계 */
/* 1024px: 태블릿 */
/* 768px: 모바일 */
/* 480px: 소형 모바일 (필요시) */

/* 유동 폰트 크기 예시 */
.section-title {
    font-size: clamp(2rem, 5vw, 4rem);
}
```

### 4.2 JS 전략

- `window.innerWidth > 1024` 분기는 이미 SOLUTIONS에 존재 → 확장 활용
- 터치 디바이스 감지: `'ontouchstart' in window`
- 모바일에서 커스텀 커서 비활성화
- 모바일에서 수평 스크롤 → 수직 스택 전환

### 4.3 작업 규칙

1. **기존 PC 디자인 절대 변경 금지** - 모바일 전용 @media 규칙만 추가
2. **인라인 스타일 최소화** - style.css에 집중 (특수한 경우만 인라인)
3. **섹션 단위 작업** - 한 섹션씩 완료 후 검증
4. **CDP 모바일 에뮬레이션** - 375px(iPhone), 768px(iPad) 기준 테스트

## 5. Estimated Scope

| Phase | 대상 | 예상 파일 수 | 복잡도 |
|-------|------|-------------|--------|
| Phase 1 | 공통 기반 | 2~3 | 중 |
| Phase 2 | index.html (9개 섹션) | 3 | **상** |
| Phase 3 | 주요 서브 7개 | 7~14 | 상 |
| Phase 4 | 나머지 서브 4개 | 4~8 | 중 |
| Phase 5 | Source 10개 | 10 | 하 (반복) |
| Phase 6 | 테스트 & 조정 | 전체 | 중 |

## 6. Risk & Considerations

| 리스크 | 대응 |
|--------|------|
| 인라인 `!important` 스타일 충돌 | @media 내에서도 `!important` 사용 |
| 수평 스크롤 JS ↔ 수직 스택 CSS 충돌 | `window.innerWidth > 1024` 조건 활용 |
| 서브페이지별 인라인 스타일 파편화 | 공통 패턴 추출 후 일괄 적용 |
| 기존 PC 디자인 regression | 섹션 단위 CDP 검증 |

## 7. Recommended Execution Order

```
추천 실행 순서:
1. Phase 1 → Phase 2 (메인부터 완성)
2. Phase 2 완료 후 CDP 검증
3. Phase 3~5 (서브페이지 일괄)
4. Phase 6 (전체 테스트)

세션별 작업 단위:
- Session 1: Phase 1 + Phase 2 (2-1 ~ 2-4) → 공통 + 메인 상반부
- Session 2: Phase 2 (2-5 ~ 2-9) → 메인 하반부
- Session 3: Phase 3 (서브 7개)
- Session 4: Phase 4 + Phase 5 (나머지 + Source)
- Session 5: Phase 6 (전체 테스트)
```

---

*Created: 2026-03-05*
*Feature: mobile-responsive*
*PDCA Phase: Plan*
