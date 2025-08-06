import os
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI

from mcp_server.crypto_price import get_crypto_price
from mcp_server.weather_tools import get_weather
# from mcp_server.geo_tools import get_coordinates_openstreetmap, get_coordinates_openmeteo

MODEL=os.getenv("MODEL", "llama3:8b-instruct-q4_K_M")
LLM_API=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

LLM_TEMPERATURE=0.3  # 0 : déterministe et précis, 0.3 : un peu plus créatif

tools = [get_weather, get_crypto_price]
# tools = [get_weather, get_coordinates_openstreetmap]
# tools = [get_coordinates_openmeteo, get_weather]

# llm -> Ollama ou tout autre LLM compatible LangChain
llm = ChatOpenAI(
    temperature=LLM_TEMPERATURE,
    model=MODEL,
    openai_api_base=LLM_API,
    openai_api_key="dummy-key-ollama",
)

# agent inférence -> LangChain Agent : llm + tools
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
