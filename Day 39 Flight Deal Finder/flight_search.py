import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from flight_data import FlightData

tequila_endpoint = "https://tequila-api.kiwi.com"
tequila_api_key = os.getenv("tequila_api_key")

headers = {
    "apikey": tequila_api_key,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata(self, city):
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
        }
        response = requests.get(
            url=f"{tequila_endpoint}/locations/query", params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "currency": "GBP"
        }
        response = requests.get(
            url=f"{tequila_endpoint}/v2/search",
            params=params,
            headers=headers
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
