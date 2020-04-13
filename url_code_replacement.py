"""
# 대체 URL 코드 - %26, %2F, %3A, %3F, %3D
"""
# 출처: https://shinb.tistory.com/398 [신비 블로그]
# - 2010. 8/10. 14:31

replaces = {
            '%20' :     ' ',
            '%26' : 	'&',
            '%2F' : 	'/',
            '%3A' : 	':',
            '%3F' : 	'?',
            '%3D' : 	'=',
        }

URL_EXAMPLES =[
'https://cafe.naver.com/',
'joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc'
]


def main():
    url = "".join(URL_EXAMPLES)
    url_ = get_replaced_url(replaces, url_copyed=url)
    print(url_)



    """
    #text.replace(",", "", -1); print(text) #안됨
    text = '123,456,789,999'

    #text = replaceRight(text, ",", "", 2)
    print("\n\n\nRESULT:")
    print(replaceRight(text, ",", "", 0))
    print(replaceRight(text, ",", "", 1))
    print(replaceRight(text, ",", "", 2))
    print(replaceRight(text, ",", "", 3))
    print(replaceRight(text, ",", "", 4))

    # 결과 :
    # 123,456,789,999
    # 123,456,789999
    # 123,456789999
    # 123456789999
    # 123456789999
    """

def get_replaced_url(dict_replace, url_copyed):
    for from_ , to_ in dict_replace.items():
        if from_ in url_copyed:
            count = url_copyed.count(from_)
            url_copyed.replace(from_, to_)
            print(f"*** {count} : '{from_}' = '{to_}' FOUND! & REPLACED ***")
    return url_copyed

def replaceRight(original, from_, to_, count_right):
    repeat = 0
    text = original
    old_len = len(from_)

    count_find = original.count(from_)
    # 바꿀 횟수가 문자열에 포함된 from_보다 많다면

    if count_right > count_find :
        # 문자열에 포함된 from_의 모든 개수(count_find)만큼 교체한다
        repeat = count_find
    else :
        # 아니라면 입력받은 개수(count)만큼 교체한다
        repeat = count_right

    while(repeat):
    # 오른쪽부터 index를 찾기위해 rfind 사용
        find_index = text.rfind(from_)
        text = text[:find_index] + to_ + text[find_index+old_len:]

        repeat -= 1
    return text

if __name__ == '__main__':
    main()
