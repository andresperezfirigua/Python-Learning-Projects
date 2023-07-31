from data_manager import DataManager
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

destinations = []
data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_spreadsheet_data()

for item in sheet_data:
    destination = item['iataCode']
    if not destination:
        data_manager.edit_iata_column(item['id'], flight_search.find_iata_code(item['city']))
    else:
        flight = flight_search.search_flights(destination)
