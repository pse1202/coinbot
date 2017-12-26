import requests
import urllib.parse

from bs4 import BeautifulSoup


code_cache = {
    '우리기술투자': '041190',
}
aliases = {
    '우기투': '우리기술투자',
}

class CodeNotfoundError(Exception):
    pass

code_search_url = 'http://finance.naver.com/search/searchList.nhn?query={}'

def extract_text_from_nodelist(l):
    return list(map(lambda a:a.get_text(), l))

def get_quote(stock_name):
    market = '한국시장'

    try:
        code = None
        if stock_name in aliases:
            stock_name = aliases[stock_name]
        if stock_name.isdigit():
            code = stock_name

        if code is None:
            if stock_name in code_cache:
                code = code_cache[stock_name]
            else:
                code_html = requests.get(
                    code_search_url.format(urllib.parse.quote_plus(stock_name.encode('euc-kr')))
                ).text
                code_soup = BeautifulSoup(code_html, "html.parser")
                lnk = code_soup.select('td.tit a')[0]
                found_name = lnk.get_text().replace('\n', '')
                if found_name == stock_name:
                    code = lnk.get('href').split('=')[1]
                    code_cache[stock_name] = code
                else:
                    raise CodeNotfoundError('코드 발견 실패: "{}" '.format(stock_name))

        info_html = requests.get('http://finance.naver.com/item/sise.nhn?code={}'.format(code)).text
        info_soup = BeautifulSoup(info_html, "html.parser")

        _is = extract_text_from_nodelist(info_soup.select('.rate_info tr td .blind'))

        stock_name = info_soup.select('.wrap_company h2 a')[0].get_text()
        prev_price = _is[0] # 전일가
        low_price = _is[5] # 저가
        high_price = _is[1] # 고가
        transaction_vol = _is[5] # 거래대금
        price_change, percentage = extract_text_from_nodelist(info_soup.select('.no_exday .blind'))
        updown = info_soup.select('.no_exday .ico')[1].get_text()
        quote_price = info_soup.select('.no_today .blind')[0].get_text() # 현재가

        result = ""
        result = '[{stock_name}({code})] 현재가 {quote_price}원({updown}{price_change}/{updown}{percentage}% | {low_price}원 - {high_price}원) / 거래대금 {transaction_vol}원 / 전일가 {prev_price}원'.format(stock_name=stock_name, code=code, quote_price=quote_price, low_price=low_price, high_price=high_price, transaction_vol=transaction_vol, prev_price=prev_price, updown=updown, price_change=price_change, percentage=percentage)
    except Exception as e:
        result = '[{market}] 에러! : {msg}'.format(market=market, msg=e.__repr__())

    return result
