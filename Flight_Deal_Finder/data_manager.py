import requests
import os
class DataManager:
    def __init__(self):
        self.sheety_endpoint = os.environ.get('Flight_Deal_Finder_Sheety_Endpoint')
        self.headers = {
            'Authorization': os.environ.get('Flight_Deal_Finder_Sheety_Key')
        }

    def retrieve_rows(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.headers)
        return response.json()['prices']

    def edit_iata_value(self, row_id, iata_code):
        row_body = {
            'price': {
                'iataCode': iata_code
            }
        }
        response = requests.put(url=f'{self.sheety_endpoint}/{row_id}', json=row_body, headers=self.headers)
        print(response.text)
