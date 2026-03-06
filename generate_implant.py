#!/usr/bin/env python3
"""Generate redesigned implant.html - data-driven approach"""
import os, shutil

BASE = r'C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW'

def rf(n):
    with open(os.path.join(BASE, n), encoding='utf-8') as f:
        return f.readlines()

def L(a, s, e):
    return ''.join(a[s-1:e])

impl = rf('implant.html')
invis = rf('invisalign.html')

# Backup
bp = os.path.join(BASE, 'implant_backup.html')
if not os.path.exists(bp):
    shutil.copy2(os.path.join(BASE, 'implant.html'), bp)
    print('Backup saved: implant_backup.html')

# ==================== DATA ====================
vs_data = [
    ('치료 기간', '3~6개월', '당일~2개월'),
    ('뼈 보존', '발치 후 잇몸뼈 흡수 발생', '발치 즉시 식립으로 뼈 흡수 최소화'),
    ('시술 횟수', '5~8회 이상 내원', '2~3회 내원으로 완료'),
    ('통증', '잇몸 절개 필요', '최소 절개 + 수면마취로 무통 시술'),
    ('잇몸 라인', '잇몸 위축 가능성', '자연스러운 잇몸 라인 유지'),
    ('심미성', '보철물 장착까지 대기', '당일 임시치아 장착 가능'),
]

feat_data = [
    ('당일 즉시 임플란트', 'images/migrated/implant/wix/implant_type1.png',
     '발치 당일 바로 임플란트를 식립하여 치료 기간을 단축하고 잇몸뼈 흡수를 최소화합니다. 자연스러운 잇몸 라인을 유지하며 빠른 회복이 가능합니다.'),
    ('네비게이션 임플란트', 'images/migrated/implant/wix/implant_type2.png',
     '3D CT 데이터를 기반으로 컴퓨터 네비게이션 시스템이 실시간으로 식립 위치를 안내합니다. 신경과 혈관을 정밀하게 피해 안전하고 정확한 시술이 가능합니다.'),
    ('뼈 이식 임플란트', 'images/migrated/implant/wix/implant_type3.png',
     '잇몸뼈가 부족한 경우 인공 뼈를 이식하여 충분한 골량을 확보한 후 임플란트를 식립합니다. 뼈가 부족해도 안정적인 임플란트가 가능합니다.'),
]

proc_flow = [
    ('images/migrated/implant/implant_6.png', '3차원 영상진단'),
    ('images/migrated/implant/implant_6.png', '3D 모의수술'),
    ('images/migrated/implant/implant_10.jpg', '보조장치/보철 제작'),
    ('images/migrated/implant/implant_7.png', '임플란트 식립'),
]
proc_steps = [
    ('ph-scan', '3차원 영상진단', '3D CT로 골조직·신경 정밀 분석'),
    ('ph-cube', '3D 모의수술', '컴퓨터 시뮬레이션 최적 설계'),
    ('ph-wrench', '보조장치/보철 제작', '맞춤 가이드 및 보철물 제작'),
    ('ph-sparkle', '임플란트 식립', '네비게이션 가이드 정밀 식립'),
]
proc_details = [
    ('images/migrated/implant/implant_6.png', '3차원 영상진단',
     'CT를 통한 3차원 입체영상으로 환자의 골조직, 신경, 혈관을 정밀 분석합니다. 임플란트 식립에 최적의 위치, 방향, 깊이를 정확하게 결정합니다.',
     ['3D CT 정밀 촬영', '골조직 분석', '신경 위치 파악', '최적 식립 위치 결정']),
    ('images/migrated/implant/implant_6.png', '3D 모의수술',
     'CT 데이터를 기반으로 컴퓨터에서 가상 수술을 시행합니다. 최적의 임플란트 위치와 각도를 시뮬레이션하여 수술의 정확도와 안전성을 극대화합니다.',
     ['가상 수술 시뮬레이션', '최적 각도 설계', '위험 요소 사전 파악', '수술 계획 확정']),
    ('images/migrated/implant/implant_10.jpg', '보조장치 및 보철 제작',
     '3D 모의수술 데이터를 바탕으로 수술용 네비게이션 가이드와 맞춤형 보철물을 제작합니다. 환자의 구강 구조에 최적화된 보철로 자연스러운 결과를 보장합니다.',
     ['맞춤 가이드 제작', '보철물 정밀 설계', '디지털 정합 검증', '최종 품질 확인']),
    ('images/migrated/implant/implant_7.png', '임플란트 식립',
     '수면마취 하에 네비게이션 시스템의 실시간 가이드를 따라 정밀하게 임플란트를 식립합니다. 사전 계획대로 정확한 위치에 식립하여 높은 성공률과 빠른 회복을 실현합니다.',
     ['수면마취 시술', '실시간 네비게이션', '정밀 식립 완료', '사후 관리 안내']),
]

