import os
from twilio.rest import Client

ACCOUNT_SID = os.environ['TW_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TW_AUTH_TOKEN']
TW_PHONE_NUMBER = os.environ['TW_PHONE_NUMBER']
DESTINATION_NUMBER = 'Your phone number here'


class NotificationManager:
    def __init__(self):
        pass
        # self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_low_price_alert(self, flight):
        message_text = f"Lower price found for {flight.destination_city} - {flight.destination_airport}!\n " \
                       f"Only ${flight.price} from {flight.out_date} to {flight.return_date}."
        print(message_text)

        # TODO - Add Twilio authentication, free trial expired

        # message = self.client.messages \
        #     .create(
        #     body=message_text,
        #     from_=TW_PHONE_NUMBER,
        #     to=DESTINATION_NUMBER
        # )
        #
        # print(message.sid)
