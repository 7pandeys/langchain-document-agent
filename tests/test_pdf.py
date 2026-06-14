from src.ingest import load_pdf
text = load_pdf("data/sample.pdf")

print(text[:500])