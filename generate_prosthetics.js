const fs = require('fs');
const path = require('path');
const { URL } = require('url');

const baseDir = __dirname;
const contentPath = path.join(baseDir, 'benchmark_data', 'content', 'prosthetics.json');
const outputHtmlPath = path.join(baseDir, 'prosthetics.html');

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
    let heroImage = 'images/migrated/benchmark/prosthetics/e66ac7_f564524f8ac44818932c2faeb73cf5a6_mv2.jpg';

    // Intro Section
    mainContentHtml += `
    <section class="prosthetics-hero">
        <div class="hero-overlay"></div>
        <div class="container text-center" style="position:relative; z-index:2;">
            <h2 class="section-title fade-up" style="color:white; margin-bottom:20px;">보철 / 일반진료</h2>
            <p class="section-desc fade-up" style="color:rgba(255,255,255,0.9);">
                소중한 자연치아를 지키는 보철치료<br>
                스마일뷰 치과가 당신의 치아 건강을 책임집니다
            </p>
        </div>
    </section>
    `;

    // Intro Text Block
    mainContentHtml += `
    <section class="content-section text-center">
        <div class="container">
            <h3 class="section-title fade-up">보철치료란?</h3>
            <p class="section-desc fade-up" style="max-width:800px; margin:0 auto;">
                손상되거나 상실된 치아를 인공적인 보철물로 대체하여<br>
                치아의 원래 형태와 기능을 회복시키는 치료입니다.<br>
                충치, 신경 손상 등으로 약해진 치아를 보호하고 심미성을 되찾아 드립니다.
            </p>
        </div>
    </section>
    `;

    // Treatments List
    // We will hardcode the structure based on the specific assets we identified to ensure perfect layout

    const treatments = [
        {
            title: "충치치료",
            subtitle: "레진 / 인레이",
            desc: "초기 충치는 간단한 레진으로, 진행된 충치는 인레이로 치료합니다.<br>충치 범위에 따라 적절한 재료를 선택하여 치아를 보존합니다.",
            img: "images/migrated/benchmark/prosthetics/_ED_83_AD_11__A__EC_B6_A9_EC_B9_98_EC_B9_98_EB_A3_8C.jpeg"
        },
        {
            title: "신경치료",
            subtitle: "염증 제거 / 밀봉",
            desc: "충치가 신경까지 침범했거나 치아에 금이 간 경우 진행합니다.<br>오염된 신경을 제거하고 소독한 뒤 밀봉하여 치아를 살리는 치료입니다.",
            img: "images/migrated/benchmark/prosthetics/_ED_83_AD_11__B__EC_8B_A0_EA_B2_BD_EC_B9_98_EB_A3_8C.jpeg"
        },
        {
            title: "크라운 보철",
            subtitle: "PFM / 골드 / 지르코니아",
            desc: "신경치료 후 약해진 치아나 파절된 치아 전체를 씌우는 치료입니다.<br>심미적이고 강도가 높은 지르코니아 등 상황에 맞는 재료를 사용합니다.",
            img: "images/migrated/benchmark/prosthetics/_ED_83_AD_11__C__EB_B3_B4_EC_B2_A0_EC_B9_98_EB_A3_8C.jpeg"
        },
        {
            title: "잇몸치료",
            subtitle: "스케일링 / 큐렛",
            desc: "치석과 염증으로 붓고 피나는 잇몸을 치료합니다.<br>정기적인 스케일링과 잇몸 치료로 치아 상실을 예방할 수 있습니다.",
            img: "images/migrated/benchmark/prosthetics/_ED_83_AD_11__D__EC_9E_87_EB_AA_B8_EC_B9_98_EB_A3_8C.jpeg"
        }
    ];

    mainContentHtml += `<section class="content-section bg-light"><div class="container">`;

    treatments.forEach((item, index) => {
        const isEven = index % 2 === 0;
        mainContentHtml += `
        <div class="treatment-row fade-up" style="display:flex; align-items:center; gap:50px; margin-bottom:80px; flex-direction:${isEven ? 'row' : 'row-reverse'};">
            <div class="treat-img" style="flex:1;">
                <img src="${item.img}" style="width:100%; border-radius:15px; box-shadow:0 10px 30px rgba(0,0,0,0.1);">
            </div>
            <div class="treat-info" style="flex:1; text-align:left;">
                <span style="color:#c4a984; font-weight:bold; letter-spacing:1px;">${item.subtitle}</span>
                <h3 style="font-size:2rem; margin:10px 0 20px;">${item.title}</h3>
                <p style="color:#666; line-height:1.8; font-size:1.05rem;">
                    ${item.desc}
                </p>
                <div style="margin-top:30px; border-top:1px solid #ddd; padding-top:20px;">
                    <span style="font-size:0.9rem; color:#888;">* 개인의 구강 상태에 따라 치료 계획이 달라질 수 있습니다.</span>
                </div>
            </div>
        </div>
        `;
    });

    mainContentHtml += `</div></section>`;


    const htmlTemplate = `<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>보철치료 | 스마일뷰치과의원</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animations.css">
    <style>
        .prosthetics-hero {
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
        .prosthetics-hero h2 {
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
        @media (max-width: 768px) {
            .treatment-row {
                flex-direction: column !important;
                gap: 30px !important;
                margin-bottom: 60px !important;
            }
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
                    <li><a href="laminate.html">원데이 라미네이트</a></li>
                    <li><a href="implant.html">수면 임플란트</a></li>
                    <li><a href="prosthetics.html" class="active">보철치료</a></li>
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
