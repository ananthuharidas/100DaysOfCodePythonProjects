import os
import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": os.environ.get("ALPHAVANTAGE_API_KEY")
}
print(os.environ.get("ALPHAVANTAGE_API_KEY"))
alpha_vantage_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
alpha_vantage_response.raise_for_status()
time_series_daily_data = alpha_vantage_response.json()["Time Series (Daily)"]
yesterday_date = str(date.today() - timedelta(days=1))
day_before_yesterday_date = str(date.today() - timedelta(days=2))

closing_price_yesterday = float(time_series_daily_data[yesterday_date]["4. close"])
closing_price_day_before_yesterday = float(time_series_daily_data[day_before_yesterday_date]["4. close"])

stock_margin = ((closing_price_yesterday / closing_price_day_before_yesterday) - 1) * 100
if stock_margin > 5 or stock_margin < -5:
    print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": os.environ.get("NEWSAPI_KEY"),
    "searchIn": "title",
    "language": "en"
}
print(os.environ.get("NEWSAPI_KEY"))
news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
relevant_articles = news_response.json()["articles"]
first_three_news_pieces = relevant_articles[:3]


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
# I'm using telegram bot instead

def telegram_bot_sendtext(bot_message):
    bot_token = os.environ.get("telegram_rain_alert_99_bot_token")
    bot_chatID = os.environ.get("CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    telegram_response = requests.get(send_text)

    return telegram_response.json()


if stock_margin > 2 or stock_margin < -2:
    # print("Get News")
    if stock_margin > 2:
        alert_text = f"{STOCK} 🔺{abs(stock_margin)}\n"
    else:
        alert_text = f"{STOCK} 🔻{abs(stock_margin)}\n"
    for news in first_three_news_pieces:
        headline = f"Headline: {news['title']}"
        brief = f"Brief: {news['description']}"
        alert_text +=(f"{headline}\n{brief}\n")
    print(alert_text)
    message = telegram_bot_sendtext(alert_text)
    print(f"Message send? {message['ok']}")
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
