from dotenv import load_dotenv
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
ACCOUNT_SID = os.getenv("account_sid")
AUTH_TOKEN = os.getenv("auth_token")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
RECIPIENT = os.getenv("RECIPIENT_NUMBER")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_msg(self, flight):
        msg_body = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
                body=msg_body,
                from_=TWILIO_NUMBER,
                to=RECIPIENT
            )
        print(message.status)
