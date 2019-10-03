"""
# general scrapping test
#
"""
# print(__doc__)

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# URL = 'http://api.aoikujira.com/ip/ini'
# URL = 'http://www.naver.com'
URL1 = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
URL2 = 'https://namu.wiki/w/Dirty%20Bomb(%EA%B2%8C%EC%9E%84)'


def get_whole_scrap(target_url):
    # READOUT Whole DATA
    _html = urlopen(url=target_url)
    _bs_obj = BeautifulSoup(_html, 'html.parser')

    byte_data = _html.read()
    return byte_data


def test1_show_whole_bytes(target_url):
    byte_data = get_whole_scrap(target_url)   # 'byte' data
    print('\n(1) DATA = ', byte_data)  # byte type 'str'

    # SHOW DATA Decoded
    _text = byte_data.decode('UTF-8')
    print('\n(2) TEXT = ', _text)  # decoded 'str' with 'CODEC=UTF-8'
    pass


def show_URL1_wiki_kevin_bacon(target_url):
    """ scraping internal links : start with '/wiki'
    /wiki/Benicio_del_Toro
    /wiki/Michael_Douglas
    /wiki/Miguel_Ferrer ....
    """
    html = urlopen(target_url)
    bs_obj = BeautifulSoup(html, 'html.parser')

    for link in bs_obj.find('div', {'id': 'bodyContent'}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def for_URL2_namu_dirty_bomb(target_url):
    html = urlopen(target_url)
    bs_obj = BeautifulSoup(html, 'html.parser')

    print(type(bs_obj))

    _f1, _f2 = ('div', {'id':'card recent-card'})
    _findAll_args = ("a", re.compile('^(/w/)((?!:).)*$')) # href=re.compile..

    for link in bs_obj.find('div', {'id':'recentChangeTable'}).findAll('a', href=re.compile('^(/w/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])
    pass


if __name__ == '__main__':
    # test1_show_whole_bytes(URL1)
    show_URL1_wiki_kevin_bacon(URL1)
    # for_URL2_namu_dirty_bomb(URL1)
    # for_URL2_namu_dirty_bomb(URL2)

    pass
