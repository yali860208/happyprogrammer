import requests
from linebot.models import *
import json
import copy

def create_pchome_buttoms(name):
    template_base = json.loads('''
        {
          "type": "carousel",
          "contents": []
        }
    ''')

    raw_template_card = json.loads('''
        {
          "type": "bubble",
          "size": "nano",
          "hero": {
            "type": "image",
            "size": "full",
            "aspectRatio": "20:20",
            "aspectMode": "cover",
            "url": "https://b.ecimg.tw/items/DAAL03A900AJYS5/000002_1590569497.jpg"
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "用STAUB鑄鐵鍋做熱甜點：舒芙蕾、蘋果派、熔岩蛋糕、法式土司…所有大師級點心，一只鍋子就能完成！",
                "wrap": true,
                "weight": "bold",
                "size": "md"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "$159",
                    "wrap": true,
                    "weight": "bold",
                    "size": "xl",
                    "flex": 0
                  }
                ]
              }
            ]
          },
          "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "go to PChome",
                  "uri": "https://linecorp.com"
                }
              }
            ]
          }
        }
    ''')


    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results'
    data = {
            'q':name,
            'page':'1',
            'sort':'sale/dc'
        }

    webContent = requests.get(url, params=data).json()

    for product in webContent['prods'][:10]:
        template_card = copy.deepcopy(raw_template_card)

        name = product['name']
        price = product['price']
        picture = 'https://b.ecimg.tw'+ product['picS']
        url_name = 'https://24h.pchome.com.tw/prod/' + product['Id']

        template_card['hero']['url'] = picture
        template_card['body']['contents'][0]['text'] = name
        template_card['body']['contents'][1]['contents'][0]['text'] = '$' + str(price)
        template_card['footer']['contents'][0]['action']['uri'] = url_name

        template_base['contents'].append(template_card)
    return template_base
# file = open('template.json', mode= 'w' ,encoding='utf-8')
# json.dump(create_pchome_buttoms('牙膏'), file, ensure_ascii=False)