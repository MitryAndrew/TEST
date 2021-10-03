import time
from typing import Dict
import datetime
import requests
from bs4 import BeautifulSoup
import json
import csv
from random import choice
from random import uniform
parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
number_of_pages = int(input('Input number pages - '))
number_selection = int(input('Введите с какой страницы начинаем - '))
item_key = [f'{i} страница' for i in range(number_selection, number_of_pages + 1)]
item_value = [f'https://www.avito.ru/astrahan/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSMUsoIpIpZmqwBmKwBlqwBlKwBiFmGWYRZglmAWQ&p={i}' for i in range(number_selection, number_of_pages + 1)]
item_dict = {x: y for x, y in zip(item_key, item_value)}

with open('href_AVITO_ru.json', 'w') as fp:
    json.dump(item_dict, fp)

with open('href_AVITO_ru.json', 'r') as fp:
    item_dict_json = json.load(fp)
# print(item_dict_json)

agent_list = open(r'C:\Python mini\venv\User_Agent_list_2.txt').read().split('\n')
proxy_list = open(r'C:\Python mini\venv\proxy_list2.txt').read().split('\n')
count = number_selection
for item_key, item_value in item_dict_json.items():
    proxy = {'http': 'http://' + choice(proxy_list)}
    agent = {'User-Agent': choice(agent_list)}
    # print(proxy, agent)
    print('Парсинг - ', count, 'страницы', item_value, 'proxy - ', proxy, 'user-agent - ', agent)
    time.sleep(uniform(6, 10))
    # print('# = ', count, ' keys - ', item_key, ' value -', item_value)
    req = requests.get(item_value, headers=agent, proxies=proxy)
    if req.status_code == 200:
        src = req.text
        with open(fr'C:\Python mini\venv\data_avito\{count}_{item_key}_AVITO_ru_{parsing_day}.html', 'w', encoding='utf-8') as file:
            file.write(src)
    else:
        print('Error', req.status_code)
    count += 1


