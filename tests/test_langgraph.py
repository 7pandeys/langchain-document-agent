from langgraph.graph import StateGraph
from langgraph.graph import END
from typing import TypedDict
from src.langgraph_demo import app

# response = app.invoke(
#     {
#         "question":
#         "What is the vacation policy?"
#     }
# )
#
# print(response["answer"])

response = app.invoke(
    {
        "question":
        "What is the vacation policy?"
    }
)
print(response)
response = app.invoke(
    {
        "question":
        "Summarize the document"
    }
)
print(response)