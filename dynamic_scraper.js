const puppeteer = require('puppeteer');
const fs = require('fs');

const targets = [
    { name: 'invisalign', url: 'https://www.smile-vdental.com/invisalign' },
    { name: 'whitening', url: 'https://www.smile-vdental.com/teeth-whitening' },
    { name: 'laminate', url: 'https://www.smile-vdental.com/laminate' },
    { name: 'prosthetics', url: 'https://www.smile-vdental.com/prosthodontics' },
    { name: 'implant', url: 'https://www.smile-vdental.com/sedation-implant-surgery' },
    // Ortho URLs
    { name: 'ortho_surgery', url: 'https://www.smile-vdental.com/surgery-first-orthodontics' },
    { name: 'ortho_nonsurgical', url: 'https://www.smile-vdental.com/non-surgical-orthodontics' },
    { name: 'ortho_partial', url: 'https://www.smile-vdental.com/partial-orthodontics' },
    { name: 'ortho_lingual', url: 'https://www.smile-vdental.com/lingual-orthodontics' },
    { name: 'ortho_conventional', url: 'https://www.smile-vdental.com/conventional-orthodontics' }
];

async function scrape() {
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();
    const results = {};

    for (const target of targets) {
        console.log(`Scraping ${target.name}...`);
        try {
            await page.goto(target.url, { waitUntil: 'networkidle2', timeout: 60000 });

            // Scroll to bottom to trigger lazy loading
            await page.evaluate(async () => {
                await new Promise((resolve) => {
                    let totalHeight = 0;
                    const distance = 100;
                    const timer = setInterval(() => {
                        const scrollHeight = document.body.scrollHeight;
                        window.scrollBy(0, distance);
                        totalHeight += distance;

                        if (totalHeight >= scrollHeight - window.innerHeight) {
                            clearInterval(timer);
                            resolve();
                        }
                    }, 100);
                });
            });

            // Wait a bit for final renders
            await new Promise(r => setTimeout(r, 2000));

            const data = await page.evaluate(() => {
                const getText = (selector) => {
                    return Array.from(document.querySelectorAll(selector)).map(el => el.innerText.trim()).filter(t => t.length > 0);
                };

                const getImages = () => {
                    const imgs = Array.from(document.querySelectorAll('img')).map(img => img.src);
                    const bgImages = Array.from(document.querySelectorAll('*')).map(el => {
                        const style = window.getComputedStyle(el);
                        return style.backgroundImage !== 'none' ? style.backgroundImage.slice(4, -1).replace(/["']/g, "") : null;
                    }).filter(url => url);
                    return [...new Set([...imgs, ...bgImages])].filter(url => url.startsWith('http'));
                };

                const getVideos = () => {
                    const videos = Array.from(document.querySelectorAll('video')).map(v => v.src || v.querySelector('source')?.src);
                    const iframes = Array.from(document.querySelectorAll('iframe')).map(i => i.src);
                    return [...new Set([...videos, ...iframes])].filter(url => url);
                };

                return {
                    title: document.title,
                    h1: getText('h1'),
                    h2: getText('h2'),
                    h3: getText('h3'),
                    p: getText('p'),
                    images: getImages(),
                    videos: getVideos()
                };
            });

            results[target.name] = data;
            console.log(`  - Found ${data.images.length} images, ${data.videos.length} videos.`);

        } catch (e) {
            console.error(`  - Failed to scrape ${target.name}: ${e.message}`);
        }
    }

    await browser.close();
    fs.writeFileSync('scraped_data.json', JSON.stringify(results, null, 2));
    console.log('All done! Saved to scraped_data.json');
}

scrape();
