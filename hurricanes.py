import requests
import os


key = os.environ.get('WUNDERGROUND_KEY')

response = requests.get('http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(key)).json()


how_many = response["response"]

hurricane_list = response['currenthurricane']

for hurricane in hurricane_list:
    print("{} with a wind seed of {} {}".format(hurricane['stormName_Nice'], hurricane["WindSpeed"]["Mph"], hurricane["Movement"]["Text"]))
