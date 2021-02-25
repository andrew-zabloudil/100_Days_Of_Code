import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
APP_ID = os.getenv("nutritionix_app_id")
API_KEY = os.getenv("nutritionix_api_key")
SHEETY_TOKEN = os.getenv("sheety_token")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/2cbcbeba781f85445893d27c438cec1e/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = input("What exercise did you do today? ")

exercise_params = {
    "query": query,
    "gender": "male",
    "age": 26
}

response = requests.post(url=NUTRITIONIX_ENDPOINT,
                         json=exercise_params, headers=headers)
result = response.json()


date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=sheety_endpoint, json=sheet_input, headers=sheety_headers)
    print(sheet_response.text)
