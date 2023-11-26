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
''''''
Задание 8.7. Вводятся два списка целых чисел каждый с новой строки (в строке наборы
чисел через пробел). Необходимо выбрать и отобразить на экране уникальные числа,
присутствующие и в первом и во втором списках одновременно. Результат выведите на
экран в виде строки чисел, записанных по возрастанию через пробел, используя команду
(здесь s - это множество): print(*sorted(s))
Пример ввода:
8 11 12 15 -2
4 11 10 15 -5 1 -2
Пример вывода:
-2 11 15
''''''
num1 = set(map(int, (input('Введите список чисел 1: ').split())))
num2 = set(map(int, (input('Введите список чисел 2: ').split())))
s = num1 & num2
print(*sorted(s))
''''''
Задание 8.8. Вводятся два списка целых чисел каждый с новой строки (в строке наборы
чисел через пробел). Необходимо выбрать и отобразить на экране уникальные числа,
присутствующие в первом списке, но отсутствующие во втором. Результат выведите на
экран в виде строки чисел, записанных по возрастанию через пробел.
Пример ввода:
8 5 3 5 -3 1
1 2 3 4
Пример вывода:
-3 5 8
''''''
num1 = set(map(int, (input('Введите список чисел 1: ').split())))
num2 = set(map(int, (input('Введите список чисел 2: ').split())))
s = num1 - num2
print(*sorted(s))
''''''
Задание 8.9. Вводятся два списка целых чисел каждый с новой строки (в строке наборы
чисел через пробел). Необходимо выбрать и отобразить на экране уникальные числа,
присутствующие в первом или втором списках, но отсутствующие одновременно в обоих.
Результат выведите на экран в виде строки чисел, записанных по возрастанию через
пробел.
Пример ввода:
1 2 3 4 5
4 5 6 7 8
Пример вывода:
1 2 3 6 7 8
''''''
num1 = set(map(int, (input('Введите список чисел 1: ').split())))
num2 = set(map(int, (input('Введите список чисел 2: ').split())))
s = num1 ^ num2
print(*sorted(s))
'''
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
#x1.update(['corge', 'garply'])
#x1 |= x2
#print(x1)

# .intersection_update() (&=) сохраняет только элементы найденные как в первом, так и во втором и удаляет остальные элементы из исходного множества.
#x1 &= x2
#print(x1)
#x1..intersection_update([...])

# метод .difference_update() удаляет элементы, найденные во втором множестве. x1 -= x2
#x1.difference_update(['foo', 'bar'])

#метод .symmetric_difference_update обновляет исходное множество, удаляя элементы, присутсвующие сразу в обоих множетсвах, и сохраняя другие элементы.
#x1 ^= x2
#x1.symmetric_difference_update(['qux', 'corge'])
#print(x1)

#метод .add() добавляет элемент в множество
# x1.add('qux')

#метод .clear() удаляет все элементы множества.

#метод .remove() и .discard() удаляют указанный элемент из множества (второй не вызывает ошибки при отсутсвии значения).

#метод .pop() удаляет случайный элемент из множества и возращает этот элемент. Если множетсво пустое, то ошибка.

#метод .copy() создаёт копию множетсва.

#метод .isdisjoint() определяет, имеют ли два множетсва какие-либо общие элементы и возвращает True, если ни один из элементов не присутсвует
# в обоих множествах, в противном случае False

#метод .issubset() опредедляет, является ли одно множество подмножеством другого. ( <= ) Каждый элемент первого множества принадлежит второму.
#print(x1.issubset({'foo', 'bar', 'baz', 'quux'}))

# оператор < определяет, является ли одно множество правильным подмножеством другого.

# метод .issuperset() определяет, является ли одно множество надмножеством другого. (противоположность подмножества) ( >= )
#print(x1 >= x2)

'''
# задача 8.10
city1 = set(input('Введите города: ').split())
city2 = set(input('Введите города: ').split())
print('Yes' if city1 == city2 else 'No')print('Yes' if city1 == city2 else 'No')

#задача 8.11
num1 = set(map(int, (input('Введите список оценок: ').split())))
num2 = {2,}
if num1 & num2 == num2:
    print('Не допущен')
else:
    print('Допущен')

#задача 8.12
city1 = set(input('Введите города: ').split())
city2 = set(input('Введите города: ').split())
if city1.issubset(city2):
    print('Yes')
else:
    print('No')

#задача 8.13 вводится натуральное число, которое может быть получено простыми множителями из следующих: 2, 3, 5, 7, 11, 13. 
# Необходимо разложить введенное число на простые множители и проверить, содержит ли оно множители 2, 3 и 5 (все указанные множители)? 
# Если это так, вывести Yes, иначе - No.

natural_num = int(input('Enter natural number: '))
multipliers = {2, 3, 5, 7, 11, 13}
multi_s = {i for i in multipliers if natural_num % i == 0}
print('Yes' if multi_s.issuperset({2, 3, 5}) else 'No')

задача 8.14
num1 = set(map(int, (input('Введите числа: ').split())))
num2 = sorted(num1)
if len(num2) > 3:
    print(num2[-3])
else:
    print('No')

#задача 8.15
Вводится текст в одну строку, слова разделены пробелом. Необходимо найти
все уникальные слова и подсчитать частоту их появления в заданной строке. Для решения
задачи используйте множества и словари. Уникальные слова и количество каждого из них
вывести на экран по шаблону из примера.
Пример ввода:
Red Green Red Blue Red Red Green
Пример вывода:
{'Red': 4, 'Blue': 1, 'Green': 2}
'''

text1 = list((input('Введите текст: ')).split())
dict1 = dict.fromkeys(text1, 0)
for i in text1:
        dict1[i] = text1.count(i)
print(dict1)