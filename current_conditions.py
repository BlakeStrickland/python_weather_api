import requests
import os


key = os.environ.get('WUNDERGROUND_KEY')

# zip_code = input("Please enter your zip code: ")
zip_code = 27615
response = requests.get('http://api.wunderground.com/api/{}/conditions/q/{}.json'.format(key, zip_code)).json()


location = response["current_observation"]["full"]
time_observed = response["observation_time_rfc822"]
weather = response["weather"]
temp = response["temp_f"]
gust = response["wind_gust_mph"]
feels_like = response["feelslike_f"]
