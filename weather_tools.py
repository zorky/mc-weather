import requests
from geo_tools import get_coordinates
def get_weather(city: str) -> str:
    # fake_weather = {
    #     "Paris": "Soleil, 25°C",
    #     "Lyon": "Nuageux, 22°C",
    #     "Marseille": "Vent fort, 28°C"
    # }
    lat, lon = get_coordinates(city)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return "Erreur de récupération des données météo."
    data = response.json()
    if "daily" not in data:
        return "Pas de données météo disponibles."
    forecast = data["daily"]
    output = "Prévisions météo pour les 3 prochains jours :\n"
    for i in range(min(3, len(forecast["time"]))):
        day = forecast["time"][i]
        t_min = forecast["temperature_2m_min"][i]
        t_max = forecast["temperature_2m_max"][i]
        rain = forecast["precipitation_sum"][i]
        output += f"- {day} : {t_min}°C → {t_max}°C, pluie : {rain} mm\n"
    print(f"Météo pour {city} : {output.strip()}")
    return output
    # return fake_weather.get(city, f"Aucune donnée météo pour {city}")