import datetime as dt
import time
import requests

DOMAIN = "https://pixe.la"

CREATE_USER_ENDPOINT = "v1/users"
USERNAME = "grimmjow"
TOKEN = "lkjdfjdlf03jd"
PYTHON_ID = "python100"
CYCLING_ID = "graph1"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

def create_user():
    response = requests.post(url=f"{DOMAIN}/{CREATE_USER_ENDPOINT}", json=user_params)
    print(response.text)

def create_graph():
    graph_config = {
        "id" : PYTHON_ID,
        "name" : "Cycling Graph",
        "unit" : "Km",
        "type" : "float",
        "color" : "ajisai",
    }

    headers = {
        "X-USER-TOKEN" : TOKEN
    }

    graph_endpoint = f"{DOMAIN}/v1/users/{USERNAME}/graphs"

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)



    
def post_a_pixel(date: dt.datetime, quantity : str):
    today = date
    todays_date = today.strftime("%Y%m%d")
    graph_config = {
        "date" : todays_date,
        "quantity" : quantity,
    }

    headers = {
        "X-USER-TOKEN" : TOKEN
    }

    graph_endpoint = f"{DOMAIN}/v1/users/{USERNAME}/graphs/{PYTHON_ID}"

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)
    isSuccess = response.json()["isSuccess"]

    if not isSuccess:
        post_a_pixel(date=date, quantity=quantity)


def update_a_pixel(date: dt.datetime, quantity : str):
    todays_date = date.strftime("%Y%m%d")
    graph_config = {
        "date" : todays_date,
        "quantity" : quantity,
    }

    headers = {
        "X-USER-TOKEN" : TOKEN
    }

    graph_endpoint = f"{DOMAIN}/v1/users/{USERNAME}/graphs/{PYTHON_ID}/{todays_date}"

    response = requests.put(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)
    print(response.json())


def delete_a_pixel(date: dt.datetime):
    todays_date = date.strftime("%Y%m%d")

    headers = {
        "X-USER-TOKEN" : TOKEN
    }

    graph_endpoint = f"{DOMAIN}/v1/users/{USERNAME}/graphs/{PYTHON_ID}/{todays_date}"

    response = requests.delete(url=graph_endpoint, headers=headers)
    print(response.text)
    print(response.json())


def update_a_graph():
    graph_config = {
        "name" : "Python 100 Days Challenge",
        "unit" : "videos",
        "type" : "float",
        "color" : "ajisai",
    }

    headers = {
        "X-USER-TOKEN" : TOKEN
    }

    graph_endpoint = f"{DOMAIN}/v1/users/{USERNAME}/graphs/{PYTHON_ID}"

    response = requests.put(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)
    




# create_user() #https://pixe.la/@grimmjow 
# create_graph()
# update_a_graph()
    
# update_a_pixel(date=dt.datetime(year=2024, month=1, day=7), quantity="26")
# delete_a_pixel(date=dt.datetime(year=2024, month=1, day=17))
    
lst = [(3, "17"), (4, "17"), (5, "22"), (6, "27"), (7, "25"), (8, "8"), (9, "10"), (10, "17"), (11, "23"), (12, "8"), (13, "5"), (14, "7"), (15, "26"), (16, "18"), (17, "26"), (18, "10"), (19, "9"), (20, "0"), (21, "0"), (22, "3"), (23, "16"), (24, "20"), (25, "26")]

for s in lst:
    time.sleep(1)
    # post_a_pixel(date=dt.datetime(year=2024, month=1, day=s[0]), quantity=s[1])
    update_a_pixel(date=dt.datetime(year=2024, month=1, day=s[0]), quantity=s[1])

