import requests, os 
from bs4 import BeautifulSoup

base_url = "https://www.malware-traffic-analysis.net/2024"


header_info = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(base_url, headers=header_info)
soup = BeautifulSoup(r.text, 'lxml')

link_url = soup.find_all("a", "main_menu")

for tag in link_url:
    url = tag.get('href')
    text = tag.get_text()
    url = base_url + url
    print(f"{text}")
    print(f"{url}")
    print("-" * 80)