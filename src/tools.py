from langchain.tools import tool

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
def summarize_document(question: str) -> str:
    """
    Summarize document.
    """
    return answer_question(
        question,
        vector_store
    )
@tool
def list_sources(question: str):
    """
    List document.
    """
    return answer_question(
        question,
        vector_store
    )

@tool
def upcoming_events(question: str):
    """
    Upcoming events document.
    """
    return answer_question(
        question,
        vector_store
    )
# @tool
# def search_document(question: str) -> str:
#     """
#     Search the document and answer questions.
#     """
#
#     return f"Searching document for: {question}"
#
#
# @tool
# def summarize_document(_: str) -> str:
#     """
#     Summarize the document.
#     """
#
#     return "This document contains company policies, product specifications and FAQs."