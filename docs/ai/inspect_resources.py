import os
import sys
from pathlib import Path
from pypdf import PdfReader

RESOURCES_DIR = Path("resources")
OUTPUT_FILE = Path("docs/ai/resources_catalog.md")

def analyze_resources():
    catalog = []
    catalog.append("# Danh mục toàn bộ tài liệu trong `resources/`\n")
    
    categories = sorted([d for d in RESOURCES_DIR.iterdir() if d.is_dir()])
    
    total_files = 0
    pdf_count = 0
    
    for cat in categories:
        catalog.append(f"\n## 📁 Danh mục: `{cat.name}`\n")
        files = sorted(list(cat.rglob("*.*")))
        files = [f for f in files if f.is_file()]
        
        for f in files:
            total_files += 1
            rel_path = f.relative_to(RESOURCES_DIR)
            file_size_mb = f.stat().st_size / (1024 * 1024)
            ext = f.suffix.lower()
            
            info = f"- **`{rel_path.as_posix()}`** ({file_size_mb:.2f} MB)"
            
            if ext == ".pdf":
                pdf_count += 1
                try:
                    reader = PdfReader(f)
                    num_pages = len(reader.pages)
                    info += f" — *{num_pages} trang*"
                    
                    # Try to extract title or first page text snippet
                    if num_pages > 0:
                        first_page_text = reader.pages[0].extract_text() or ""
                        snippet = " ".join(first_page_text.split()[:25])
                        if snippet:
                            info += f"\n  > *Trích đoạn đầu:* {snippet}..."
                except Exception as e:
                    info += f" — *(Lỗi đọc PDF: {str(e)[:50]})*"
            elif ext in [".jpg", ".png", ".jpeg"]:
                info += " — *Hình ảnh sơ đồ kiến thức*"
            elif ext == ".txt":
                try:
                    content = f.read_text(encoding="utf-8", errors="ignore")
                    snippet = " ".join(content.split()[:30])
                    info += f"\n  > *Nội dung:* {snippet}..."
                except Exception as e:
                    info += f" — *(Lỗi đọc txt: {e})*"
            
            catalog.append(info)
            
    catalog.insert(1, f"\n**Tổng số tài liệu:** {total_files} files (trong đó có {pdf_count} files PDF).\n")
    
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(catalog), encoding="utf-8")
    print(f"Hoàn thành phân tích: {total_files} files, ghi vào {OUTPUT_FILE}")

if __name__ == "__main__":
    analyze_resources()
