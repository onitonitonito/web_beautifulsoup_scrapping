"""
* 청라, 송도지역 미세먼지 측정값 스크래핑
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup

columns = []

URLS = [
    'http://air.incheon.go.kr/airinch/real3.html?area_other_index=999991',
    'http://air.incheon.go.kr/airinch/real3.html?area_other_index=999992',
]

""" 주의!: 송도와 청라는 데이터 갯수가 틀려서 필터링 방법을 달리해야 함. """
URL = URLS[0]  # 0=청라 - 측정치 4개
URL = URLS[1]  # 1=송도 - 측정치 7개

RESPONSE = requests.get(URL)
SOUP = BeautifulSoup(RESPONSE.content, 'html.parser')
TABLE = SOUP.find_all('table', {'class': 'view'})

TDS = TABLE[0].find_all('td')
FONTS = TABLE[0].find_all('font')
SPANS = TABLE[0].find_all('span')

DATA = []
DATE = []

for n, span in enumerate(SPANS, 0):
    neat_span = str(span.text).strip()

    if len(neat_span) > 12:
        """ 날짜와 시간을 분리해서 각각 넣는다 """
        DATE.append(neat_span[:-3])     # 날짜
        DATA.append(neat_span[-3:])     # 시간
    else:
        DATA.append(neat_span)

""" 리스트에 담긴 해당 날짜를 보여준다, 그래봤자 2개 지만.. """
print(DATE[0])
print(DATE[1])

START = 8               # 8,
REPEAT = 100

NUM = 0
for n in range(START, (6 * (REPEAT + 2)), 7):
    datum = DATA[n:n + 7]

    if len(datum) is not 0:
        NUM += 1
        print("%2s .. %s" % (NUM, datum))
    else:
        break
