import requests
from bs4 import BeautifulSoup

url = "http://www.boannews.com/media/t_list.asp"

header_info = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=header_info)
soup = BeautifulSoup(r.text, 'lxml')
tags = soup.select("#main_HitNews > ul > li > a")

print(tags)

