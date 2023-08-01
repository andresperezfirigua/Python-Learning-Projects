from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_spreadsheet_data()

for item in sheet_data:
    destination = item['iataCode']
    if not destination:
        data_manager.edit_iata_column(item['id'], flight_search.find_iata_code(item['city']))
    else:
        flight = flight_search.search_flights(destination)

        if flight.price < int(item['lowestPrice']) and abs(flight.price - int(item['lowestPrice'])) >= 50000:
            notification_manager.send_low_price_alert(flight)
