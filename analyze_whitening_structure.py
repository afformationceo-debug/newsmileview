import re
import sys

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

def extract_meaningful_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    with open('whitening_analysis.txt', 'w', encoding='utf-8') as outfile:
        # Extract headings specifically
        headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', content, flags=re.IGNORECASE | re.DOTALL)
        outfile.write("--- HEADINGS ---\n")
        print("--- HEADINGS ---")
        for h in headings:
            cleaned = clean_text(h)
            if cleaned:
                outfile.write(f"H: {cleaned}\n")
                print(f"H: {cleaned}")

        # Extract other meaningful text blocks (p, div, span with significant length)
        outfile.write("\n--- CONTENT BLOCKS ---\n")
        print("\n--- CONTENT BLOCKS ---")
        # Split by tags that usually break blocks
        blocks = re.split(r'<(div|p|br|li|h[1-6])', content)
        
        seen = set()
        for block in blocks:
            text = clean_text(block)
            # Filter: Length > 10, not code-like
            if len(text) > 10 and text not in seen:
                if '{' not in text and 'function' not in text and 'var ' not in text and 'return' not in text:
                    outfile.write(f"B: {text}\n")
                    print(f"B: {text}") 
                    seen.add(text)

if __name__ == "__main__":
    extract_meaningful_text('source_whitening.html')
