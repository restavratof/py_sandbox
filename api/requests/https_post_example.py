import requests


URL = "https://YOUR URL HERE"

cert_path = 'CA CERT PATH'

data = {
    "param1" : 1,
    "param2" : 2
}

token = "JWT TOKEN PLACEHOLDER"

headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

r = requests.post(URL, params = data, headers=headers, verify=cert_path)


print(f'response    : {r}')
print(f'text        : {r.text}')
print(f'status_code : {r.status_code}')


