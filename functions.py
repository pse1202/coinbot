import datetime
import random
from market import yahoo, coinone, poloniex

alias = { '비트': 'BTC', '빗코': 'BTC', '비트코인': 'BTC', '이더': 'ETH', '이클': 'ETC', 
        '리플': 'XRP', 'zcash': 'ZEC' , '대시': 'DASH', '리스크': 'LSK', '스팀': 'STEEM',
        '모네로': 'XMR', '스텔라': 'STR', '*': 'all', '$': 'usdt', '라코': 'LTC', '젝': 'ZEC'}

def functionlist(msg):
    if msg == 'PING':
        return 'PONG'

    elif msg.find('!코인') >= 0:
        currency = msg[msg.find('!코인')+4:].strip()
        if len(currency) == 0:
            currency = 'ALL'
        if currency in alias:
            currency = alias[currency]
        return str(coinone.get_currency(currency))

    elif msg.find('!폴로') >= 0:
        currencies = msg[msg.find('!폴로')+4:].strip().split(maxsplit=1)
        for i in range(len(currencies)):
            if currencies[i] in alias:
                currencies[i] = alias[currencies[i]]
        return str(poloniex.get_currency(*currencies))
    elif msg.find('!축하') >= 0 or msg.find('털었습니다') >= 0:
        return "축하드립니다"
    elif msg.find('!감사') >= 0:
        return "감사합니다"
    elif msg.find('!손절') >= 0:
        return "영-구-손-실"
    elif msg.find('!암드') >= 0:
        return "암숏딱"
    return None
