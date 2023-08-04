import requests
import os
import pprint
import datetime as dt
from flight_data import FlightData

DEPARTURE_LOCATION = 'BOG'

TOMORROW = dt.datetime.now() + dt.timedelta(days=1)
DEP_START_DATE = TOMORROW.strftime('%d/%m/%Y')
DATE_RANGE = dt.datetime.now() + dt.timedelta(days=180)
DEP_LAST_DATE = DATE_RANGE.strftime('%d/%m/%Y')

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'
TEQUILA_API_KEY = os.environ.get('Flight_Deal_Finder_Tequila_Key')


class FlightSearch:
    def __init__(self):
        self.headers = {
            'apikey': TEQUILA_API_KEY
        }

    # /locations/query
    def find_iata_code(self, city_name):
        location_endpoint = f'{TEQUILA_ENDPOINT}/locations/query'
        parameters = {
            'term': city_name,
            'location_types': 'city',
            # 'sort': 'name'
        }

        response = requests.get(url=location_endpoint, params=parameters, headers=self.headers)

        return response.json()['locations'][0]['code']

    def search_flights(self, destination):
        search_endpoint = f'{TEQUILA_ENDPOINT}/v2/search'
        parameters = {
            'fly_from': DEPARTURE_LOCATION,
            'fly_to': destination,
            'date_from': DEP_START_DATE,
            'date_to': DEP_LAST_DATE,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 10,
            'one_for_city': 1,
            'curr': 'COP',
            'max_stopovers': 0,
            'vehicle_type': 'aircraft'
        }

        response = requests.get(url=search_endpoint, params=parameters, headers=self.headers)
        # print(response.status_code)

        try:
            cheapest_flight = response.json()['data'][0]
        except IndexError:
            print(f'\nNo direct flights found for this destination {destination}\n\n\n')
            parameters['max_stopovers'] = 2
            response = requests.get(url=search_endpoint, params=parameters, headers=self.headers)
            # pprint.pprint(response.json())

            try:
                cheapest_flight = response.json()['data'][0]

            except:
                print('\nNo flights found for this destination at all.')
                return None

            else:
                flight_data = FlightData(
                    price=int(cheapest_flight['price']),
                    origin_city=cheapest_flight["cityFrom"],
                    origin_airport=cheapest_flight["cityCodeFrom"],
                    destination_city=cheapest_flight["cityTo"],
                    destination_airport=cheapest_flight["cityCodeTo"],
                    out_date=cheapest_flight["route"][0]["local_departure"].split("T")[0],
                    return_date=cheapest_flight["route"][-1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=cheapest_flight["route"][0]["cityTo"],
                    number_of_days=cheapest_flight['nightsInDest']
                )

                # print(f'Departure: {flight_data.origin_city}\n'
                #       f'Code: {flight_data.origin_airport}\n'
                #       f'Destination: {flight_data.destination_city}\n'
                #       f'Code: {flight_data.destination_airport}\n'
                #       f'Nights in destination: {flight_data.number_of_days}\n'
                #       f'From: {flight_data.out_date} to {flight_data.return_date}\n'
                #       f'Price: ${flight_data.price}\n'
                #       )

                return flight_data

        else:
            flight_data = FlightData(
                price=int(cheapest_flight['price']),
                origin_city=cheapest_flight["route"][0]["cityFrom"],
                origin_airport=cheapest_flight["route"][0]["flyFrom"],
                destination_city=cheapest_flight["route"][0]["cityTo"],
                destination_airport=cheapest_flight["route"][0]["flyTo"],
                out_date=cheapest_flight["route"][0]["local_departure"].split("T")[0],
                return_date=cheapest_flight["route"][1]["local_departure"].split("T")[0],
                number_of_days=cheapest_flight['nightsInDest']
            )

            # print(f'Departure: {flight_data.origin_city}\n'
            #       f'Code: {flight_data.origin_airport}\n'
            #       f'Destination: {flight_data.destination_city}\n'
            #       f'Code: {flight_data.destination_airport}\n'
            #       f'Nights in destination: {flight_data.number_of_days}\n'
            #       f'From: {flight_data.out_date} to {flight_data.return_date}\n'
            #       f'Price: ${flight_data.price}\n'
            #       )

            return flight_data
