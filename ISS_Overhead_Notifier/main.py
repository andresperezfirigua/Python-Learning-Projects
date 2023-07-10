import time
import requests
import smtplib
from datetime import datetime

MY_LAT = 43.507351 # Your latitude
MY_LONG = -35.127758 # Your longitude

EMAIL = 'Your email here'
PASSWORD = 'Your app generated password here'


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude)
    print(iss_longitude)

    if int(iss_latitude) in range(int(MY_LAT - 5), int(MY_LAT + 5)) and int(iss_longitude) in range(int(MY_LONG - 5), int(MY_LONG + 5)):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(f'{data}\n{sunrise}\n{sunset}')

    time_now = datetime.now()

    if sunrise <= time_now.hour >= sunset:
        return True


while True:
    time.sleep(60)

    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs='Destination email here',
                msg='Subject:ISS Overhead Notification\n\nHey there,\nThe ISS is now over your position, look up!'
            )
    else:
        print("The ISS is still far away")
