import time
import requests
import datetime as dt
import smtplib

MY_LAT = 24.894930 # Your latitude
MY_LONG = 91.868706 # Your longitude
FROM_EMAIL = "enter_email_from"
TO_EMAIL = "enter_email_to"
PASSWORD = "enter_pass"

def is_dark(sunrise: int, sunset: int):
    date = dt.datetime.now()
    print(date.hour)
    if date.hour >= sunset or date.hour <= sunrise:
        return True
    else:
        return False

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 6
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 6

print(f"Sunrise: {sunrise}")
print(f"SUnset: {sunset}")

print(f"ISS position: ({iss_latitude}, {iss_longitude})")
print(f"My position : ({MY_LAT}, {MY_LONG})")

print(is_dark(sunrise=sunrise, sunset=sunset))

while True:
    time.sleep(60)
    if abs((iss_latitude-MY_LAT)) <=5 and abs((iss_longitude-MY_LONG)) and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL, 
                to_addrs=TO_EMAIL, 
                msg=f"Subject: ISS on Sky\n\nLookup"
            )
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



