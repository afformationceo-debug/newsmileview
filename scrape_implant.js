const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

// Target URLs
const targets = [
    { name: 'implant', url: 'https://www.smile-vdental.com/sedation-implant-surgery' }
];

// Output Directories
const outputDir = path.join(__dirname, 'benchmark_data');
const contentDir = path.join(outputDir, 'content');
const assetsDir = path.join(outputDir, 'assets');

(async () => {
    const browser = await puppeteer.launch({
        headless: "new",
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const combinedAssets = [];

    for (const target of targets) {
        console.log(`[START] Processing ${target.name}...`);
        const page = await browser.newPage();
        await page.setViewport({ width: 1920, height: 1080 });

        // Asset Extraction
        const pageAssets = new Set();
        await page.setRequestInterception(true);
        page.on('request', (req) => {
            const type = req.resourceType();
            const url = req.url();
            req.continue();
            if (['image', 'media', 'font'].includes(type) && !url.includes('google-analytics') && !url.includes('facebook')) {
                pageAssets.add(url);
            }
        });

        try {
            await page.goto(target.url, { waitUntil: 'networkidle2', timeout: 90000 });
        } catch (e) {
            console.error(`[WARN] Timeout loading ${target.url}, proceeding...`);
        }

        // Auto-Scroll
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

        await new Promise(r => setTimeout(r, 3000));

        // Content Extraction
        const content = await page.evaluate(() => {
            const data = {
                title: document.title,
                sections: []
            };
            const sections = Array.from(document.querySelectorAll('section, div[data-testid="richTextElement"], div[id^="comp-"]'));
            sections.forEach((sec, idx) => {
                const text = sec.innerText.trim();
                const images = Array.from(sec.querySelectorAll('img')).map(img => img.src);
                const bgImage = window.getComputedStyle(sec).backgroundImage;

                if (text.length > 0 || images.length > 0 || (bgImage && bgImage !== 'none')) {
                    data.sections.push({
                        index: idx,
                        text: text.substring(0, 500),
                        full_text: text,
                        images: images,
                        background: bgImage
                    });
                }
            });
            return data;
        });

        fs.writeFileSync(path.join(contentDir, `${target.name}.json`), JSON.stringify(content, null, 2));

        combinedAssets.push({
            page: target.name,
            urls: Array.from(pageAssets)
        });

        await page.close();
        console.log(`[DONE] ${target.name}`);
    }

    await browser.close();

    // Overwrite manifest with just implant assets for now, so downloader only does this
    fs.writeFileSync(path.join(outputDir, 'assets_manifest.json'), JSON.stringify(combinedAssets, null, 2));
    console.log('[SUCCESS] Implant Scrape Complete.');
})();
