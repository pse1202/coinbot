import requests
import json

def USD():
    return float(requests.get("https://api.coinone.co.kr/currency/").json()['currency'])

def BTC():
    return float(requests.get("https://api.coinone.co.kr/ticker/").json()['last'])

def coin(currency):
    return requests.get("https://api.coinone.co.kr/ticker/",params={'currency': currency}).json()['last']
