import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# 특정 p 태그
# print(soup.select("body > div > p:nth-child(2)"))

# 모든 p 태그
print(soup.select("body > div > p"))