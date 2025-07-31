import requests
from langchain.tools import tool

@tool
def get_coordinates(city: str) -> tuple:
    """
    Récupère la latitude et la longitude d'une ville (et optionnellement d'un pays)
    à l'aide de l'API Nominatim d'OpenStreetMap.

    Args:
        city (str): Le nom de la ville.
        country (str, optional): Le nom du pays (pour plus de précision).

    Returns:
        dict: Un dictionnaire contenant la latitude et la longitude.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "MCPGeocodingTool/1.0"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return f"Erreur de géocodage pour {city}."

    data = response.json()
    if not data:
        return f"Aucune coordonnée trouvée pour {city}."

    latitude = data[0]["lat"]
    longitude = data[0]["lon"]
    print(f"Coordonnées de {city} : latitude = {latitude}, longitude = {longitude}")
    return latitude, longitude
