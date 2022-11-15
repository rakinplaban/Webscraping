from flask import Flask, render_template
from flask_restful import Api, Resource
from bs4 import BeautifulSoup
import requests

# source = requests.get('https://webscraper.netlify.com/').text

# soup = BeautifulSoup(source,'lxml')

# head = soup.find('main').select_one("article:nth-of-type(4)").div.text

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {'message' : "Hello World!"}

api.add_resource(Hello,'/')

if __name__ == '__main__':
    app.run(debug=True,port=8000)

