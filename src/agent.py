from src.tools import (
    search_document,
    summarize_document,
    upcoming_events, list_sources

)
def run_agent(query):

    query = query.lower()

    if "summary" in query:
        return summarize_document.invoke(
            {"question": query}
        )

    elif "event" in query:
        return upcoming_events.invoke(
            {"question": query}
        )

    elif "source" in query:
        return list_sources.invoke(
            {"question": query}
        )

    else:
        return search_document.invoke(
            {"question": query}
        )