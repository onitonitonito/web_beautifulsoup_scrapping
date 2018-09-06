"""
* http://krksap.tistory.com/651
* p.32 - 파이썬을 이용한 데이터 분석 - 04 Chapter2
* json 화일 불러오기
"""

import json
import codecs

PROJ_PATH = "usagov_bitly_data2012-03-16-1331923249.json"

f = codecs.open(PROJ_PATH, "r", "utf-8")
records = [json.loads(line) for line in f]

print (records[1])

""" records[1] - JSON 데이터 화일의 내용 (딕셔너리 타입) """
# {
#     'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11',
#     'c': 'US',
#     'nk': 1,
#     'tz': 'America/New_York',
#     'gr': 'MA',
#     'g': 'A6qOVH',
#     'h': 'wfLQtf',
#     'l': 'orofrog',
#     'al': 'en-US,en;q=0.8',
#     'hh': '1.usa.gov',
#     'r': 'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf',
#     'u': 'http://www.ncbi.nlm.nih.gov/pubmed/22415991',
#     't': 1331923247,
#     'hc': 1331822918,
#     'cy': 'Danvers',
#     'll': [42.576698, -70.954903]
# }
