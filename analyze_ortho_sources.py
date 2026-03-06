import re
import os

files = [
    "source_ortho_conventional.html",
    "source_ortho_lingual.html",
    "source_ortho_nonsurgical.html",
    "source_ortho_partial.html",
    "source_ortho_surgeryfirst.html"
]

keywords = {
    "source_ortho_conventional.html": ["일반", "클리피씨", "메탈", "세라믹"],
    "source_ortho_lingual.html": ["설측", "콤비", "안보이게"],
    "source_ortho_nonsurgical.html": ["비수술", "돌출입"],
    "source_ortho_partial.html": ["부분", "MTA", "앞니"],
    "source_ortho_surgeryfirst.html": ["선수술", "양악"]
}

print("--- KEYWORD ANALYSIS ---")
for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"\nFile: {fname}")
            
            # Check keywords
            found_keys = []
            for k in keywords.get(fname, []):
                if k in content:
                    found_keys.append(k)
            print(f"  Matched Keywords: {found_keys}")

            # Extract Images
            images = re.findall(r'https://static\.wixstatic\.com/media/[^"\')\s]+', content)
            unique_images = sorted(list(set(images)))
            print(f"  Found {len(unique_images)} images")
            
            # Print first 3 jpg/png images for verification
            count = 0
            for img in unique_images:
                if any(x in img for x in ['.jpg', '.png', '.webp']) and count < 3:
                    print(f"  Image: {img.split('/v1/')[0]}")
                    count += 1

    except Exception as e:
        print(f"Error reading {fname}: {e}")
