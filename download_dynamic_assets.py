import json
import os
import urllib.request
import re

DATA_FILE = 'scraped_data.json'
BASE_DIR = 'images/migrated'

def download_file(url, save_path):
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, save_path)
        print(f"  [OK] Saved to {save_path}")
        return True
    except Exception as e:
        print(f"  [ERR] Failed {url}: {e}")
        return False

def main():
    if not os.path.exists(DATA_FILE):
        print("Data file not found!")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for category, content in data.items():
        print(f"Processing {category}...")
        
        # Create category folder
        cat_dir = os.path.join(BASE_DIR, category)
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)

        # Download Images
        for i, img_url in enumerate(content.get('images', [])):
            if i >= 10: break # Limit to top 10 per category to avoid spam
            
            ext = os.path.splitext(img_url)[1]
            if not ext or len(ext) > 5: ext = '.jpg'
            if 'wixstatic' in img_url:
                 # Clean wix params
                clean_url = img_url.split('/v1/')[0] 
                # Re-check extension
                if '.' in os.path.basename(clean_url):
                    ext = os.path.splitext(clean_url)[1]
            
            save_name = f"{category}_{i+1}{ext}"
            save_path = os.path.join(cat_dir, save_name)
            
            if not os.path.exists(save_path):
                download_file(img_url, save_path)
            else:
                print(f"  [SKIP] {save_name} exists")

        # Download Videos
        for i, vid_url in enumerate(content.get('videos', [])):
            save_name = f"{category}_video_{i+1}.mp4"
            save_path = os.path.join(cat_dir, save_name)
            
            if not os.path.exists(save_path):
                download_file(vid_url, save_path)
            else:
                print(f"  [SKIP] {save_name} exists")

if __name__ == "__main__":
    main()
