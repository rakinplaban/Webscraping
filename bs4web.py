from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.coreyms.com').text

soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())

article = soup.find('article')

headline = article.h2.a.text
#print(headline)

# paragraph = soup.find('iframe',class_='entry-content')
# summary = paragraph.p.text
# print(summary)

vid_link = soup.find('iframe',class_='youtube_player')
print(vid_link)