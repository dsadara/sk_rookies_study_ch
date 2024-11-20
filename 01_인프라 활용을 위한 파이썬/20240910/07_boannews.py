import requests
from bs4 import BeautifulSoup

url = "http://www.boannews.com"
header_info = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=header_info)
soup = BeautifulSoup(r.text, 'lxml')

for link in soup.find_all('a'):
    link_text = link.get_text()
    link_url = link.get('href')
    # if 문으로 http ,https 문 가리기
    print(f"{link_text} 링크: {url}{link_url}")


# for el in result:
#     combi_url = ""
#     if 'http' not in el.get('href'):
#     if '@' in el.get('href'):
#     combi_url = el.get('href')
#     else:
#     combi_url = url+el.get('href')
#     else:
#     combi_url = el.get('href')