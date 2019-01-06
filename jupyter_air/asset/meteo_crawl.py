"""
# 기상청 오픈API 이용하기 - 시간별 데이터 API
# ---------
# https://data.kma.go.kr/apiData/getData?type=json
# &dataCd=ASOS&dateCd=HR
# &startDt=20181230&startHh=01
# &endDt=20190101&endHh=12
# &stnIds=112
# &schListCnt=10&pageIndex=1
# &apiKey={?사용자키}
#
\n\n\n"""
# print(__doc__)


import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://data.kma.go.kr/apiData/getData?type=json'

pageIndex =  1          # ?
schListCnt =  30        # 데이터의 갯수

keys = [
    'stnIds',
    'dataCd',
    'dateCd',
    'startDt',
    'startHh',
    'endDt',
    'endHh',
    'apiKey',
    'pageIndex',
    'schListCnt',
]

opt = {
    'stnIds': '112',
    'dataCd': 'ASOS',
    'dateCd': 'HR',
    'startDt': '20181230',
    'startHh': '00',
    'endDt': '20190101',
    'endHh': '12',
    'pageIndex' : str(pageIndex),
    'schListCnt' : str(schListCnt),
    'apiKey': 'VjB7n%2BXskvO1NDDCYhVP6YiXWdG4kRGdfm4VzmY0uSR50ofTsnlrv6TL5l%2BkVlmBxX',
}


opt_str = [f'&{key}={opt[key]}' for key in opt.keys()]
opt_str = ''.join(opt_str)
full_url = f'{url}{opt_str}'



if __name__ == '__main__':
    print(full_url)
