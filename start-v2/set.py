x = {5, 10, 15, 20, (2, 3, 5, 7, 11)}
#print(x)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#print(set1)
#print(set2)
#print(set3)
set5 = {"abc", 34, True, 40.5, "male"}
#print(set5)
cities = ['Dubai', 'Milan', 'Miami', 'Paris', 'Tolyo']
cities_set = set(cities)
#print(cities_set)

x = set() # только так можно создать пустое множество.

#print(len({1, 2, 3, 4, 4, 5}))

thisset = {"apple", "banana", "cherry"}
#for x in thisset:
#    print(x)

#print('banana' in thisset)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
#print(x1 | x2)

#print(x1.union(x2))
set_x = x1.union(('baz', 'qux', 'quux'))
#print(set_x)

### a.union(b, c, d)
# метод .intersection() возвращает только пересекающиеся одинаковые элементы (или &)
set_x2 = x1.intersection(x2)
#print(set_x2)
set_x3 = x1 & x2
#print(set_x3)

# метод .difference() возвращает множество, содержащее только элементы в первом множетсве, но не во втором. (или - )

#print(x1.difference(x2))
#print(x2 - x1) # любые элементы x2 удаляются или вычитаются из x1

a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
#print(a.difference(b, c))
# или a - b - c

# метод symmetric_difference() возвращает элементы либо в первом либо во втором (или ^)

#print(x1.symmetric_difference(x2))
#print(x1^x2)

'''
#задача 8.1
s = set(map(float, input('Введите строку из вещественных чисел через пробел: ').split()))
print(*sorted(s))

#задача 8.2
text = set(input('Введите текст: ').lower().split())
print(len(text))

#задача 8.3
s = set(input('Введите текст: '))
num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
rez = num & s
x = list(map(int, rez))
if x == '':
    print('No')
else:
    print(*x)
print(s)

### string = input('Enter string: ')
### s = set([int(i) for i in string if i.isdigit()])
### print(*sorted(s)) if sorted(s) else print('No')

#задача 8.4
list1 = []
while True:
    name = input('Введите имя гостя: ')
    if name == '0':
        x = set(list1)
        print(len(x))
        break
    else:
        list1.append(name)

#задача 8.5
dict1 = {}
while True:
    text = input('Введите комментарий (для выхода введите 0): ')
    if text == '0':
        break
    else:
        name, text = text.split(':')
        dict1 = dict1.update([(name, text)])
        print(dict1)
        
while True:
    comments = input('Enter name guest: ')
    if comments == '0':
        break
    s = len(set([i.split(':')[0] for i in comments]))
print(s)

#задача 8.6

city1 = set()
while True:
    city = (input('Введите город: '))
    if city == "0":
        break
    city1.add(city)
print(len(city1))

cities = set()
while True:
    city = (input('Введите город: '))
    if city == "0":
        break
    cities = cities & set(city)
print(len(cities))
'''