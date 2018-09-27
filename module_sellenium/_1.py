"""
#
#
#
"""
print(__doc__)

import os
import sys
# '루트'와 '작업'디렉토리 설정 - for 스크립트런
HOME = "web_beautifulsoup_scrapping"
DIRS = os.path.dirname(__file__).partition(HOME)
ROOT = DIRS[0] + DIRS[1] + "/"

# 스크립트런 '한글' 표시를 위한 커스텀 모듈 실행
sys.path.append(ROOT)
from _static.config import _script_run_utf8
_script_run_utf8.main()




import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
