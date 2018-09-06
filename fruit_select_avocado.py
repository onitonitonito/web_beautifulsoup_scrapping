""" LESSON : Various EXTRACTION of WORD 'AVOCADO' from Web-site (p.39)
* select from CSS
* extract form -- find.METHOD
* Use find.METHOD repeatedly!
"""

import os
from bs4 import BeautifulSoup

FILE_NAME = '01_fruit.html'
DESTIN_DIR = os.path.join(os.path.dirname(__file__),'sample_html', FILE_NAME)
print(DESTIN_DIR)

f = open(DESTIN_DIR, encoding='UTF-8')
SOUP = BeautifulSoup(f, 'html.parser')

# (1) select from CSS
print(SOUP.select_one('li:nth-of-type(8)').string)              # AVOCADO
print(SOUP.select_one('#ve-list > li:nth-of-type(4)').string)   # AVOCADO

print(SOUP.select("#ve-list > li[data-lo='us']")[1].string)     # AVOCADO
print(SOUP.select('#ve-list > li.black')[1].string)             # AVOCADO


# (2) extract form -- find.METHOD
condition_dict = {"data-lo":'us', 'class':'black'}
print(SOUP.find("li", condition_dict).string)                   # AVOCADO

# (3) Use find.METHOD repeatedly!
print(SOUP.find(id='ve-list')
          .find("li", condition_dict)
          .string)                                              # AVOCADO
