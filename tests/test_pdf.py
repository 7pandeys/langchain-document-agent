from src.ingest import load_pdf_documents
text = load_pdf_documents("data/sample.pdf")

print(text[:500])