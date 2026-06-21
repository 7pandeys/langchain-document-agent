from langchain.tools import tool
from src.llm import get_llm
from src.pipeline import get_vector_store
from src.rag import answer_question


vector_store = get_vector_store()
@tool
def search_document(question: str) -> str:
    """
    Search document and return relevant information.
    """
    return answer_question(
        question,
        vector_store
    )

@tool
def summarize_document(question: str):
    """
    Summarize the entire document.
    """

    docs = vector_store.similarity_search(
        "",
        k=20
    )

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Summarize this document.

Context:
{context}
"""

    response = get_llm().invoke(prompt)

    return response.content
@tool
def list_sources(question: str):
    """
    List document sources and page numbers.
    """

    docs = vector_store.similarity_search(
        question,
        k=5
    )

    sources = set()

    for doc in docs:
        sources.add(
            f"{doc.metadata['source']} "
            f"(Page {doc.metadata['page']})"
        )

    return "\n".join(sources)

@tool
def upcoming_events(question: str):
    """
    Extract upcoming events and dates from documents.
    """

    docs = vector_store.similarity_search(
        "events workshop meeting dates",
        k=5
    )

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Extract upcoming events and dates.

Context:
{context}

Return only events.
"""

    response = get_llm().invoke(prompt)

    return response.content
