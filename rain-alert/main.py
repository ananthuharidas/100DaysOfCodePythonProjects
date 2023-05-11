import requests
import os

API_KEY = os.environ.get("OWM_API_KEY")
print(API_KEY)
MY_LATITUDE = 10.148830
MY_LONGITUDE = 76.229843

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather_slice = weather_data["hourly"][:12]  # Slice first 12 hours of weather data

will_rain = False

for hour_data in hourly_weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True


def telegram_bot_sendtext(bot_message):
    bot_token = os.environ.get("telegram_rain_alert_99_bot_token")
    bot_chatID = os.environ.get("CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    telegram_response = requests.get(send_text)

    return telegram_response.json()


if will_rain:
    message = telegram_bot_sendtext("It's going to rain today!")
    print(message['ok'])
