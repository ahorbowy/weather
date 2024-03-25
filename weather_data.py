import requests  # Import modułu requests
from key import api_key  # Import klucza API


class WeatherData:
    """
    Klasa odpowiedzialna za pobranie danych o pogodzie dla danego miasta
    """

    def __init__(self, city):
        self.city = city

    def fetch_weather(self):
        # Pobieranie danych pogodowych z API
        api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{
            self.city}/today?unitGroup=metric&include=current&key={api_key}&contentType=json"
        response = requests.get(api_url)
        # Pobranie danych pogodowych dla danego dnia
        weather = response.json()["days"][0]
        # Zwrócenie słownika z danymi pogodowymi
        return {
            "temp": weather["temp"],
            "sunrise": weather["sunrise"],
            "sunset": weather["sunset"],
            "pressure": weather["pressure"],
            "windspeed": weather["windspeed"],
            "description": weather["description"],
        }
