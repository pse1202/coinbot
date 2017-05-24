import requests


def get_currency(from_currency, to_currency='BTC'):
    market = 'Poloniex'
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    url = 'https://poloniex.com/public'
    params = {
        'command': 'returnTicker'
    }
    try:
        json = requests.get(url, params=params).json()
        price = float(json['{}_{}'.format(to_currency, from_currency)]['last'])

        result = '[{} | {}] {:1,.8f} {}'.format(
            market, from_currency, price, to_currency)
    except:
        result = '[{}] 에러!'.format(market)

    return result
