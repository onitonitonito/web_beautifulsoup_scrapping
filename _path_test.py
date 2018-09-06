import os
import sys

WORK_DIR = os.path.dirname(__file__)
ROOT_WORD = 'k_mooc_reboot'                 # root directory
ROOT_DIR = WORK_DIR.partition(ROOT_WORD)[0] + WORK_DIR.partition(ROOT_WORD)[1]
PICKLE_WITH_DIR = ROOT_DIR + '\\_static\\_pickle\\'

print("WORK_DIR = ", WORK_DIR)
print("ROOT_DIR = ", ROOT_DIR)

# 리스트를 만들때 ROOT_DIR 를 리스트 맴버로 포함하느냐, 빼느냐의 문제
# 포함할때 = 파티션()
# 제외할대 = 스플릿()
print("partition(ROOT_WORD)=", WORK_DIR.partition(ROOT_WORD))
print("split(ROOT_WORD)=", WORK_DIR.partition(ROOT_WORD))
