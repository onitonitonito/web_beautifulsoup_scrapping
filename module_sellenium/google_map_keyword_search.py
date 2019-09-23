"""
# [Python] Selenium 으로 구글 맵에서 정보 뽑기 - 2017-12-07 14:03
# http://mcchae.egloos.com/11281390
"""
# [CODE]
# https://gist.github.com/mcchae/c9323d426aba8fcde3c1b54731f6cfbe
# print(__doc__)


import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# SEARCH = "Hotels in California, CA, USA"
SEARCH = "인천 송도 호텔"
TIMEOUT = 5

driver = None
try:
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 800)

    # 1) search
    driver.get("https://www.google.co.kr/maps")
    driver.implicitly_wait(TIMEOUT)

    # 검색 엘리먼트를 찾아 검색어를 입력하고
    elem = driver.find_element_by_id("searchboxinput")
    elem.send_keys(SEARCH)

    # 검색 단추를 누른다
    elem = driver.find_element_by_id("searchbox-searchbutton")
    elem.click()

    # 2) get result list
    for ndx in range(100):
        driver.implicitly_wait(TIMEOUT)
        # 현재 검색 목록에 대해 목록의 상위에 해당하는 엘리먼트를 구해옴 (기다렸다)
        elem = driver.find_element_by_class_name('widget-pane-content-holder')
        dt = elem.find_element_by_xpath('.//div/div[@role="listbox"]')
        rd = {}
        try:
            # 검색 결과 중에 ndx 번째 결과의 엘리먼트를 구해옴
            d = dt.find_element_by_xpath(f'.//div[@data-result-index="{ndx}"]')
            lines = d.text.split('\n')

            # 첫번째 줄은 호텔이름
            rd['hotel'] = lines[0]

            # 나머지 줄은 정보로
            rd['info'] = ','.join(lines[1:])

            # 해당 정보를 눌러 상세 정보 보기
            d.click()

            # 다음 몇초를 쉬는 이유는 아래의 elem 이나 back_button 등을
            # WebDriverWait로 구해와도 ElementNotVisibleException 등의 예외 때문
            # (아마도 지도에 표시를 하는 등 data binding 시간이 꽤 걸리는 듯)
            driver.implicitly_wait(TIMEOUT)

            # 상세 정보 엘리먼트 구해옴 (기다리며)
            elem = driver.find_element_by_class_name('widget-pane-content-holder')



            # 주소 구해옴 : 생략될 수 있기 때문에 try
            try:
                it = elem.find_element_by_xpath('.//div/div[@data-section-id="ad"]')
                rd['address'] = it.text
            except Exception:
                pass



            # 홈페이지 구해옴 : 생략될 수 있기 때문에 try
            try:
                it = elem.find_element_by_xpath('.//div/div[@data-section-id="ap"]')
                rd['homepage'] = it.text
            except Exception:
                pass


            # phone 구해옴 : 생략될 수 있기 때문에 try
            try:
                it = elem.find_element_by_xpath('.//div/div[@data-section-id="pn0"]')
                rd['phone'] = it.text
            except Exception:
                pass



            print(rd)
            # 이전 "검색결과로 돌아가기" 누름
            back_button = elem.find_element_by_xpath('.//div/button')
            back_button.click()

        except NoSuchElementException:
            # 검색 결과 중에 구해오기 위한 ndx 번째를 너머서면 못구하고 해당 오류가
            # 발생하므로 for loop 빠짐
            break   # End of list

        except Exception:
            raise

finally:
    # quit
    if driver is not None:
        driver.quit()
