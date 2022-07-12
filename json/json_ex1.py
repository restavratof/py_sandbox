import json

jsonVal = {'isCat': True, 'miceCaught': 0, "name": "Gerda"}
StrOfJsonData = json.dumps(jsonVal)
print(StrOfJsonData)
