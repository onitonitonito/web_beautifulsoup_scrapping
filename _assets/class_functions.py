"""
# class_functions.py - define general functions for own use.
"""
# using for :
print(__doc__)
import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup



def get_response(url_target, getter=1):
    """
    # get beautifulsoup response, using selecting 1 out of 2 ways
    #   * getter=1 ... requests.get(url_target)
    #   * getter=2 ... urlopen(url_target)
    """
    html = requests.get(url_target).text   # getter == 1
    if getter == 2:
        html = urlopen(url_target)
    return BeautifulSoup(markup=html, features='html.parser')


def get_finders(tags, response):
    """ response에서 Tags기준에 부합하는 결과array(finders)추출반환"""
    return response.find_all(*tags)


def get_regex_extracts(regex_pattern, string_target):
    """스트링에서 href 부분을 regex패턴으로 찾아서 추출 반환한다"""
    try:
        extracts = re.compile(regex_pattern).findall(
            string_target)  # finder array
    except:
        extracts = ["N/A", ]
    return extracts
