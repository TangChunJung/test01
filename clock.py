from bs4 import BeautifulSoup

token="6UwPzWyGqN1ucBbDeyNEdYqhnTD1PePXEjMqhLk0tSv"
rs = requests.session()
res = rs.get('https://www.dcard.tw/f/savemoney?latest=true')
print(res.text)