import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
SHEETY_TOKEN = os.getenv("sheety_token")
SHEETY_ENDPOINT = "https://api.sheety.co/2cbcbeba781f85445893d27c438cec1e/flightDeals/prices"

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_rows(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        return response.json()['prices']

    def update_rows(self, iata_code, row_id):
        data = {
            "price": {
                "iataCode": iata_code
            }
        }

        response = requests.put(
            url=f"{SHEETY_ENDPOINT}/{row_id}",
            json=data,
            headers=sheety_headers
        )
        response.raise_for_status()
