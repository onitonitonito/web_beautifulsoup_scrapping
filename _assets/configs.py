"""
# configs.py - root_name 기준, 기본폴더 시스템을 dirs_dict 로 등록.
"""
# join 과 dirs_dict 를 임포트하여 쓰면 된다.
# 나머지는 시스템dir목록 -dirs_dict를 만드는 단순한 과정

import os
import sys
from os.path import join

print(__doc__)
root_name="web_beautifulsoup_scrapping"

def get_dirs_dict(root_name):
    """ roor_name 폴더를 기준으로 현재 프로젝트 폴더의 주요정보를 받는다. """
    dirs_dict = {}

    dirs_temp = os.getcwd().partition(root_name)
    dirs_dict['root_name'] = root_name
    dirs_dict['dir_root'] = "".join(dirs_temp[:2])

    dirs_dict['dir_assets'] = join(dirs_dict['dir_root'], "_assets", "")
    dirs_dict['dir_statics'] = join(dirs_dict['dir_root'], "_statics", "")
    dirs_dict['dir_results'] = join(dirs_dict['dir_root'], "_results", "")
    return dirs_dict


def show_dirs_dict(root_name):
    """get_dict_dir 의 내용을 보여주고 / dirs_dict 를 반환한다"""
    dirs_dict = get_dirs_dict(root_name)

    print("\tKEY" ,"\t" * 3, "VALUE")
    print("----------"*6)
    for i, (item_key, item_value) in enumerate(dirs_dict.items(), 1):
        print(f"{i:2}. {item_key:11} : {item_value}")
    print()
    return dirs_dict



dirs_dict = show_dirs_dict(root_name)




if __name__ == '__main__':
    print(dirs_dict)
