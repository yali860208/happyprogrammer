import requests
from bs4 import BeautifulSoup
from linebot.models import *
import json
import copy
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials

def importworksheet():
    scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('HP2020-6545eb07aff6.json',scope)
    client = gspread.authorize(creds)
    spreadSheet = client.open('hp2020linebot')

    workSheet_status = spreadSheet.worksheet('status')
    workSheet_worldcupQ = spreadSheet.worksheet('worldcupQ')
    workSheet_worldcupA = spreadSheet.worksheet('worldcupA')
    return workSheet_status,workSheet_worldcupQ,workSheet_worldcupA


def create_worldcup_quick_replyButtons():
    theme_list = themeList()
    itemList = []
    for theme in themeList:
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

def themeList():
    workSheet_worldcupQ = importworksheet()[1]
    theme_list = []
    for i in workSheet_worldcupQ.col_values(1):
        if i != '':
            theme_list.append(i)
    return theme_list


def start_worldcup(user_worldcup, userSend, user_row):
    workSheet_status,workSheet_worldcupQ,workSheet_worldcupA = importworksheet()
    user_row = user_row
    worldQ_name = workSheet_worldcupQ.find(theme).row
    worldQ_url = workSheet_worldcupQ.find(theme).row + 1
    if user_worldcup == 'start':
        nameList = []
        for i in workSheet_worldcupQ.row_values(worldQ_name)[1:]:
            if i != '':
                nameList.append(i)
        workSheet_worldcupA.append_row(nameList,value_input_option=user_row)
        workSheet_status.update_cell(user_row,5,'round 1')
    else:
        nameList = []
        for i in workSheet_worldcupQ.row_values(worldQ_name)[1:]:
            if i != '':
                nameList.append(i)
    return nameList





    return nameList


def create_worldcup_bubble(nameA,nameB):
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
    for cell in [nameA,nameB]:
        template_card = copy.deepcopy(raw_template_card)
        name_col = workSheet_worldcupQ.find(cell).col
        url = workSheet_worldcupQ.cell(world_row,name_col).value

        template_card['body']['contents'][2]['contents'][0]['text'] = cell
        template_card['body']['contents'][0]['url'] = url
        template_card['action']['data'] = cell

        template_base['contents'].append(template_card)


    return template_base