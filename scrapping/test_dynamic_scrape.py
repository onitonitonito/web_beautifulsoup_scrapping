"""
# Normal WebScrapping Example - TutorialPoint.com
# https://www.tutorialspoint.com/python_web_scraping/
  python_web_scraping_dynamic_websites.htm
"""

"""
"""
import re
import urllib.request

response = urllib.request.urlopen('http://example.webscraping.com/places/default/search')
html = response.read()
text = html.decode()
re.findall('(.*?)',text)
# OUTPUT []

"""
import requests
url=requests.get('http://example.webscraping.com/ajax/search.json?page=0&page_size=10&search_term=a')
url.json()
"""

import string
import requests

PAGE_SIZE = 15

url = 'http://example.webscraping.com/ajax/'
file = 'search.json'
query = 'page={}&page_size={}&search_term={}'

url_combo = f"{url}{file}?{query}"

countries = set()

page = 0

for letter in string.ascii_lowercase:
    print("Searching with '%s'" % letter)
    page = 0

    while True:
        response = requests.get(url_combo.format(page, PAGE_SIZE, letter))
        data = response.json()

        print('adding %d records from the page %d' %
        (len(data.get('records')), page))

        for record in data.get('records'):
            countries.add(record['country'])
            page += 1
            if page >= data['num_pages']:
                break

with open('countries.txt', 'w') as countries_file:
    countries_file.write('n'.join(sorted(countries)))
