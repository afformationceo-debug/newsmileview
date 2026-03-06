# Plan: 보철 치료 서브페이지 → 임플란트 콘텐츠 전환 수정

## Feature Name
prosthetics-implant-redesign

## Overview
prosthetics.html 서브페이지의 현재 디자인(섹션 구조, 애니메이션, 레이아웃)을 유지하면서 콘텐츠를 임플란트(수면 임플란트) 내용으로 전면 교체. 기존 implant.html 콘텐츠 + 스마일뷰치과 참조 콘텐츠를 활용하여 트렌디하고 완성도 높은 임플란트 페이지로 재구성.

## 현재 prosthetics.html 섹션 구조 분석

| # | 섹션 | 클래스 | 현재 내용 | 애니메이션 |
|---|------|--------|-----------|-----------|
| 1 | Hero | `.lm-h-panel` | "DENTAL PROSTHETICS" | GSAP horizontal scroll, scale zoom, slide-in |
| 2 | Title Band | `.lm-h-panel--title` | "Dental Prosthetics" / "보철치료" | Marquee, overlay zoom |
| 3 | Definition | `.lm-h-panel--def` | "보철치료란?" + 설명 | Rotating scroll circle, stagger fade |
| 4 | Speciality | `.lm-speciality` | 4카드 (정밀 설계/심미성/내구성/착용감) | IntersectionObserver fade |
| 5 | Feature | `.lm-feature` | 6카드 (크라운/인레이/브릿지/틀니) | Staggered fade |
| 6 | Procedure Info | `.lm-info-section` | 4카드 (시술시간/마취/내원/유지) | Staggered fade |
| 7 | Recommendation | `.lm-recommend` | 이미지 + 체크리스트 5항목 | fade-in |
| 8 | Process | `.lm-process` | 4단계 타임라인 | Staggered fade |
| 9 | FAQ | `.lm-faq-section` | 4개 아코디언 | fade + JS toggle |

## 섹션별 수정 계획

### Mod 1: Hero 섹션 (Panel 1)
- **현재**: "DENTAL" / "PROSTHETICS" + 보철 설명
- **변경**:
  - 타이틀: "SLEEP" / "IMPLANT"
  - 설명 텍스트: 수면 임플란트 핵심 소개
    - "잠자는 사이, 편안하게 완성되는 임플란트"
    - "통증 걱정 없이 전문 수면마취 하에 진행되는 안전한 임플란트 시술"
  - 배경 이미지: `images/migrated/implant/implant_4.jpg` (기존 implant.html 동일)
- **디자인 유지**: GSAP horizontal scroll, scale zoom, slide-in 애니메이션 100% 유지

### Mod 2: Title Band 섹션 (Panel 2)
- **현재**: "Dental Prosthetics" / "보철치료" / SMILEVIEW SIGNATURE 배지
- **변경**:
  - 타이틀: "Sleep\nImplant"
  - 서브타이틀: "수면 임플란트"
  - 배지: "SMILEVIEW SIGNATURE" (유지)
  - Marquee: "SMILEVIEW・IMPLANT" 반복
  - 배경 이미지: `images/migrated/implant/implant_9.jpg`
- **디자인 유지**: Marquee 애니메이션, dark overlay, scale 효과 유지

### Mod 3: Definition 섹션 (Panel 3)
- **현재**: "보철치료란?" + 보철 설명 + 치료 종류
- **변경**:
  - 번호: "01"
  - 타이틀: "수면 임플란트란?"
  - 본문: 수면마취(정맥진정) 하에 진행되는 임플란트 시술 설명
  - 종류: "일반 임플란트, 즉시 임플란트, All-on-4, All-on-6, 미니 임플란트 등"
- **콘텐츠 소스**: implant.html Definition 섹션 참조
- **디자인 유지**: Cream 배경, rotating scroll circle, stagger fade

