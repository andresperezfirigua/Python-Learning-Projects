import requests
import os
from twilio.rest import Client

weather_api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'

parameters = {
    'q': 'Bogota,CO',
    'units': 'metric',
    'lang': 'sp',
    'appid': 0 # Weather Key here
}

response = requests.get(url=weather_api_endpoint, params=parameters)

response.raise_for_status()

data = response.json()

condition_code = int(data['weather'][0]['id'])

if condition_code < 700:
    print('Bring an umbrella')


