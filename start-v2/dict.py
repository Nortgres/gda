'''
capitals = {
    'United Kingdom': 'London',
    'Canada': 'Ottawa',
    'Italy': 'Rome'
}
capitals2 = dict(
    (('United Kingdom','London'),
     ('Canada','Ottawa'),
     ('Italy','Rome'))
      )
capitals2['Japan'] = 'Tokyo'
print(capitals)
print(capitals2)
print(capitals2['United Kingdom'])
capitals2['Japan'] = 'Osaka'
print(capitals2)
'''
car1 = {
    'brabd': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car2 = {
    'brand': 'Ford',
    'elactric': False,
    'year': 1964,
    'color': ['red', 'blue']
}
#print(car1)
#print(car2)

myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}
#print(myfamily['child2']['name'])
capitals1 = {'United Kingdom': 'London','Canada': 'Ottawa'}
capitals2 = {'Italy': 'Rome','Japan': 'Tokyo'}
capitals3 = {'Egypt': 'Cairo'}
#capitals = capitals1 | capitals2

capitals = {**capitals1, **capitals2, **capitals3}
#print(capitals)

# Методы словарей
# capitals.clear()
capitals3 = {'United Kingdom': 'London','Canada': 'Ottawa'}
#capitals3.copy()
capitals4 = capitals3.copy()
capitals4['Egypt'] = 'Cairo'
#print(capitals3)
#print(capitals4)

res = ('food', 'wood', 'stone')
quantity = 0
#dict.fromkeys - возвращает словарь с указанными ключами и одинаковым для всех них значением
total = dict.fromkeys(res, quantity)
#print(total)

capitals5 = {'United Kingdom': 'London','Canada': 'Ottawa','Italy': 'Rome'}
#dict.setdefault - возвращает значение элемента со значением...
#print(capitals5.setdefault('Canada', 'Paris'))
#print(capitals5.setdefault('France', 'Paris'))
#print(capitals5)

#Метод get
capitals6 = {'United Kingdom': 'London','Canada': 'Ottawa','Italy': 'Rome'}
#if 'Canada' in capitals6:
#    print(f"{capitals6['Canada']} is the capital of Canada.")
#print(capitals6.get('Italy'))
#print(capitals6.get('Russia', 'Unknown'))

#Метод .items()
capitals7 = {'Italy': 'Rome','Japan': 'Tokyo'}
x = capitals7.items()
#print(x)
capitals7['France'] = 'Paris'
#print(x)
#print(list(x))
#print(list(x)[0])
#print(list(x)[0][1])

# Метод .keys() возвращает объект представления, содержащий ключи словаря в виде списка.
capitals8 = {'Italy': 'Rome','Japan': 'Tokyo'}
y = capitals8.keys()
#print(y)
capitals8['France'] = 'Paris'
#print(y)
#print(list(y))
#print(list(y)[0])

# Метод .values() возвращает объект представления, содержащий значения словаря в виде списка.
capitals9 = {'Italy': 'Rome','Japan': 'Tokyo'}
z = capitals9.values()
#print(z)
capitals9['France'] = 'Paris'
#print(z)
#print(list(z))
#print(list(z)[0])

# Метод .pop() удаляет и возвращает его значение
capitals10 = {'United Kingdom': 'London','Canada': 'Ottawa','Italy': 'Rome'}
#print(capitals10.pop('Italy'))
#print(capitals10)
#print(capitals10.pop('Russia', 'Unknow'))
#print(capitals10)

# удаление оператором del:
capitals11 = {'United Kingdom': 'London','Canada': 'Ottawa','Italy': 'Rome'}
#print(capitals11)
del capitals11['Canada']
#print(capitals11)

# метод .popitem() удаляет элемент, добавленный последним и возвращает его значение в виде кортежа.
capitals12 = {'United Kingdom': 'London','Canada': 'Ottawa','Italy': 'Rome'}
#print(capitals12.popitem())
#print(capitals12)

#метод .update() вставляет указанные элементы в словарь (если есть обновляет)
capitals13 = {'United Kingdom': 'London','Canada': 'Ottawa'}
capitals14 = {'Italy': 'Rome','Japan': 'Tokyo'}
capitals13.update(capitals14)
#print(capitals13)
capitals13.update([('France', 'Paris'), ('Egypt', 'Cairo')])
#print(capitals13)

capitals15 = {'United Kingdom': 'London','Canada': 'Ottawa','Italy': 'Rome'}
#for country in capitals15:
#    print(country)
#for country in capitals15.keys():
#    print(country)
#for country in capitals15:
#    print(capitals15[country])
#for capital in capitals15.values():
#    print(capital)
#for country, capital in capitals15.items():
#    print(country, '-', capital)

