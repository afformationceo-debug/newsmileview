const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');
const { URL } = require('url');

const manifestPath = path.join(__dirname, 'benchmark_data', 'assets_manifest.json');
const outputBaseDir = path.join(__dirname, 'images', 'migrated', 'benchmark');

if (!fs.existsSync(outputBaseDir)) fs.mkdirSync(outputBaseDir, { recursive: true });

async function downloadFile(url, dest) {
    return new Promise((resolve, reject) => {
        const file = fs.createWriteStream(dest);
        const protocol = url.startsWith('https') ? https : http;

        const request = protocol.get(url, (response) => {
            if (response.statusCode === 200) {
                response.pipe(file);
                file.on('finish', () => {
                    file.close(resolve);
                });
            } else {
                file.close();
                fs.unlink(dest, () => { }); // Delete partial file
                reject(`Server responded with ${response.statusCode}: ${url}`);
            }
        });

        request.on('error', (err) => {
            fs.unlink(dest, () => { });
            reject(err.message);
        });
    });
}

function sanitizeFilename(url) {
    const parsed = new URL(url);
    const basename = path.basename(parsed.pathname);
    // Handle wix/dynamic urls or query params if needed, but usually basename is enough
    // If basename is empty or weird, use hash
    if (!basename || basename.length < 3) {
        return `asset_${Math.random().toString(36).substring(7)}.jpg`;
    }
    return basename.replace(/[^a-zA-Z0-9._-]/g, '_');
}

async function runDownloader() {
    if (!fs.existsSync(manifestPath)) {
        console.error(`[ERROR] Manifest not found at ${manifestPath}`);
        return;
    }

    const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

    for (const pageData of manifest) {
        const pageName = pageData.page;
        const assets = pageData.urls || []; // Handle array or set converted to array

        console.log(`[PROCESSING] ${pageName} - ${assets.length} assets`);

        const pageDir = path.join(outputBaseDir, pageName);
        if (!fs.existsSync(pageDir)) fs.mkdirSync(pageDir, { recursive: true });

        for (const assetUrl of assets) {
            try {
                const filename = sanitizeFilename(assetUrl);
                const dest = path.join(pageDir, filename);

                if (fs.existsSync(dest)) {
                    console.log(`  [SKIP] Exists: ${filename}`);
                    continue;
                }

                await downloadFile(assetUrl, dest);
                console.log(`  [OK] Downloaded: ${filename}`);
            } catch (err) {
                console.error(`  [ERR] Failed ${assetUrl}: ${err}`);
            }
        }
    }
    console.log('[SUCCESS] All assets processed.');
}

runDownloader();
