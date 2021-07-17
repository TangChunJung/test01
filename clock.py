from bs4 import BeautifulSoup

token = 6UwPzWyGqN1ucBbDeyNEdYqhnTD1PePXEjMqhLk0tSv
rs = requests.session()
res = rs.get('httpswww.dcard.twfsavemoneylatest=true')
soup = BeautifulSoup(res.text)

titles =soup.find_all(a,{classtgn9uw-3})

headers = {
        Authorization Bearer  + token,
        Content-Type applicationx-www-form-urlencoded
                }

params = {message 低卡文章更新}
r = requests.post(httpsnotify-api.line.meapinotify,
headers=headers, params=params)    
    
for x in titles
    if 情報 in x.string or 優惠 in x.string or 分享 in x.string 
        or 註冊 in x.string or 免費 in x.string or LinePoint in x.string
        params = {message httpswww.dcard.tw+x.get('href')}
        r = requests.post(httpsnotify-api.line.meapinotify,
        headers=headers, params=params)
               