"""
# class_functions.py - define general functions for own use.
"""
# using for :
print(__doc__)
import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup



def get_html_soup(url_target, getter=1):
    """
    # get beautifulsoup response, using selecting 1 out of 2 ways
    #   * getter=1 ... requests.get(url_target)
    #   * getter=2 ... urlopen(url_target)
    """
    if getter == 1:
        response = requests.get(url_target)   # getter == 1
        status_code = response.status_code
        markup = response.text
    else:
        response = urlopen(url_target)
        status_code = response.getcode()
        markup = response
    print(f"status_code = [{status_code}] \n")
    return BeautifulSoup(markup=markup, features='html.parser')


def get_finders(tags, html_soup):
    """ html_soup에서 Tags기준에 부합하는 결과array(finders)추출반환"""
    return html_soup.find_all(*tags)


def get_regex_extracts(regex_pattern, string_target):
    """스트링에서 href 부분을 regex패턴으로 찾아서 추출 반환한다"""
    try:
        extracts = re.compile(regex_pattern).findall(
            string_target)  # finder array
    except:
        extracts = ["N/A", ]
    return extracts


def save_str_file(string_data, filename_with_dir):
    """ string_data 를 txt형 화일로 저장한다."""
    filename = filename_with_dir.split("\\")[-1]
    print(f"'string_data'가 txt형 화일({filename})로 생성 되었습니다..")

    with open(file=filename_with_dir, mode='w', encoding='utf8') as f:
        f.write(string_data)


def save_excel(rows_2d_array, filename_with_dir):
    """
    # openpyxl을 이용하여 excel 화일로 저장한다 / import openpyxl 필요
    # rows_2d_array 를 입력받아 row(1d)로 한줄씩 쪼개서 WS.append(row)한다.
    # 최종적으로 WB.save(file_dir) / WB.close() 한다
    """
    import openpyxl as opx
    filename = filename_with_dir.split("\\")[-1]

    WB = opx.Workbook()
    WS = WB.active

    for row in rows_2d_array:
        WS.append(row)

    WB.save(filename_with_dir)
    WB.close()
    print(f"'rows_2d_array'가 excel화일({filename})로 생성 되었습니다..")



if __name__ == '__main__':
    # only for test!
    tags = ['a', {'class' : 'link_txt'}]
    html_soup = get_html_soup("http://www.daum.net", getter=2)
    finders = get_finders(tags, html_soup)

    [print(find.text) for find in finders]
