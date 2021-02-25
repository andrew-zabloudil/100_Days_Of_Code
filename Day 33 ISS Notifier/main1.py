import requests
from datetime import datetime

""" response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position) """

MY_LAT = 35.653141
MY_LNG = -97.481506

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

current_hour = datetime.now().hour

print(sunrise_hour)
print(sunset_hour)
print(current_hour)
