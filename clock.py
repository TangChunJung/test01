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

params = {message �C�d�峹��s}
r = requests.post(httpsnotify-api.line.meapinotify,
headers=headers, params=params)    
    
for x in titles
    if ���� in x.string or �u�f in x.string or ���� in x.string 
        or ���U in x.string or �K�O in x.string or LinePoint in x.string
        params = {message httpswww.dcard.tw+x.get('href')}
        r = requests.post(httpsnotify-api.line.meapinotify,
        headers=headers, params=params)
               