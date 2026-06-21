from typing import TypedDict

from langgraph.graph import END
from langgraph.graph import StateGraph
from src.embeddings import get_embeddings
from src.ingest import chunk_text, load_pdf_documents
from src.llm import get_llm
from src.vector_store import create_vector_store

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
    retrieved_docs: list
    context: str
    answer: str
    sources: list[str]


def retrieve_node(state):
    docs = vector_store.similarity_search(
        state["question"],
        k=5
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

    # return {
    #     **state,
    #     "context": context,
    #     "sources": sources
    # }
    return {
        **state,
        "retrieved_docs": docs
    }


def answer_node(state):
    prompt = f"""
    You are a document assistant.

    Answer ONLY using the provided context.

    If the answer is not explicitly present in the context,
    reply exactly:

    I could not find that information in the document.

    Do not make assumptions.
    Do not add external knowledge.

    Context:
    {state["context"]}

    Question:
    {state["question"]}
    """

    response = get_llm().invoke(
        prompt
    )

    return {
        **state,
        "answer": response.content
    }


def rerank_node(state):

    docs = state["retrieved_docs"]

    chunks_text = ""

    for i, doc in enumerate(docs):
        chunks_text += f"""
Chunk {i+1}:
{doc.page_content}

"""

    prompt = f"""
Question:
{state["question"]}

Rank these chunks from most relevant to least relevant.

{chunks_text}

Return ONLY chunk numbers.

Example:
1,3,2,5,4
"""

    response = get_llm().invoke(
        prompt
    )

    ranking = response.content.strip()

    print("LLM Ranking:")
    print(ranking)

    # ranked_indices = []
    #
    # for num in ranking.split(","):
    #     ranked_indices.append(
    #         int(num.strip()) - 1
    #     )
    ranked_indices = []

    for num in ranking.split(","):

        idx = int(num.strip()) - 1

        if idx < len(docs):
            ranked_indices.append(idx)

    top_docs = [
        docs[i]
        for i in ranked_indices[:2]
    ]

    context = "\n\n".join(
        doc.page_content
        for doc in top_docs
    )

    sources = list(
        {
            doc.metadata["source"]
            for doc in top_docs
        }
    )

    return {
        **state,
        "context": context,
        "sources": sources
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

# graph.add_node(
#     "sources",
#     source_node
# )

graph.set_entry_point(
    "retrieve"
)

graph.add_node(
    "rerank",
    rerank_node
)

graph.add_edge(
    "retrieve",
    "rerank"
)

graph.add_edge(
    "rerank",
    "answer"
)

graph.add_edge(
    "answer",
    END
)

app = graph.compile()
