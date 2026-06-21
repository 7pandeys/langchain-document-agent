from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY
from src.llm import get_llm

# def get_llm():
#     return ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",
#         google_api_key=GOOGLE_API_KEY,
#         temperature=0
#     )


def answer_question(question, vector_store):
    docs = vector_store.similarity_search(
        question,
        # k=5
        k=1
    )

    print("\nRetrieved Chunks")
    print("=" * 50)

    for doc in docs:
        print(doc.page_content[:300])
        print()
    # Source Attribution

    unique_sources = set()

    for doc in docs:
        unique_sources.add(
            f"{doc.metadata['source']} "
            f"(Page {doc.metadata['page']})"
        )


    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
    You are a document assistant.
    
    Answer using ONLY the provided context.
    
    If the answer is not present in the context,
    reply:
    "I could not find that information in the document."
    
    Context:
    {context}
    
    Question:
    {question}
    """

    llm = get_llm()

    response = llm.invoke(prompt)

    answer = response.content

    return (
            f"{answer}\n\n"
            f"Sources:\n"
            + "\n".join(unique_sources)
    )