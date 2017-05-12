import requests
import json

def USD():
    return float(requests.get("https://api.coinone.co.kr/currency/").json()['currency'])