why_cards = [
    ('effect01', '오스템 임플란트', '세계 시장점유율 1위 오스템 임플란트를 사용합니다. 38년 이상의 임상 데이터를 바탕으로 검증된 안전성과 높은 성공률을 자랑합니다.'),
    ('effect02', '3D 네비게이션', '컴퓨터 네비게이션 시스템으로 실시간 가이드하여 0.1mm 단위의 정밀한 식립이 가능합니다. 신경 손상 위험을 최소화합니다.'),
    ('effect03', '무통 수면마취', '정맥진정(수면) 마취를 통해 잠든 상태에서 편안하게 시술받으실 수 있습니다. 치과 공포증이 있는 분도 안심하고 치료가 가능합니다.'),
    ('effect04', '빠른 회복', '최소 절개 시술과 첨단 기술로 시술 후 부기와 통증을 최소화합니다. 당일 즉시 임플란트로 치료 횟수와 기간도 크게 단축됩니다.'),
]

rec_data = [
    ('ph-tooth', '치아 상실로 불편하신 분', '충치, 외상, 치주 질환 등으로 치아를 상실하여 저작 기능이 저하되신 분에게 적합합니다.'),
    ('ph-hand-palm', '틀니가 불편하신 분', '틀니의 이물감, 탈락, 통증으로 불편을 겪고 계시는 분에게 고정식 임플란트가 해답입니다.'),
    ('ph-shield-check', '인접 치아를 보존하고 싶은 분', '브릿지 시술 시 필요한 건강한 인접 치아의 삭제 없이 독립적인 치아 복원이 가능합니다.'),
    ('ph-eye', '자연스러운 심미성을 원하시는 분', '자연 치아와 유사한 외관과 기능을 제공하여 심미적으로 자연스러운 결과를 원하시는 분에게 적합합니다.'),
    ('ph-heartbeat', '전신 질환이 있으신 분', '골다공증, 당뇨 등 전신질환이 있어 정밀 진단과 안전한 시술이 필요하신 분도 치료가 가능합니다.'),
    ('ph-smiley-nervous', '치과 공포증이 있으신 분', '수면마취를 통해 잠든 상태에서 편안하게 시술받을 수 있어 치과 공포증이 있으신 분도 안심입니다.'),
]

clinic_data = [
    ('ph-user-focus', '1:1 전담 케어', '상담부터 시술, 사후관리까지 전문의가 1:1로 전담합니다. 환자 개인에게 최적화된 맞춤 치료를 제공합니다.'),
    ('ph-cube', '3D CT 정밀 진단', '최신 3D 컴퓨터 단층촬영으로 골조직, 신경, 혈관을 정밀하게 분석하여 안전한 시술 계획을 수립합니다.'),
    ('ph-certificate', '오스템 공식 파트너', '세계 1위 오스템 임플란트 공식 파트너 의원으로 정품 제품만을 사용하여 높은 성공률을 보장합니다.'),
    ('ph-moon-stars', '수면마취 전문', '전문 마취 모니터링 하에 안전한 수면마취를 진행합니다. 시술 중 불안감 없이 편안하게 치료받으실 수 있습니다.'),
    ('ph-lightning', '당일 즉시 식립', '발치와 동시에 임플란트를 식립하여 치료 기간을 크게 단축합니다. 당일 임시치아 장착도 가능합니다.'),
    ('ph-heart', '평생 관리 시스템', '임플란트 시술 후에도 정기적인 검진과 관리를 통해 오랫동안 건강하게 사용할 수 있도록 합니다.'),
]

