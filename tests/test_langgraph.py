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

for i in ["What is the vacation policy?", "Summarize the document", "List the products", "What upcoming events are scheduled?"]:
    response = app.invoke(
        {
            "question":
                i
        }
    )
    print(response)