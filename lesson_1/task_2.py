# Изучить список открытых API (https://www.programmableweb.com/category/all/apis). 
# Найти среди них любое, требующее авторизацию (любого типа). 
# Выполнить запросы к нему, пройдя авторизацию. 
# Ответ сервера записать в файл.

import json
import requests

params = {
    'latitude': '54.93262',    #55.80186
    'longitude': '37.38603', #49.260556
    'guery': 'манты'     #манты
}

url = 'https://api.delivery-club.ru/api1.2/vendors/search'

response = requests.get(url=url, params=params)

vendors = response.json()['vendors']

for vendor in vendors:
    print(vendor['name'])
