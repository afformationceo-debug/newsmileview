const fs = require('fs');
const path = require('path');
const { URL } = require('url');

const baseDir = __dirname;
const contentPath = path.join(baseDir, 'benchmark_data', 'content', 'laminate.json');
const outputHtmlPath = path.join(baseDir, 'laminate.html');

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

    // Hero Section
    // Using the specific hero image found in JSON or directory listing
    let heroImage = 'images/migrated/benchmark/laminate/e66ac7_4ab2b0c532114a609295ed2775d124ed_mv2.jpg';

    // Intro Section
    mainContentHtml += `
    <section class="laminate-hero">
        <div class="hero-overlay"></div>
        <div class="container text-center" style="position:relative; z-index:2;">
            <h2 class="section-title fade-up" style="color:white; margin-bottom:20px;">최소삭제 라미네이트</h2>
            <p class="section-desc fade-up" style="color:rgba(255,255,255,0.9);">
                자연스러운 아름다움, 최소한의 삭제로 완성하는<br>
                스마일뷰 치과만의 프리미엄 라미네이트
            </p>
        </div>
    </section>
    `;

    // Intro Text Block
    mainContentHtml += `
    <section class="content-section">
        <div class="container text-center">
            <h3 class="section-title fade-up">라미네이트란?</h3>
            <p class="section-desc fade-up">
                치아 성형의 한 종류로, 치아 사이의 간격이나 치아의 배열이 불균일한 경우,<br>
                또는 치아의 색을 밝히거나 반점을 처리할 때 사용됩니다.<br>
                치과에서 얇은 치아와 같은 재질의 도자기를 사용하여 치아 표면에 부착하는 심미 치료입니다.
            </p>
        </div>
    </section>
    `;

    // Recommendations Section (Who needs it)
    mainContentHtml += `
    <section class="content-section bg-light">
        <div class="container">
            <div class="text-center mb-5">
                <h3 class="section-title">이런 분들에게 필요합니다</h3>
            </div>
            <div class="row" style="display:flex; flex-wrap:wrap; justify-content:center; gap:20px;">
                <!-- Case 1 -->
                <div class="col-md-3 text-center fade-up" style="flex:1; min-width:200px; max-width:280px;">
                    <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___ED_95_84_EC_9A_94_ED_95_9C_EC_82_AC_EB_9E_8C_201.png" style="width:100px; height:auto; margin-bottom:15px;">
                    <p style="font-weight:600;">치아 배열이 좋지 않은 경우</p>
                    <p style="font-size:0.9rem; color:#666;">앞니가 겹치거나<br>공간이 있는 분</p>
                </div>
                <!-- Case 2 -->
                <div class="col-md-3 text-center fade-up" style="flex:1; min-width:200px; max-width:280px;">
                    <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___ED_95_84_EC_9A_94_ED_95_9C_EC_82_AC_EB_9E_8C_202.png" style="width:100px; height:auto; margin-bottom:15px;">
                    <p style="font-weight:600;">치아 크기가 일정하지 않은 경우</p>
                    <p style="font-size:0.9rem; color:#666;">치아가 너무 크거나<br>작은 분</p>
                </div>
                <!-- Case 3 -->
                <div class="col-md-3 text-center fade-up" style="flex:1; min-width:200px; max-width:280px;">
                    <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___ED_95_84_EC_9A_94_ED_95_9C_EC_82_AC_EB_9E_8C_203.png" style="width:100px; height:auto; margin-bottom:15px;">
                    <p style="font-weight:600;">심미적으로 우수하지 않은 경우</p>
                    <p style="font-size:0.9rem; color:#666;">앞니가 깨지거나<br>기존 보철물이 맘에 안 드는 분</p>
                </div>
                <!-- Case 4 -->
                <div class="col-md-3 text-center fade-up" style="flex:1; min-width:200px; max-width:280px;">
                    <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___ED_95_84_EC_9A_94_ED_95_9C_EC_82_AC_EB_9E_8C_204.png" style="width:100px; height:auto; margin-bottom:15px;">
                    <p style="font-weight:600;">영구적인 미백을 원하는 경우</p>
                    <p style="font-size:0.9rem; color:#666;">치아가 심하게<br>변색된 분</p>
                </div>
            </div>
        </div>
    </section>
    `;

    // Before & After (Hardcoded based on assets)
    mainContentHtml += `
    <section class="content-section">
        <div class="container text-center">
            <h3 class="section-title mb-5">Before & After</h3>
            
            <div class="ba-grid" style="display:flex; flex-direction:column; gap:40px; max-width:800px; margin:0 auto;">
                <!-- Case 1 -->
                <div class="ba-row" style="display:flex; justify-content:center; gap:20px; align-items:center;">
                    <div style="flex:1;">
                        <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___EB_9D_BC_EB_AF_B8_EB_84_A4_EC_9D_B4_ED_8A_B8_20_EB_B9_84_ED_8F_AC_201.jpg" style="width:100%; border-radius:10px;">
                        <p style="margin-top:10px; font-weight:bold; color:#888;">Before</p>
                    </div>
                    <div class="arrow" style="font-size:2rem; color:#c4a984;">&#8594;</div>
                    <div style="flex:1;">
                        <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___EB_9D_BC_EB_AF_B8_EB_84_A4_EC_9D_B4_ED_8A_B8_20_EC_95_A0_ED_94_84_ED_84_B0_201.jpg" style="width:100%; border-radius:10px;">
                        <p style="margin-top:10px; font-weight:bold; color:#c4a984;">After</p>
                    </div>
                </div>

                <!-- Case 2 -->
                <div class="ba-row" style="display:flex; justify-content:center; gap:20px; align-items:center;">
                    <div style="flex:1;">
                        <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___EB_9D_BC_EB_AF_B8_EB_84_A4_EC_9D_B4_ED_8A_B8_20_EB_B9_84_ED_8F_AC_202.jpg" style="width:100%; border-radius:10px;">
                        <p style="margin-top:10px; font-weight:bold; color:#888;">Before</p>
                    </div>
                    <div class="arrow" style="font-size:2rem; color:#c4a984;">&#8594;</div>
                    <div style="flex:1;">
                        <img src="images/migrated/benchmark/laminate/_ED_83_AD_9___EB_9D_BC_EB_AF_B8_EB_84_A4_EC_9D_B4_ED_8A_B8_20_EC_95_A0_ED_94_84_ED_84_B0_202.jpg" style="width:100%; border-radius:10px;">
                        <p style="margin-top:10px; font-weight:bold; color:#c4a984;">After</p>
                    </div>
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
    <title>라미네이트 | 스마일뷰치과의원</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animations.css">
    <style>
        .laminate-hero {
            height: 50vh;
            background-image: url('${heroImage}');
            background-size: cover;
            background-position: center;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .hero-overlay {
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.4);
        }
        .laminate-hero h2 {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .content-section {
            padding: 80px 0;
        }
        .bg-light {
            background-color: #f9f9f9;
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
                    <li><a href="whitening.html">치아미백</a></li>
                    <li><a href="laminate.html" class="active">원데이 라미네이트</a></li>
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
