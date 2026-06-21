from langgraph.graph import StateGraph
from langgraph.graph import END
from typing import TypedDict
from src.agent_qwen import choose_tool
from src.ingest import chunk_text, load_pdf_documents
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.llm import get_llm



class GraphState(TypedDict):
    question: str
    tool: str
    answer: str
    context: str


def retrieve_node(state):
    text = load_pdf_documents("data/sample.pdf")

    chunks = chunk_text(text)

    embeddings = get_embeddings()

    vector_store = create_vector_store(
        chunks,
        embeddings
    )
    docs = vector_store.similarity_search(
        state["question"],
        k=2
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return {
        **state,
        "context": context
    }


def answer_node(state):
    prompt = f"""
Answer ONLY using context.

Context:
{state['context']}

Question:
{state['question']}
"""

    response = get_llm().invoke(
        prompt
    )

    return {
        **state,
        "answer": response.content
    }


graph = StateGraph(GraphState)

graph.add_node(
    "retrieve",
    retrieve_node
)

graph.add_node(
    "answer",
    answer_node
)

graph.set_entry_point(
    "retrieve"
)

graph.add_edge(
    "retrieve",
    "answer"
)

graph.add_edge(
    "answer",
    END
)

app = graph.compile()
