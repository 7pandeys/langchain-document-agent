from src.ingest import load_pdf, chunk_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store

text = load_pdf("data/sample.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings()

vector_store = create_vector_store(
    chunks,
    embeddings
)

query = "What is the vacation policy?"

results = vector_store.similarity_search(
    query,
    k=2
)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print(doc.page_content)