faq_data = [
    ('수면 임플란트는 어떻게 진행되나요?', '수면(진정) 마취를 통해 환자가 잠든 상태에서 시술이 진행됩니다. 치과 공포증이 있거나 통증에 민감한 분들에게 적합하며, 전문 마취과 의료진이 시술 내내 환자의 상태를 모니터링합니다.'),
    ('임플란트 수명은 얼마나 되나요?', '적절한 구강 관리와 정기 검진을 받으시면 임플란트는 반영구적으로 사용할 수 있습니다. 일반적으로 10~20년 이상 사용이 가능하며, 관리 상태에 따라 평생 사용하시는 분들도 많습니다.'),
    ('당일 즉시 임플란트는 안전한가요?', '당일 즉시 임플란트는 기존 임플란트와 성공률에서 큰 차이가 없습니다. 환자의 잇몸뼈 상태를 정밀하게 진단한 후 적합한 분에게만 권해드리므로 안심하셔도 됩니다.'),
    ('뼈가 부족해도 임플란트가 가능한가요?', '네, 뼈 이식 임플란트를 통해 가능합니다. 인공 뼈를 이식하여 골량을 보충한 후 안정적으로 임플란트를 식립합니다. 정밀 검사를 통해 최적의 치료 계획을 수립해 드립니다.'),
    ('네비게이션 임플란트의 장점은 무엇인가요?', '네비게이션 임플란트는 3D CT 데이터를 기반으로 실시간 가이드를 제공하여 0.1mm 단위의 정밀한 식립이 가능합니다. 신경과 혈관 손상 위험을 최소화하고, 최소 절개로 빠른 회복을 도와줍니다.'),
    ('임플란트 시술 후 주의사항은 무엇인가요?', '시술 후 2~3일간은 부드러운 음식을 섭취하고, 시술 부위에 자극을 피해주세요. 처방된 약을 복용하고, 정기적인 검진을 받으시면 빠른 회복과 장기적인 유지가 가능합니다.'),
    ('오스템 임플란트를 사용하는 이유는?', '오스템 임플란트는 세계 시장점유율 1위의 글로벌 브랜드로, 38년 이상의 임상 데이터와 높은 골유착 성공률을 자랑합니다. 스마일뷰치과는 오스템 공식 파트너로 정품만을 사용합니다.'),
    ('임플란트 비용은 어떻게 되나요?', '임플란트 비용은 시술 부위, 종류, 추가 시술(뼈이식 등) 여부에 따라 달라집니다. 정확한 비용은 정밀 검진 후 상담을 통해 안내해 드립니다. 스마일뷰치과는 합리적인 가격과 무이자 할부를 제공합니다.'),
]

# ==================== GENERATORS ====================
def gen_vs():
    rows = '\n'.join(f'                            <tr class="lm-vs-row"><td>{n}</td><td class="lm-vs-td-label">{l}</td><td class="lm-vs-td-highlight">{h}</td></tr>' for l,n,h in vs_data)
    cards = '\n'.join(f'                    <div class="lm-vs-card lm-vs-row"><div class="lm-vs-card-label">{l}</div><div class="lm-vs-card-row"><div class="lm-vs-card-col lm-vs-card-col--normal"><span class="lm-vs-card-col-tag">일반</span><span class="lm-vs-card-col-text">{n}</span></div><div class="lm-vs-card-col lm-vs-card-col--highlight"><span class="lm-vs-card-col-tag">즉시</span><span class="lm-vs-card-col-text">{h}</span></div></div></div>' for l,n,h in vs_data)
    return f'''
        <!-- ===== VS COMPARISON ===== -->
        <section class="lm-vs-section">
            <div class="lm-inner">
                <div class="lm-vs-header lm-fade">
                    <h2 class="lm-vs-title">당일 즉시 임플란트<br>어떤 점이 다를까?</h2>
                    <p class="lm-vs-subtitle">일반 임플란트 vs 당일 즉시 임플란트</p>
                </div>
                <div class="lm-vs-images lm-fade">
                    <div class="lm-vs-img-col"><img src="images/migrated/implant/implant_5.png" alt="일반 임플란트" loading="lazy"><span class="lm-vs-img-label">일반 임플란트</span></div>
                    <div class="lm-vs-vs-badge">VS</div>
                    <div class="lm-vs-img-col lm-vs-img-col--highlight"><img src="images/migrated/implant/wix/implant_type1.png" alt="당일 즉시 임플란트" loading="lazy"><span class="lm-vs-img-label">당일 즉시 임플란트</span></div>
                </div>
                <div class="lm-vs-table-wrap">
                    <table class="lm-vs-table">
                        <thead><tr><th class="lm-vs-th-normal">일반 임플란트</th><th class="lm-vs-th-label">비교 항목</th><th class="lm-vs-th-highlight"><span class="lm-vs-badge">RECOMMEND</span><br>당일 즉시 임플란트</th></tr></thead>
                        <tbody>
{rows}
                        </tbody>
                    </table>
                </div>
                <div class="lm-vs-mobile">
{cards}
                </div>
            </div>
        </section>
'''

