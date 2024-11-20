import requests
from bs4 import BeautifulSoup

base_url = "http://www.boannews.com"
base_url_https = "https://www.boannews.com"

header_info = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(base_url, headers=header_info)
soup = BeautifulSoup(r.text, 'lxml')

# link_url = soup.select("a[href]")

# print(len(link_url))

link_url2 = soup.select("[href]")

# print(len(link_url2))

# link_url3 = soup.select("link[href]")

# print(len(link_url3))
      
for tag in link_url2:
    url = tag.get('href')
    text = tag.get_text()
    print(f"[{text}] 링크:{base_url + url}")