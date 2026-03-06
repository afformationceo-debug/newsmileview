# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"C:\Users\rlcks\OneDrive\Desktop\SMILEVIEW"

with open(os.path.join(BASE, 'index_jp.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Test each pattern
tests = [
    ('nav INVISALIGN', 'href="invisalign_jp.html">INVISALIGN</a>' in html),
    ('lang-current button exact', '<button class="lang-current" onclick="document.getElementById(\'langSelector\').classList.toggle(\'open\')">JP</button>' in html),
    ('line-btn href=#', '<a href="#" class="line-btn"' in html),
    ('btn-reserve href=#', '<a href="#" class="btn-reserve">' in html),
    ('float-btn-line href=#', '<a href="#" class="sv-float-btn sv-float-btn--line"' in html),
    ('instagram smileview_dental', 'href="https://www.instagram.com/smileview_dental/" class="sv-float-btn sv-float-btn--instagram"' in html),
]

print("=== index_jp.html pattern tests ===")
for name, found in tests:
    print(f"  {'OK' if found else 'FAIL'}  {name}")

# Show actual nav content around invisalign
print("\n=== actual nav invisalign link ===")
m = re.search(r'href="invisalign_jp\.html"[^<]{0,50}</a>', html)
if m:
    print(f"  {m.group(0)!r}")

# Show actual lang-current button
print("\n=== actual lang-current button ===")
m = re.search(r'<button class="lang-current"[^>]*>[^<]*</button>', html)
if m:
    print(f"  {m.group(0)!r}")

# Show line-btn
print("\n=== actual line-btn ===")
m = re.search(r'<a [^>]*class="line-btn"[^>]*>', html)
if m:
    print(f"  {m.group(0)!r}")

# Show btn-reserve
print("\n=== actual btn-reserve ===")
m = re.search(r'<a [^>]*class="btn-reserve"[^>]*>', html)
if m:
    print(f"  {m.group(0)!r}")

# Show float-line-btn
print("\n=== actual sv-float-btn--line ===")
m = re.search(r'<a [^>]*class="sv-float-btn sv-float-btn--line"[^>]*>', html)
if m:
    print(f"  {m.group(0)!r}")

# Show instagram
print("\n=== actual instagram btn ===")
m = re.search(r'<a [^>]*instagram[^>]*>', html)
if m:
    print(f"  {m.group(0)!r}")
