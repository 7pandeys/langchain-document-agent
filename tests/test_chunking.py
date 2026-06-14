from src.ingest import load_pdf, chunk_text

text = load_pdf("data/sample.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk[:200])