import re
import os
import urllib.request

# Mapping of source files to target prefixes
sources = {
    "source_ortho_conventional.html": "ortho_general",
    "source_ortho_lingual.html": "ortho_lingual",
    "source_ortho_nonsurgical.html": "ortho_nonsurgery",
    "source_ortho_partial.html": "ortho_partial",
    "source_ortho_surgeryfirst.html": "ortho_surgery"
}

# Common layout/icon images to ignore
IGNORED = [
    "11062b_55e4be1e75564866b6c28290f9a9d271",
    "11062b_8dcadfa428954b1d919f8499f75aa27a",
    "cd2835_83ef872f44624983843b51dd912c59df",
]

save_dir = "images/migrated"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

for fname, prefix in sources.items():
    print(f"Processing {fname}...")
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract all image URLs
        images = re.findall(r'https://static\.wixstatic\.com/media/([^"\')\s]+)', content)
        unique_images = []
        for img in images:
            # Filter matches
            if not any(ig in img for ig in IGNORED) and any(ext in img for ext in ['.jpg', '.png', '.webp']):
                if img not in unique_images:
                    unique_images.append(img)

        # Download first 2 unique images
        count = 0
        for img_name in unique_images:
            if count >= 2: break
            
            url = f"https://static.wixstatic.com/media/{img_name}"
            # Clean extension for filename
            ext = os.path.splitext(img_name)[1]
            if '~mv2' in ext: ext = os.path.splitext(img_name)[1].split('~')[0]
            if not ext: ext = '.jpg'

            save_name = f"{prefix}_{count+1}{ext}"
            save_path = os.path.join(save_dir, save_name)
            
            try:
                print(f"  Downloading {url} to {save_name}")
                urllib.request.urlretrieve(url, save_path)
                count += 1
            except Exception as e:
                print(f"  Failed to download {url}: {e}")

    except Exception as e:
        print(f"Error processing {fname}: {e}")
