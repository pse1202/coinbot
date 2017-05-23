import datetime
import random
from market import yahoo, coinone


def functionlist(msg):
    if '편지' in msg:
        now = datetime.datetime.now()
        if random.random() > 0.7 and (now.month <= 6 or now.day <= 22):
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
        return str(coinone.get_currency(currency))

    return None
