import requests

url = 'https://crix-api.upbit.com/v1/crix/recent'
market = 'Upbit'
code_format = 'CRIX.UPBIT.{to_currency}-{from_currency}'
codes = [
  "BCC",
  "BTC",
  "BTG",
  "POWR",
  "ETH",
  "NEO",
  "ETC",
  "LSK",
  "DASH",
  "XMR",
  "ZEC",
  "XLM",
  "STRAT",
  "REP",
  "OMG",
  "ADA",
  "LTC",
  "WAVES",
  "QTUM",
  "STORJ",
  "XRP",
  "KMD",
  "SBD",
  "EMC2",
  "ARK",
  "MER",
  "XEM",
  "GRS",
  "STEEM",
  "MTL",
  "ARDR",
  "SNT",
# mi sang jang coins:
#   "GBYTE",
#   "DGD",
#   "GNO",
#   "DCR",
#   "ZEN",
#   "BLOCK",
#   "XZC",
#   "FCT",
#   "SLS",
#   "NMR",
#   "PART",
#   "MCO",
#   "CLOAK",
  "VTC",
#   "KORE",
  "PIVX",
#   "DYN",
#   "RADS",
#   "SPHR",
#   "MONA",
#   "SALT",
#   "IOP",
#   "TX",
#   "BNT",
#   "GAME",
#   "EXP",
#   "PAY",
#   "VIA",
#   "ANT",
#   "SWT",
#   "EXCL",
#   "UBQ",
#   "SIB",
#   "ION",
#   "NBT",
#   "SHIFT",
#   "NXS",
#   "ADX",
#   "NAV",
#   "BSD",
#   "VRC",
#   "QRL",
#   "MYST",
#   "RLC",
#   "EDG",
#   "DCT",
#   "WINGS",
#   "AGRS",
#   "MAID",
#   "1ST",
#   "CVC",
#   "XEL",
#   "UNB",
#   "OK",
#   "RISE",
#   "SYNX",
#   "MEME",
#   "BLK",
#   "SYS",
#   "GNT",
#   "XAUR",
  "TIX",
#   "SNGLS",
#   "PTOY",
#   "AMP",
#   "LBC",
#   "BAT",
#   "GUP",
#   "FTC",
#   "MUE",
#   "HMQ",
#   "CFI",
#   "NXT",
#   "VOX",
#   "RCN",
#   "BAY",
#   "ADT",
#   "FUN",
#   "MANA",
#   "XVG",
#   "DGB",
#   "VIB",
#   "SAFEX",
#   "BURST",
#   "SC",
#   "BITB",
#   "XDN",
#   "DOGE",
#   "RDD"
] # use `copy($('table.highlight tr td.tit em').map((i, e) => e.textContent.replace('/KRW', '')).toArray())` to retrieve
params_all = ','.join(map(lambda s:code_format.format(to_currency='{to_currency}', from_currency=s), codes))

def format_number(title, input, to_currency):
    form = '[{title}] {number:,} {to_currency}  '
    if to_currency == 'KRW':
        if input > 300:
            number = int(input)
        else:
            number = input
    elif to_currency == 'BTC':
        sats = int(input * 100000000)
        if sats > 10000:
            number = input
        else:
            number = sats
            to_currency = 'sats'
    else:
        number = input
    
    return form.format(title=title, number=number, to_currency=to_currency)

def get_currency(from_currency, to_currency='KRW'):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    try:
        result = "{} >> ".format(market)
        params = {
            'codes': ''
        }
        if from_currency == 'ALL' or from_currency == '*':
            params['codes'] = params_all.format(to_currency=to_currency)
            li = requests.get(url, params=params).json()
            for idx, c in enumerate(codes):
                formatted = format_number(c.upper(), li[idx]['tradePrice'], to_currency)
                result += formatted
        elif from_currency == 'TOP5' or from_currency == 'TOP10':
            cut = 5 if from_currency == 'TOP5' else 10
            params['codes'] = params_all.format(to_currency=to_currency)
            li = requests.get(url, params=params).json()
            li = sorted(li, key=lambda currency: currency['accTradePrice24h'], reverse=True)[:cut]
            for c in li:
                tit = c['code'].replace('CRIX.UPBIT.{to_currency}-'.format(to_currency=to_currency), '')
                formatted = format_number(tit, c['tradePrice'], to_currency)
                result += formatted
        else:
            params['codes'] = code_format.format(from_currency=from_currency, to_currency=to_currency)
            li = requests.get(url, params=params).json()
            formatted = format_number(from_currency, li[0]['tradePrice'], to_currency)
            result = formatted
    except IndexError as e:
        result = '[{market}] 에러! : {msg}'.format(market=market, msg=e.__repr__() + ' (존재하지 않는 화폐 가능성)')
    except Exception as e:
        result = '[{market}] 에러! : {msg}'.format(market=market, msg=e.__repr__())

    return result
