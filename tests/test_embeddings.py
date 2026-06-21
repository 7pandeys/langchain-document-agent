from src.ingest import  load_pdf_documents, chunk_text
from src.embeddings import get_embeddings

text = load_pdf_documents("data/sample.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings()

vector = embeddings.embed_query(chunks[0])

print(type(vector))
print(len(vector))
print(vector[:10])