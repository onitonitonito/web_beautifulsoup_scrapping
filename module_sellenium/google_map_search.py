"""
# Selenium으로 구글 맵에서 정보뽑기 Develop Tip - 2017/12/07 13:19
# to crawl information from google map using selenium not API
# http://mcchae.egloos.com/11281390
"""
print(__doc__)


from selenium import webdriver

browser = webdriver.Chrome()
url_target = "https://www.google.co.kr/maps"

SEARCH_KEY = "인천 송도 호텔"


browser.get(url_target)
browser.implicitly_wait(3)

elem = browser.find_element_by_id("searchboxinput")
elem.send_keys(SEARCH_KEY)

elem = browser.find_element_by_id("searchbox-searchbutton")
elem.click()

class_names = [
    'section-listbox',
    'section-scrollbox',
    'scrollable-y',
    'scrollable-show',
]

elem = browser.find_element_by_class_name(' '.join(class_names))

""" now ... ing """