capitals16 = {'France':'Paris', 'Canada': 'Ottawa', 'Italy': 'Rome'}
#print(sorted(capitals16))
#print(sorted(capitals16.items()))

'''
#Задание 7.1
Вводится целое положительное число n. Создайте словарь, где ключи - это
числа от 1 до n (включая оба), а значения - это квадраты ключей. Выведите словарь на
экран.
Пример ввода:
12
Пример вывода:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
''' '''

n = int(input('Введите число: '))
dict1 = {i: i**2 for i in range(1, n+1)}
print(dict1)
''' '''
Задание 7.2. Вводятся данные в формате ключ=значение в одну строчку через пробел.
Значениями здесь являются целые числа (см. пример ниже). Необходимо на их основе
создать словарь d с помощью функции dict() и вывести его на экран командой:
print(*sorted(d.items()))
Пример ввода:
one=1 two=2 three=3
Пример вывода:
('one', 1) ('three', 3) ('two', 2)
''''''
text = input("Введите данные: ").split()
y = []
for i in text:
    y.append(i.split('='))
d = dict(y)
for key in d:
    d[key] = int(d[key])
print(*sorted(d.items()))
''''''
Задание 7.3. Вводятся данные в формате ключ=значение в одну строчку через пробел.
Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в
словарь d (без использования функции dict()) и вывести его на экран командой:
print(*sorted(d.items()))
Пример ввода:
5=отлично 4=хорошо 3=удовлетворительно
Пример вывода:
(3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
''''''
text = input("Введите данные: ").split()
y = []
d = {}
for i in text:
    y.append(i.split('='))
d.update(y)
print(*sorted(d.items()))
''''''
Задание 7.4. Вводятся данные в формате ключ=значение в одну строчку через пробел.
Необходимо на их основе создать словарь, затем проверить, существуют ли в нем ключи со
значениями: 'house', 'True' и '5' (все ключи - строки). Если все они существуют, то вывести на
экран Yes, иначе - No.
Пример ввода:
вологда=город house=дом True=1 5=отлично 9=божественно
Пример вывода:
Yes
''''''
text = input("Введите данные: ").split()
d = {i.split('=')[0]: i.split('=')[1] for i in text}
if 'house' in d.keys() or 'True' in d.keys() or 5 in d.keys():
    print('Yes')
else:
    print('No')
''''''
Задание 7.5. Вводятся номера телефонов в одну строчку через пробел с разными кодами
стран: +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6, +2
и т.п., а значения - список номеров (следующих в том же порядке, что и во входной строке) с
соответствующими кодами. Полученный словарь вывести командой:
print(*sorted(d.items()))
Пример ввода:
+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110
+71232267890
Пример вывода:
('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7',
['+71234567890', '+71234567854', '+71232267890'])
''''''
num1 = input("Введите номера телефонов: ").split()
d = {}
for phone in num1:
    code = phone[:2]
    if code in d:
        d[code].append(phone)
    else:
        d[code] = [phone]
print(d)
print(*sorted(d.items()))
''''''

Задание 7.6. Вводятся номера телефонов в формате (пока не встретится число 0):
номер_1 имя_1
номер_2 имя_2
...
номер_N имя_N
Необходимо создать словарь d, где ключами будут имена, а значениями - список номеров
телефонов для этого имени. Обратите внимание, что одному имени может принадлежать
несколько разных номеров. Полученный словарь вывести командой: print(*sorted(d.items()))
Пример ввода:
+71234567890 Сергей
+71234567810 Сергей
+51234567890 Михаил
+72134567890 Николай
0
Пример вывода:
('Михаил', ['+51234567890']) ('Николай', ['+72134567890']) ('Сергей', ['+71234567890',
'+71234567810'])
''''''
d = {}
while True:
    text = input('Введите телефон и имя, через пробел (для выхода введите 0): ')
    if text == '0':
        break
    else:
        phone, name = text.split()
        if name in d:
            d[name].append(phone)
        else:
            d[name] = [phone]
print(*sorted(d.items()))
''''''
Задание 7.7. Пользователь вводит в цикле целые положительные числа, пока не введет
число 0. Для каждого числа вычисляется квадратный корень (с точностью до сотых) и
значение выводится на экран (в столбик). С помощью словаря выполните кэширование
данных так, чтобы при повторном вводе того же самого числа результат не вычислялся, а
бралось ранее вычисленное значение из словаря. При этом на экране должно выводиться:
значение из кэша: <число>
''''''
d = {}
while True:
    num = int(input('Введите целые положительные числа (для выхода введите 0): '))
    if num == 0:
        break
    else:
        if num in d:
            print(f"значение из кеша: {d[num]}")
        else:
            #d.update({num: (round((num**0.5), 2))})
            d[num] = (round((num**0.5), 2))
            print(d[num])
'''