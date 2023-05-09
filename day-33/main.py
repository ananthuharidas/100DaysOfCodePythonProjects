import smtplib

import requests
from datetime import datetime
import time

MY_LAT = 10.148830
MY_LONG = 76.229840


'''Objectives:
    If the international space station is close to my current location
    and it's night then send an email to notify me.
    BONUS: Run the code every 60 seconds'''


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # To raise an exception

    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)
    # Your position is within +5 or -5 degress of the ISS position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG +5:
        return True

    # print(iss_position)

# --------------------------- Sunrise and Sunset --------------------------- #

def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    rise_hour = int(sunrise.split("T")[1].split(":")[0])
    set_hour = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    print(rise_hour)
    print(set_hour)
    print(time_now.hour)
    if time_now.hour >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login("email@gamil.com", "password")
        connection.sendmail(
            from_addr="email@gamil.com",
            to_addrs="email@gamil.com",
            msg="Subject:Look Up\n\n The Internation space station is above you in the sky"
        )
