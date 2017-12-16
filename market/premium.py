import requests
import json


def get():
    market = 'Premium'
    url = 'https://coinpremiums.herokuapp.com/json'

    try:
        result = ""
        premiums = requests.get(url).json()

        for exchange, exchange_currencies in premiums['premium'].items():
            result += '[[{} | '.format(exchange.title())
            _sum = 0
            _cnt = 0
            for currency_name, currency in exchange_currencies.items():
                premium = currency['raw'] - 1
                result += '[{}] {:.2%} '.format(currency_name.upper(), premium)
                _cnt += 1
                _sum += premium
            result += '[평균] {:.2%} ]] '.format(_sum / _cnt)
    except Exception as e:
        result = '[{market}] 에러! : {msg}'.format(market=market, msg=e.__repr__())

    return result
