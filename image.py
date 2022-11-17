import requests

url = 'https://scontent.fdac41-1.fna.fbcdn.net/v/t39.30808-6/315313264_2065860516945875_7018028041850009722_n.png?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeGeji5NCswWnKnRLylsUHIZW9om4f025kxb2ibh_TbmTOvtKs3lS24bfRCZKroiJjGR2AZSBsTwfFIQWPIdBWMV&_nc_ohc=x8AnJWuNbtwAX_wsoig&_nc_ht=scontent.fdac41-1.fna&oh=00_AfAKcL3t20w4Y5nk6NJAW2nFh0uAv8P3v-yUWQtiUYNNmg&oe=637A1B3B'

r= requests.get(url)

with open('img.png','wb') as f:
    f.write(r.content)