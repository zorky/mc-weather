import requests

def get_coordinates(city: str) -> str:
    """
    Renvoie les coordonnées latitude et longitude pour une ville (optionnellement 'ville, pays').
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
    return f"Coordonnées de {city} : latitude = {latitude}, longitude = {longitude}"