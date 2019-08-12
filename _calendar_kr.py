import locale
import calendar

# 한국어 로케일을 설정 --- (* 1)
locale.setlocale(category=locale.LC_ALL, locale='ko_KR')

lc = calendar.HTMLCalendar()
body = lc.formatyear(theyear=2019, width=4)

# HTML의 머리말과 꼬리말을 지정 --- (* 2)
html = """
<html>
  <head>
    <style>
      table {padding: 15px}
      th {border - bottom: 1px solid gray}
      td {
        padding: 4px
        vertical - align: top
        }
      .sun {color: red}
      .sat {color: blue}
    </style>
  </head>
  <body>
  """ + body + """
  </body>
</html>"""

# 파일에 저장 --- (* 3)
with open(file="calendar2019.html", mode='wt', encoding='utf8') as f:
    f.write(html)
