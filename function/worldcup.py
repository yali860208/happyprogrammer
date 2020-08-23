import requests
from bs4 import BeautifulSoup
from linebot.models import *
import json
import copy
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def create_worldcup_quick_replyButtons():
    itemList = []
    for theme in ['團體','女生']:
        itemList.append(
            QuickReplyButton(
                action=PostbackAction(
                    label=theme,
                    data=theme
                    )
                )
            )
    message = TextSendMessage(
    text='選擇主題',
    quick_reply=QuickReply(
        items=itemList
        )
    )
    return message

def create_worldcup_bubble(theme, user_row):
    template_base = json.loads('''
      {
        "type": "carousel",
        "contents": []
      }
    ''')
    raw_template_card = json.loads('''
        {
          "type": "bubble",
          "size": "micro",
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.imgur.com/NOOXNlF.png",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "1:1",
                "gravity": "center"
              },
              {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                "position": "absolute",
                "aspectMode": "fit",
                "aspectRatio": "2:1",
                "offsetTop": "80px",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "size": "5xl"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "SHINee",
                    "size": "sm",
                    "color": "#ffffff",
                    "offsetTop": "15px",
                    "align": "center"
                  }
                ],
                "position": "absolute",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "paddingAll": "20px"
              }
            ],
            "paddingAll": "0px"
          },
          "action": {
            "type": "postback",
            "label": "action",
            "data": "hello"
          }
        }
    ''')

    scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('My First Project-e46ee2dd4299.json',scope)
    client = gspread.authorize(creds)
    spreadSheet = client.open('hp2020linebot')

    workSheet_status = spreadSheet.worksheet('status')
    workSheet_worldcup = spreadSheet.worksheet('worldcup')
    user_row = user_row
    status_col = 5
    world_col = 2
    world_row = workSheet_worldcup.find(theme).row+1
    nameList = []
    while world_col <= 9:
        name = workSheet_worldcup.cell(1,world_col).value
        nameList.append(name)
        workSheet_status.update_cell(user_row,status_col,name)
        status_col += 1
        world_col += 1
    random.shuffle(nameList)
    i = 0
    pickone_nameList = []
    while i <= 6:
        for cell in nameList[i:i+2]:
            template_card = copy.deepcopy(raw_template_card)
            name_col = workSheet_worldcup.find(cell).col
            url = workSheet_worldcup.cell(world_row,name_col).value

            template_card['body']['contents'][2]['contents'][0]['text'] = cell
            template_card['body']['contents'][0]['url'] = url
            template_card['action']['data'] = pickone_nameList.append(cell)

            template_base['contents'].append(template_card)
        i += 2
    pickone = ''
    for pickone_name in pickone_nameList:
        pickone += pickone_name

    return template_base, pickone
