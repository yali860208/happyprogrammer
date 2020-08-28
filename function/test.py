import requests
from bs4 import BeautifulSoup
import json
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('HP2020-6545eb07aff6.json',scope)
client = gspread.authorize(creds)
spreadSheet = client.open('hp2020linebot')

workSheet_status = spreadSheet.worksheet('status')
workSheet_worldcupQ = spreadSheet.worksheet('worldcupQ')
workSheet_worldcupA = spreadSheet.worksheet('worldcupA')

nameList = [1,2,3,4,5]
workSheet_worldcupA.delete_row(1)
workSheet_worldcupA.insert_row(nameList,index=5)
nameList = workSheet_worldcupA.row_values(userSend)


# url = 'https://www.dcard.tw/f'
# webContent = requests.get(url)
# webContent.encoding = 'UTF-8'
# soup = BeautifulSoup(webContent.text, 'html.parser')

# for i in soup.select('article'):
#     title = i.select('h2 a span')[0].text
#     article = i.select('div div span')[4].text
#     # if article == '回應':
#     #     article = i.select('div div')[3].text

#     if article == title:
#         article = i.select('div div span')[5].text
#     if article == '回應':
#         article = i.select('div div span')[3].text
#     if article.isdigit() == True:
#         article = i.select('div div span')[2].text
#     print(article)
#     print('-------------------')