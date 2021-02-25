# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
import data_manager
import flight_data
import flight_search
import notification_manager

data_manager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
sheet_data = data_manager.get_rows()
notification_manager = notification_manager.NotificationManager()

ORIGIN_CITY_IATA = "LON"

for row in sheet_data:
    if row["iataCode"] == '':
        row["iataCode"] = flight_search.get_iata(row["city"])
        data_manager.update_rows(row["iataCode"], row["id"])

tomorrow = datetime.now() + timedelta(days=1)
six_months_later = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_months_later
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_msg(flight)
