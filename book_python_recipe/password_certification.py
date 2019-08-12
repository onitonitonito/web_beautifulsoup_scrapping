"""
# 패스워드 검증기
#  1. input() 함수로 사용자로부터 패스워드를 입력 받는다.
#  2. 패스워드 규칙 : 8자 이상 / 영어 숫자 혼합
#  3. 입력된 패스워드 규칙에 맞으면 True 틀리면 False를 리턴
#  4. 패스워드를 검증하는 부분을 별도의 함수로 작성 최종적으로 메시지 출력
"""
print(__doc__)


def get_password():
    return input('\nENTER PASSWORD : ')


def get_certifed_array(password):
    """ passward certification returns True or False """
    answers = [
        (len(password) > 8) * 1,   # 1 / 0 --> should be bigger than 9
        password.isnumeric() * 1,  # 0 / 1 --> should be combined /w Alpha
        password.isalpha() * 1,    # 0 / 1 --> should be combined /w number
    ]
    return answers


def show_password_result(password=''):
    """ show result of checking password """
    if not password:
        password = get_password()

    answers = get_certifed_array(password)
    error_cases = [0, 1, 1]
    echo_messages = {
        'NG': [
            f"\n",
            f"NG! have a problems .... with '{password}' ",
            f"-------------------",
        ],
        'OK': [
            f"\n" * 15,
            f"OK! Perfect ... with '{password}' ",
            f"-------------------",
            f"Log-In Procesure Complete! {len(password) * '*'}",
            f"\n" * 5,
        ],
        'ERROR': [
            f"   -> should be longer than 8 digit",
            f"   -> should be combined /w Alpha",
            f"   -> should be combined /w number",
        ],
    }

    if answers == [1, 0, 0]:
        [print(echo) for echo in echo_messages['OK']]      # OK Messages
        return True

    else:
        [print(echo) for echo in echo_messages['NG']]      # NG Messages
        for i in range(3):
            if answers[i] == error_cases[i]:
                print(echo_messages['ERROR'][i])
        return False


def main():
    while True:
        if show_password_result():
            break


if __name__ == '__main__':
    main()
