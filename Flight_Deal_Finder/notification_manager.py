import os
import smtplib
from twilio.rest import Client

ACCOUNT_SID = os.environ['TW_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TW_AUTH_TOKEN']
TW_PHONE_NUMBER = os.environ['TW_PHONE_NUMBER']
DESTINATION_NUMBER = 'Your phone number here'


class NotificationManager:
    def __init__(self):
        pass
        # self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms_alert(self, message):
        print(message)

        # TODO - Add Twilio authentication, free trial expired

        # message = self.client.messages \
        #     .create(
        #     body=message_text,
        #     from_=TW_PHONE_NUMBER,
        #     to=DESTINATION_NUMBER
        # )
        #
        # print(message.sid)

    def send_email_alert(self, destination_email, message):
        email = 'Your email here'
        password = 'Your app generated password here'
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=destination_email,
                msg=f'Subject:New Flight Deal! - Alert\n\n{message}'.encode('utf-8')
            )
