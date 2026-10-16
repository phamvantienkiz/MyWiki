import os
from pathlib import Path
from pypdf import PdfReader

def extract_snippets(pdf_path, search_terms, max_pages=100):
    p = Path(pdf_path)
    if not p.exists():
        return f"File {pdf_path} not found"
    try:
        reader = PdfReader(p)
        results = []
        for i, page in enumerate(reader.pages[:max_pages]):
            text = page.extract_text() or ""
            for term in search_terms:
                if term.lower() in text.lower():
                    results.append((i+1, term, text[:400].replace("\n", " ")))
                    break
        return results
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    terms = ["transformer", "rag", "retrieval", "agent", "react", "lora", "rlhf", "mle", "bias-variance"]
    # Check GenAI books
    print("GenAI Encyclopedia terms:")
    enc_results = extract_snippets("resources/genai/Encyclopedia of LLMs and Foundation Models.pdf", terms, 50)
    for page, term, snippet in enc_results[:5]:
        print(f"Page {page} [{term}]: {snippet[:150]}...")
