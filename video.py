import sys
import os
import requests
import wget

folder = os.path.join("C:/Users/Rakin Shahriar/Downloads")
url = 'https://www.facebook.com/watch?v=487977326624719'
r = requests.get(url)

wget.download(url,folder)
print("Download Completed!")

