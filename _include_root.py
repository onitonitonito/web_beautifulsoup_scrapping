"""
# Root dir 을 시스템 Path 에 포함시키는 모듈
#   - 모든 프로그램을 루트기준으로 실행 시키기 위함
#   - _script_run_utf8 같은 기본 모듈을 asset 에 저장후 실행
#
"""
print(__doc__)

import os
import sys

# ROOT_NAME =  "web_beautifulsoup_scrapping"
# DIRS = os.path.dirname(__file__).partition(ROOT_NAME)
# DIR_ROOT = DIRS[0] + DIRS[1]
# DIR_ASSET = DIR_ROOT + "/asset/"


def get_dict_dir(root_name):
    """ roor_name 폴더를 기준으로 현재 프로젝트 폴더의 주요정보를 받는다. """
    dict_dirs = {}
    dict_dirs['root_name'] = root_name
    dict_dirs['dirs'] = os.path.dirname(
        __file__).partition(dict_dirs['root_name'])
    dict_dirs['dir_root'] = dict_dirs['dirs'][0] + dict_dirs['dirs'][1]
    dict_dirs['dir_asset'] = os.path.join(dict_dirs['dir_root'], "asset", "")
    return dict_dirs


def main():
    DIRS = get_dict_dir(root_name="web_beautifulsoup_scrapping")

    for i, (_, item_value) in enumerate(DIRS.items(), 1):
        print(f"{i:2}. {_:10} : {item_value}")


if __name__ == '__main__':
    main()
