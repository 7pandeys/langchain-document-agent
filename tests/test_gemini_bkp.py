from src.rag import get_llm  # gemini
from src.llm import get_llm  # qwen

llm = get_llm()

query = "Summarize the document"

prompt = f"""
You are an AI agent.

Your job is to choose exactly one tool.

Available tools:

1. search_document
   - Use for answering questions from documents

2. summarize_document
   - Use for summarizing documents

3. list_sources
   - Use for showing document sources

4. upcoming_events
   - Use for listing upcoming events

User Request:
{query}

Return ONLY the tool name.
"""

response = llm.invoke(prompt)

print(response.content)