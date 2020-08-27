import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.dcard.tw/f'
webContent = requests.get(url)
webContent.encoding = 'UTF-8'
soup = BeautifulSoup(webContent.text, 'html.parser')

for i in soup.select('article'):
    article = i.select('div div span')[4].text
    title = i.select('h2 a span')[0].text

    for article = title or '回應':
        article = i.select('div div span')[3].text
    print(article)