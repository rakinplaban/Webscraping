from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

#print(soup)
articles = soup.find_all('div',class_='article')
for article in articles:

    heading = article.h2.text
    print(heading)

    summary = article.p.text
    print(summary)
