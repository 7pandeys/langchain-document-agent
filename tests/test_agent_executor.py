from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

from src.rag import get_llm
from src.tools import (
    search_document,
    summarize_document
)

llm = get_llm()

tools = [
    search_document,
    summarize_document
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a helpful document assistant."),
        ("human",
         "{input}"),
        ("placeholder",
         "{agent_scratchpad}")
    ]
)

agent = create_tool_calling_agent(
    llm,
    tools,
    prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

response = agent_executor.invoke(
    {
        "input":
        "What is the vacation policy?"
    }
)

print(response)