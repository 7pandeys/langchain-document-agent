from src.ingest import load_pdf, chunk_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store

def get_vector_store():
    text = load_pdf("data/sample.pdf")

    chunks = chunk_text(text)

    embeddings = get_embeddings()

    return create_vector_store(
        chunks,
        embeddings
    )