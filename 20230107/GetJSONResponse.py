#Script donde uso request para consumo de webservices
import json
from urllib.request import urlopen
import requests

urlws = 'https://api.bluelytics.com.ar/v2/latest'
response = urlopen(urlws)
data_json = json.load(response)
value = json['blue']['value_sell']
print(value)
print(data_json)


#según chatgpt
url = "https://api.bluelytics.com.ar/v2/latest"
response = requests.get(url)
data = response.json()
value_avg = data['blue']['value_avg']
print(value_avg)

