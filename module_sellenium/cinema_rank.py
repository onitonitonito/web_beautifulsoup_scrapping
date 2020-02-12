"""
# Python-API
# [API]영화진흥원 박스오피스 순위 분위 = http://bit.ly/2uDXcSz
"""
# Coder AnKiWoong 2020. 2. 11. 21:14
# ------ ROOT path 를 sys.path.insert 시키는 코드 ... 최소 4줄 필요------
import os, sys                                                      # 1
TOP = "web_beautifulsoup_scrapping"                                 # 2
ROOT = "".join(os.path.dirname(__file__).partition(TOP)[:2])+"\\"   # 3
sys.path.insert(0, ROOT)                                            # 4
# ---------------------------------------------------------------------

import json
import requests
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

today = dt.datetime.now()
delta = dt.timedelta(days=-1)
yesterday = (today + delta).strftime('%Y%m%d')

urls = [
        'https://www.kobis.or.kr',
        'kobisopenapi',
        'webservice',
        'rest',
        'boxoffice',
        'searchDailyBoxOfficeList.json',
    ]

api_key = 'db71138481ee9a68cbd0ce4cf173e7fc'
api_url = '/'.join(urls) + f'?key={api_key}&targetDt={yesterday}'

# api URL 결과 확인하기
# print('API_URL = \n' + api_url)

r = requests.get(api_url)
r.encoding = 'utf-8'

if r.status_code != 200:
    print('[%d Error] %s' % (r.status_code, r.reason))
    quit()

result = json.loads(r.text)

filename_with_dir = ROOT + f'module_sellenium/statics/cinema_{yesterday}.json'
with open(file=filename_with_dir, mode='w', encoding='utf8') as file:
    json.dump(obj=result, fp=file, sort_keys=True, indent=2, ensure_ascii=False)


# 결과에서 영화 목록 배열을 데이터프레임으로 변환
df = pd.DataFrame(result['boxOfficeResult']['dailyBoxOfficeList'])
print(df.head())

# 분석이 필요한 컬럼을 추출하기
# 영화제목과 관람객수만 필터링 --> 막대그래프 생성
df_filter = df.filter(items=['movieNm', 'audiCnt'])
print(df_filter.head())

# 영화제목 -> 데이터프레임 인덱스
#  영화이름을 딕셔너리의 리스트로 사용하기

movie_list = list(df['movieNm'])   # 영화이름만 리스트로 추출
index_dict = {}

for idx, val in enumerate(movie_list):
    index_dict[idx] = val

# 딕셔너리의 인텍스와 컬럼이름을 변경
df_filter.rename(
    index=index_dict,
    columns={'audiCnt' : '관람객수'},
    inplace=True,
    )

print(df_filter.head())

df_filter_drop = df_filter.copy()
df_filter_drop.drop('movieNm', axis=1, inplace=True)
print(df_filter_drop.head())

# 통계를 수행할 컬럼의 데이터를 확인한다
# 관람객수 열 확인
print(df_filter['관람객수'])

# 관람객수 데이터를 숫자로 바꿔준다 --> 막대그래프를 그리기 위해서
df_filter_drop['관람객수'] = df_filter_drop['관람객수'].apply(pd.to_numeric)

# dtype : object --> int64 형식으로 형 변환 확인
print(df_filter_drop['관람객수'])

# 특성 열로 내림차순 정렬
# ascending=True(오름차순-기본값) / False(내림차순)
df_filter_drop.sort_values('관람객수', ascending=True, inplace=True)
print(df_filter_drop)

# 관람객수가 집계되지 않는 경우도 있기때문에 결측치를 제거한다
# 결측치가 있는 모든 행을 삭제한다 (관람객수 = 0, NA)
df_filter_drop.dropna()
empty_sum = df_filter_drop.isnull().sum()
print(empty_sum)


# 그래프 만들기 - 그래프 한글 깨짐 방지
from matplotlib import font_manager
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()

# plt.rcParams['font.family'] = 'NaruGothic'
plt.rcParams['font.family'] = font_name
plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = (16, 8)

# 전체 컬럼에 대한 시각화
df_filter_drop.plot.barh()
plt.title(f'{yesterday} 박스 오피스 순위')
plt.savefig(ROOT + f'module_sellenium/statics/cinema_{yesterday}.png')
plt.legend()
plt.grid()

plt.show()
plt.close()
