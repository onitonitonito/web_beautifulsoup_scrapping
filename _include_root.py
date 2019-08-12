"""
# Root dir 을 시스템 Path 에 포함시키는 모듈
#   - 모든 프로그램을 루트기준으로 실행 시키기 위함
#   - _script_run_utf8 같은 기본 모듈을 asset 에 저장후 실행
#
"""
print(__doc__)

import os
import sys

ROOT_NAME =  "web_beautifulsoup_scrapping"

DIRS = os.path.dirname(__file__).partition(ROOT_NAME)
DIR_ROOT = DIRS[0] + DIRS[1]
DIR_ASSET = DIR_ROOT + "/asset/"


if __name__ == '__main__':
    print(DIRS)
    print(ROOT_NAME)
    print(DIR_ROOT)
    print(DIR_ASSET)
