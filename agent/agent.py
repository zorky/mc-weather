from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI

from mcp_server.weather_tools import get_weather
# from mcp_server.geo_tools import get_coordinates_openstreetmap, get_coordinates_openmeteo

MODEL="mistral" #  Mistral-7B-Instruct-v0.3 sous Ollama
# MODEL="llama3:8b"
# MODEL="llama3:8b-instruct-q4_K_M"

LLM_API="http://localhost:11434/v1"  # URL de l'API Ollama

tools = [get_weather]
# tools = [get_coordinates_openstreetmap, get_weather]
# tools = [get_coordinates_openmeteo, get_weather]

# llm -> Ollama ou tout autre LLM compatible LangChain
llm = ChatOpenAI(
    temperature=0,
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
