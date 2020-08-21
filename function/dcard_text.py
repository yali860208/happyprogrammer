import requests
from bs4 import BeautifulSoup
from linebot.models import *
import json

url = 'https://www.dcard.tw/f'
webContent = requests.get(url)
webContent.encoding = 'UTF-8'

soup = BeautifulSoup(webContent.text, 'html.parser')
articleList = []
index = 1

for i in soup.select('article'):
    tempList = []
    try:
        if i.select('div div span')[4].text in ['回應']:
            continue
        else:
            if i.select('div div span')[0].text == '':
                article = i.select('div div span')[4].text + '...'
            else:
                article = i.select('div div span')[3].text + '...'
            title = i.select('h2 a span')[0].text
            for j in i.select('h2 a'):
                url = 'https://www.dcard.tw' + j['href']
            tempList.append(title)
            tempList.append(article)
            tempList.append(url)
            index += 1
            articleList.append(tempList)
        if index > 10:
            break

    except:
        continue

for i,j,k in articleList:
    print(i)
    print(j)
    print(k)
    print('---------------')