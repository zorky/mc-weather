from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI

from mcp_server.geo_tools import get_coordinates
from mcp_server.weather_tools import get_weather

tools = [get_coordinates, get_weather]

llm = ChatOpenAI(
    temperature=0,
    model="llama3",
    openai_api_base="http://localhost:11434/v1",
    openai_api_key="sk-ollama",  # Dummy key
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
