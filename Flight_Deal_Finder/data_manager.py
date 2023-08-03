import requests
import os

SHEETY_ENDPOINT = os.environ.get('Flight_Deal_Finder_Sheety_Endpoint')
SHEETY_API_KEY = os.environ.get('Flight_Deal_Finder_Sheety_Key')


class DataManager:
    def __init__(self):
        self.headers = {
            'Authorization': SHEETY_API_KEY
        }

    def get_spreadsheet_price_data(self):
        response = requests.get(url=f'{SHEETY_ENDPOINT}/prices', headers=self.headers)
        return response.json()['prices']

    def get_spreadsheet_user_data(self):
        response = requests.get(url=f'{SHEETY_ENDPOINT}/users', headers=self.headers)
        return response.json()['users']

    def edit_iata_column(self, row_id, iata_code):
        row_body = {
            'price': {
                'iataCode': iata_code
            }
        }

        requests.put(url=f'{SHEETY_ENDPOINT}/prices/{row_id}', json=row_body, headers=self.headers)

    def add_new_user(self, name, last_name, email):
        row_body = {
            'user': {
                'firstName': name,
                'lastName': last_name,
                'email': email
            }
        }

        requests.post(url=f'{SHEETY_ENDPOINT}/users', json=row_body, headers=self.headers)

    # Use in case the price column is missing values in the spreadsheet
    def fill_price_column(self, row_id, flight_price):
        row_body = {
            'price': {
                'lowestPrice': flight_price
            }
        }

        requests.put(url=f'{SHEETY_ENDPOINT}/prices/{row_id}', json=row_body, headers=self.headers)
