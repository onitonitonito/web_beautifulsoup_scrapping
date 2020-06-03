"""
# wang-xxxx 로그인 - http://bit.ly/2O4kkR4
# Python korea - selenium 이 아닌(리소스 크다), requests 로 로그인
"""
# javascript 처리나 세션얻는 문제에 selenium을 많이 사용하시는 걸로 알고 있습니다.
# 그런데 selenium = 무겁고 느리고 리소스 많이 먹고 한번에 여러개 띄우기 어렵습니다.
# 대부분의 경우 requests 만으로도 javascript 가 하는일을 할수 있고
# 속도고 빠르게, 리소스도 적게 먹는 웹 자동화를 requests 만으로 구현이 가능합니다.

import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print(__doc__)


ID = 'yout id'
PASS = 'your pass'
MemberNo = "member no found from Fiddler"

ss = requests.session()
localtime = time.localtime()

login_hdr= '''Host: joagift.com
Connection: keep-alive
Cache-Control: max-age=0
Origin: http://wang-gift.com
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: nested-navigate
Referer: http://wang-gift.com/new/member/login.php
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'''

redir_hdr = '''Host: wang-gift.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
'''

data = 'nowdomain=wang-gift.com&preurl=http://wang-gift.com/new/member/join_result.php' + \
    f'?md=view&member_no={MemberNo}&join_url=wang-gift.com&join_ymd={localtime[0]}|{localtime[1]}|{localtime[2]}' + \
    f'&id={ID}&x=41&y=29&passwd={PASS}'

veri_hdr =  '''Host: wang-gift.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: http://wang-gift.com/new/member/loginok.php?hash=5508f78d3c254420c432bfdb7a821c11&returnStr=anVuZTk3MTM%3D&GAGALOGIN=&preurl=http://wang-gift.com/new/member/join_result.php?md=view&member_no=11255527&join_url=wang-gift.com&join_ymd=2019|11|19
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
'''

def main():
    print("your Id : " , ID)
    print("your pass : " , PASS)
    print("your memeber no : " , MemberNo)
    print("************* Now login process is starting***************\n\n")
    print("post datas for login to https://joagift.com/new/member/loginok.php\n")

    r = ss.post(
        url='https://joagift.com/new/member/loginok.php',
        headers=mkhdr(login_hdr),
        verify=False,
        data=data
        )

    if r.status_code == 200:
        print("first login process is successed")

    tmp = "top.location.href = '"
    cnt = r.text.find(tmp)
    cnt2 = r.text.find('//-->' , cnt)
    redirect = r.text[cnt + len(tmp) : cnt2].strip()[:-1]

    r2 = ss.get(
        url=redirect,
        verify=False,
        headers=mkhdr(redir_hdr),
        )

    print(f"redirect Address : {redirect}")


    r3= ss.get(
        url='http://wang-gift.com/new/member/join_result.php?md=view',
        verify=False,
        headers=mkhdr(veri_hdr)
        )

    # will print True
    print("\n\nIs your id in response text? : " , ID in r3.text)
    print("Finally your login process is succesd")


def mkhdr(hds):
    """스트링hds를 받아서 Dict로 반환"""
    x = {}
    for hd in hds.strip().split("\n"):
        tmp = hd.split(":")
        key = tmp[0].strip()
        data = ":".join( hd.split(":")[1:]).strip()
        x[ key ] = data
    return x


if __name__ == '__main__':
    main()

"""
    # 결과 확인하기
    from assets import script_run
    from pyprnt import prnt

    prnt("\nlogin_hdr")
    prnt(mkhdr(hds=login_hdr))

    prnt("\nredir_hdr")
    prnt(mkhdr(hds=redir_hdr))

    prnt("\nveri_hdr")
    prnt(mkhdr(hds=veri_hdr))

    [print(f"{key} : {value}")
            for key, value in globals().items()
            if not key.startswith('_')
            ]

    prnt(globals())
"""
