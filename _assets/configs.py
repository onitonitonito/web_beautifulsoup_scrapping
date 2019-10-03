"""
# _assets/configs.py - 각종변수 및 Path를 지정
"""
print(__doc__)
import os
import sys


name_top = "web_beautifulsoup_scrapping"

dir_dict = {
    '_assets' : ['_assets',],
    '_misc' : ['_miscellaneous',],
    '_statics' : ['_statics',],
}

def get_dir_by_name(name_top):
    """
    top level name을 기준으로 dir을 반환한다.
    사용환경에 따라, 실행기준이 달라지기 때문에
    탑레벨을 시스템 path 에 추가한다.
    """
    dir_array = os.getcwd().partition(name_top)
    dir_by_name = "".join(dir_array[:2])
    return dir_by_name

def join_dir(*dirs_array):
    return os.path.join(*dirs_array)

def get_dir(dir_top, dir_dict, key_name):
    return os.path.join(dir_top, *dir_dict[key_name])





def main():
    dir_top = get_dir_by_name(name_top)
    print("top :", dir_top)

    print()
    print("_assets :", get_dir(dir_top, dir_dict, "_assets"))
    print("_misc :", get_dir(dir_top, dir_dict, "_misc"))
    print("_statics :", get_dir(dir_top, dir_dict, "_statics"))

if __name__ == '__main__':
    main()
