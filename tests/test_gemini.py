from src.rag import get_llm

llm = get_llm()

response = llm.invoke(
    "What is Retrieval Augmented Generation in one sentence?"
)

print(response.content)