import requests
from twilio.rest import Client
import os


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API =  "6X9IM1T53IT1J174"
NEWS_API = "2e1b491ac27d404a8edeac63ca75030f"
ACCOUNT_SID = "ACbd51f52e65e53d01547de54aa805cfc2"
ACCESS_TOKEN = "7f5a93b16bc459149ac4e019fa19efdf"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price))*100
print(diff_percent)

if abs(diff_percent) > 0:
    # Determine symbol for message
    up_down = "🔺" if diff_percent > 0 else "🔻"

    # Fetch News
    news_parameter = {
        "apikey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]  # Get top 3 articles

    # 4. Send SMS via Twilio
    client = Client(ACCOUNT_SID, ACCESS_TOKEN)

    for article in articles:
        message_body = (
            f"{STOCK_NAME}: {up_down}{round(abs(diff_percent), 2)}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )

        message = client.messages.create(
            body=message_body,
            from_="+12513252544",  # Your Twilio number
            to="+917676606499"  # Your verified number
        )
        print(f"Message sent: {message.sid}")
