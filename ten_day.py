import requests
import os


key = os.environ.get('WUNDERGROUND_KEY')

# zip_code = input("Please enter your zip code: ")
zip_code = 27615
response = requests.get('http://api.wunderground.com/api/{}/forecast10day/q/{}.json'.format(key, zip_code)).json()

data = []
for request in response['forecast']['txt_forecast']['forecastday']:
    data.append(request['title'] + ": " + request['fcttext'])

print(data)
