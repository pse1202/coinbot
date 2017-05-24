import requests


def get_currency(currency='USD'):
    market = 'Yahoo'
    currency = currency.upper()

    url = 'http://query.yahooapis.com/v1/public/yql'
    params = {
        'q': 'SELECT * FROM yahoo.finance.xchange WHERE pair in ("{}")'.format(currency + 'KRW'),
        'format': 'json',
        'env': 'store://datatables.org/alltableswithkeys'
    }

    try:
        json = requests.get(url, params).json()
        price = json['query']['results']['rate']['Rate']

        result = '[{} | {}] {} KRW'.format(
            market, currency, price)
    except Exception as err:
        result = '[{}] 에러!'.format(market)

    return result
