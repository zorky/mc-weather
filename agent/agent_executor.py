import os
import logging
from logger import init_logger
logger = init_logger(level=logging.DEBUG)

from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate

from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama

from mcp_server.weather_tools import get_weather
# from mcp_server.geo_tools import get_coordinates_openstreetmap, get_coordinates_openmeteo

MODEL=os.getenv("MODEL", "llama3:8b-instruct-q4_K_M")
LLM_API=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

LLM_TEMPERATURE=0.3  # 0 : déterministe et précis, 0.3 : un peu plus créatif

# Agent hybride intelligent
def create_hybrid_agent():
    logger.debug("creating hybrid agent")
    logger.debug(f"Utilisation du modèle: {MODEL} sur {LLM_API} avec la temperature {LLM_TEMPERATURE}")
    # llm = Ollama(
    #     model=MODEL,
    #     base_url=LLM_API,
    #     temperature=LLM_TEMPERATURE
    # )
    llm = ChatOpenAI(
        temperature=LLM_TEMPERATURE,
        model=MODEL,
        openai_api_base=LLM_API,
        openai_api_key="dummy-key-ollama",
    )
    # Outils disponibles
    # tools = [get_weather]
    # tools_names = "get_weather"
    tools = [
        Tool(
            name="get_weather",
            func=lambda ville: get_weather(ville),
            description="Obtient les prévisions météo sur plusieurs jours d'une ville. Input: nom de la ville"
        ),
    ]
    # Prompt hybride permettant connaissances générales + outils
    hybrid_prompt = PromptTemplate.from_template("""
Tu es un assistant intelligent polyvalent. Tu peux :
1. Répondre à des questions générales grâce à tes connaissances
2. Utiliser des outils spécialisés pour des informations spécifiques

Outils disponibles: {tool_names}
{tools}

IMPORTANT: 
- Pour les questions générales (histoire, sciences, etc.), réponds directement avec tes connaissances
- Pour la météo, utilise les outils appropriés
- Si une question combine les deux, traite chaque partie séparément

Format ReAct pour les outils seulement:
Question: la question d'entrée
Thought: réflexion sur ce qui est demandé
Action: [OPTIONNEL] outil à utiliser si nécessaire (doit être parmi {tool_names}), sinon réponds directement
Action Input: [OPTIONNEL] paramètres de l'outil
Observation: [OPTIONNEL] résultat de l'outil
Thought: je peux maintenant donner une réponse complète
Final Answer: réponse complète incluant connaissances générales ET résultats d'outils

Question: {input}
Thought: {agent_scratchpad}
""")

    agent = create_react_agent(llm, tools, hybrid_prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5,  # Plus d'itérations pour questions complexes
        return_intermediate_steps=True
    )

    return agent_executor