### Mod 4: Speciality 섹션 (4개 카드)
- **현재**: 정밀한 보철 설계 / 자연치아 같은 심미성 / 오래 가는 내구성 / 편안한 착용감
- **변경 (임플란트 특장점)**:
  1. **무통 수면 마취** (effect01) - "정맥진정법을 통한 무통 수면 상태에서 시술, 치과 공포증 환자도 안심"
  2. **첨단 3D 디지털 진단** (effect02) - "CT 촬영과 3D 시뮬레이션으로 정밀한 식립 계획 수립"
  3. **빠른 회복** (effect03) - "최소 절개 시술로 부종·통증 최소화, 일상 복귀 단축"
  4. **높은 성공률** (effect04) - "숙련된 전문의의 풍부한 임상 경험으로 98% 이상 성공률"
- **디자인 개선**: 각 카드에 미니 아이콘/일러스트 추가 고려

### Mod 5: Feature 섹션 (6개 카드 → 임플란트 종류)
- **현재**: 올세라믹 크라운 / 지르코니아 / 골드 / 인레이·온레이 / 브릿지 / 틀니
- **변경 (임플란트 종류별 특징)**:
  1. **01. 일반 임플란트** - 가장 보편적, 3~6개월 치유 기간, 자연치아와 유사한 기능 회복
  2. **02. 즉시 임플란트** - 발치 당일 식립, 치료 기간 단축(2~4개월), 추가 수술 최소화
  3. **03. All-on-4** - 4개 임플란트로 전체 치아 복원, 시술 시간 2~3시간, 당일 임시치아 가능
  4. **04. All-on-6** - 6개 임플란트로 더 강한 지지력, 3~4시간, 골이식 없이 가능한 경우 다수
  5. **05. 미니 임플란트** - 직경 작은 임플란트, 30분~1시간, 틀니 고정용으로 활용
  6. **06. 상악동 거상 임플란트** - 위턱 뼈 부족 시 골이식 병행, 1~2시간, 전문 술식 필요
- **카드 하단**: 시술 시간/기간 표시 + "View more" 링크
- **디자인 개선**: 카드 hover 시 subtle scale + shadow 트랜지션 강화

### Mod 6: Procedure Info 섹션 (4개 정보 카드)
- **현재**: 시술시간 1~2시간 / 국소마취 / 내원 2~3회 / 유지 10~15년
- **변경 (임플란트 시술 정보)**:
  - 시술시간: "약 1~2시간" (유지)
  - 마취방법: "수면마취(정맥진정)" ← 핵심 변경
  - 시술횟수: "2~3회"
  - 회복기간: "2~4개월"
- **아이콘**: 동일 Phosphor Icons 유지 (clock, syringe, arrows-clockwise, calendar-check)

### Mod 7: Recommendation 섹션
- **현재**: 보철치료 추천 대상 5항목
- **변경 (임플란트 추천 대상)**:
  1. 치아 상실로 저작 기능이 저하되신 분
  2. 틀니가 불편하여 고정식 보철을 원하시는 분
  3. 브릿지로 인한 인접 치아 손상이 걱정되시는 분
  4. 심미적으로 자연스러운 치아 복원을 원하시는 분
  5. 치과 공포증이 있어 수면마취 시술을 원하시는 분
- **이미지**: `images/migrated/implant/implant_5.png`
- **디자인 유지**: 2컬럼 레이아웃, 체크 아이콘 리스트

### Mod 8: Process 섹션 (4단계 타임라인)
- **현재**: 보철치료 4단계 (구강검진 → 치아삭제 → 보철물제작 → 장착)
- **변경 (임플란트 시술 과정)**:
  1. **정밀 검사 & CT 촬영** - 구강 상태 종합 진단, 3D CT 촬영으로 뼈 상태 분석, 맞춤 치료 계획 수립
  2. **맞춤 시술 계획 수립** - 디지털 가이드 제작, 식립 위치·각도·깊이 정밀 설계, 환자 상담
  3. **수면 마취 하 임플란트 식립** - 정맥진정 수면마취 후 최소절개 식립, 통증 없는 편안한 시술
  4. **보철물 완성 & 사후관리** - 맞춤 크라운 제작·장착, 정기 검진 프로그램 안내
