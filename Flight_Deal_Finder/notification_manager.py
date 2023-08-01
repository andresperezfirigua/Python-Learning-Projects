import os
from twilio.rest import Client


class NotificationManager:
    def send_low_price_alert(self, flight):
        message_text = f"Lower price found for {flight.destination_city} - {flight.destination_airport}!\n " \
                       f"Only ${flight.price} from {flight.out_date} to {flight.return_date}."
        print(message_text)

        # TODO - Add Twilio authentication, free trial expired

        # account_sid = os.environ['TW_ACCOUNT_SID']
        # auth_token = os.environ['TW_AUTH_TOKEN']
        # tw_phone_number = os.environ['TW_PHONE_NUMBER']
        # client = Client(account_sid, auth_token)

        # message = client.messages \
            # .create(
            # body=f"Lower price found for {flight.destination_city} - {flight.destination_airport}, "
                 # f"Only ${flight.price} from {flight.out_date} to {flight.return_date}.",
            # from_=tw_phone_number,
            # to='+573208638202'
        # )

        #print(message.sid)
