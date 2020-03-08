"""
#
"""
import requests as rq

from noti import send
from table import print_table
from bs4 import BeautifulSoup

def template(data):
    '''
    도시 | 확진자증감 | 확진환자수 | 사망자수 | 발생률 | 일일검사건수(명)
    '''
    body = []
    for i in range(0, data['count']):
        body.append([
            data['city'][i],
            data['prev_rise'][i],
            data['confirm'][i],
            data['die'][i],
            data['rate'][i],
            data['check'][i]
        ])

    interests = ["city", "CheckInc", "Confirm", "Dead", "Incidence", "Inspec"]
    inside = print_table(lines=body, header=interests, totalwidth=80, mincol=6)
    string_inside = '\n'.join(inside)
    string = f"<code>{string_inside}</code>"
    return string

queries = [ "brdId=1",
            "brdGubun=13",
            "ncvContSeq=",
            "contSeq=",
            "board_id=",
            "gubun=",
        ]
        
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
query_string = "&".join(queries)

BASE_URL = f"{url}?{query_string}"
res = rq.get(BASE_URL)

soup = BeautifulSoup(res.content, 'html.parser')
total = soup.select('.sumline td')

result = {
    "city":["총합"],
    "prev_rise": [str(total[0].text)],
    "confirm": [str(total[1].text)],
    "die": [str(total[2].text)],
    "rate": [str(total[3].text)],
    "check": [str(total[4].text)],
    'count': 1
}

table_rows = soup.select('.num tbody tr')

for row in table_rows[1:]:
    city=row.select('th')[0].text
    tds = row.select('td')
    result["city"].append(city)
    result["prev_rise"].append(tds[0].text)
    result["confirm"].append(tds[1].text)
    result["die"].append(tds[2].text)
    result["rate"].append(tds[3].text)
    result["check"].append(tds[4].text)
    result['count'] += 1

data = template(result)
print(data)

helper = '''

Column Description:
- city: 도시
- CheckInc: 확진자증감
- Confirm: 확진자
- Dead: 사망자
- Incidence: 발생률
- Inspec: 검사자수
'''

send(data + helper)
