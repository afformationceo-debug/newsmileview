import re
import sys

# Force UTF-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

def extract_meaningful_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove scripts and styles
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
        
        # Clean tags from extracted text
        def clean_tags(text):
            text = re.sub(r'<[^>]+>', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text

        print(f"--- Analysis for {filepath} ---")
        
        # 1. Headings (h1-h6)
        headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', content, flags=re.DOTALL)
        print("\n[HEADINGS]")
        for h in headings:
            cleaned = clean_tags(h)
            if cleaned and len(cleaned) > 1: 
                print(f"- {cleaned}")
                
        # 2. Paragraphs (p)
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, flags=re.DOTALL)
        print("\n[PARAGRAPHS]")
        for p in paragraphs:
            cleaned = clean_tags(p)
            if cleaned and len(cleaned) > 5: 
                print(f"- {cleaned}")

        # 3. Spans with specific classes (Wix often uses these for text)
        # Looking for text that might be missed by p/h tags
        # This is a bit noisy but helpful if p tags are missing
        # spans = re.findall(r'<span[^>]*>(.*?)</span>', content, flags=re.DOTALL)
        # print("\n[SPANS]")
        # for s in spans:
        #     cleaned = clean_tags(s)
        #     if cleaned and len(cleaned) > 20: 
        #         print(f"- {cleaned}")
        
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_meaningful_text('source_laminate.html')
