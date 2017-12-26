import datetime
import random
from market import yahoo, coinone, poloniex, upbit, bithumb, premium, bitflyer, korean_stock

alias = { '비트': 'BTC', '빗코': 'BTC', '비트코인': 'BTC', '이더': 'ETH', '이클': 'ETC', 
        '리플': 'XRP', 'zcash': 'ZEC' , '대시': 'DASH', '리스크': 'LSK', '스팀': 'STEEM',
        '모네로': 'XMR', '스텔라': 'STR', '*': 'all', '$': 'usdt', '라코': 'LTC', '젝': 'ZEC',
        '파워레인저': 'POWR', '빗골': 'BTG', '흑트라': 'STRAT', '히오스': 'EOS', '어미새': 'OMG',
        '엠쥐': 'OMG'}

def process_command(msg, command_name, multiple=False, default_arg='ALL'):
    if multiple: # multiple arg condition like `!폴로 btc usdt`
        currencies = msg[msg.find(command_name)+4:].strip().split(maxsplit=1)
        for i in range(len(currencies)):
            if currencies[i] in alias:
                currencies[i] = alias[currencies[i]]
        return currencies
    else:
        currency = msg[msg.find(command_name)+4:].strip()
        if default_arg and len(currency) == 0:
            currency = default_arg
        if currency in alias:
            currency = alias[currency]
        return currency

def functionlist(msg):
    if msg == 'PING':
        return 'PONG'

    elif msg.find('!코인') >= 0:
        currency = process_command(msg, '!코인')
        return str(coinone.get_currency(currency))

    elif msg.find('!폴로') >= 0:
        currencies = process_command(msg, '!폴로', multiple=True, default_arg=None)
        return str(poloniex.get_currency(*currencies))

    elif msg.find('!업빗') >= 0:
        currencies = process_command(msg, '!업빗', multiple=True, default_arg='TOP5')
        return str(upbit.get_currency(*currencies))

    elif msg.find('!빗썸') >= 0:
        currency = process_command(msg, '!빗썸')
        return str(bithumb.get_currency(currency))

    elif msg.find('!빗플') >= 0:
        currency = process_command(msg, '!빗플', default_arg='BTC')
        return str(bitflyer.get_currency(currency))

    elif msg.find('!프리미엄') >= 0 or msg.find('!김프') >= 0:
        return str(premium.get())

    elif msg.find('!주식') >= 0:
        stock = process_command(msg, '!주식', default_arg=None)
        return str(korean_stock.get_quote(stock))

    elif msg.find('!마켓캡') >= 0:
        pass

    elif msg.find('!축하') >= 0 or msg.find('털었습니다') >= 0:
        return "축하드립니다"
    elif msg.find('!감사') >= 0:
        return "감사합니다"
    elif msg.find('!익절') >= 0:
        return "영-구-손-실"
    elif msg.find('!손절') >= 0:
        return "영-구-손-실"
    elif msg.find('!암드') >= 0:
        return "암숏딱"
    return None
