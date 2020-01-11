"""
# config_autogui.py - 함수 및 변수들
"""
import os, sys

print(__doc__)

dir_top = "web_beautifulsoup_scrapping"
dir_array = os.path.dirname(__file__).partition(dir_top)
dir_root = "".join(dir_array[:2]) + "\\"
sys.path.insert(0, dir_root)

dir_assets = dir_root + "_assets\\"
dir_statics = dir_root + "_statics\\"
dir_logging = dir_root + "_logging\\"

dir_home = dir_root + "xautogui\\"
dir_home_images = dir_home + "images\\"


# COLOR CODE
BG_COLOR = (31, 231, 231)   # rgb(31,231,231)
RED = (237, 17, 121)        # rgb(237, 17, 121)
BLUE = (61, 92, 224)        # rgb(61, 92, 224)
GREEN = (22, 172, 13)       # rgb(22, 172, 13)
YELLOW = (245, 236, 49)     # rgb(245, 236, 49)
MAGENTA = (167, 87, 213)    # rgb(167, 87, 213)


def get_prep_time(str_time_fire="00:00:00", minute_before=1):
    """ 2분 전 시간으로 준비시간(str)을 반환한다"""
    fires = str_time_fire.split(":")
    minut_prep = int(fires[1]) - minute_before
    if minut_prep < 0:
        minut_prep += 59
    return f"{fires[0]}:{minut_prep:02}:{fires[2]}"





if __name__ == '__main__':
    # for TEST ... dir_root 변수만 필요 함 (가공하기 위한 과정)
    print(dir_root)
    print(dir_assets)
    print(dir_statics)
    print(dir_logging)
    print(dir_home)
    print(dir_home_images)
