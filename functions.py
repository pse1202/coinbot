from coinone import USD

def functionlist(msg):
    if msg.find('!환율') == 0:
        return str(USD())
    
    return None
