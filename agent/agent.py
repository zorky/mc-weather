import os
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI

from mcp_server.weather_tools import get_weather
from mcp_server.geo_tools import get_coordinates_openstreetmap, get_coordinates_openmeteo

MODEL=os.getenv("MODEL", "llama3:8b-instruct-q4_K_M")
LLM_API=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

# MODEL="mistral" #  Mistral-7B-Instruct-v0.3 sous Ollama
# MODEL="llama3:8b" # Modèle Llama 3 8B non quantifié
# MODEL="llama3:8b-instruct-q4_K_M" # Modèle Llama 3 8B Instruct quantifié
# MODEL="qwen3:30b-a3b"
# MODEL="phi3:mini"

LLM_TEMPERATURE=0  # 0 : déterministe et précis, 0.3 : un peu plus créatif

tools = [get_weather]
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
