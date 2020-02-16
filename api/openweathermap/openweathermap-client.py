import requests
import json
import os

# API_KEY = os.environ['OPENWEATHERMAP_API_KEY'] or 'you-will-never-guess'

print(f"OS ENV: {os.environ}")

for k, v in os.environ.items():
    print(f'{k}={v}')

print(type(os.environ))


print(f"API_KEY: {API_KEY}")





# MSG = '*Hello* - This is a test message from Dima. Ignore that, please.'
# DATA = {"text":MSG}
#
# r = requests.post(url = WEBHOOK_URL, data=json.dumps(DATA))
#
#
#
# print('-'*50)
# # extracting response text
# pastebin_url = r.text
# print("The pastebin URL is:%s"%pastebin_url)

