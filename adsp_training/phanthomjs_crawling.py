"""
# 웹크롤링 - . XPATH를 이용하여 크롤링하기
# https://www.fun-coding.org/crawl_advance5.html
# -----
# facebook : opentutorial.org
#
\n\n\n"""
print(__doc__)

import selenium as se
from selenium import webdriver


url='http://v.media.daum.net/v/20170922175202762'
file_loc_mac = '/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs'
file_loc_win = 'C:/phantomjs-2.1.1-windows/bin/phantomjs.exe'

options = se.webdriver.ChromeOptions()
options.add_argument('headless')

driver = se.webdriver.Chrome(chrome_options=options)
driver.get(url)


title = driver.find_element_by_xpath("//title")

# head 태그 안에 있는 title 정보는 get_attribute('text') 메서드로 추출할 수 있습니다.
# driver.quit()
print('\n\n\n\n\n')
print (title.get_attribute('text'))
