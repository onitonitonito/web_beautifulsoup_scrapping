"""
# 간단한 크로울링 샘플 ( 다음과 네이버 비교 )
# https://wonderbout.tistory.com/31?category=1022729
# Posted on 2018.12.08 19:14 by 원더바웃
#
\n"""
print(__doc__)

import requests
from bs4 import BeautifulSoup


scrap_dict = {
    "naver": [
        "https://www.naver.com",
        ".ah_roll .ah_k",
    ],
    "daum": [
        "https://www.daum.net",
        ".hotissue_builtin .link_issue",
    ],
}


def arrange_list(list):
    """ refine doubled items to single in the list """
    refined_list = []
    for item in list:
        if not item in refined_list:
            refined_list.append(item)
    return refined_list


def get_soup_selections(url_target, class_filtered):
    """ using BS4 + requests, get filtered soup selections object """
    html = requests.get(url_target)
    response = BeautifulSoup(html.text, "html.parser")
    return response.select(class_filtered)


def get_scrapped_array(url_target, class_filtered):
    """ get text(str) list from filtered soup selections object """
    soup_selections = get_soup_selections(url_target, class_filtered)
    return [select.get_text() for select in soup_selections]


def get_name_array(url_target, class_filtered):
    """ url_name, rank_array from scrapping """
    rank = get_scrapped_array(url_target, class_filtered)
    rank_array = arrange_list(rank)
    url_name = url_target.split('.')[1].upper()
    return url_name, rank_array


def show_rank_echo(dict_key):
    """
    TIPS!: ( url_target, class_filtered ) = scrap_dict["name"]
    WARN!: Independancy --> *scrap_dict[dict_key]
    """
    (url_name, rank_array) = get_name_array(*scrap_dict[dict_key])

    print(f"  {url_name}")
    print("-" * 30)
    [print(f'{i:2}. {item}') for i, item in enumerate(rank_array, 1)]
    print("\n")


def show_comparison_rank(dict_key1, dict_key2):
    """
    WARN!: Independancy --> *scrap_dict[dict_key]
    ranking comparison with daum vs. naver for example, upto 10!
    """
    # (url_name, rank_array) = get_name_array(*scrap_dict[dict_key=name])
    (name01, rank01) = get_name_array(*scrap_dict[dict_key1])
    (name02, rank02) = get_name_array(*scrap_dict[dict_key2])

    print(f"  {name01:30} {name02}")
    print("-" * 40)
    for i in range(10):
        same01 = "*" if rank01[i] in rank02 else " "
        same02 = "*" if rank02[i] in rank01 else " "
        print(f'{i+1:2}. {same01} {rank01[i]:15} {rank02[i]} {same02}')
    print("\n")


def main():
    # Example.01 - 비교리스트 보기
    show_comparison_rank("daum", "naver")

    # Example.02 - 싱글리스트 보기
    show_rank_echo("naver")
    show_rank_echo("daum")



if __name__ == '__main__':
    main()
