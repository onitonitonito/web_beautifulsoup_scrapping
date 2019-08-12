"""
# HRD 수업>파이썬 자동화 스크립트
# - 이메일 추출기  http://bit.ly/2Kj14h1
# - 대상 문서 전체를 선택해서 ctrl-A,  ctrl-c
# - 그리고 프로그램을 실행한다
#     1. 클립보드에서 텍스트를 가져온다.
#     2. 텍스트에서 이메일 주소를 가져온다.
#     3. 클립보드에 다시 복사한다.
"""
print(__doc__)

import pyperclip
import re

email_regex = re.compile(
    r'''(
            [a-zA-Z0-9._%+-]+       # username
            @                       # @ symbol
            [a-zA-Z0-9.-]+          # domain name
            (\.[a-zA-Z]{2,4}){1,2}  # dot-something
            )''',
    re.VERBOSE
)


def fin_email_list():
    clip_board = pyperclip.paste()
    match = []
    for email in email_regex.findall(clip_board):
        match.append(email[0])
    return match


def resule_copy(match):
    if len(match) > 0:
        pyperclip.copy('\n'.join(match))
        print('클립보드에 복사 되었습니다.')
    else:
        print('패턴을 발견 하지 못하였습니다.')


def main():
    match = fin_email_list()
    resule_copy(match)


if __name__ == '__main__':
    main()
