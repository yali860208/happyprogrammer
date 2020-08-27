import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.dcard.tw/f'
webContent = requests.get(url)
webContent.encoding = 'UTF-8'
soup = BeautifulSoup(webContent.text, 'html.parser')

for i in soup.select('article'):
    article = i.select('div div')[5].text
    title = i.select('h2 a span')[0].text
    if article == title:
        article = i.select('div div')[6].text
    print(article)
    print('------------------------')