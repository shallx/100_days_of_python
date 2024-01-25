import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "GDWLVBJ4O8726K8Z"
NEWS_API_KEY = "2e1d19dc88324ec0ae36c5f8ee08af12"



def get_stock_difference():
    '''Request stock changes'''
    params = {
        "function" : "TIME_SERIES_DAILY",
        "symbol" : STOCK,
        "apikey" : ALPHA_API_KEY,
        
    }
    respose = requests.get("https://www.alphavantage.co/query", params = params)
    respose.raise_for_status()
    stock_data = respose.json()

    stock_records = [value for (_,value) in stock_data["Time Series (Daily)"].items()]

    yesterday_stock = float(stock_records[0]["4. close"])
    previous_day_stock = float(stock_records[1]["4. close"])
    difference = abs(yesterday_stock-previous_day_stock)

    print(difference/previous_day_stock * 100)


def get_news():

    params = {
        "q" : f"({COMPANY_NAME})",
        "searchIn" : "title",
        "apiKey" : NEWS_API_KEY,
    }
    endpiont = "https://newsapi.org/v2/everything"
    respose = requests.get(endpiont, params = params)
    respose.raise_for_status()
    articles = respose.json()["articles"]

    for article in articles[:3]:
        print(article["title"])

get_news()
get_stock_difference()



# def message_sending(diff, diff_percent):
#     if difference > 0:
#         up_down = "🔺"
#     else:
#         up_down = "🔻"
#     formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#     print(formatted_articles)
#     #Send each article as a separate message via Twilio.
#     client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#     #TODO 8. - Send each article as a separate message via Twilio.
#     for article in formatted_articles:
#         message = client.messages.create(
#             body=article,
#             from_=VIRTUAL_TWILIO_NUMBER,
#             to=VERIFIED_NUMBER
#         )
