const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

// Target URLs
const targets = [
    { name: 'invisalign', url: 'https://www.smile-vdental.com/invisalign' },
    { name: 'ortho_surgery', url: 'https://www.smile-vdental.com/surgery-first-orthodontics' },
    { name: 'ortho_non_surgery', url: 'https://www.smile-vdental.com/non-surgical-orthodontics' },
    { name: 'ortho_partial', url: 'https://www.smile-vdental.com/partial-orthodontics' },
    { name: 'ortho_lingual', url: 'https://www.smile-vdental.com/lingual-orthodontics' },
    { name: 'ortho_conventional', url: 'https://www.smile-vdental.com/conventional-orthodontics' },
    { name: 'whitening', url: 'https://www.smile-vdental.com/teeth-whitening' },
    { name: 'laminate', url: 'https://www.smile-vdental.com/laminate' },
    { name: 'prosthetics', url: 'https://www.smile-vdental.com/prosthodontics' }
];

// Output Directories
const outputDir = path.join(__dirname, 'benchmark_data');
if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

const contentDir = path.join(outputDir, 'content');
if (!fs.existsSync(contentDir)) fs.mkdirSync(contentDir, { recursive: true });

const assetsDir = path.join(outputDir, 'assets');
if (!fs.existsSync(assetsDir)) fs.mkdirSync(assetsDir, { recursive: true });

(async () => {
    const browser = await puppeteer.launch({
        headless: "new",
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const combinedAssets = [];
    const designSystem = {
        colors: new Set(),
        fonts: new Set(),
        buttons: []
    };

    for (const target of targets) {
        console.log(`[START] Processing ${target.name}...`);
        const page = await browser.newPage();
        await page.setViewport({ width: 1920, height: 1080 });

        // --- Agent C: Asset Extraction (Network Intercept) ---
        const pageAssets = new Set();
        await page.setRequestInterception(true);
        page.on('request', (req) => {
            const type = req.resourceType();
            const url = req.url();

            // Allow all requests to ensure content loads
            req.continue();

            // Filter for assets
            if (['image', 'media', 'font'].includes(type) && !url.includes('google-analytics') && !url.includes('facebook')) {
                pageAssets.add(url);
            }
        });

        try {
            // Updated timeout to 90s for robustness
            await page.goto(target.url, { waitUntil: 'networkidle2', timeout: 90000 });
        } catch (e) {
            console.error(`[WARN] Timeout loading ${target.url}, proceeding with partial load...`);
        }

        // Auto-Scroll to load lazy content
        await page.evaluate(async () => {
            await new Promise((resolve) => {
                let totalHeight = 0;
                const distance = 100;
                const timer = setInterval(() => {
                    const scrollHeight = document.body.scrollHeight;
                    window.scrollBy(0, distance);
                    totalHeight += distance;

                    if (totalHeight >= scrollHeight) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        });

        // Wait a bit for final renders
        await new Promise(r => setTimeout(r, 3000));

        // --- Agent A: Content Extraction ---
        const content = await page.evaluate(() => {
            const data = {
                title: document.title,
                sections: []
            };

            // Heuristic using large containers or sections
            const sections = Array.from(document.querySelectorAll('section, div[data-testid="richTextElement"], div[id^="comp-"]'));

            sections.forEach((sec, idx) => {
                const text = sec.innerText.trim();
                const images = Array.from(sec.querySelectorAll('img')).map(img => img.src);
                const bgImage = window.getComputedStyle(sec).backgroundImage;

                if (text.length > 0 || images.length > 0 || (bgImage && bgImage !== 'none')) {
                    data.sections.push({
                        index: idx,
                        text: text.substring(0, 500), // Limit text per block for summary
                        full_text: text,
                        images: images,
                        background: bgImage
                    });
                }
            });

            return data;
        });

        fs.writeFileSync(path.join(contentDir, `${target.name}.json`), JSON.stringify(content, null, 2));

        // --- Agent B: Design Analysis ---
        // Extract basic styles from body and headings
        const styles = await page.evaluate(() => {
            const heading = document.querySelector('h1, h2');
            const body = document.body;
            const btn = document.querySelector('button, a.btn, [role="button"]');

            const getStyle = (el) => {
                if (!el) return null;
                const s = window.getComputedStyle(el);
                return {
                    color: s.color,
                    fontFamily: s.fontFamily,
                    fontSize: s.fontSize,
                    backgroundColor: s.backgroundColor
                };
            };

            return {
                body: getStyle(body),
                heading: getStyle(heading),
                button: getStyle(btn)
            };
        });

        if (styles.heading?.color) designSystem.colors.add(styles.heading.color);
        if (styles.body?.color) designSystem.colors.add(styles.body.color);
        if (styles.button?.backgroundColor) designSystem.colors.add(styles.button.backgroundColor);
        if (styles.body?.fontFamily) designSystem.fonts.add(styles.body.fontFamily);

        combinedAssets.push({
            page: target.name,
            urls: Array.from(pageAssets)
        });

        await page.close();
        console.log(`[DONE] ${target.name}`);
    }

    await browser.close();

    // Save Aggregated Data
    fs.writeFileSync(path.join(outputDir, 'assets_manifest.json'), JSON.stringify(combinedAssets, null, 2));

    // Convert Sets to Arrays for JSON
    const finalDesign = {
        colors: Array.from(designSystem.colors),
        fonts: Array.from(designSystem.fonts)
    };
    fs.writeFileSync(path.join(outputDir, 'theme.json'), JSON.stringify(finalDesign, null, 2));

    console.log('[SUCCESS] Benchmark Mission Complete.');
})();
