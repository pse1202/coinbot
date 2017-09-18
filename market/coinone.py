import requests

def get_currency(currency):
    market = 'Coinone'
    currency = currency.upper()
    url = 'https://api.coinone.co.kr/ticker/'
    params = {
        'currency': currency
    }

    try:
        result = ""
        json = requests.get(url, params=params).json()
        if currency == 'ALL':
            for c in ['btc','eth','etc','xrp', 'bch','qtum']:
                price = int(json[c]['last'])
                result += '[{} | {}] {:,} KRW '.format(market,c.upper(),price)
        else:
            price = int(json['last'])

            result = '[{} | {}] {:,} KRW'.format(market, currency, price)
    except:
        result = '[{}] 에러!'.format(market)

    return result
