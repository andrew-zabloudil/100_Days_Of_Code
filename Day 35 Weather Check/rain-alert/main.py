import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
MY_LAT = os.getenv("MY_LAT")
MY_LON = os.getenv("MY_LNG")
api_key = os.getenv("api_key")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
RECIPIENT_NUMBER = os.getenv("RECIPIENT_NUMBER")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=OWM_endpoint, params=params)
response.raise_for_status()

weather_data = response.json()
hourly_weather = weather_data["hourly"][:12]

condition_ids = [hourly_weather[i]["weather"][0]["id"]
                 for i, _ in enumerate(hourly_weather) if hourly_weather[i]["weather"][0]["id"] < 700]

if condition_ids:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☔",
                        from_=TWILIO_NUMBER,
                        to=RECIPIENT_NUMBER
                    )
    print(message.status)
