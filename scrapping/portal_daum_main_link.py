"""
#
#
"""
# print(__doc__)
import re
import requests
import script_run

from bs4 import BeautifulSoup
from urllib.request import urlopen

url_target = "http://www.daum.net"

tags = ["a", { 'class' : 'link_txt'}]       # 주요기사
tags = ["a", { 'class' : 'link_favorsch'}]  # 인기 검색어

def main():
    response = get_html_soup(url_target, getter=2)
    finders = get_finders(tags, response)

    show_results_listed(finders, tags, detailed=0)
    show_results_listed(finders, tags, detailed=1)


def get_html_soup(url_target, getter=1):
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


def get_hyper_ref_url(string):
    """스트링에서 href 부분을 regex패턴으로 찾아서 추출 반환한다"""
    pattern = re.compile('(?<=href=").*?(?=")')

    try:
        hrefs = pattern.findall(string)  # finder array
    except:
        hrefs = ["N/A",]

    return hrefs[0]


def show_results_listed(finders, tags, detailed=False):
    print(f"find('{tags}') : {len(finders)}")
    print('-----------------'*4)
    for i, find in enumerate(finders, 1):
        text_string = find.text.replace('\n', '')
        href_string = get_hyper_ref_url(str(find))

        if detailed:
            print(f"{i:>02}. {text_string}")
            print(f"  - {href_string}")
            print('-----------------'*4)
        else:
            print(f"   {i:>02}. {text_string}")

    print("\n")



if __name__ == '__main__':
    main()
