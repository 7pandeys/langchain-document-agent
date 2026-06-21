from langgraph.graph import StateGraph
from langgraph.graph import END
from typing import TypedDict

class GraphState(TypedDict):
    question: str
def search_node(state):

    print("Search Node Executed")

    return state

graph = StateGraph(GraphState)

graph.add_node(
    "search",
    search_node
)

graph.set_entry_point(
    "search"
)

graph.add_edge(
    "search",
    END
)

app = graph.compile()
