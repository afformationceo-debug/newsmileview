import re

with open('source_invisalign.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Capture everything until a quote, space, or parenthesis
images = re.findall(r'https://static\.wixstatic\.com/media/[^"\')\s]+', content)
unique_images = sorted(list(set(images)))

print(f"--- FOUND {len(unique_images)} IMAGES ---")
for img in unique_images:
    # Filter for likely image extensions or high-res
    if any(x in img for x in ['.jpg', '.png', '.webp', '.jpeg']):
        # Clean up trailing characters if any
        clean_img = img.split('/v1/')[0] 
        print(clean_img)
