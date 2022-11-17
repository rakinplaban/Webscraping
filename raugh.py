import requests
from bs4 import BeautifulSoup
url = 'https://www.facebook.com/'

headers = {
   
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",

}

r = requests.get(url,headers=headers)

with open('fb.html','wb') as f:
    f.write(r.content)

soup = BeautifulSoup(r.text,'lxml')
print(r.status_code)
print(soup.prettify())