def gen_feature():
    delays = ['', ' lm-fade-delay-1', ' lm-fade-delay-2']
    cards = '\n'.join(f'''                    <div class="lm-feature-card lm-fade{delays[i]}">
                        <div class="lm-feature-card-img"><img src="{img}" alt="{t}"></div>
                        <div class="lm-feature-card-body">
                            <div class="lm-feature-card-num">{i+1:02d}</div>
                            <h3 class="lm-feature-card-title">{t}</h3>
                            <p class="lm-feature-card-desc">{d}</p>
                        </div>
                    </div>''' for i,(t,img,d) in enumerate(feat_data))
    return f'''
        <hr class="lm-feature-divider">
        <section class="lm-feature-section">
            <div class="lm-inner">
                <div class="lm-feature-header lm-fade">
                    <p class="lm-feature-sub">IMPLANT TYPES</p>
                    <h2 class="lm-feature-title">스마일뷰 임플란트 3가지 유형</h2>
                </div>
                <div class="lm-feature-grid">
{cards}
                </div>
            </div>
        </section>
'''

def gen_process():
    flow_items = []
    for i,(img,label) in enumerate(proc_flow):
        flow_items.append(f'                    <div class="lm-process-flow-item"><img src="{img}" alt="{label}"><span class="lm-process-flow-label">{label}</span></div>')
        if i < 3:
            flow_items.append('                    <div class="lm-process-flow-arrow"><i class="ph-bold ph-arrow-right"></i></div>')
    flow = '\n'.join(flow_items)

    steps = '\n'.join(f'''                    <div class="lm-process-step">
                        <div class="lm-process-step-top"><div class="lm-process-step-icon"><i class="ph-bold {ic}"></i></div><span class="lm-process-step-num">{i+1:02d}</span></div>
                        <div class="lm-process-step-title">{t}</div>
                        <div class="lm-process-step-sub">{s}</div>
                    </div>''' for i,(ic,t,s) in enumerate(proc_steps))

    details = ''
    for i,(img,t,d,checks) in enumerate(proc_details):
        ch = ''.join(f'<div class="lm-process-detail-check"><span class="lm-process-detail-check-icon"><i class="ph-bold ph-check"></i></span><span>{c}</span></div>' for c in checks)
        n = f'{i+1:02d}'
        details += f'''
                    <div class="lm-process-detail-wrap">
                        <div class="lm-process-detail">
                            <div class="lm-process-detail-img">
                                <img src="{img}" alt="{t}">
                                <div class="lm-process-detail-img-overlay"></div>
                                <div class="lm-process-detail-num">{n}</div>
                                <div class="lm-process-detail-badge">STEP {n}</div>
                            </div>
                            <div class="lm-process-detail-info">
                                <div class="lm-process-detail-step">STEP {n}</div>
                                <h3>{t}</h3>
                                <p>{d}</p>
                                <div class="lm-process-detail-checks">{ch}</div>
                                <a href="#" class="lm-process-cta">상담 예약하기 &rarr;</a>
                            </div>
                        </div>
                    </div>'''

    return f'''
        <section class="lm-process">
            <div class="lm-inner" style="text-align:center;">
                <span class="lm-section-label lm-fade">PROCESS</span>
                <h2 class="lm-section-h2 lm-fade">네비게이션 임플란트 시술 과정</h2>
                <div class="lm-process-intro lm-fade">
                    <p>3D CT 정밀 진단부터 네비게이션 가이드 식립까지, 스마일뷰치과는 첨단 디지털 시스템으로 안전하고 정확한 임플란트 시술을 완성합니다.</p>
                </div>
            </div>
            <div class="lm-inner">
                <div class="lm-process-flow lm-fade">
{flow}
                </div>
            </div>
            <div class="lm-inner">
                <div class="lm-process-steps lm-fade">
{steps}
                </div>
                <div class="lm-process-details">{details}
                </div>
            </div>
        </section>
'''

