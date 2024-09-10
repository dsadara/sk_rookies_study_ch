from bs4 import BeautifulSoup

# 간단한 HTML 문서
# 도르마우스 스토리(이상한나라 엘리스 캐릭터 중 하나)
html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
    <div data-role="page" data-last-modified="2022-01-01" data-foo="value">This is a div with data attributes.</div>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2" data-info="more info">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3" data-info="even more info">Tillie abcd</a>
    ; and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
</html>
"""

# HTML 문서를 Beautiful Soup 객체로 변환
# html.parser 파서 사용
soup = BeautifulSoup(html_doc, 'html.parser')


# 문서를 보기 좋게 출력
# print(soup.prettify())

# print(soup.title.parent.name)
# print(soup.p['class'])
# print(soup.find_all('a'))
# print(soup.find(id="link3"))

# # a 태크 리스트에서 url 가져오기

# for link in soup.find_all('a'):
#     link_href = print(link.get('href'))

# soup 에 있는 텍스트 데이터 가져오기 태그없이
# print(soup.get_text())


# soup.select("p.sister")  # 'sister' 클래스를 가진 모든 <p> 태그 선택
# soup.select("#first")    # ID가 'first'인 요소 선택
soup.select("a[href]")   # 'href' 속성을 가진 모든 <a> 태그 선택