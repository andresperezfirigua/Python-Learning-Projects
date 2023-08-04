from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


# |-----------------------------------   User interaction   -----------------------------------|
# print('Welcome to the Flight Hunters club!\nSign up to get the best flight deals via email.')
# name = input('What is your name?\n').title()
# last_name = input('What is your last name?\n').title()
# email = input('What is your email?\n').lower().strip()
# email_confirmation = input('Type your email again.\n').lower().strip()
#
# while True:
#     if email == email_confirmation and email and email_confirmation:
#         print("You're in the club! Awaiting for the best deal notification in your email.")
#         data_manager.add_new_user(name, last_name, email)
#         break
#     else:
#         print('Email does not match or is empty, type it again.')
#         email = input('What is your email?\n').lower().strip()
#         email_confirmation = input('Type your email again.\n').lower().strip()


# |-----------------------------------     Flight lookup     --------------------------------|

sheet_data = data_manager.get_spreadsheet_price_data()

for item in sheet_data:
    destination = item['iataCode']
    if not destination:
        data_manager.edit_iata_column(item['id'], flight_search.find_iata_code(item['city']))
    else:
        flight = flight_search.search_flights(destination)

        if flight is None:
            continue

        if flight.price < int(item['lowestPrice']) and abs(flight.price - int(item['lowestPrice'])) >= 50000:
            message_text = f"Lower price found for {flight.destination_city} - {flight.destination_airport}!\n" \
                            f"Only ${flight.price} from {flight.out_date} to {flight.return_date}.\n"
            if flight.stop_overs > 0:
                message_text += f"\nThis flight has {flight.stop_overs} stop over, via {flight.via_city}\n\n"

            notification_manager.send_sms_alert(message_text)

            email_list = data_manager.get_spreadsheet_user_data()

            for row in email_list:
                email = row['email']
                message = f'Hi {row["firstName"]},\nWe have great news for you!\n' + message_text
                notification_manager.send_email_alert(email, message)

