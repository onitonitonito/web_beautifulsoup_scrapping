"""
# 파이썬 셀레니움(selenium) 이용 네이버 자동로그인
# --------
# 2018.09.24 07:29 by 테리엇의 디지털 놀이터
# https://tariat.tistory.com/397?category=678799
#
# Optional argument, if not specified, will search path.
# driver = webdriver.Chrome('/Anaconda3/chromedriver')
# Registered already in sys.path '/Anaconda3/chromedriver'
# ChromeDriver Ver 2.43
\n\n"""
print(__doc__)

import time
from selenium import webdriver

site_goto = 'http://www.naver.com'

# browser = webdriver.Chrome('/Users/open/Documents/chromedriver')
browser = webdriver.Chrome()
browser.get(site_goto)

login_bt=browser.find_element_by_class_name('lg_local_btn')
login_bt.click()

id=browser.find_element_by_id('id')
id.send_keys("ID입력-type your ID here..")
time.sleep(1)

id=browser.find_element_by_id('pw')
id.send_keys("PW입력-type your PW here..")
time.sleep(1)


time.sleep(4)
naver_submit=browser.find_element_by_class_name('btn_global')
naver_submit.click()
