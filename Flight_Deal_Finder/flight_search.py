import requests
import os

class FlightSearch:
    def __init__(self):
        self.tequila_endpoint = 'https://api.tequila.kiwi.com'
        self.headers = {
            'apikey': os.environ.get('Flight_Deal_Finder_Tequila_Key')
        }

    # /locations/query
    def find_iata_code(self, city_name):
        location_endpoint = f'{self.tequila_endpoint}/locations/query'
        parameters = {
            'term': city_name,
            # 'location_types': 'city',
            # 'sort': 'name'
        }

        response = requests.get(url=location_endpoint, params=parameters, headers=self.headers)

        return response.json()['locations'][0]['code']
