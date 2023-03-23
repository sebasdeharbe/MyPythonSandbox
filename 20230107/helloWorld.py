#Script para el valor del dolar blue
import json
from urllib.request import urlopen

print('Hello World!')

urlws = 'https://api.bluelytics.com.ar/v2/latest'

response = urlopen(urlws)

data_json = json.load(response)

print(data_json)
