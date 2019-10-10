"""
# crawl_webtoon_title_naver.py - 네이버 웹툰 제목 가져오기
# - http://bit.ly/2YK0r49
"""
# https://comic.naver.com/webtoon/weekday.nhn
# 먼저 월요일 웹툰의 제목만 추출을 해봅시다.

# root path 를 sys.path.insert 시키기 위한 코드 ... 최소 4줄 필요------------
import os, sys                                                          # 1
root_name = "web_beautifulsoup_scrapping"                               # 2
root = "".join(os.getcwd().partition(root_name)[:2])                    # 3
sys.path.insert(0, root)                                                # 4
# -------------------------------------------------------------------------

import requests
import _assets.script_run
from bs4 import BeautifulSoup

print(__doc__)

# 웹 페이지를 열고 소스코드를 읽어오는 작업
url_target = "http://comic.naver.com/webtoon/weekday.nhn"
html = requests.get(url_target)
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

def basic_crawl():
    # 요일별 웹툰영역 추출하기
    data1_list = soup.findAll('div', {'class': 'col_inner'})
    # pprint(data1_list)

    # 전체 웹툰 리스트
    week_title_list = []

    for data1 in data1_list:
        # 제목 포함영역 추출하기
        data2 = data1.findAll('a', {'class': 'title'})
        # pprint(data2)

        # 텍스트만 추출 2
        title_list = [dat.text for dat in data2]
        # pprint(title_list)
        week_title_list.extend(title_list)  # 단순하게 값을 추가해 1차원으로 만들려면 extend
        # week_title_list.append(title_list) #요일별로 나눠 2차원 리스트를 만들려면 append


def main():
    # 모든 웹툰 제목 영역 추출
    data = soup.findAll('a', {'class': 'title'})
    [print(f"{i+1:02}. {item.text}") for i, item in enumerate(data)]



if __name__ == '__main__':
    main()
    basic_crawl()
