from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

source = requests.get('https://webscraper.netlify.com/').text

soup = BeautifulSoup(source,'lxml')

print(soup)