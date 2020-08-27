import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.dcard.tw/f'
webContent = requests.get(url)
webContent.encoding = 'UTF-8'
soup = BeautifulSoup(webContent.text, 'html.parser')

for i in soup.select('article'):
    title = i.select('h2 a span')[0].text
    article = i.select('div div span')[4].text
    # if article == '回應':
    #     article = i.select('div div')[3].text

    if article == title:
        article = i.select('div div span')[5].text
    if article == '回應':
        article = i.select('div div')[4].text
    if article.isdigit() == True:
        article = i.select('div div span')[2].text
    print(article)
    print('-------------------')