# Web scraping with flask and beautifulsoup

**required**
1. beautifulsoup4
2. requests
3. lxml
4. flask

### RESTful API
```pip install restful``` <br>
This code will install rest api in my application.

*Note* --**To fix a number of port I will do this**
```
if __name__ == '__main__':
    app.run(debug=True,port=8000)
```

### Get Api resources:
```
api = Api(app)

class Hello(Resource):
    def get(self):
        return webScrapper()

api.add_resource(Hello,'/')

```

