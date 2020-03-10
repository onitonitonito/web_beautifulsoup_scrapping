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
        'mode'  :   'form',
        'url'   :   'https://www.naver.com',
    }
QUERY = "&".join([f"{key}={value}" for key, value in QUERIES.items()])

URL = 'https://nid.naver.com/nidlogin.login'
URL_TARGET = f"{URL}?{QUERY}"

# print(URL_TARGET); quit() # FOR TEST

# to load the user account information from config.ini(*hidden)
config = configparser.ConfigParser()
config.read('config.ini')

id = config.get('naver', 'id')
pw = config.get('naver', 'pw')

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(URL_TARGET)

# to extract 'id' input part
clipboard.copy(id)
driver.find_element_by_xpath('//*[@id="id"]').click()

ActionChains(driver).\
    key_down(Keys.CONTROL).send_keys('v').\
    key_up(Keys.CONTROL).perform()


# to extract 'pw' input part
clipboard.copy(pw)
driver.find_element_by_xpath('//*[@id="pw"]').click()

ActionChains(driver).\
    key_down(Keys.CONTROL).send_keys('v').\
    key_up(Keys.CONTROL).perform()

# to click 'log-in' button
driver.find_element_by_xpath('//*[@id="log.login"]').click()

# to move onto 'MAIL-MENU'
driver.get('https://mail.naver.com/')
titles = driver.find_elements_by_css_selector("strong.mail_title")

for idx, title in enumerate(titles, 1):
    print(f"{idx:02} - {title.text}")

# driver.quit()


def main():
    pass

if __name__ == '__main__':
    main()
