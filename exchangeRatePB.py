import requests
from datetime import datetime

# currency ex. 'USD' etc
#action - 'sale' or 'purchase'


def exchangeRatePB(currency='USD', action='saleAndPurchahse'):
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + \
        datetime.now().strftime(f'%d.%m.%Y')
    data = requests.get(url).json()
    for item in data['exchangeRate']:
        if 'currency' in item.keys():
            if item['currency'] == currency:
                if (action == 'sale') & ('saleRate' in item.keys()):
                    sale = item['saleRate']
                    return sale
                elif (action == 'purchase') & ('purchaseRate' in item.keys()):
                    purchase = item['purchaseRate']
                    return purchase
                elif (action == 'saleAndPurchahse') & ('saleRate' in item.keys()):
                    sale = item['saleRate']
                    purchase = item['purchaseRate']
                    return sale, purchase
        else:
            continue
