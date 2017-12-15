import requests


def get_currency(currency):
    market = 'Bithumb'
    currency = currency.upper()
    if currency == 'ALL':
        url = 'https://api.bithumb.com/public/ticker/all'
    else:
        url = 'https://api.bithumb.com/public/ticker/{currency}'.format(currency=currency)

    try:
        result = ""
        json = requests.get(url).json()
        if json['status'] != '0000':
            raise Exception(json['message'])
        data = json['data']
        if currency == 'ALL':
            result = '{market} >> '.format(market=market)
            for c in ['btc', 'eth', 'etc', 'xrp', 'bch', 'btg', 'ltc', 'qtum', 'dash', 'xmr', 'zec', 'eos']:
                price = int(data[c.upper()]['closing_price'])
                result += '[{}] {:,} KRW  '.format(c.upper(), price)
        else:
            price = int(data['closing_price'])
            result = '[{} | {}] {:,} KRW'.format(market, currency, price)
    except Exception as e:
        result = '[{market}] 에러! : {msg}'.format(market=market, msg=e.__repr__())

    return result
