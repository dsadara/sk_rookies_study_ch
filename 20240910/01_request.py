import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
print(response)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

title = soup.find('h1').text
paragraphs = soup.find_all('p')
print(title)