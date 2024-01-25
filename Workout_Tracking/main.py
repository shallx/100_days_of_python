from dotenv import load_dotenv
import os
import requests
import gspread
import datetime as dt

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_TITLE = "Dourani Logs"

print(f"{APP_ID} | {API_KEY}")

base_url = "https://trackapi.nutritionix.com/v2"

def get_result(query: str):
    endpoint = f"{base_url}/natural/exercise"
    body = {
        "query": query,
    }
    
    header = {
        "x-app-id" : APP_ID,
        "x-app-key" : API_KEY,
    }
    response = requests.post(url=endpoint, json=body, headers=header)
    print(response.json())
    return response.json()["exercises"]
    
def gspread_call(exercises):
    client = gspread.service_account(filename="credentials.json")
    wb_1 = client.open(SHEET_TITLE)
    worksheet = wb_1.get_worksheet(0)
    
    today_date = dt.datetime.now().strftime("%d/%m/%Y")
    now_time = dt.datetime.now().strftime("%X")
    rows = []
    for exercise in exercises:
        rows.append([today_date, now_time, exercise["name"].title(), exercise["duration_min"], exercise["nf_calories"]])
    
    print(rows)
    worksheet.append_rows(rows)

exercises = get_result(input("Provide your running data:"))
gspread_call(exercises)

