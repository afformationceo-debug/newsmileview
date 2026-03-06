const fs = require('fs');
const path = require('path');
const { URL } = require('url');

const baseDir = __dirname;
const contentDir = path.join(baseDir, 'benchmark_data', 'content');
const outputHtmlPath = path.join(baseDir, 'ortho.html');

// Categories and their files
const categories = [
    { id: 'conventional', name: '일반 교정', file: 'ortho_conventional.json', dir: 'ortho_conventional' },
    { id: 'partial', name: '부분 교정', file: 'ortho_partial.json', dir: 'ortho_partial' },
    { id: 'lingual', name: '설측 교정', file: 'ortho_lingual.json', dir: 'ortho_lingual' },
    { id: 'non_surgery', name: '비수술 교정', file: 'ortho_non_surgery.json', dir: 'ortho_non_surgery' },
    { id: 'surgery', name: '선수술 교정', file: 'ortho_surgery.json', dir: 'ortho_surgery' }
];

function sanitizeFilename(url) {
    const parsed = new URL(url);
    const basename = path.basename(parsed.pathname);
    if (!basename || basename.length < 3) {
        return `asset_${Math.random().toString(36).substring(7)}.jpg`;
    }
    return basename.replace(/[^a-zA-Z0-9._-]/g, '_');
}

function generateHtml() {
    let mainContentHtml = '';

    // Generate Tab Buttons
    mainContentHtml += `
    <section class="ortho-tabs-section">
        <div class="container">
            <div class="tab-buttons">
                ${categories.map((cat, index) =>
        `<button class="tab-btn ${index === 0 ? 'active' : ''}" onclick="openTab(event, '${cat.id}')">${cat.name}</button>`
    ).join('')}
            </div>
        </div>
    </section>
    `;

    // Generate Tab Content
    mainContentHtml += '<div class="container ortho-content-container">';

    categories.forEach((cat, index) => {
        const jsonPath = path.join(contentDir, cat.file);
        if (!fs.existsSync(jsonPath)) {
            console.error(`Missing file: ${jsonPath}`);
            return;
        }
        const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

        mainContentHtml += `<div id="${cat.id}" class="tab-content ${index === 0 ? 'active' : ''}">`;

        // Iterate sections
        // Skipping index 0-3 usually as they are header/menu clutter from scraper, looking for actual content
        // But let's check the JSONs. Usually mostly text/images.
        // We will render all sections that have content.

        data.sections.forEach(section => {
            if (section.index < 3) return; // Skip potential nav/logo scraps if they exist at top

            // Check if section has meaningful content
            const hasText = section.text && section.text.trim().length > 0;
            const hasImages = section.images && section.images.length > 0;

            if (!hasText && !hasImages) return;

            mainContentHtml += '<div class="ortho-section">';

            if (hasText) {
                // Convert newlines to <br>
                const formattedText = section.text.split('\n').map(line => line.trim()).filter(line => line.length > 0).join('<br>');
                if (formattedText) {
                    mainContentHtml += `<div class="ortho-text"><p>${formattedText}</p></div>`;
                }
            }

            if (hasImages) {
                mainContentHtml += '<div class="ortho-images">';
                section.images.forEach(imgUrl => {
                    const filename = sanitizeFilename(imgUrl);
                    const localPath = `images/migrated/benchmark/${cat.dir}/${filename}`;
                    mainContentHtml += `<img src="${localPath}" alt="Orthodontics Image" loading="lazy">`;
                });
                mainContentHtml += '</div>';
            }

            mainContentHtml += '</div>'; // End ortho-section
        });

        mainContentHtml += '</div>'; // End tab-content
    });

    mainContentHtml += '</div>'; // End container

    // Construct full HTML
    const htmlTemplate = `<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>치아교정 | 스마일뷰치과의원</title>
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animations.css">
    <style>
        /* Specific Styles for Ortho Tabs */
        .ortho-tabs-section {
            background: #f5f5f5;
            padding: 20px 0;
            position: sticky;
            top: 80px; /* Adjust based on header height */
            z-index: 90;
        }
        .tab-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .tab-btn {
            padding: 12px 24px;
            border: 1px solid #ddd;
            background: #fff;
            cursor: pointer;
            font-size: 1rem;
            border-radius: 30px;
            transition: all 0.3s;
            font-family: inherit;
        }
        .tab-btn:hover {
            background: #eee;
        }
        .tab-btn.active {
            background: #c4a984; /* Theme color */
            color: white;
            border-color: #c4a984;
        }
        
        .ortho-content-container {
            padding: 40px 20px;
            min-height: 600px;
        }
        .tab-content {
            display: none;
            animation: fadeIn 0.5s;
        }
        .tab-content.active {
            display: block;
        }
        
        .ortho-section {
            margin-bottom: 60px;
            text-align: center;
        }
        .ortho-text p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #444;
            max-width: 800px;
            margin: 0 auto 30px;
        }
        .ortho-images {
            display: flex;
            flex-direction: column;
            gap: 20px;
            align-items: center;
        }
        .ortho-images img {
            max-width: 100%;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Hero for Ortho */
        .ortho-hero {
            height: 50vh;
            background-color: #333; /* Fallback */
            background-image: url('images/migrated/benchmark/ortho_conventional/e66ac7_4c7c73c41a6c410289944238c011f481_mv2.jpg'); /* Use one of the hero images */
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }
        .ortho-hero::after {
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.3);
        }
        .ortho-hero-content {
            position: relative;
            z-index: 2;
            color: white;
            text-align: center;
        }
        .ortho-hero h2 {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            margin-bottom: 20px;
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
                    <li><a href="ortho.html" class="active">치아교정</a></li>
                    <li><a href="whitening.html">치아미백</a></li>
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
        <section class="ortho-hero">
            <div class="ortho-hero-content">
                <h2>치아교정 Center</h2>
                <p>스마일뷰만의 특별한 교정 솔루션</p>
            </div>
        </section>

        ${mainContentHtml}
    </main>

    <footer>
        <div class="container footer-content">
            <p>© 2026 SMILEVIEW DENTAL CLINIC. All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        function openTab(evt, tabId) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tab-content");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
                tabcontent[i].classList.remove("active");
            }
            tablinks = document.getElementsByClassName("tab-btn");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }
            document.getElementById(tabId).style.display = "block";
            setTimeout(() => {
                document.getElementById(tabId).classList.add("active");
            }, 10);
            evt.currentTarget.className += " active";
        }
    </script>
</body>
</html>`;

    fs.writeFileSync(outputHtmlPath, htmlTemplate, 'utf8');
    console.log(`Generated ${outputHtmlPath}`);
}

generateHtml();
