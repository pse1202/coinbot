import requests

def get_currency(currency):
    market = 'bitFlyer'
    currency = currency.upper()

    code_alias = {
        'BTC': 'BTC_JPY',
        'ETH': 'ETH_BTC',
        'BCH': 'BCH_BTC'
    }

    # API documentation at https://lightning.bitflyer.jp/docs
    base_url = 'https://api.bitflyer.jp'

    def get_ticker(product_code):
        ticker_url = base_url + '/v1/ticker'
        params = {
            'product_code': product_code
        }
        json = requests.get(ticker_url, params=params).json()
        price = float(json['ltp'])

        if len(product_code) == 7 and product_code[3] == '_':
            product, _, unit = product_code.partition('_')
            return product, price, unit
        else:
            return product_code, price, ''

    def get_product_codes():
        product_codes = []
        market_url = base_url + '/v1/markets'
        json = requests.get(market_url).json()
        for market in json:
            product_codes.append(market['product_code'])

        market_url = base_url + '/v1/markets/usa'
        json = requests.get(market_url).json()
        for market in json:
            product_codes.append(market['product_code'])
        return product_codes

    try:
        if currency == 'ALL' or currency == '*':
            result = '{market} >> '.format(market=market)
            for product_code in get_product_codes():
                product, price, unit = get_ticker(product_code)
                result += '[{}] {:,.5f} {}  '.format(product, price, unit)
        else:
            product_code = code_alias.get(currency, currency)
            product, price, unit = get_ticker(product_code)
            result = '[{} | {}] {:,.5f} {}'.format(market, product, price, unit)
    except:
        result = '[{}] 에러!'.format(market)
    return result
