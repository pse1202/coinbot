import requests

def get_currency(currency):
    market = 'Coinone'
    currency = currency.upper()
    url = 'https://api.coinone.co.kr/ticker/'
    params = {
        'currency': currency
    }

    try:
        json = requests.get(url, params=params).json()
        price = int(json['last'])

        result = '[{} | {}] {:,} KRW'.format(market, currency, price)
    except:
        result = '[{}] 에러!'.format(market)

    return result
