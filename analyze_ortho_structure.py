import re
import sys
import glob

# Force UTF-8 output for stdout
sys.stdout.reconfigure(encoding='utf-8')

def clean_text(text):
    # Remove script and style content
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_meaningful_text(filepath, title):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return ""

    result = f"\n\n=== {title} ({filepath}) ===\n"

    # Extract headings specifically
    headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', content, flags=re.IGNORECASE | re.DOTALL)
    result += "--- HEADINGS ---\n"
    for h in headings:
        cleaned = clean_text(h)
        if cleaned:
            result += f"H: {cleaned}\n"

    # Extract other meaningful text blocks (p, div, span with significant length)
    result += "\n--- CONTENT BLOCKS ---\n"
    # Split by tags that usually break blocks
    blocks = re.split(r'<(div|p|br|li|h[1-6])', content)
    
    seen = set()
    for block in blocks:
        text = clean_text(block)
        # Filter: Length > 10, not code-like
        if len(text) > 10 and text not in seen:
            if '{' not in text and 'function' not in text and 'var ' not in text and 'return' not in text:
                result += f"B: {text}\n"
                seen.add(text)
    return result

def main():
    with open('ortho_analysis.txt', 'w', encoding='utf-8') as outfile:
        # List of ortho source files
        files = [
            ("Surgery First", "source_ortho_surgeryfirst.html"),
            ("Non-Surgical", "source_ortho_nonsurgical.html"),
            ("Partial", "source_ortho_partial.html"),
            ("Lingual", "source_ortho_lingual.html"),
            ("Conventional", "source_ortho_conventional.html")
        ]
        
        for title, filename in files:
            print(f"Analyzing {title}...")
            text = extract_meaningful_text(filename, title)
            outfile.write(text)

if __name__ == "__main__":
    main()
