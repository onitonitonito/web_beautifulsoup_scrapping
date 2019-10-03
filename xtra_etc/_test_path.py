"""
# 1. 루트DIR 모듈 실행 시키기 / 상위DIR 모듈 실행시키기
#
# 2. 파티션 / 스플릿의 차이
#    - 리스트를 만들때 ROOT_DIR 를 리스트 맴버로 포함하느냐, 빼느냐의 문제
#    - 포함할때 = 파티션() / 제외할때 = 스플릿()
"""
import os
import sys

ROOT_WORD = 'web_beautifulsoup_scrapping'                 # root directory

WORK_DIR = os.path.dirname(__file__)
ROOT_DIR = WORK_DIR.partition(ROOT_WORD)[0] + WORK_DIR.partition(ROOT_WORD)[1]

print("WORK_DIR = ", WORK_DIR)
print("ROOT_DIR = ", ROOT_DIR)

print("partition(ROOT_WORD)=", WORK_DIR.partition(ROOT_WORD))
print("split(ROOT_WORD)=", WORK_DIR.split(ROOT_WORD))

sys.path.append(ROOT_DIR)

import _script_run_utf8
_script_run_utf8.main()

print(__doc__)
print("헬로우 스크립트런 월드!")
