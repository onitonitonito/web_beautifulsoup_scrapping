"""
# 파이썬을 이용한 자동화 스크립트 - 연습문제 15
# http://bit.ly/2GWN6z4
#
"""
# 1. baseball_databank_master 폴더의 모든 csv 화일탐색
# 2. CSV 화일 읽기
# 3. CSV 화일의 첫번째 줄을 제거하고 다른 화일로 저장
# 4. 로깅 화일을 작성한다.

# /baseball_databank_master
# - log.txt
# ㄴ core
#     - original_csvfile.csv
# ㄴ header_removed
#     - header_removed.csv

print(__doc__)

import os
import csv
import logging

DIRS = {
        'current' : os.path.dirname(__file__),
        'genesis': 'web_beautifulsoup_scrapping',
        'root': 'baseball_databank_master',
        'core': 'core',
        'modify': 'header_removed',
    }

logging.basicConfig(
    level=logging.DEBUG,
    filename=DIRS['root'] + 'log.txt',
    format='%(asctime)s - %(message)s'
)


def save_and_remove_header(filename):
    csv_rows = []
    with open(
            file=os.path.join('baseball_databank_master', 'core', filename),
            mode='r',
            encoding='utf8',) as f:

        reader = csv.reader(file)

        for row in reader:
            if reader.line_num == 1:
                continue                # 첫번째 라인은 Skip
            csv_rows.append(row)

    with open(file=os.path.join('baseball_databank_master', 'header-removed', filename),
              mode='w',
              newline='',
              encoding='utf8',) as f:

        writer = csv.writer(file)

        for row in csv_rows:
            writer.writerow(row)


def main():
    # 해더가 제거된 ㅠㅏ일이 저장될 폴더를 만든다.
    os.makedirs(os.path.join('baseball_databank_master',
                             'header-removed'), exist_ok=True,)

    # 작업디렉토리의 모든 CSV 파일을 순회한다.
    for filename in os.listdir(os.path.join('baseball_databank_master', 'core')):
        if not filename.endswith('.csv'):
            continue                    # 확장자가 .csv가 아니면 skip

        # 작업현황 로깅
        logging.debug(f'saving file: {filename}')

        print(f'saving file : {filename}')

        save_and_remove_header(filename)


if __name__ == '__main__':
    main()
