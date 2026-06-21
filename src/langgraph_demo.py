from langgraph.graph import StateGraph
from langgraph.graph import END
from typing import TypedDict
from src.tools import search_document, summarize_document
from agent_qwen import choose_tool


class GraphState(TypedDict):
    question: str
    tool: str
    answer: str


def router_node(state):

    question = state["question"]

    if "summarize" in question.lower():
        tool = "summary"
    else:
        tool = "search"

    print(f"Router selected: {tool}")

    return {
        **state,
        "tool": tool
    }


def search_node(state):

    answer = search_document.invoke(
        {
            "question":
            state["question"]
        }
    )

    return {
        **state,
        "answer": answer
    }

def summary_node(state):

    answer = summarize_document.invoke(
        {
            "question":
            state["question"]
        }
    )

    return {
        **state,
        "answer": answer
    }

def route_tool(state):

    return state["tool"]


graph = StateGraph(GraphState)

graph.add_node(
    "router",
    router_node
)

graph.add_node(
    "search",
    search_node
)

graph.add_node(
    "summary",
    summary_node
)

graph.set_entry_point(
    "router"
)

graph.add_conditional_edges(
    "router",
    route_tool,
    {
        "search": "search",
        "summary": "summary"
    }
)

graph.add_edge(
    "search",
    END
)

graph.add_edge(
    "summary",
    END
)

app = graph.compile()
