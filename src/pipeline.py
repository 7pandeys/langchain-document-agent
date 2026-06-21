from src.ingest import load_pdf_documents, chunk_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store

def get_vector_store():
    text = load_pdf_documents("data/sample.pdf")

    chunks = chunk_text(text)

    embeddings = get_embeddings()

    return create_vector_store(
        chunks,
        embeddings
    )