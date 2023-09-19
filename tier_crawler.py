# My Little crawler for TIER

import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.tier.org.tw/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

news_content = soup.find_all('div', class_='news_content')

for list in news_content:
    print("訊息公告：" + list.text)
