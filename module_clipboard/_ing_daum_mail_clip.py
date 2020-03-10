"""
# crawling naver mail title by clipboard
# http://bit.ly/3aDR7VK - 2020.03/08 by An.KW
"""
# https://developer-ankiwoong.tistory.com/55

import time
import clipboard
import configparser

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

print(__doc__)

QUERIES = {
        'continue' : 'https://logins.daum.net/accounts/ksso.do?rescue=true',
        'url'      : 'https://www.daum.net/',
    }
QUERY = "&".join([f"{key}={value}" for key, value in QUERIES.items()])

URL = 'https://accounts.kakao.com/login'
URL_TARGET = f"{URL}?{QUERY}"

# print(URL_TARGET); quit()   # FOR TEST!

# to load the user account information from config.ini(*hidden)
config = configparser.ConfigParser()
config.read('config.ini')

try:
    id = config.get('daum', 'id')
    pw = config.get('daum', 'pw')

except:
    print("\n *** ERROR *** - There's no config.ini! Check it out, plz!")
    quit()


driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get(URL_TARGET)



clipboard.copy(id)
driver.find_element_by_xpath('//*[@id="id_email_2"]').click()

ActionChains(driver).\
    key_down(Keys.CONTROL).send_keys('v').\
    key_up(Keys.CONTROL).perform()


clipboard.copy(pw)
driver.find_element_by_xpath('//*[@id="id_password_3"]').click()

ActionChains(driver).\
    key_down(Keys.CONTROL).send_keys('v').\
    key_up(Keys.CONTROL).perform()


driver.find_element_by_xpath('//*[@id="btn_g btn_confirm submit"]').click()


# You can try the below 2 methods to click on element.

"""
 # to extract 'id' input part
    <input data-type="text"
    class="tf_g tf_email"
    name="email"
    validator="email_or_phone"
    tabindex="1"
    type="text"
    id="id_email_2"
    data-error-empty="이메일 또는 전화번호를 입력해주세요."
    data-error-invalid="이메일 또는 전화번호 형식이 올바르지 않습니다.">

 # to extract 'pw' input part
    <label for="id_password_3" class="lab_g lab_txt screen_out">
    비밀번호</label>

 # to click 'log-in' button
    <button class="btn_g btn_confirm submit" type="button" tabindex="3">
    로그인</button>
"""
# METHODS - 1
element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
driver.execute_script("arguments[0].click();", element)

# METHODS - 2
element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()


# to move onto 'MAIL-MENU'
driver.get('https://mail.naver.com/')
titles = driver.find_elements_by_css_selector("strong.mail_title")

for idx, title in enumerate(titles, 1):
    print(f"{idx:02} - {title.text}")

# driver.quit()
