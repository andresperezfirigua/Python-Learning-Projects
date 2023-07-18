import datetime
import requests
import os
from twilio.rest import Client

date = datetime.datetime.now().date()
today = datetime.datetime.now().day

STOCK = "TSLA"
COMPANY_NAME = "tesla"

STOCK_PRICE_API_KEY = os.environ.get('STOCK_PRICE_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
TW_ACCOUNT_SID = os.environ['TW_ACCOUNT_SID']
TW_AUTH_TOKEN = os.environ['TW_AUTH_TOKEN']
TW_PHONE_NUMBER = '+18146225203'

stock_price_endpoint = 'https://www.alphavantage.co/query'

stock_price_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_PRICE_API_KEY
}

stock_price_response = requests.get(url=stock_price_endpoint, params=stock_price_parameters)
stock_price_response.raise_for_status()

data = stock_price_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_price = float(data_list[0]['4. close'])
day_before_yesterday_price = float(data_list[1]['4. close'])

print(data)
print(yesterday_price)
print(day_before_yesterday_price)

difference = yesterday_price - day_before_yesterday_price
percentage = round((difference / yesterday_price) * 100, 2)

up_down = None

if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

if abs(percentage) > 3:
    news_endpoint = 'https://newsapi.org/v2/everything'

    news_parameters = {
        'q': COMPANY_NAME,
        'searchIn': 'title',
        'language': 'en',
        'sources': 'google-news',
        'pageSize': 3,
        'sortBy': 'publishedAt',
        'apiKey': NEWS_API_KEY
    }

    news_response = requests.get(url=news_endpoint, params=news_parameters)
    news_response.raise_for_status()

    list_of_news = news_response.json()['articles']
    formatted_articles = [f"\n{STOCK}: {up_down}{percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in list_of_news]

    client = Client(TW_ACCOUNT_SID, TW_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages \
            .create(
                body=article,
                from_=TW_PHONE_NUMBER,
                to='+573208638202'
            )

        print(message.status)

        print(article)
