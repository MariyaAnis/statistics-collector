import requests
import os
import time

from cities.models import City
from weather.models import Weather
from dotenv import load_dotenv
load_dotenv()


def save_weather(request):
    cities_list = City.objects.all()
    api_key = os.getenv('API_KEY')
    for city in cities_list:
        lat = city.lat
        lon = city.lon
        try:
            url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=current&units=metric&appid={api_key}'
        except:
            return('error, сайт не доступен')
        response = requests.get(url).json()
        weather, created = Weather.objects.get_or_create(city=city)
        weather.temp = response[current][temp]
        weather.rain = response[current][rain]
        weather.clouds = response[current][clouds]
        weather.wind_speed = response[current][wind_speed]

    time.sleep(3600)
    return save_weather(request)