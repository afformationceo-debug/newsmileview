import re

with open('source_invisalign.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Links
links = re.findall(r'href="https://www\.smile-vdental\.com/[^"]+"', content)
unique_links = sorted(list(set(links)))

print(f"--- FOUND {len(unique_links)} LINKS ---")
for link in unique_links:
    print(link)
