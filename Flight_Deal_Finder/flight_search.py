import requests
import os
import datetime as dt
from flight_data import FlightData

DEPARTURE_LOCATION = 'BOG'

TOMORROW = dt.datetime.now() + dt.timedelta(days=1)
DEP_START_DATE = TOMORROW.strftime('%d/%m/%Y')
DATE_RANGE = dt.datetime.now() + dt.timedelta(days=180)
DEP_LAST_DATE = DATE_RANGE.strftime('%d/%m/%Y')


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
            'location_types': 'city',
            # 'sort': 'name'
        }

        response = requests.get(url=location_endpoint, params=parameters, headers=self.headers)

        return response.json()['locations'][0]['code']

    def search_flights(self, destination):
        search_endpoint = f'{self.tequila_endpoint}/v2/search'
        parameters = {
            'fly_from': DEPARTURE_LOCATION,
            'fly_to': destination,
            'date_from': DEP_START_DATE,
            'date_to': DEP_LAST_DATE,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 10,
            'curr': 'COP',
            'max_stopovers': 0,
            'vehicle_type': 'aircraft'
        }

        response = requests.get(url=search_endpoint, params=parameters, headers=self.headers)
        print(response.status_code)

        try:
            cheapest_flight = response.json()['data'][0]
        except IndexError:
            print(f'No flight found for this destination {destination}\n\n\n')
            return None

        flight_data = FlightData(
            price=cheapest_flight['price'],
            origin_city=cheapest_flight["route"][0]["cityFrom"],
            origin_airport=cheapest_flight["route"][0]["flyFrom"],
            destination_city=cheapest_flight["route"][0]["cityTo"],
            destination_airport=cheapest_flight["route"][0]["flyTo"],
            out_date=cheapest_flight["route"][0]["local_departure"].split("T")[0],
            return_date=cheapest_flight["route"][1]["local_departure"].split("T")[0]
        )

        print(f'Departure: {flight_data.origin_city}\n'
              f'Code: {flight_data.origin_airport}\n'
              f'Destination: {flight_data.destination_city}\n'
              f'Code: {flight_data.destination_airport}\n'
              f'Nights in destination: {cheapest_flight["nightsInDest"]}\n'
              f'From: {flight_data.out_date} to {flight_data.return_date}\n'
              f'Price: ${int(flight_data.price)}\n'
              )

        print(f'Cantidad de vuelos encontrados para {flight_data.origin_city}: '
              f'{len(response.json()["data"])}\n\n\n')

        return flight_data
