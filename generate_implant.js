const fs = require('fs');
const path = require('path');
const { URL } = require('url');

const baseDir = __dirname;
const contentPath = path.join(baseDir, 'benchmark_data', 'content', 'implant.json');
const outputHtmlPath = path.join(baseDir, 'implant.html');

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
    let heroImage = 'images/migrated/benchmark/implant/e66ac7_f8fab2400c304dc5912cc9bb7f6abbf0_mv2.jpg';

    mainContentHtml += `
    <section class="implant-hero">
        <div class="hero-overlay"></div>
        <div class="container text-center" style="position:relative; z-index:2;">
            <h2 class="section-title fade-up" style="color:white; margin-bottom:20px;">수면 임플란트</h2>
            <p class="section-desc fade-up" style="color:rgba(255,255,255,0.9);">
                자연 치아와 가장 유사한 제3의 치아<br>
                스마일뷰 치과에서 편안하고 안전하게 시작하세요
            </p>
        </div>
    </section>
    `;

    // Intro Text
    mainContentHtml += `
    <section class="content-section text-center">
        <div class="container">
            <h3 class="section-title fade-up">임플란트란?</h3>
            <p class="section-desc fade-up" style="max-width:800px; margin:0 auto;">
                손실된 치아를 대신하여 인공 치아를 식립하는 치료입니다.<br>
                저작 기능과 심미성을 동시에 회복시켜 삶의 질을 높여드립니다.
            </p>
        </div>
    </section>
    `;

    // Implant Types List
    const implantTypes = [
        {
            title: "당일 즉시 임플란트",
            desc: "발치 후 즉시 임플란트를 식립하여<br>치료 기간을 획기적으로 단축합니다.<br>통증과 붓기를 최소화하고 잇몸 뼈 보존에 유리합니다.",
            img: "images/migrated/benchmark/implant/_ED_83_AD_8___EC_9E_84_ED_94_8C_EB_9E_80_ED_8A_B8_201.png"
        },
        {
            title: "네비게이션 임플란트",
            desc: "3D 컴퓨터 모의수술을 통해 최적의 식립 위치를 결정합니다.<br>최소 절개로 진행되어 통증이 적고 회복이 빠릅니다.<br>정확하고 안전한 디지털 임플란트입니다.",
            img: "images/migrated/benchmark/implant/_ED_83_AD_8___EC_9E_84_ED_94_8C_EB_9E_80_ED_8A_B8_202.png"
        },
        {
            title: "뼈 이식 임플란트",
            desc: "잇몸 뼈가 부족한 경우 뼈 이식재를 보강하여<br>임플란트가 단단하게 고정될 수 있도록 합니다.<br>기초가 튼튼해야 임플란트를 오래 사용할 수 있습니다.",
            img: "images/migrated/benchmark/implant/_ED_83_AD_8___EC_9E_84_ED_94_8C_EB_9E_80_ED_8A_B8_203.png"
        }
    ];

    mainContentHtml += `<section class="content-section bg-light"><div class="container">`;

    implantTypes.forEach((item, index) => {
        const isEven = index % 2 === 0;
        mainContentHtml += `
        <div class="implant-row fade-up" style="display:flex; align-items:center; gap:50px; margin-bottom:100px; flex-direction:${isEven ? 'row' : 'row-reverse'};">
            <div class="implant-img" style="flex:1;">
                <img src="${item.img}" style="width:100%; border-radius:20px; box-shadow:0 15px 40px rgba(0,0,0,0.1);">
            </div>
            <div class="implant-info" style="flex:1; text-align:left;">
                <h3 style="font-size:2.2rem; margin-bottom:25px; color:#333;">${item.title}</h3>
                <p style="color:#666; line-height:1.8; font-size:1.1rem; margin-bottom:30px;">
                    ${item.desc}
                </p>
                <div class="btn-group">
                    <a href="https://booking.naver.com/booking/13/bizes/606969" class="btn btn-primary">상담 예약하기</a>
                </div>
            </div>
        </div>
        `;
    });
    mainContentHtml += `</div></section>`;

    // Osstem Section
    mainContentHtml += `
    <section class="content-section text-center">
        <div class="container">
            <h3 class="section-title fade-up">정품 오스템 임플란트 사용</h3>
            <p class="section-desc fade-up" style="margin-bottom:50px;">
                스마일뷰치과는 세계적인 품질을 인정받은 정품 오스템 임플란트만을 사용합니다.<br>
                정품 인증서 발급으로 사후 관리까지 철저하게 보장합니다.
            </p>
            <div class="osstem-images fade-up" style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap;">
                <img src="images/migrated/benchmark/implant/_ED_83_AD_8___EC_98_A4_EC_8A_A4_ED_85_9C_201.png" style="height:80px; object-fit:contain;">
                <img src="images/migrated/benchmark/implant/_ED_83_AD_8___EC_98_A4_EC_8A_A4_ED_85_9C_202.jpg" style="height:200px; border-radius:10px;">
                <img src="images/migrated/benchmark/implant/_ED_83_AD_8___EC_98_A4_EC_8A_A4_ED_85_9C_203.jpg" style="height:200px; border-radius:10px;">
            </div>
        </div>
    </section>
    `;


    const htmlTemplate = `<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수면 임플란트 | 스마일뷰치과의원</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animations.css">
    <style>
        .implant-hero {
            height: 60vh;
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
            background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7));
        }
        .implant-hero h2 {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        .content-section {
            padding: 100px 0;
        }
        .bg-light {
            background-color: #f8f9fa;
        }
        .btn-primary {
            display: inline-block;
            padding: 12px 30px;
            background-color: #c4a984;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }
        .btn-primary:hover {
            background-color: #a38865;
        }
        @media (max-width: 768px) {
            .implant-row {
                flex-direction: column !important;
                gap: 30px !important;
            }
            .implant-hero h2 {
                font-size: 2.5rem;
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
                    <li><a href="implant.html" class="active">수면 임플란트</a></li>
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
