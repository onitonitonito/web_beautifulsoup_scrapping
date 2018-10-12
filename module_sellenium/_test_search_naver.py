"""
# 셀레니움 / 크롬 드라이버 브라우저 자동제어 테스트
# 구글을 열고, 'ChromeDriver'에 대해서 키워드 검색 해주고,
# 잠시 대기후, 종료 - 각 단계마다, 5초씩 sleep
# ---------------------------------------------------
# 구글의 키워드 검색은 쿼리(q=)명령어 다음 파라메터로 실행
# 네이버는, &query=... / 구글, 다음은, &q=...
#
# Optional argument, if not specified, will search path.
# driver = webdriver.Chrome('/Anaconda3/chromedriver')
# Registered already in sys.path '/Anaconda3/chromedriver'
# ChromeDriver Ver 2.43
"""
print(__doc__)


import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('http://search.naver.com')
time.sleep(3)

search_box = driver.find_element_by_name('query')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)

driver.quit()
