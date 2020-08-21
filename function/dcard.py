import requests
from bs4 import BeautifulSoup
from linebot.models import *
import json
import copy

def create_dcard_hot_buttoms():
    template_base = json.loads('''
        {
            "type": "carousel",
            "contents": []
        }
    ''')

    raw_template_card = json.loads('''
        {
          "type": "bubble",
          "size": "kilo",
          "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "標題",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold"
              }
            ],
            "backgroundColor": "#27ACB2",
            "paddingTop": "19px",
            "paddingAll": "12px",
            "paddingBottom": "16px"
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "內文",
                    "color": "#222222",
                    "size": "xs",
                    "wrap": true
                  }
                ],
                "flex": 1
              }
            ],
            "spacing": "md",
            "paddingAll": "12px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://linecorp.com/"
            }
          },
          "styles": {
            "footer": {
              "separator": false
            }
          }
        }
    ''')
    
    url = 'https://www.dcard.tw/f'
    webContent = requests.get(url)
    webContent.encoding = 'UTF-8'

    soup = BeautifulSoup(webContent.text, 'html.parser')
    articleList = []
    index = 0

    for i in soup.select('article'):
        tempList = []
        try:
            if i.select('div div span')[4].text in ['??��??']:
                continue
            else:
                if i.select('div div span')[0].text == '':
                    article = i.select('div div span')[4].text + '....'
                else:
                    article = i.select('div div span')[3].text + '....'
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

    
    for ti,ar,ur in articleList:
        template_card = copy.deepcopy(raw_template_card)

        template_card['header']['contents'][0]['text'] = ti
        template_card['body']['contents'][0]['contents'][0]['text'] = ar
        template_card['body']['action']['uri'] = ur

        template_base['contents'].append(template_card)
    return template_base

# file = open('template.json', mode= 'w' ,encoding='utf-8')
# json.dump(create_dcard_hot_buttoms(), file, ensure_ascii=False)
