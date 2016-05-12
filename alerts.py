import requests
import os


key = os.environ.get('WUNDERGROUND_KEY')

# zip_code = input("Please enter your zip code: ")
zip_code = 27615
response = requests.get('http://api.wunderground.com/api/{}/alerts/q/{}.json
'.format(key, zip_code)).json()
