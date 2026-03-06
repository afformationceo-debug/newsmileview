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
        
        # Extract text from specific semantic tags or commonly used classes
        
        # 1. Headings (h1-h6)
        headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', content, flags=re.DOTALL)
        
        # 2. Paragraphs (p)
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, flags=re.DOTALL)
        
        # Clean tags from extracted text
        def clean_tags(text):
            text = re.sub(r'<[^>]+>', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text

        print(f"--- Analysis for {filepath} ---")
        
        print("\n[HEADINGS]")
        for h in headings:
            cleaned = clean_tags(h)
            if cleaned and len(cleaned) > 1: 
                print(f"- {cleaned}")
                
        print("\n[PARAGRAPHS/CONTENT]")
        for p in paragraphs:
            cleaned = clean_tags(p)
            if cleaned and len(cleaned) > 5: 
                print(f"- {cleaned}")
                
        # Also try to find list items or specific divs that might contain content
        # For Wix sites, content is often in spans or divs with specific classes, but p tags usually catch the bulk text
        
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_meaningful_text('source_prosthetics.html')
