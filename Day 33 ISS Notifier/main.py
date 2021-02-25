import requests
import smtplib
from datetime import datetime, timezone
import time
import os
from dotenv import load_dotenv

load_dotenv()
MY_GMAIL = os.getenv("my_gmail")
GMAIL_PASSWORD = os.getenv("gmail_password")
MY_LAT = os.getenv("MY_LAT")
MY_LNG = os.getenv("MY_LNG")


def iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LNG) <= 5:
        return True
    else:
        return False


def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc)

    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False


while True:
    if is_dark() and iss_overhead():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=GMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs=MY_GMAIL,
                msg=f"Subject:Look Up!\n\nThe ISS is currently overhead! Go take a look!"
            )

    time.sleep(60)
