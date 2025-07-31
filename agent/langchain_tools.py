from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI  # ou ton LLM local

from mcp_server.geo_tools import get_coordinates
from mcp_server.weather_tools import get_weather

tools = [
    Tool.from_function(get_coordinates),
    Tool.from_function(get_weather),
]

agent = initialize_agent(tools, llm=OpenAI(), agent="zero-shot-react-description", verbose=True)

agent.run("Quelle est la météo des 3 prochains jours à Bordeaux, France ?")