import re
import os
import urllib.request

save_dir = "images/migrated"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

with open('source_whitening.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Capture everything until a quote, space, or parenthesis
# Filter common noise
images = re.findall(r'https://static\.wixstatic\.com/media/([^"\')\s]+)', content)
unique_images = []
ignored = [
    "11062b_55e4be1e75564866b6c28290f9a9d271", 
    "11062b_8dcadfa428954b1d919f8499f75aa27a",
    "cd2835_83ef872f44624983843b51dd912c59df", 
    "e66ac7_8b72941613c44f84907bd409a2efe7a3", # likely footer logo
    "e66ac7_95e9bd6fa15a4d94b5b5cf1bbc4f60fc", # likely icon
]

for img in images:
    if not any(ig in img for ig in ignored) and any(ext in img for ext in ['.jpg', '.png', '.webp']):
        clean_img = img.split('/v1/')[0]
        if clean_img not in unique_images:
            unique_images.append(clean_img)

print(f"--- DOWNLOADING {len(unique_images)} IMAGES ---")
for i, img_name in enumerate(unique_images):
    if i >= 5: break # Limit to top 5 relevant images
    
    url = f"https://static.wixstatic.com/media/{img_name}"
    ext = os.path.splitext(img_name)[1]
    if '~mv2' in ext: ext = os.path.splitext(img_name)[1].split('~')[0]
    if not ext: ext = '.jpg'

    save_name = f"whitening_{i+1}{ext}"
    save_path = os.path.join(save_dir, save_name)
    
    try:
        print(f"  Downloading {url} to {save_name}")
        urllib.request.urlretrieve(url, save_path)
    except Exception as e:
        print(f"  Failed to download {url}: {e}")
