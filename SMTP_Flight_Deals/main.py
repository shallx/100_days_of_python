from data_manager import DataManager
from flight_search import FlightSearch

data_man = DataManager()


flight_search = FlightSearch()



def update_iata_code():
    flight_deals = data_man.get_cities() # data from sheet
    new_data = [flight_search.get_destination_code(row["City"]) for row in flight_deals]
    data_man.update(f"B2:B{len(new_data)+1}", new_data)
    
