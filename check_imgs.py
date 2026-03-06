# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"

for fname in ['prosthetics_tw.html', 'prosthetics_jp.html']:
    print(f"=== {fname} ===")
    with open(os.path.join(BASE, fname), 'r', encoding='utf-8') as f:
        html = f.read()
    imgs = re.findall(r'<img[^>]+src="(images/prosthodontics/[^"]+)"', html)
    for img in imgs:
        print(" ", img)
    print()

# Also show LINE btn patterns
for fname in ['index_tw.html', 'index_jp.html']:
    print(f"=== {fname} LINE/Instagram patterns ===")
    with open(os.path.join(BASE, fname), 'r', encoding='utf-8') as f:
        html = f.read()
    patterns = [
        r'<a href="[^"]*" class="line-btn"[^>]*>',
        r'<a href="[^"]*" class="btn-reserve">',
        r'<a href="[^"]*" class="sv-float-btn sv-float-btn--line"[^>]*>',
        r'<a href="[^"]*" class="sv-float-btn sv-float-btn--instagram"[^>]*>',
    ]
    for pat in patterns:
        for m in re.finditer(pat, html):
            print(" ", m.group(0))
    print()
