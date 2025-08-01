from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI

from mcp_server.geo_tools import get_coordinates
from mcp_server.weather_tools import get_weather

# MODEL="tinyllama"
MODEL="llama3:8b"

tools = [get_coordinates, get_weather]
# tools = [get_weather]

# llm -> Ollama ou tout autre LLM compatible LangChain
llm = ChatOpenAI(
    temperature=0,
    model=MODEL,
    openai_api_base="http://localhost:11434/v1",
    openai_api_key="dummy-key-ollama",
)

# agent inférence -> LangChain Agent : llm + tools
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
