import re
import os

with open('source_whitening.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all image URLs
images = re.findall(r'https://static\.wixstatic\.com/media/([^"\')\s]+)', content)
unique_images = []
ignored = [
    "11062b_55e4be1e75564866b6c28290f9a9d271", # social icon?
    "11062b_8dcadfa428954b1d919f8499f75aa27a", # social icon?
    "cd2835_83ef872f44624983843b51dd912c59df", # logo?
]

print(f"--- FOUND {len(images)} IMAGES ---")
for img in images:
    # Filter matches
    if not any(ig in img for ig in ignored) and any(ext in img for ext in ['.jpg', '.png', '.webp']):
        if img not in unique_images:
            unique_images.append(img)

print(f"--- UNIQUE IMAGES: {len(unique_images)} ---")
for i, img in enumerate(unique_images):
    print(f"Image {i+1}: https://static.wixstatic.com/media/{img}")
