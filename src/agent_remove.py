from src.tools import (
    search_document,
    summarize_document
)

def run_agent(query: str):

    query_lower = query.lower()

    if "summarize" in query_lower:
        return summarize_document.invoke(
            {"question": query}
        )

    return search_document.invoke(
        {"question": query}
    )
#
# agent = create_tool_calling_agent(
#     llm,
#     tools,
#     prompt
# )