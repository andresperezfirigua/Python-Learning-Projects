import requests
import os
from twilio.rest import Client

weather_api_key = os.environ.get("WEATHER_API_KEY")
tw_account_sid = os.environ.get('TW_ACCOUNT_SID')
tw_auth_token = os.environ.get('TW_AUTH_TOKEN')
tw_phone_number = os.environ.get('TW_PHONE_NUMBER')

weather_api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'

parameters = {
    'q': 'Bogota,CO',
    'units': 'metric',
    'lang': 'sp',
    'appid': weather_api_key
}

response = requests.get(url=weather_api_endpoint, params=parameters)

response.raise_for_status()

data = response.json()

condition_code = int(data['weather'][0]['id'])

if condition_code < 700:
    client = Client(tw_account_sid, tw_auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella",
                        from_=tw_phone_number,
                        to='Destination phone number'
                    )
    print(message.status)
