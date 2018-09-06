""" -------LESSON.01--The first BeautifulSoup! Enjoy Taste!(P.53)
  :URL = en.wikipedia.org/
    - link contains in <div id='bodyContent'> .. </div>
    - URL doesn't contain ';'
    - URL always start with '/wiki/'
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

URL = 'https://en.wikipedia.org/wiki/Kevin_Bacon'

def test01_wiki_kevin_bacon(URL):
    """ scraping internal links : start with '/wiki/'
    /wiki/Benicio_del_Toro
    /wiki/Michael_Douglas
    /wiki/Miguel_Ferrer ....
    """
    html = urlopen(URL)
    bs_obj = BeautifulSoup(html, 'html.parser')

    for link in bs_obj.find('div', { 'id':'bodyContent' }).findAll("a",
        href=re.compile('^(/wiki/)((?!:).)*$')):

        if 'href' in link.attrs:
            print(link.attrs['href'])
# test01_wiki_kevin_bacon(URL)

""" -------- LESSON.02 -- Make function / add module. (P.56)
  : get <article_name>
    - get whole links in <article>, return it in <links>
"""
import datetime
import random

random.seed(datetime.datetime.now())        # init. hashable internals.
URL = 'https://en.wikipedia.org'

def get_links(article_url):
    """ from the contentsfunc() lesson_01 --> make function """
    html = urlopen(URL + article_url)
    bs_obj = BeautifulSoup(html, 'html.parser')

    link = bs_obj.find('div',{ 'id':'bodyContent' }).findAll("a",
        href=re.compile('^(/wiki/)((?!:).)*$'))

    # """--- TEST ------------------"""
    # print('1)',type(link))
    # print('2)',link.__class__.__name__)
    # raise SystemExit
    # """--- END --------------------"""
    return link

links = get_links('/wiki/Kevin_Bacon')

while len(links) > 0:
    """ randomly surf the target <article_url> link's links until None """
    new_article = links[random.randint(0, len(links)-1)].attrs['href']

    print(new_article)
    links = get_links(new_article)  # randomly changes
