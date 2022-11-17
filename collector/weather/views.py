import os
import time

import requests
from django.shortcuts import get_object_or_404
from dotenv import load_dotenv

from cities.models import City
from weather.models import Weather

load_dotenv()


def save_weather(request):
    cities_list = City.objects.all()
    api_key = os.getenv('API_KEY')
    for city in cities_list:
        lat = city.lat
        lon = city.lon
        try:
            url = (f'https://api.openweathermap.org/data/2.5/weather?'
                   f'lat={lat}&lon={lon}&exclude=current&'
                   f'units=metric&appid={api_key}'
                   )
            response = requests.get(url).json()
        except requests.exceptions.ConnectionError:
            return 'Error, сайт не доступен'

        try:
            weather = get_object_or_404(Weather, city=city.id)
            weather.temp = response['main']['temp']

        except:
            Weather.objects.create(city=city,
                                   temp=response['main']['temp'],
                                   )
    time.sleep(3600)
    return save_weather(request)
