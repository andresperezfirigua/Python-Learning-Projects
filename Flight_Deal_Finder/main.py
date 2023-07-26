from data_manager import DataManager
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.retrieve_rows()
print(sheet_data)

for item in sheet_data:
    if not item['iataCode']:
        data_manager.edit_iata_value(item['id'], flight_search.find_iata_code(item['city']))
