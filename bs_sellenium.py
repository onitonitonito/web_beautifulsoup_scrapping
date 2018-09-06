"""
# from : facebook/pythonkorea
# https://www.facebook.com/groups/pythonkorea/permalink/1542991832450639/
"""
# python3 와 BeautifulSoup 그리고 selenium을 활용한 instagram crawling 프로그램을 개발중에 있습니다.
# 많은분들의 도움을 받아, 현재 selenium을 사용하여 원격으로 로그인을 하여 원하는 해시태그를 검색하는 로직 까지는 개발이 완료되었습니다.
# 하지만, 검색을 완료한 시점에서 해당 결과에 대해서 제가 원하는 정보들을 가져오고자 하는데 약간의 문제가 있는데.. 도움을 받을 수 있을까 하여 질문드립니다.

import time
import requests
import pymysql

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

hashTag = input("#해시태그를 입력 하세요 : ")


driver = webdriver.Chrome("C:\\Users\\{user_id}\\AppData\\Local\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/")

element_id = driver.find_element_by_name("username")
element_id.send_keys("{user_id}")

element_password = driver.find_element_by_name("password")
element_password.send_keys("{user_pw}")


driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/input""").submit()
driver.implicitly_wait(5)

driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""").send_keys(hashTag)
driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""").click()


# 실시간 검색어를 제공하는 웹이지를 읽음

time.sleep(15)
searchGet = driver.get('https://www.instagram.com/explore/tags/'+hashTag[1:])
time.sleep(15)

totalResult = driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/header/span/span""").text()
print(totalResult)



# 이런식으로 totalResult 의 값을 출력하면

# <selenium.webdriver.remote.webelement.WebElement (session="91fd434be1a131d848f0118f8c8d65cf", element="0.9582438371412298-1")>
# 라는 이상한 session 값만 가져오는데 해결방법이나 제가 잘못 코딩한 부분을 아시는 분을 지적해주시면 감사하겠습니다.

# find_element_by_xpath
# find_element_by_css_selector

# 이거저거 사용하여도 결과값을 동일하네요
# 추가로 사진 첨부합니다.

# 마지막 문단을 print(driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/header/span/span""").text)
# 와 같은 형태로 수정하였더니 정상적으로 작동합니다 감사합니다!
