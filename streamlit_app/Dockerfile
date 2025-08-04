FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier l'app Streamlit
COPY app.py .

# Installer Streamlit (et requests si tu fais des appels à ton backend FastAPI)
RUN pip install --no-cache-dir streamlit requests

# Port par défaut de Streamlit
EXPOSE 8501

# Lancer l'application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]