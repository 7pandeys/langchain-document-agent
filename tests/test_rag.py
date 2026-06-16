from src.ingest import load_pdf, chunk_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.rag import answer_question
from langchain_community.vectorstores import FAISS

text = load_pdf("data/sample.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings()

vector_store = create_vector_store(
    chunks,
    embeddings
) # run before the demo
# vector_store.save_local("faiss_index") # store and run in the demo
# FAISS.load_local("faiss_index")


question = ["What is the vacation policy?","What is the remote work policy?","What products are listed?","When is the next RAG workshop?"]

for i in question:
    answer = answer_question(
        i,
        vector_store
    )

    print(answer)