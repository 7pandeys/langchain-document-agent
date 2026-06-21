from langgraph.graph import StateGraph
from langgraph.graph import END
from typing import TypedDict
from src.langgraph_rag_chain import app

response = app.invoke(
    {
        "question":
        "What is the vacation policy?"
    }
)

print(response)