def gen_why():
    dl = ['', ' lm-fade-delay-1', ' lm-fade-delay-2', ' lm-fade-delay-3']
    col1 = '\n'.join(f'''                            <div class="lm-spec-card lm-fade{dl[i]}">
                                <div class="lm-spec-badge">{b}</div>
                                <h3>{t}</h3>
                                <p>{d}</p>
                            </div>''' for i,(b,t,d) in enumerate(why_cards) if i%2==0)
    col2 = '\n'.join(f'''                            <div class="lm-spec-card lm-fade{dl[i]}">
                                <div class="lm-spec-badge">{b}</div>
                                <h3>{t}</h3>
                                <p>{d}</p>
                            </div>''' for i,(b,t,d) in enumerate(why_cards) if i%2==1)
    return f'''
        <section class="lm-why">
            <div class="lm-why-bg"></div>
            <div class="lm-inner">
                <h2 class="lm-why-title lm-fade">Why Smileview?</h2>
                <div class="lm-spec-layout">
                    <div class="lm-spec-left lm-fade">
                        <p class="lm-spec-text">
                            세계 1위 <span class="lm-gold">오스템 임플란트</span>와<br>
                            첨단 네비게이션 시스템으로<br>
                            안전한 시술을 약속합니다.
                        </p>
                    </div>
                    <div class="lm-spec-right">
                        <div class="lm-spec-col">
{col1}
                        </div>
                        <div class="lm-spec-col">
{col2}
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

def gen_recommend():
    dl = ['', ' lm-fade-delay-1', ' lm-fade-delay-2', ' lm-fade-delay-1', ' lm-fade-delay-2', ' lm-fade-delay-3']
    cards = '\n'.join(f'''                    <div class="lm-rec-card lm-fade{dl[i]}">
                        <div class="lm-rec-card-icon"><i class="ph {ic}"></i></div>
                        <h3>{t}</h3>
                        <p>{d}</p>
                    </div>''' for i,(ic,t,d) in enumerate(rec_data))
    return f'''
        <section class="lm-recommend">
            <div class="lm-inner">
                <div class="lm-rec-header lm-fade">
                    <span class="lm-rec-label">RECOMMEND</span>
                    <h2 class="lm-rec-title">이런 분들에게<br>임플란트를 추천드립니다</h2>
                </div>
                <div class="lm-rec-cards">
{cards}
                </div>
            </div>
        </section>
'''

def gen_clinic():
    dl = ['', ' lm-fade-delay-1', ' lm-fade-delay-2', ' lm-fade-delay-1', ' lm-fade-delay-2', ' lm-fade-delay-3']
    cards = '\n'.join(f'''                    <div class="lm-clinic-card lm-fade{dl[i]}">
                        <div class="lm-clinic-card-icon"><i class="ph {ic}"></i></div>
                        <h3>{t}</h3>
                        <p>{d}</p>
                    </div>''' for i,(ic,t,d) in enumerate(clinic_data))
    return f'''
        <section class="lm-clinic">
            <div class="lm-inner" style="text-align:center;">
                <span class="lm-section-label lm-fade">OUR CLINIC</span>
                <h2 class="lm-clinic-title lm-fade">Our Smileview</h2>
                <p class="lm-clinic-subtitle lm-fade">스마일뷰가 특별한 이유</p>
            </div>
            <div class="lm-inner">
                <div class="lm-clinic-cards">
{cards}
                </div>
            </div>
        </section>
'''

def gen_faq():
    dl = ['', ' lm-fade-delay-1', ' lm-fade-delay-2', ' lm-fade-delay-3', '', ' lm-fade-delay-1', ' lm-fade-delay-2', ' lm-fade-delay-3']
    items = '\n'.join(f'''                        <div class="lm-faq-item lm-fade{dl[i]}">
                            <button class="lm-faq-q" onclick="toggleFaq(this)"><span class="lm-faq-prefix">Q.</span><span style="flex:1;">{q}</span><i class="ph ph-caret-down"></i></button>
                            <div class="lm-faq-a"><span class="lm-faq-a-prefix">A.</span>{a}</div>
                        </div>''' for i,(q,a) in enumerate(faq_data))
    return f'''
        <section class="lm-faq-section">
            <div class="lm-inner">
                <div class="lm-faq-layout">
                    <div class="lm-faq-left lm-fade">
                        <div class="lm-faq-deco">FAQ</div>
                        <p class="lm-faq-left-text">임플란트 치료에 대해<br>자주 묻는 질문들을<br>확인해 보세요.</p>
                    </div>
                    <div class="lm-faq-list">
{items}
                    </div>
                </div>
            </div>
        </section>
