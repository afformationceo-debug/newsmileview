import re

with open('source_invisalign.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Images
images = re.findall(r'https://static\.wixstatic\.com/media/[a-zA-Z0-9_.-]+', content)
unique_images = list(set(images))

print("--- FOUND IMAGES ---")
for img in unique_images:
    if 'jpg' in img or 'png' in img or 'webp' in img:
        print(img)

# Extract Text Context (simple find)
print("\n--- FOUND TEXT ---")
keywords = ["투명하고 편리한", "왜 많은 사람들이", "치료 과정"]
for k in keywords:
    start = content.find(k)
    if start != -1:
        print(f"Found '{k}': {content[start:start+200]}...")
