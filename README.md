# Sous Windows et WSL

```bash
wsl
```

# Initialisation environement python

## UV

```bash
uv .venv
source .venv/bin/activate
uv sync
```

## PIP

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Météo et coordonnées

- l'API météo utilisée est : https://open-meteo.com/ - ne nécessite pas de clé d'API, open-meteo permet de récupérer les prévisions météo à 7 jours pour une ville donnée, avec les températures minimales et maximales, ainsi que les précipitations à partir des coordonnées géographiques (latitude et longitude).
- l'API de géocodage sera utilisée pour obtenir les coordonnées GPS : https://nominatim.openstreetmap.org/ (autre alternative : https://geocoding-api.open-meteo.com/v1/search), User-Agent doit être identifié dans les headers de la requête

# Lancer le serveur MCP avec l'ASGI uvicorn pour FastAPI

```bash
uvicorn main:app --reload
```

L'API est disponible à l'adresse suivante : http://127.0.0.1:8000/docs

- les *tools* sont disponibles à l'adresse : http://127.0.0.1:8000/mcp/tools
- un appel vers le tool `mcp` est disponible à l'adresse : http://127.0.0.1:8000/mcp/tool_call avec le schéma MCP

```json
{
  "name": "get_weather",
  "parameters": {
    "city": "Paris"
  }
}
```
par exemple avec la commande `curl` :

```bash
curl -X POST http://127.0.0.1:8000/mcp/tool_call \
  -H "Content-Type: application/json" \
  -d '{
    "name": "get_weather",
    "parameters": {
      "city": "Paris, France"
    }
  }'
  {"result":"Prévisions météo pour les 3 prochains jours :\n- 2025-07-31 : 16.3°C → 26.1°C, pluie : 0.2 mm\n- 2025-08-01 : 18.0°C → 24.9°C, pluie : 0.2 mm\n- 2025-08-02 : 14.8°C → 23.5°C, pluie : 0.0 mm\n"}
```
les coordonnées de la ville sont récupérées via l'API de géocodage, puis la météo est récupérée via l'API météo.

```bash
curl -X POST http://127.0.0.1:8000/mcp/tool_call \
  -H "Content-Type: application/json" \
  -d '{
    "name": "get_coordinates",
    "parameters": {
      "city": "Paris, France"
    }
  }'
  {"result":"Coordonnées de Paris : latitude = 48.8588897, longitude = 2.3200410"}
```

