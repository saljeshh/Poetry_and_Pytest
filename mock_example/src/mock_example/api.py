import requests 
from typing import Dict

def get_weather(city: str) -> Dict:
    response = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
    return response