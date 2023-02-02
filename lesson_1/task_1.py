# 1. Посмотреть документацию к API GitHub, 
# разобраться как вывести список репозиториев 
# для конкретного пользователя, 
# сохранить JSON-вывод в файле *.json.

import json
import requests

url = 'https://api.github.com'
user='SvetlanaMaslennikova'

response = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as file:
    json.dump(response.json(), file)

for repo in response.json():
    print(repo['name'])
