from langgraph.graph import StateGraph
from langgraph.graph import END
from typing import TypedDict
from src.agent_qwen import choose_tool
from src.ingest import chunk_text, load_pdf_documents
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.llm import get_llm

documents = load_pdf_documents(
    "data/sample.pdf"
)

chunks = chunk_text(
    documents
)

embeddings = get_embeddings()

vector_store = create_vector_store(
    chunks,
    embeddings
)

class GraphState(TypedDict):
    question: str
    context: str
    answer: str
    sources: list[str]


def retrieve_node(state):

    docs = vector_store.similarity_search(
        state["question"],
        k=2
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    sources = list(
        {
            doc.metadata["source"]
            for doc in docs
        }
    )

    return {
        **state,
        "context": context,
        "sources": sources
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

# def source_node(state):
#
#     return {
#         **state,
#         "sources":
#         "data/sample.pdf"
#     }

graph = StateGraph(GraphState)

graph.add_node(
    "retrieve",
    retrieve_node
)

graph.add_node(
    "answer",
    answer_node
)

# graph.add_node(
#     "sources",
#     source_node
# )

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
