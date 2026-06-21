from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0
    )


def answer_question(question, vector_store):
    docs = vector_store.similarity_search(
        question,
        k=2
    )


    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
    You are a document question-answering assistant.

    Use ONLY the provided context.

    If the answer is not present in the context, respond:

    "I could not find that information in the provided document."

    Do not use external knowledge.

    Context:
    {context}

    Question:
    {question}
    """

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content