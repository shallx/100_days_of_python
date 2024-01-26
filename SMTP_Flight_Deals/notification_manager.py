import html
import smtplib
from dotenv import load_dotenv
import os

from flight_data import FlightData

FROM_EMAIL = os.getenv("FROM_EMAIL")
STMP_PASS = os.getenv("STMP_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")
class NotificationManager:
    def send_email(self,flight : FlightData):
        # message = f"Subject:Low price alert!\n\nOnly £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=STMP_PASS)
            connection.sendmail(
                from_addr=FROM_EMAIL, 
                to_addrs=TO_EMAIL, 
                msg=f"Subject:Low Price Alert\n\n Price oly at {flight.price}"
                # msg=html.unescape(message.encode())
            )