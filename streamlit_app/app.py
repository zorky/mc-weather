import streamlit as st
import requests
import os

# import logging
# from logger import init_logger

# logger = init_logger(level=logging.DEBUG)

AGENT_WEATHER_URL = os.getenv("AGENT_WEATHER_URL", "http://localhost:8000/ask")
print(AGENT_WEATHER_URL)
st.set_page_config(page_title="Agent météo", page_icon="⛅")

st.title("Assistant météo avec Ollama + Tools 🌍")
st.markdown("Posez une question, par exemple : *Quelle est la météo à Paris demain ?*")

user_input = st.text_input("Votre question", placeholder="Ex: Quelle est la météo à Lyon dans 2 jours ?")

if st.button("Envoyer") and user_input.strip():
    with st.spinner("Réflexion de l'agent... 🤔"):
        try:
            print(f"Envoi de la question à l'API {AGENT_WEATHER_URL}")
            # Envoie la question à ton API backend
            response = requests.get(
                f"{AGENT_WEATHER_URL}?question={user_input}",  # adapte selon ton endpoint
                timeout=240
            )
            if response.status_code == 200:
                answer = response.json().get("response", "Pas de réponse.")
                st.success(answer)
            else:
                st.error(f"Erreur API : {response.status_code}")
        except Exception as e:
            st.error(f"Erreur lors de l'appel à l'API : {e}")