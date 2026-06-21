from src.llm import get_llm
from src.tools import (
    search_document,
    summarize_document,
    upcoming_events, list_sources
)

llm = get_llm()

def choose_tool(query):
    tool_prompt = f"""
    You are a routing agent.

    Available tools:

    search_document
    - Answer questions from document

    summarize_document
    - Summarize document
    
    list_sources
    - Show document source information and page numbers
    
    upcoming_events
    - Extract upcoming events, workshops and dates from documents

    User Request:
    {query}

    Return EXACTLY one tool name.

    Allowed outputs:

    search_document
    summarize_document
    list_sources
    upcoming_events
    """

    response = llm.invoke(tool_prompt)

    # return response.content.strip()
    return response.content.strip().lower().replace(" ", "")

def run_agent(query):

    tool_name = choose_tool(query)

    print(f"Chosen Tool: {tool_name}")

    if tool_name == "search_document":
        return search_document.invoke(
            {"question": query}
        )

    elif tool_name == "summarize_document":
        return summarize_document.invoke(
            {"question": query}
        )

    elif tool_name == "list_sources":
        return list_sources.invoke(
            {"question": query}
        )

    elif tool_name == "upcoming_events":
        return upcoming_events.invoke(
            {"question": query}
        )

    return "No tool selected."