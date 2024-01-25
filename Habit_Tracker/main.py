import requests

DOMAIN = "https://pixe.la"

CREATE_USER_ENDPOINT = "v1/users"
USERNAME = "grimmjow"
TOKEN = "lkjdfjdlf03jd"

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
        "id" : "graph1",
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


create_graph()
# create_user() #https://pixe.la/@grimmjow 