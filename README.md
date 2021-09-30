

## 1. 註冊 By老師

![](https://i.imgur.com/30TnHxH.png)

<br>

![](https://i.imgur.com/l3Z3zfo.png)

### 使用工具

1. [Line 模組](https://hackmd.io/@KJWang/BJd2CcPiI#LineBot%E4%B8%BB%E7%A8%8B%E5%BC%8F) (linebot.models)

```python=
# 選生日的神奇模組
message = TextSendMessage(
    text='請到手機上選擇日期~',
    quick_reply=QuickReply(
        items=[
            QuickReplyButton(
                action=
                    DatetimePickerAction(
                        label="請輸入生日~",
                        data="birthday",
                        mode="date",
                        initial="1990-01-01",
                        max="2002-12-31",
                        min="1930-01-01"
                )
            )
        ]
    )
)

```
2. [Google Sheet API](https://hackmd.io/@KJWang/r106nQdzP) (gspread)
3. [Email 套件](https://hackmd.io/@KJWang/Hy0LcWPAL)(email.message, smtplib)

### 成果展示
- Google Sheet
![](https://i.imgur.com/3Z2G91A.png)
- Line
![](https://i.imgur.com/NBb3TJ0.png)
- Email驗證碼
![](https://i.imgur.com/jjAlrU9.png)


<br><br><br>

## 2. 天氣、AQI、紫外線 By 老師
![](https://i.imgur.com/X9yp00K.png)

<br>

![](https://i.imgur.com/VVhPoXm.png)

### 使用工具

1. [OpenWeatherMap](https://openweathermap.org/)
[教學1](https://hackmd.io/@KJWang/S1QDB2DoU#%E5%8F%96%E5%BE%97API-key)[教學2](https://hackmd.io/@KJWang/B1BDHhvj8#%E9%96%B1%E8%AE%80API-doc)[教學3](https://hackmd.io/@KJWang/BkDvHhPsI#%E5%90%91OWM%E8%AB%8B%E6%B1%82%E8%B3%87%E8%A8%8A%EF%BC%81)

2. [政府資料開放平台](https://data.gov.tw/)
[輻射值](https://data.gov.tw/dataset/119233) [AQI](https://data.gov.tw/dataset/40448)

### 成果展示

![](https://i.imgur.com/icdMlww.png)

## 3. pchome 跟老師合作

![](https://i.imgur.com/KgRiV9u.pn)
![](https://i.imgur.com/Lfit7DX.png)


### 使用工具

1. [爬網頁](https://hackmd.io/@KJWang/S18FM2DiU#PChome%E7%B7%9A%E4%B8%8A%E8%B3%BC%E7%89%A9)
2. Line的[Flex Message](https://developers.line.biz/flex-simulator/?status=success)
3. [Google Sheet API](https://hackmd.io/@KJWang/r106nQdzP) (gspread)

### 成果展示

![](https://i.imgur.com/LqE5mjO.png)

## 4. Dcard

### 使用工具

1. 爬網頁
2. Line的[Flex Message](https://developers.line.biz/flex-simulator/?status=success)

### 自己做就會有困境

解決法 Proxy

1. Dcard對ngrok施了魔咒
- 我的json檔直接跑掉!!!
![](https://i.imgur.com/9PTu0rT.png)
![](https://i.imgur.com/xJ0MrQ1.pn)

2. Dcard對Heroku施了魔咒
- 文章跑掉

```python=
for i in soup.select('article'):
    article = i.select('div div')[5].text
    title = i.select('h2 a span')[0].text
    if article == title:
        article = i.select('div div')[6].text
    print(article)
    print('------------------------')
```
![](https://i.imgur.com/k1z9rqb.png)
![](https://i.imgur.com/2qA5P7x.png =50%x)

```python=
for i in soup.select('article'):
    title = i.select('h2 a span')[0].text
    article = i.select('div div span')[4].text
    if article == title:
        article = i.select('div div span')[5].text
    if article == '回應':
        article = i.select('div div span')[3].text
    if article.isdigit() == True:
        article = i.select('div div span')[2].text
    print(article)
    print('-------------------')
```

<br>

### 成果展示
![](https://i.imgur.com/LIRoYKb.png)

![](https://i.imgur.com/Zgccus2.png)


## 5. 二選一

### 使用工具
1. Google Sheet
2. Line的[Flex Message](https://developers.line.biz/flex-simulator/?status=success)
3. [Google Sheet API](https://gspread.readthedocs.io/en/latest/index.html) (gspread)



### 成果展示

![](https://i.imgur.com/b8G6wSV.png)
![](https://i.imgur.com/GRxV7NX.png)
![](https://i.imgur.com/ARbur7Z.png)



