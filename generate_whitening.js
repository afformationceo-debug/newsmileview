const fs = require('fs');
const path = require('path');
const { URL } = require('url');

const baseDir = __dirname;
const contentPath = path.join(baseDir, 'benchmark_data', 'content', 'whitening.json');
const outputHtmlPath = path.join(baseDir, 'whitening.html');

function sanitizeFilename(url) {
    const parsed = new URL(url);
    const basename = path.basename(parsed.pathname);
    if (!basename || basename.length < 3) {
        return `asset_${Math.random().toString(36).substring(7)}.jpg`;
    }
    return basename.replace(/[^a-zA-Z0-9._-]/g, '_');
}

function generateHtml() {
    if (!fs.existsSync(contentPath)) {
        console.error(`Missing file: ${contentPath}`);
        return;
    }
    const data = JSON.parse(fs.readFileSync(contentPath, 'utf8'));

    let mainContentHtml = '';

    // Hero Section (using first nice image found or fallback)
    // Finding a hero image from the first few sections
    let heroImage = 'images/migrated/benchmark/whitening/e66ac7_45858edcced243eda13980a2dbfaa92e_mv2.jpg'; // Default fallback from json inspection

    // Attempt to finding specific content sections
    // Filtering for meaningful sections
    const meaningfulSections = data.sections.filter(s => {
        // Skip nav items or footer items if possible
        const text = s.text || "";
        if (text.includes("스마일뷰치과의원") && text.includes("사업자번호")) return false; // Footer
        if (text.includes("진료시간 안내")) return false; // Footer
        if (text.includes("스마일뷰 치과") && text.includes("인비절라인")) return false; // Nav garbage
        return true;
    });

    // Intro Section
    mainContentHtml += `
    <section class="whitening-intro section-padding">
        <div class="container text-center">
            <h2 class="section-title fade-up">밝고 자신감 있는 미소</h2>
            <p class="section-desc fade-up">
                치아 미백은 변색된 치아를 밝고 깨끗하게 회복시켜<br>
                당신의 미소를 더욱 아름답게 만들어 드립니다.
            </p>
        </div>
    </section>
    `;

    // Process Content Loop
    meaningfulSections.forEach(section => {
        const text = section.text || "";
        const images = section.images || [];

        if (!text && images.length === 0) return;

        // Simple Heuristic for layout
        // If "치아미백은 이런 분들에게 권해드립니다" detected -> Candidate Section
        if (text.includes("이런 분들에게 권해드립니다")) {
            mainContentHtml += `
            <section class="content-section bg-light">
                <div class="container">
                    <div class="text-center mb-5">
                        <h3 class="section-title">치아미백 대상</h3>
                        <p class="section-desc">이런 고민이 있으신 분들에게 추천합니다.</p>
                    </div>
                    <div class="feature-grid">
                        <div class="feature-card"><h4>01</h4><p>선천적으로 누런 치아</p></div>
                        <div class="feature-card"><h4>02</h4><p>후천적 변색 (커피, 흡연 등)</p></div>
                        <div class="feature-card"><h4>03</h4><p>노화로 인한 변색</p></div>
                        <div class="feature-card"><h4>04</h4><p>외상으로 인한 변색</p></div>
                        <div class="feature-card"><h4>05</h4><p>약물 부작용 변색</p></div>
                        <div class="feature-card"><h4>06</h4><p>웨딩/면접 등 중요한 일정을 앞둔 분</p></div>
                    </div>
                </div>
            </section>
            `;
            return;
        }

        // If "치아미백 종류" -> Types Section
        if (text.includes("치아미백 종류") || text.includes("자가 미백") || text.includes("전문가 미백")) {
            // We will handle types manually based on known structure to make it look good
            return;
        }

        // Generic Content Block
        // Only output if it looks like a paragraph
        if (text.length > 20 && !text.includes("01") && !text.includes("06")) {
            mainContentHtml += `
             <section class="content-section">
                <div class="container text-center">
                    <div class="whitening-text-block fade-up">
                        <p>${text.replace(/\n/g, '<br>')}</p>
                    </div>
                    ${images.length > 0 ? `
                    <div class="whitening-images mt-5 fade-up">
                        ${images.map(img => `<img src="images/migrated/benchmark/whitening/${sanitizeFilename(img)}" style="max-width: 800px; margin: 20px auto; border-radius: 10px;">`).join('')}
                    </div>
                    ` : ''}
                </div>
             </section>
             `;
        }
    });

    // Hardcoded Types Section based on JSON insights (it's better than parsing messy text)
    mainContentHtml += `
    <section class="content-section">
        <div class="container">
            <div class="text-center mb-5">
                <h3 class="section-title">치아미백 프로그램</h3>
                <p class="section-desc">스마일뷰 치과의 체계적인 미백 솔루션</p>
            </div>
            <div class="row" style="display:flex; gap:30px; justify-content:center; flex-wrap:wrap;">
                <!-- Expert Whitening -->
                <div class="program-card" style="flex:1; min-width:300px; border:1px solid #eee; padding:30px; border-radius:15px; text-align:center;">
                    <img src="images/migrated/benchmark/whitening/_ED_83_AD_7___EB_AF_B8_EB_B0_B1_EC_A2_85_EB_A5_98__EC_A0_84_EB_AC_B8_EA_B0_80_EB_AF_B8_EB_B0_B1.png" style="max-width:100%; height:auto; margin-bottom:20px; border-radius:10px;">
                    <h4 style="font-size:1.5rem; margin-bottom:20px; color:#c4a984;">전문가 미백</h4>
                    <p style="color:#666; margin-bottom:20px;">치과 내에서 고농도의 미백제와 특수 광선을 이용하여 단시간에 확실한 효과를 보는 시술입니다.</p>
                    <ul style="text-align:left; color:#555; line-height:1.8; list-style:disc; padding-left:20px;">
                        <li>1회 시술로 즉각적인 효과</li>
                        <li>의료진의 정밀한 시술</li>
                        <li>안전하고 검증된 미백제 사용</li>
                    </ul>
                </div>
                <!-- Self Whitening -->
                <div class="program-card" style="flex:1; min-width:300px; border:1px solid #eee; padding:30px; border-radius:15px; text-align:center;">
                    <img src="images/migrated/benchmark/whitening/_ED_83_AD_7___EB_AF_B8_EB_B0_B1_EC_A2_85_EB_A5_98__EC_9E_90_EA_B0_80_EB_AF_B8_EB_B0_B1.png" style="max-width:100%; height:auto; margin-bottom:20px; border-radius:10px;">
                    <h4 style="font-size:1.5rem; margin-bottom:20px; color:#c4a984;">자가 미백</h4>
                    <p style="color:#666; margin-bottom:20px;">개인 맞춤형 미백 틀을 제작하여 집에서 편안하게 진행하는 미백 관리 프로그램입니다.</p>
                    <ul style="text-align:left; color:#555; line-height:1.8; list-style:disc; padding-left:20px;">
                        <li>지속적인 밝기 유지 가능</li>
                        <li>원하는 시간, 장소에서 가능</li>
                        <li>전문가 미백 후 보조요법으로 우수</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    `;


    const htmlTemplate = `<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>치아미백 | 스마일뷰치과의원</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animations.css">
    <style>
        .whitening-hero {
            height: 50vh;
            background-image: url('images/migrated/benchmark/whitening/e66ac7_45858edcced243eda13980a2dbfaa92e_mv2.jpg');
            background-size: cover;
            background-position: center;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .whitening-hero::after {
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.3);
        }
        .whitening-hero h2 {
            position: relative;
            z-index: 2;
            color: white;
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
        }
        .whitening-text-block p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #444;
            max-width: 800px;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <header id="main-header">
        <div class="header-container">
            <div class="logo">
                <a href="index.html">SMILEVIEW</a>
            </div>
            <nav class="main-nav">
                <ul>
                    <li><a href="introduction.html">스마일뷰치과</a></li>
                    <li><a href="invisalign.html">인비절라인</a></li>
                    <li><a href="ortho.html">치아교정</a></li>
                    <li><a href="whitening.html" class="active">치아미백</a></li>
                    <li><a href="laminate.html">원데이 라미네이트</a></li>
                    <li><a href="implant.html">수면 임플란트</a></li>
                    <li><a href="prosthetics.html">보철치료</a></li>
                </ul>
            </nav>
            <div class="header-right">
                <div class="header-socials">
                    <a href="#" class="h-icon-btn" title="Instagram"><i class="ph ph-instagram-logo"></i></a>
                    <a href="#" class="h-icon-btn" title="LINE"><i class="ph-fill ph-chat-circle-dots"></i></a>
                    <a href="#" class="h-icon-btn" title="YouTube"><i class="ph ph-youtube-logo"></i></a>
                </div>
                <div class="mobile-menu-btn"><i class="ph ph-list"></i></div>
            </div>
        </div>
    </header>

    <main>
        <section class="whitening-hero">
            <h2>Whitening Center</h2>
        </section>

        ${mainContentHtml}

    </main>

    <footer>
        <div class="container footer-content">
            <p>© 2026 SMILEVIEW DENTAL CLINIC. All Rights Reserved.</p>
        </div>
    </footer>
</body>
</html>`;

    fs.writeFileSync(outputHtmlPath, htmlTemplate, 'utf8');
    console.log(`Generated ${outputHtmlPath}`);
}

generateHtml();