- **디자인 유지**: vertical timeline, step numbers, connecting lines

### Mod 9: FAQ 섹션 (4개 아코디언)
- **현재**: 보철 관련 4개 질문
- **변경 (임플란트 FAQ)**:
  1. **수면 임플란트는 어떻게 진행되나요?**
     → 정맥진정법을 통해 수면 상태를 유도한 뒤, 환자가 편안하게 잠든 사이 임플란트 시술을 진행합니다. 시술 중 통증이나 불안감이 없으며, 시술 후에도 통증이 크지 않습니다.
  2. **임플란트 수명은 얼마나 되나요?**
     → 적절한 관리 시 반영구적(10~20년 이상) 사용이 가능합니다. 정기적인 검진과 올바른 구강 관리가 수명 연장의 핵심입니다.
  3. **당일 즉시 임플란트는 위험하지 않나요?**
     → 정밀 CT 진단과 디지털 가이드를 통해 안전하게 진행됩니다. 뼈 상태가 충분한 경우에만 시행하며, 풍부한 임상 경험으로 높은 성공률을 유지합니다.
  4. **뼈가 부족해도 임플란트가 가능한가요?**
     → 네, 골이식(GBR)이나 상악동 거상술을 병행하면 대부분 가능합니다. 사전 CT 촬영으로 정확한 진단 후 최적의 방법을 안내해 드립니다.

## 디자인 개선 포인트 (트렌디 요소)

| 개선 항목 | 내용 |
|----------|------|
| Micro Interaction | Feature 카드 hover 시 subtle lift + glow 효과 |
| Typography | 기존 serif/sans-serif 조합 유지, 강조 텍스트 gradient 적용 검토 |
| Color Accent | 임플란트 전문성 강조를 위한 gold + medical blue 포인트 검토 |
| Image Treatment | 섹션별 이미지 오버레이 일관성 확보 |
| Scroll Animation | 기존 GSAP ScrollTrigger 유지, 부드러운 parallax 효과 강화 |

## Target Files

| File | Changes |
|------|---------|
| `prosthetics.html` | HTML 콘텐츠 교체 + CSS 미세 조정 + 이미지 경로 변경 |

## Available Images (임플란트 이미지)

| Image | Purpose |
|-------|---------|
| `images/migrated/implant/implant_4.jpg` | Hero 배경 |
| `images/migrated/implant/implant_9.jpg` | Title Band 배경 |
| `images/migrated/implant/implant_5.png` | Recommendation 섹션 이미지 |
| `images/migrated/implant/implant_1.png` | Speciality 배경 (선택) |
| `images/migrated/benchmark/implant/*` | 추가 참조 이미지 |
| `images/migrated/benchmark/prosthetics/*` | 기존 보철 이미지 (필요시) |

## Implementation Order

1. **Phase A** (텍스트 교체): Mod 1 Hero + Mod 2 Title Band + Mod 3 Definition
2. **Phase B** (카드 콘텐츠): Mod 4 Speciality + Mod 5 Feature 카드 내용 교체
3. **Phase C** (정보 섹션): Mod 6 Procedure Info + Mod 7 Recommendation
4. **Phase D** (프로세스/FAQ): Mod 8 Process + Mod 9 FAQ
5. **Phase E** (디자인 개선): 이미지 교체 + hover 효과 + 반응형 확인

## Risks
- 외부 스마일뷰치과 페이지(smile-vdental.com)가 동적 로딩이라 CDP/WebFetch로 콘텐츠 추출 불가 → 기존 implant.html 콘텐츠 활용
- 임플란트 이미지 일부가 benchmark 폴더에 있어 경로 확인 필요
- 보철→임플란트 전환 시 <title>, meta 태그도 함께 수정 필요
- Feature 카드 6개의 세부 설명 텍스트 보완 필요할 수 있음
