"""
# 셀레니움 / 크롬 드라이버 브라우저 자동제어 테스트
# 구글을 열고, 'ChromeDriver'에 대해서 키워드 검색 해주고,
# 잠시 대기후, 종료 - 각 단계마다, 5초씩 sleep
# ---------------------------------------------------
# 구글의 키워드 검색은 쿼리(q=)명령어 다음 파라메터로 실행
# 네이버는, &query=... / 구글, 다음은, &q=...
#
"""
# Optional argument, if not specified, will search path.
# driver = webdriver.Chrome('/Anaconda3/chromedriver')
# Registered already in sys.path '/Anaconda3/chromedriver'
# ChromeDriver Ver 2.43

import os
import sys

# '루트'와 '작업'디렉토리 설정 - for 스크립트런
HOME = "web_beautifulsoup_scrapping"
DIRS = os.path.dirname(__file__).partition(HOME)
ROOT = DIRS[0] + DIRS[1] + "/"
sys.path.append(ROOT)

# 스크립트런 '한글' 표시를 위한 커스텀모듈 실행
from _statics.config import _script_run_utf8
_script_run_utf8.main()

print(__doc__, flush=True)


import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('http://www.google.com')
time.sleep(3)

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)

driver.quit()
