def get_weather(city: str) -> str:
    fake_weather = {
        "Paris": "Soleil, 25°C",
        "Lyon": "Nuageux, 22°C",
        "Marseille": "Vent fort, 28°C"
    }
    return fake_weather.get(city, f"Aucune donnée météo pour {city}")