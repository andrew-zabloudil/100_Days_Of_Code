import requests
import os
import datetime as dt
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_VANTAGE_KEY = os.getenv("alphavantage_key")
NEWS_API_KEY = os.getenv("news_api_key")
ACCOUNT_SID = os.getenv("account_sid")
AUTH_TOKEN = os.getenv("auth_token")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
RECIPIENT_NUMBER = os.getenv("RECIPIENT NUMBER")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def check_stocks():
    stock_endpoint = "https://www.alphavantage.co/query"

    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_VANTAGE_KEY
    }

    stock_response = requests.get(url=stock_endpoint, params=stock_params)
    stock_response.raise_for_status()

    stock_data = stock_response.json()

    now = dt.datetime.now()
    date_now = str(now).split(" ")[0].split("-")

    if now.weekday() != 0 and now.weekday != 6:
        day_prior = int(date_now[2]) - 1
        two_days_prior = int(date_now[2]) - 2
    elif now.weekday() == 0:
        day_prior = int(date_now[2]) - 3
        two_days_prior = int(date_now[2]) - 4
    else:
        day_prior = int(date_now[2]) - 2
        two_days_prior = int(date_now[2]) - 3

    if day_prior > 9:
        day_prior = str(day_prior)
    else:
        day_prior = f"0{day_prior}"

    if two_days_prior > 9:
        two_days_prior = str(two_days_prior)
    else:
        two_days_prior = f"0{two_days_prior}"

    date_prior = f"{date_now[0]}-{date_now[1]}-{day_prior}"
    date_two_prior = f"{date_now[0]}-{date_now[1]}-{two_days_prior}"

    close_price_day_prior = float(
        stock_data["Time Series (Daily)"][f"{date_prior}"]["4. close"])
    close_price_two_days_prior = float(
        stock_data["Time Series (Daily)"][f"{date_two_prior}"]["4. close"])

    change = close_price_day_prior - close_price_two_days_prior
    percent_change = abs(round(change / close_price_two_days_prior * 100))

    if percent_change >= 5:
        news = get_news(date_two_prior)
        send_message(change, percent_change, news)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news(date):
    news_params = {
        "qInTitle": COMPANY_NAME,
        "from": date,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    news_endpoint = "http://newsapi.org/v2/everything?"
    news_response = requests.get(url=news_endpoint, params=news_params)
    news_response.raise_for_status()

    news_data = news_response.json()["articles"][:3]

    return news_data

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


def send_message(change, percent_change, news=""):
    arrow = ""
    if change > 0:
        arrow = "🔺"
    elif change < 0:
        arrow = "🔻"

    for article in news:
        body = f"{STOCK}:{arrow}{percent_change}%\nHeadline: {article['title']}\nBrief: {article['description']}"

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
                        .create(
                            body=body,
                            from_=TWILIO_NUMBER,
                            to=RECIPIENT_NUMBER
                        )
        print(message.status)


check_stocks()

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
