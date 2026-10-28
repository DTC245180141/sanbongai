import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from docx import Document

docx_path = r"c:\Users\klqdo\Downloads\BAO_CAO_DO_AN_TOT_NGHIEP_SAN_BONG_AI_FULL_PLANTUML (1).docx"
doc = Document(docx_path)

# Print last 60 non-empty paragraphs to see what's at the end
non_empty = [(i, p) for i, p in enumerate(doc.paragraphs) if p.text.strip()]
print(f"Total non-empty paragraphs: {len(non_empty)}")
print(f"\n=== LAST 60 paragraphs ===")
for i, p in non_empty[-60:]:
    print(f"[{i}] [{p.style.name}] {p.text[:100]}")

