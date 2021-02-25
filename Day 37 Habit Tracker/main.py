import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "hours",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

graph1_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")


post_params = {
    "date": today,
    "quantity": input("How many hours did you program today? "),
}


update_endpoint = f"{graph1_endpoint}/{today}"

update_params = {
    "quantity": "1",
}

# response = requests.put(
#     url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# response = requests.delete(
#     url=update_endpoint, headers=headers)
# print(response.text)
