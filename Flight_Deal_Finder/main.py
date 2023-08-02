from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

print('Welcome to the Flight Hunters club!\nSign up to get the best flight deals via email.')
name = input('What is your name?\n').title()
last_name = input('What is your last name?\n').title()
email = input('What is your email?\n').lower().strip()
email_confirmation = input('Type your email again.\n').lower().strip()

while True:
    if email == email_confirmation and email and email_confirmation:
        print("You're in the club! Awaiting for the best deal notification in your email.")
        data_manager.add_new_user(name, last_name, email)
        break
    else:
        print('Email does not match or is empty, type it again.')
        email = input('What is your email?\n').lower().strip()
        email_confirmation = input('Type your email again.\n').lower().strip()


# sheet_data = data_manager.get_spreadsheet_data()
#
# for item in sheet_data:
#     destination = item['iataCode']
#     if not destination:
#         data_manager.edit_iata_column(item['id'], flight_search.find_iata_code(item['city']))
#     else:
#         flight = flight_search.search_flights(destination)
#
#         if flight is None:
#             continue
#
#         if flight.price < int(item['lowestPrice']) and abs(flight.price - int(item['lowestPrice'])) >= 50000:
#             notification_manager.send_low_price_alert(flight)

