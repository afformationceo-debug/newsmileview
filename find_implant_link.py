import re

with open('source_prosthetics.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all hrefs
links = re.findall(r'href=["\'](.*?)["\']', content)

print("--- Found Links ---")
for link in links:
    if "implant" in link or "임플란트" in link:
        print(link)
    # Also print all relative links to see structure
    if link.startswith("/") and len(link) > 1:
        print(f"Relative: {link}")
