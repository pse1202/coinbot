import requests


def get_currency(currency):
    currency = currency.upper()
    url = 'https://api.coinone.co.kr/ticker/'
    params = {
        'currency': currency
    }

    try:
        json = requests.get(url, params=params).json()
        result = '[{}/KRW] {}'.format(currency, json['last'])
    except:
        result = '[Coinone] 에러!'

    return result
