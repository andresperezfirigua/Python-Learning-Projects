import datetime

import requests
import os

date = datetime.datetime.now().date()
today = datetime.datetime.now().day

STOCK = "TSLA"

COMPANY_NAME = "tesla"
STOCK_PRICE_API_KEY = os.environ.get('STOCK_PRICE_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

stock_price_endpoint = 'https://www.alphavantage.co/query'

stock_price_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_PRICE_API_KEY
}

news_endpoint = 'https://newsapi.org/v2/everything'

news_parameters = {
    'q': COMPANY_NAME,
    'language': 'en',
    'sources': 'google-news',
    'pageSize': 3,
    # 'from': date.replace(day=today - 1),
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_price_response = requests.get(url=stock_price_endpoint, params=stock_price_parameters)
stock_price_response.raise_for_status()

yesterday_price = float(stock_price_response.json()["Time Series (Daily)"][f'{date.replace(day=today - 2)}']['4. close'])
day_before_yesterday_price = float(stock_price_response.json()["Time Series (Daily)"][f'{date.replace(day=today - 3)}']['4. close'])

print(yesterday_price)
print(day_before_yesterday_price)

if -3 < yesterday_price - day_before_yesterday_price or yesterday_price - day_before_yesterday_price > 3:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(url=news_endpoint, params=news_parameters)
    news_response.raise_for_status()

    list_of_news = news_response.json()['articles']

    for news in list_of_news:
        print(
                f"TSLA:\n"
                f"Headline: {news['title']}\n"
                f"Brief: {news['description']}"
        )

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

