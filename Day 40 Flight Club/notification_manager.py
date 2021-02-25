from dotenv import load_dotenv
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
MY_GMAIL = os.getenv("my_gmail")
GMAIL_PASSWORD = os.getenv("gmail_password")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_msg(self, flight, users):
        for user in users:
            msg_body = f"Subject:Low Price Alert!\n\nLow price alert! Only {flight.price} GBP to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
            if flight.stop_overs > 0:
                msg_body += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}"
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_GMAIL, password=GMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=MY_GMAIL,
                    to_addrs=user["email"],
                    msg=msg_body
                )
