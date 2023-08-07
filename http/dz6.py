'''
Напишите функцию is_exists, которая делает запрос к сайту (на ваш выбор) и проверяет существует ли та или иная
страница (ознакомьтесь со статус кодами в доп. материалах). И соответственно возвращает  True или False
'''
# Например: https://github.com/

import requests


def is_exists():
    if requests.get(input('Введиите URL: ')).status_code == 200:
        print('True')
    else:
        print('False')


try:
    is_exists()
except:
    print('False')
