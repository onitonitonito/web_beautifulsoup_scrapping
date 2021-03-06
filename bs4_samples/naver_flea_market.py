"""
# 웹크롤링 - . XPATH를 이용하여 크롤링하기
# https://www.fun-coding.org/crawl_advance5.html
# -----
# facebook : opentutorial.org
#
\n\n\n"""
print(__doc__)
from selenium import webdriver


file_loc_mac = '/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs'
file_loc_win = 'C:/phantomjs-2.1.1-windows/bin/phantomjs.exe'
driver = webdriver.PhantomJS(file_loc_win) # 윈도우

url='http://v.media.daum.net/v/20170922175202762'
driver.get(url)


# ----- main / problematic part -----------
curr_page = 1

while curr_page < 6:
    elem = driver.find_element_by_xpath("//div[@id='main-area']/div[5]")
    trs = elem.find_element_by_xpath("./table/tbody/tr")

    for tr in trs:
        # if not lit.get_attribure('align'):
        #     continue

        atag = tr.find_element_by_xpath("./td/div[2]/div/a")
        print(atag.text)

    input()

    curr_page = curr_page + 1
    page = driver.find_element_by_link_text(str(curr_page))
    page.click()



"""
에러 = main 이하,
-------------------
selenium.common.exceptions.NoSuchElementException:
Message: {
    "errorMessage":"Unable to find element with xpath '//div[@id='main-area']/div[5]'",

    "request":{
        "headers":{"Accept":"application/json",
        "Accept-Encoding":"identity",
        "Content-Length":"113",
        "Content-Type":"application/json;charset=UTF-8",
        "Host":"127.0.0.1:4007",
        "User-Agent":"selenium/3.14.0 (python windows)"
    },

    "httpVersion":"1.1",
    "method":"POST",

    "post":"{\"using\": \"xpath\", \"value\": \"//div[@id='main-area']/div[5]\", \"sessionId\": \"d1f72aa0-27ae-11e9-9cdc-a732dc688137\"}",

    "url":"/element",
    "urlParsed":{
        "anchor":"",
        "query":"",
        "file":"element",
        "directory":"/",
        "path":"/element",
        "relative":"/element",
        "port":"",
        "host":"",
        "password":"",
        "user":"",
        "userInfo":"",
        "authority":"",
        "protocol":"",
        "source":"/element",
        "queryKey":{},
        "chunks":[
            "element"]
    },

    "urlOriginal":"/session/d1f72aa0-27ae-11e9-9cdc-a732dc688137/element"
    }
}
Screenshot: available via screen
"""
