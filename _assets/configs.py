"""
# configs.py - root_name 기준, 기본폴더 시스템을 dict_dirs 로 등록.
"""
print(__doc__)

import os
import sys
from os.path import join

root_name="web_beautifulsoup_scrapping"

def get_dict_dirs(root_name):
    """ roor_name 폴더를 기준으로 현재 프로젝트 폴더의 주요정보를 받는다. """
    dict_dirs = {}

    dirs_temp = os.getcwd().partition(root_name)
    dict_dirs['root_name'] = root_name
    dict_dirs['dir_root'] = "".join(dirs_temp[:2])

    dict_dirs['dir_assets'] = join(dict_dirs['dir_root'], "_assets", "")
    dict_dirs['dir_statics'] = join(dict_dirs['dir_root'], "_statics", "")
    dict_dirs['dir_results'] = join(dict_dirs['dir_root'], "_results", "")
    return dict_dirs


def show_dict_dirs(root_name):
    """get_dict_dir 의 내용을 보여주고 / dict_dirs 를 반환한다"""
    dict_dirs = get_dict_dirs(root_name)

    for i, (item_key, item_value) in enumerate(dict_dirs.items(), 1):
        print(f"{i:2}. {item_key:10} : {item_value}")
    print()
    return dict_dirs



dict_dirs = show_dict_dirs(root_name)




if __name__ == '__main__':
    print(dict_dirs)
