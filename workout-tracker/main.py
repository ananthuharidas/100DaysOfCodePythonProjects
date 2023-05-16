import os
import requests
from datetime import datetime, time

APP_ID = os.environ.get("APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

exercise_text = input("Tell me which exercises you did: ")
sheety_headers = {
    "Authorization": f"Bearer {os.environ.get('SHEETY_BEARER_AUTH')}"
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

data = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 74.5,
    "height_cm": 181.00,
    "age": 26
}

response = requests.post(url=EXERCISE_ENDPOINT, json=data, headers=headers)

# Adding data to google sheets using sheety API
exercise = response.json()["exercises"][0]["name"].capitalize()
date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
duration = float(response.json()["exercises"][0]["duration_min"])
calories = float(response.json()["exercises"][0]["nf_calories"])

new_row = {
    "workout":{
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

add_data_to_sheets_response = requests.post(url=SHEETY_ENDPOINT, json=new_row, headers=sheety_headers)
print(add_data_to_sheets_response.text)