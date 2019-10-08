"""
# patents_extract.py - extract patent information from webpage
# url_target = "http://www.erubberdam.co.kr/technology.php"
"""
import os, sys                                          # 1
root_name = "web_beautifulsoup_scrapping"               # 2
root = "".join(os.getcwd().partition(root_name)[:2])    # 3
sys.path.insert(0, root)                                # 4
print(__doc__)

import _assets.script_run
from _assets.configs import *
from _assets.class_functions import *


url_target = "http://www.erubberdam.co.kr/technology.php"
tags = ['div', {'class': 'text_box'}]

regex_pattern = '(?<=href=").*?(?=")'
regex_pattern = '제10-\d\d\d\d\d\d\d호'


def main():
    response = get_html_soup(url_target, getter=1)
    finders = get_finders(tags, response)

    result_dict = {}
    index_dict = 0

    for find in finders:
        string_target = str(find.text)

        extracts = get_regex_extracts(regex_pattern, string_target)

        if extracts:
            extract = extracts[0]
            title = string_target.strip()
            title = title.replace("\n", "")
            title = title.replace(extract, "")

            pattern = '\d\d-\d\d\d\d\d\d\d'
            number = get_regex_extracts(pattern, extract)[0]

            result_dict[index_dict] = [number, title]
            index_dict += 1

            print(f"{index_dict:>2}. 제{number}호 - {title}")

    # print(result_dict)          # for test
    result_json = join(dict_dirs['dir_results'],'patents_extract.json')
    with open(file=result_json, mode='w', encoding='utf8') as f:
        f.write(str(result_dict))



if __name__ == '__main__':
    main()
