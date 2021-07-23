import requests

url = "http://echo.jsontest.com/key/value/one/two"

def api_call():
    response = requests.get(url)
    print(response.json())

api_call()
