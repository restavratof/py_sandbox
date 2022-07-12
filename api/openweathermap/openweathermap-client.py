import requests
import json
import configparser

location = 'Gomel'


config = configparser.ConfigParser()
config.sections()
config.read('env.properties')

API_KEY = config['DEFAULT']['API_KEY']

print(API_KEY)

# URL = 'api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111'

#    "id": 627907,
#     "name": "Homyel",
#     "country": "BY",
#     "coord": {
#       "lon": 30.975401,
#       "lat": 52.434502
#     }
# city_id = 627907

# Minski Rayon
city_id = 625140

# Download the JSON data from OpenWeatherMap.org's API.
URL = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={API_KEY}"


response = requests.get(URL)
response.raise_for_status()


print('-'*50)
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

print(weatherData)
print('-'*50)
# Print weather descriptions.
w = weatherData['list']
print('Current weather inbox %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

print('-'*50)
# print(json.dumps(weatherData, indent=4, sort_keys=True))
