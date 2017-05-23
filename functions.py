from coinone import USD, coin
import datetime
import random

def functionlist(msg):
    if msg.find('!환율') == 0:
        return str(USD())
    if "편지" in msg:
        now = datetime.datetime.now()
        if random.random() > 0.7 and (now.month <= 6 or now.day <= 22):
            return "https://goo.gl/OlqK2c"
    if msg == "PING":
        return "PONG"
    if msg.find('!코인') == 0:
        return str(coin(msg[4:]))
    return None
