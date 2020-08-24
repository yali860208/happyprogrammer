import requests
from bs4 import BeautifulSoup
from linebot.models import *
import json
import copy
import time

def dcard_ban_list():
    url = 'https://www.dcard.tw/forum/popular'
    webContent = requests.get(url)
    webContent.encoding = 'UTF-8'
    soup = BeautifulSoup(webContent.text, 'html.parser')
    
    urlList = []
    banList = []
    urlList.append('https://www.dcard.tw/f')
    banList.append('熱門')

    for i in soup.select('a')[6:14]:
        urlList.append('https://www.dcard.tw'+i['href'])
        banList.append(i.select('div div')[0].text)
    return banList, urlList


def create_dcard_quick_replyButtons():
    banList, urlList = dcard_ban_list()
    itemList = []
    for ban in banList:
        itemList.append(
            QuickReplyButton(
                action=PostbackAction(
                    label=ban,
                    data=ban
                    )
                )
            )

    message = TextSendMessage(
    text='選擇Dcard熱門看板',
    quick_reply=QuickReply(
        items=itemList
        )
    )
    return message

def create_dcard_hot_buttoms(ban):
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
                "color": "#222222",
                "size": "lg",
                "weight": "bold"
              }
            ],
            "backgroundColor": "#D3A4FF",
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
    banList, urlList = dcard_ban_list()
    ban_index = banList.index(ban)
    url = urlList[ban_index]
    webContent = requests.get(url)
    webContent.encoding = 'UTF-8'

    soup = BeautifulSoup(webContent.text, 'html.parser')
    articleList = []
    index = 0

    for i in soup.select('article'):
        tempList = []
        article = i.select('div div')[5].text
        if article == '置頂':
            continue
        else:
            pass
        if article.isdigit() == False:
            pass
        else:
            article = i.select('div div')[4].text
        title = i.select('h2 a span')[0].text
        for j in i.select('h2 a'):
            url = 'https://www.dcard.tw' + j['href']
        time.sleep(0.5)
        tempList.append(title)
        tempList.append(article)
        tempList.append(url)
        index += 1
        articleList.append(tempList)
        
        if index > 9:
            break

    
    for ti,ar,ur in articleList:
        template_card = copy.deepcopy(raw_template_card)
        print(ti)
        print(ar)
        print(ur)

        template_card['header']['contents'][0]['text'] = ti
        template_card['body']['contents'][0]['contents'][0]['text'] = ar
        template_card['body']['action']['uri'] =ur 

        template_base['contents'].append(template_card)
        time.sleep(0.5)
    return template_base

# print(create_dcard_hot_buttoms('心情'))

# file = open('template.json', mode= 'w' ,encoding='utf-8')
# json.dump(create_dcard_hot_buttoms('YouTuber'), file, ensure_ascii=False)
