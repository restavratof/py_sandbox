import requests
import json
import os
import configparser


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
city_id = 627907

# Minski Rayon
city_id = 625140


URL = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={API_KEY}"

DATA = {
    "id":city_id,
    "APPID":API_KEY
}

# r = requests.post(url = URL, data=json.dumps(DATA))
r = requests.post(url = URL)



print('-'*50)
# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

