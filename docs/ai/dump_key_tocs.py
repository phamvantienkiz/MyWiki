import os
from pathlib import Path
from pypdf import PdfReader

books = [
    ("genai/Encyclopedia of LLMs and Foundation Models.pdf", 7, 14, "Encyclopedia of LLMs"),
    ("genai/giao_trinh_rag.pdf", 1, 4, "Giao Trinh RAG"),
    ("genai/giao_trinh_agentic.pdf", 1, 4, "Giao Trinh Agentic AI"),
    ("genai/Agentic AI Design Patterns(2026 Edition).pdf", 1, 3, "Agentic AI Design Patterns 2026"),
    ("genai/Master All 20 Agentic AI Design Patterns.pdf", 1, 4, "Master All 20 Agentic AI Design Patterns"),
    ("machine-learning/Mathematics-for-Machine-Learning.pdf", 6, 12, "Mathematics for Machine Learning"),
    ("machine-learning/understanding-machine-learning-theory-algorithms.pdf", 7, 13, "Understanding Machine Learning"),
    ("deep-learning/The-Principles-of-Deep-Learning-Theory.pdf", 8, 14, "Principles of Deep Learning Theory"),
    ("software/Fundamentals of Database System.pdf", 1, 6, "Fundamentals of Database Systems"),
]

output = []
for rel_path, start_p, end_p, title in books:
    p = Path("resources") / rel_path
    if not p.exists():
        continue
    output.append(f"\n========================================\n# {title} ({rel_path})\n========================================\n")
    reader = PdfReader(p)
    for p_num in range(start_p - 1, min(end_p, len(reader.pages))):
        text = reader.pages[p_num].extract_text() or ""
        output.append(f"--- Page {p_num + 1} ---\n{text}\n")

Path("docs/ai/key_books_toc.md").write_text("\n".join(output), encoding="utf-8")
print("Saved key TOCs to docs/ai/key_books_toc.md")
