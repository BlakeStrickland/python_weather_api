import requests
import os


key = os.environ.get('WUNDERGROUND_KEY')

# zip_code = input("Please enter your zip code: ")
zip_code = 27615
response = requests.get('http://api.wunderground.com/api/{}/astronomy/q/{}.json'.format(key, zip_code)).json()

sun_rise = "Sunrise at {}: {} am".format(response['sun_phase']['sunrise']['hour'], response['sun_phase']['sunrise']['minute'])

sun_set = "Sunrise at {}: {} pm".format(response['sun_phase']['sunset']['hour'], response['sun_phase']['sunset']['minute'])
print(sun_rise)
print(sun_set)
