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
                "text": "我拿哀鳳很了不起⋯？",
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
                    "text": "前段日子發生了一件扯爆的事 比扯鈴還扯（這梗好老 印象深刻 決定發上來跟你各位分享  事情是這樣ㄉ 前陣子的時候我為了準備考試 幾乎每天都去圖書館自修室唸書 那天有兩個看樣子感覺應該是國中年紀的女生拿著書包坐到我旁邊的位置 然後也不辦正經事 在那邊嘰哩呱啦講話 用的是我戴著耳機還聽得到的音量欸 拜託哦我的小姐 要聊不會出去聊完再進來 白目哦 到圖書館不唸書聊天是要待著吸取日月精華膩？",
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

    template_card = copy.deepcopy(raw_template_card)
    for ti,ar,ur in articleList:
        template_card['header']['contents'][0]['text'] = ti
        template_card['body']['contents'][0]['contents'][0]['text'] = ar
        template_card['body']['action']['uri'] = ur
        template_base['contents'].append(template_card)
    return template_base

# file = open('template.json', mode= 'w' ,encoding='utf-8')
# json.dump(create_dcard_hot_buttoms(), file, ensure_ascii=False)