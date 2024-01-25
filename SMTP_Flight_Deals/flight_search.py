import requests
from dotenv import load_dotenv
import os
load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:
    def get_destination_code(self, city_name):
        # print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": os.getenv("FLIGHT_TRACKER_API_KEY")}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code