'''

# ==================== ASSEMBLE ====================
o = []

# 1. Head tags (implant lines 1-12)
o.append(L(impl, 1, 12))
o.append('    <style>\n')

# 2. CSS: root vars + base + fade delays (implant lines 14-40) + delay-4
o.append(L(impl, 14, 40))
o.append('    .lm-fade-delay-4 { transition-delay: 0.6s; }\n\n')

# 3. CSS: horizontal scroll -> definition (implant lines 42-236)
o.append(L(impl, 42, 236))

# 4. CSS: Why + Spec + VS + Feature Step (invisalign lines 256-693)
o.append(L(invis, 256, 693))

# 5. CSS: floating quick link + scroll top + footer + section label + info (implant lines 384-472)
o.append(L(impl, 384, 472))
o.append('\n')

# 6. CSS: Recommend + Process + Clinic + FAQ (invisalign lines 695-1217)
o.append(L(invis, 695, 1217))
o.append('\n')

# 7. CSS: responsive (invisalign lines 1258-1362)
o.append(L(invis, 1258, 1362))

# 8. CSS: implant-specific responsive overrides
o.append('''    @media (max-width: 1024px) {
        .lm-hero-lbx span, .lm-hero-rbx span { font-size: 80px; }
        .lm-info-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
        .lm-hero-lbx span, .lm-hero-rbx span { font-size: 60px; }
        .lm-hero-desc { font-size: 15px; }
        .lm-info-grid { grid-template-columns: 1fr 1fr; gap: 12px; }
        .lm-info-card { padding: 24px 16px; }
        .lm-info-section { padding: 80px 0; }
        .lm-quick { right: 20px; bottom: 100px; width: 55px; }
        .lm-quick-toggle { width: 55px; height: 55px; }
    }
''')
o.append('    </style>\n</head>\n')

# 9. HTML: body + header (implant lines 568-598)
o.append(L(impl, 568, 598))

# 10. HTML: main + horizontal scroll (implant lines 600-695)
o.append(L(impl, 600, 695))

# 11. HTML: NEW SECTIONS
o.append(gen_vs())
o.append('\n')
o.append(L(impl, 850, 878))  # Procedure Info
o.append(gen_feature())
o.append(gen_process())
o.append(gen_why())
o.append(gen_recommend())
o.append(gen_clinic())
o.append(gen_faq())
o.append('\n')

# 12. HTML: floating quick link + scroll top (implant lines 1016-1033)
o.append(L(impl, 1016, 1033))
o.append('\n    </main>\n\n')

# 13. HTML: footer (implant lines 1036-1084)
o.append(L(impl, 1036, 1084))

# 14. JS: extract from current file and patch IntersectionObserver selector
js = L(impl, 1086, 1240)
old_sel = "'.lm-speciality .lm-fade, .lm-feature .lm-fade, .lm-info-section .lm-fade, .lm-recommend .lm-fade, .lm-process .lm-fade, .lm-faq-section .lm-fade'"
new_sel = "'.lm-vs-section .lm-fade, .lm-vs-section .lm-vs-row, .lm-info-section .lm-fade, .lm-feature-section .lm-fade, .lm-process .lm-fade, .lm-why .lm-fade, .lm-recommend .lm-fade, .lm-clinic .lm-fade, .lm-faq-section .lm-fade'"
js = js.replace(old_sel, new_sel)
js = js.replace("document.querySelectorAll('.lm-fade')", "document.querySelectorAll('.lm-fade, .lm-vs-row')")
o.append(js)

# 15. Floating SNS + closing scripts + close tags (implant lines 1241 to end)
o.append(L(impl, 1241, len(impl)))

# ==================== WRITE ====================
result = ''.join(o)
outpath = os.path.join(BASE, 'implant.html')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Done! implant.html generated: {len(result):,} bytes, {result.count(chr(10)):,} lines')
