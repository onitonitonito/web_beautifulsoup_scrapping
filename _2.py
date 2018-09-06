from bs4 import BeautifulSoup

url = "http://www.naver.com/"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
rank = soup.find("div")


print(rank)

# for i in rank.find_all("a", value=True, id=False):
#     print(i)
    # print(i.get_text(" ", strip=True))
