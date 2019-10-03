"""
# root_name 을 기준으로 기본폴더 시스템을 dict_dirs 에 등록한다.
"""
print(__doc__)

import os
import sys

root_name="web_beautifulsoup_scrapping"

def get_dict_dirs(root_name):
    """ roor_name 폴더를 기준으로 현재 프로젝트 폴더의 주요정보를 받는다. """
    dict_dirs = {}
    dict_dirs['root_name'] = root_name

    dirs_temp = os.path.dirname(os.path.abspath(root_name)).partition(dict_dirs['root_name'])
    dict_dirs['dir_root'] = dirs_temp[0] + dirs_temp[1]
    dict_dirs['dir_assets'] = os.path.join(dict_dirs['dir_root'], "_assets", "")
    dict_dirs['dir_statics'] = os.path.join(dict_dirs['dir_root'], "_statics", "")
    return dict_dirs


def show_dict_dirs(root_name):
    """get_dict_dir 의 내용을 모니터링 / dict_dirs 를 반환한다"""
    dict_dirs = get_dict_dirs(root_name)

    for i, (item_key, item_value) in enumerate(dict_dirs.items(), 1):
        print(f"{i:2}. {item_key:10} : {item_value}")
    return get_dict_dirs(root_name)



if __name__ == '__main__':
    dict_dirs = show_dict_dirs(root_name)
    print(dict_dirs)
