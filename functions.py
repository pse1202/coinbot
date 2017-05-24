import datetime
import random
from market import yahoo, coinone, poloniex

alias = {'빗코': 'BTC', '비트코인': 'BTC', '이더': 'ETH', '이클': 'ETC', '리플': 'XRP', 'zcash': 'ZEC'}

def functionlist(msg):
    if '!편지' in msg:
        now = datetime.datetime.now()
        if (now.month <= 6 or now.day <= 22):
            return 'https://goo.gl/OlqK2c'

    if msg == 'PING':
        return 'PONG'

    if msg.find('!환율') == 0:
        currency = msg[4:].strip()
        if len(currency) == 0:
            currency = 'USD'
        return str(yahoo.get_currency(currency))

    if msg.find('!코인') == 0:
        currency = msg[4:].strip()
        if len(currency) == 0:
            currency = 'BTC'
        if currency in alias:
            currency = alias[currency]
        return str(coinone.get_currency(currency))

    if msg.find('!폴로') == 0:
        currencies = msg[4:].strip().split(maxsplit=1)
        for i in range(len(currencies)):
            if currencies[i] in alias:
                currencies[i] = alias[currencies[i]]
        return str(poloniex.get_currency(*currencies))

    return None
