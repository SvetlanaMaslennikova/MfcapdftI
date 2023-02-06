# Написать приложение или функцию, которые собирают основные новости с сайта lenta.ru.
# Для парсинга использовать XPath.
# Структура данных в виде словаря должна содержать:
# - наименование новости;
# - ссылку на новость;
# - дату публикации.

from lxml import html
import requests

url = 'https://lenta.ru/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

response = requests.get(url, headers=headers)

dom = html.fromstring(response.text)
items = dom.xpath('//div[@class="topnews"]/div[2]/a')

items_dict = {}
for item in items:
    item_name = item.xpath('./div/span/text()')[0]
    item_link = url + item.xpath('./@href')[0]
    item_time = item.xpath('./div/div/time/text()')[0]
    
    items_dict[item_name] = {
        'link': item_link,
        'time': item_time,
    }

print(items_dict)
