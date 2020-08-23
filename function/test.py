import requests
from bs4 import BeautifulSoup
from linebot.models import *
import json
import copy
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials

url = 'https://www.dcard.tw/f'
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
    print(article)
    print('-----------------')

# scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('My First Project-e46ee2dd4299.json',scope)
# client = gspread.authorize(creds)
# spreadSheet = client.open('hp2020linebot')

# workSheet_status = spreadSheet.worksheet('status')
# workSheet_worldcup = spreadSheet.worksheet('worldcup')
# for i in workSheet_worldcup.col_values(1):
#     print(i)
    # for j in i:
        # for k in j:
            # print(k)
    # user_row = get_user_info_from_gsheet(event)[0]
    # user_row = 1
    # status_col = 5
    # world_col = 2
    # world_row = workSheet_worldcup.find(theme).row+1
    # nameList = []
    # while world_col <= 9:
    #     name = workSheet_worldcup.cell(1,world_col).value
    #     nameList.append(name)
    #     workSheet_status.update_cell(user_row,status_col,name)
    #     status_col += 1
    #     world_col += 1
    # random.shuffle(nameList)
    # i = 0
    # pickone_nameList = []
    # while i <= 6:
    #     for cell in nameList[i:i+2]:
    #         template_card = copy.deepcopy(raw_template_card)
    #         name_col = workSheet_worldcup.find(cell).col
    #         url = workSheet_worldcup.cell(2,name_col).value

    #         template_card['body']['contents'][2]['contents'][0]['text'] = cell
    #         template_card['body']['contents'][0]['url'] = url
    #         template_card['action']['data'] = pickone_nameList.append(cell)

    #         template_base['contents'].append(template_card)
    #     i += 2
    # pickone = ''
    # for pickone_name in pickone_nameList:
    #     pickone += pickone_name

    # return pickone