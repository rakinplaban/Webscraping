import requests
from bs4 import BeautifulSoup

def webScrapper():
    res = requests.get('https://www.worldometers.info/coronavirus/')
    if res.status_code != 200:
        return {"message":"Failed to connect the server"}

    soup = BeautifulSoup(res.text,'lxml')
    table = soup.table
    headings = table.thead.tr.find_all('th')
    data = []
    text = [i.text for i in headings]
    data.append(text)
    table_rows = table.find_all('tr')
    for row in table_rows:
        td = row.find_all('td')
        check = False
        for j in td:
            if j.text == 'World' or  j.text == "China":
                check = True
        if check:
            item = [i.text for i in td]
            data.append(item)

    res = {'data':[]}
    for i in range(1,3):
        temp = {}
        for j in range(len(data[i])):
            if data[i][j] == "":
                data[i][j] = "0"
            temp[data[0][j]] = data[i][j]
        res["data"].append(temp)
    return res