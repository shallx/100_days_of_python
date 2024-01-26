from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime,timedelta

data_man = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"


def update_iata_code():
    flight_deals = data_man.get_cities() # data from sheet
    new_data = [flight_search.get_destination_code(row["City"]) for row in flight_deals]
    data_man.update(f"B2:B{len(new_data)+1}", new_data)

data_man.get_cities()

def search_flights():
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in data_man.records:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["IATA Code"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight.price < destination["Lowest Price"]:
            notification_manager.send_email(flight)


search_flights()