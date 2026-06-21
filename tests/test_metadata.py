from src.ingest import load_pdf, chunk_text, load_pdf_documents
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.rag import answer_question
from langchain_community.vectorstores import FAISS

text = load_pdf_documents("data/sample.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings()

vector_store = create_vector_store(
    chunks,
    embeddings
)
results = vector_store.similarity_search(
    "vacation policy",
    k=2
)
print(results[0].metadata)
# for doc in results:
#
#     print(doc.page_content)
#
#     print(doc.metadata)