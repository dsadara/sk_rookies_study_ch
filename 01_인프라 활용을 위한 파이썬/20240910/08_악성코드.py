import requests
from bs4 import BeautifulSoup

url = "https://www.malware-traffic-analysis.net/2024"
header_info = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=header_info)
soup = BeautifulSoup(r.text, 'lxml')

datas = soup.select("#main_content > div.blog_entry > ul > li > a.main_menu")

for data in datas:
    link_text = data.get_text()
    link_url = data.get('href')
    # if 문으로 http ,https 문 가리기
    print(f"{link_text} 링크: {url}{link_url}")