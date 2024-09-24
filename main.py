import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# ensures that website won't mark as spam
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

# urls of the stock webpages
urls = [
    'https://finance.yahoo.com/quote/NKE/',
    'https://finance.yahoo.com/quote/PTN/',
    'https://finance.yahoo.com/quote/MSFT/',
    'https://finance.yahoo.com/quote/AAL/',
    'https://finance.yahoo.com/quote/AXP/',
    'https://finance.yahoo.com/quote/AAPL/',
    'https://finance.yahoo.com/quote/BA/',
    'https://finance.yahoo.com/quote/CSCO/',
    'https://finance.yahoo.com/quote/GS/',
    'https://finance.yahoo.com/quote/IBM/',
    'https://finance.yahoo.com/quote/INTC/',
    'https://finance.yahoo.com/quote/JPM/',
    'https://finance.yahoo.com/quote/MCD/',
    'https://finance.yahoo.com/quote/CRM/',
    'https://finance.yahoo.com/quote/VZ/',
    'https://finance.yahoo.com/quote/V/',
    'https://finance.yahoo.com/quote/WMT/',
    'https://finance.yahoo.com/quote/DIS/',
]

results = []

def extract(text):
    match = re.match(r'^(.*) \(([^)]+)\)$', text)
    if match:
        name = match.group(1).strip()
        symbol = match.group(2).strip()
        return name, symbol
    else:
        return None, None


for url in urls:
    response = requests.get()

response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

#company and symbol
foo = soup.find('h1', {'class': 'yf-3a2v0c'}).text
#print(extract(foo))

price = soup.find('fin-streamer', {'class': 'livePrice yf-mgkamr'}).text
print(price)

price_change = soup.find('fin-streamer', {'class': 'priceChange yf-mgkamr', 'data-testid':'qsp-price-change'}).text
print(price_change)

percent_change = soup.find('fin-streamer', {'class': 'priceChange yf-mgkamr', 'data-testid':'qsp-price-change-percent'}).text
print(percent_change)

volume = soup.find('fin-streamer', {'data-field': 'regularMarketVolume'}).text
print(volume)
