from src.llm import get_llm
from src.tools import (
    search_document,
    summarize_document,
)

llm = get_llm()

def choose_tool(query):
    prompt = f"""
    You are a routing agent.
    You are a document assistant.

    Answer ONLY using the provided context.

    If the answer is not present in the context,
    reply:

    "I could not find that information in the document."
    
    Do not use external knowledge.

    Available tools:

    search_document
    - Use when the user asks a question about the document.

    summarize_document
    - Use when the user wants a summary of the document.

    User Request:
    {query}

    Return EXACTLY one tool name.

    Allowed outputs:
    search_document
    summarize_document

    No explanation.
    No spaces.
    No punctuation.
    """

    response = llm.invoke(prompt)

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

    return "No tool selected."