import re
import os
import urllib.request

sources = {
    "source_ortho_conventional.html": "ortho_general",
    "source_ortho_lingual.html": "ortho_lingual",
    "source_ortho_nonsurgical.html": "ortho_nonsurgery",
    "source_ortho_partial.html": "ortho_partial",
    "source_ortho_surgeryfirst.html": "ortho_surgery"
}

save_dir = "images/migrated"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

# Step 1: Gather all images per file
file_images = {}
all_image_counts = {}

for fname in sources.keys():
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        imgs = set(re.findall(r'https://static\.wixstatic\.com/media/([^"\')\s]+)', content))
        # Filter for extensions
        imgs = {i for i in imgs if any(ext in i for ext in ['.jpg', '.png', '.webp'])}
        file_images[fname] = imgs
        
        for img in imgs:
            all_image_counts[img] = all_image_counts.get(img, 0) + 1
            
    except Exception as e:
        print(f"Error reading {fname}: {e}")
        file_images[fname] = set()

# Step 2: Identify common images (appearing in > 2 files)
common_images = {img for img, count in all_image_counts.items() if count > 2}
print(f"Found {len(common_images)} common header/footer images to ignore.")

# Step 3: Download unique images
for fname, prefix in sources.items():
    print(f"Processing {fname}...")
    unique_to_file = [img for img in file_images[fname] if img not in common_images]
    
    # Sort to be deterministic? Or maybe reverse to get content which is often later?
    # Usually content images are big. Wix URLs often have dimensions or quality in them but not always in the base name.
    # Let's just take the first 3 *unique* ones.
    
    count = 0
    for img_name in unique_to_file:
        if count >= 3: break
        
        url = f"https://static.wixstatic.com/media/{img_name}"
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
