from src.ingest import  load_pdf_documents, chunk_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store

text = load_pdf_documents("data/sample.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings()

vector_store = create_vector_store(
    chunks,
    embeddings
)
query = "When is the next RAG workshop?"
docs = vector_store.similarity_search(
    query,
    k=5
)

for i, doc in enumerate(docs):
    print(f"\nChunk {i+1}")
    print(doc.metadata)
    print(doc.page_content)