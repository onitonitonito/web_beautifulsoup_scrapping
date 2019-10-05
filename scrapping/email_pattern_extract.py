"""
# HRD 수업>파이썬 자동화 스크립트 - http://bit.ly/2Kj14h1
# - 클립보드 카피 된 내용중에서 이메일 주소만 추출
# - 다시 클립보드에 저장 (기존 내용 변경)
"""
# - 대상 문서 전체를 선택해서 ctrl-A,  ctrl-c
# - 그리고 프로그램을 실행한다
#     1. 클립보드에서 텍스트를 가져온다.
#     2. 텍스트에서 이메일 주소를 가져온다.
#     3. 클립보드에 다시 복사한다.
import os, sys                                          # 1
root_name = "web_beautifulsoup_scrapping"               # 2
root = "".join(os.getcwd().partition(root_name)[:2])    # 3
sys.path.insert(0, root)                                # 4

import re
import pyperclip

import _assets.script_run
from _assets.configs import *
print(__doc__)

json_file_with_dir = join(dict_dirs['dir_results'], 'email_extracts.json')
excel_file_with_dir = join(dict_dirs['dir_results'], 'email_extracts.xls')
regex_pattern = r'''(
        [ㄱ-힣]+[ㄱ-힣][ ]{0,2}[ㄱ-힣]+  # name consits with Korean
        [ ]{0,3}<                       # white space before bracket-open
        [a-zA-Z0-9._%+-]+               # email_id
        @                               # @ symbol
        [a-zA-Z0-9.-]+                  # domain name
        (\.[a-zA-Z]{2,4}){1,2}          # dot-something
        >                               # bracket-close
        )'''



def main():
    matches = find_email_list(regex_pattern)    # 이름 <{email_address}>
    result_dict = get_result_dict(matches)

    [print(f"{key+1:>2}. {value}") for key, value in result_dict.items()]

    if len(matches) > 0:
        string_cliped = '\n'.join(matches)
        pyperclip.copy(string_cliped)
        print('\n이메일 주소(regex_pattern)결과가 클립보드에 복사 되었습니다.')

        data_string =  str(result_dict)
        save_json(data_string, json_file_with_dir)

        rows_2d_array = [value for key, value in result_dict.items()]
        save_excel(rows_2d_array, excel_file_with_dir)

    else:
        print('이메일 주소(regex_pattern 패턴을 발견하지 못 하였습니다.')


def find_email_list(regex_pattern):
    """
    # 클립보드 copy내용 중에서 regex_pattern 만 추출한다
    # 추출 된 결과 들을 matches(array)로 반환한다
    """
    clip_board = pyperclip.paste()
    extracts = re.compile(regex_pattern, re.VERBOSE).findall(clip_board)

    matches = []
    for extract in extracts:
        matches.append(extract[0])
    return matches


def get_result_dict(matches):
    """
    # 추출된 결과(matches)는 regex_pattern 에 매칭되는 정보의 array 임
    # 추출된 regex array(matches)를 각각 필요정보를 분리하여 result_dict로 반환.
    """
    # 파이썬 라이브러리 기본 - 정규표현식
    # https://wikidocs.net/4308
    # https://www.fun-coding.org/DS&AL3-4.html
    # 필요한 정보의 종류는 그때그때 달라지는 custom 정보임
    pattern_domain = '@[a-zA-Z0-9]+'                    # @{domain name}
    pattern_name = '[ㄱ-힣]+[ ]{0,2}[ㄱ-힣]+'            # 한글+_한글+
    pattern_email = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+"  # 이메일 주소

    result_dict = {}
    index_dict = 0

    for match in matches:
        # 분리되는 정보 필터 들
        domain_name = re.compile(pattern_domain).findall(match)
        domain_name = str(domain_name[0]).replace("@", "")

        email_name = re.compile(pattern_name).findall(match)
        email_name = str(email_name[0]).strip()

        email_address = re.compile(pattern_email).findall(match)
        email_address = str(email_address[0]).strip()

        # 분리된 결과정보 result_dict의 내용 구성은 custom
        result_dict[index_dict] = [domain_name,
                                    email_name,
                                    email_address,
                                    match,
                                    ]
        index_dict += 1
    return result_dict


def save_json(json_type_data_string, filename_with_dir):
    """ json_type_data_string(result_dict)를 json 화일로 저장한다."""
    filename = filename_with_dir.split("\\")[-1]
    print(f"'json_type_data_string'가 json화일({filename})로 생성 되었습니다..")

    with open(file=filename_with_dir, mode='w', encoding='utf8') as f:
        f.write(json_type_data_string)


def save_excel(rows_2d_array, filename_with_dir):
    """
    # openpyxl을 이용하여 excel 화일로 저장한다 / import openpyxl 필요
    # rows_2d_array 를 입력받아 row(1d)로 한줄씩 쪼개서 WS.append(row)한다.
    # 최종적으로 WB.save(file_dir) / WB.close() 한다
    """
    import openpyxl as opx
    filename = filename_with_dir.split("\\")[-1]

    WB = opx.Workbook()
    WS = WB.active

    for row in rows_2d_array:
        WS.append(row)

    WB.save(excel_file_with_dir)
    WB.close()
    print(f"'rows_2d_array'가 excel화일({filename})로 생성 되었습니다..")




if __name__ == '__main__':
    main()
