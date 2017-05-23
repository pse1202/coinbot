import requests


def get_currency(currency='USD'):
    currency = currency.upper() + 'KRW'
    url = 'http://query.yahooapis.com/v1/public/yql'
    params = {
        'q': 'SELECT * FROM yahoo.finance.xchange WHERE pair in ("{}")'.format(currency),
        'format': 'json',
        'env': 'store://datatables.org/alltableswithkeys'
    }

    try:
        json = requests.get(url, params).json()
        result = '[{}] {}'.format(json['query']['results']['rate']['Name'],
                                  json['query']['results']['rate']['Rate'])
    except Exception as err:
        result = '[Yahoo] 에러!'

    return result
