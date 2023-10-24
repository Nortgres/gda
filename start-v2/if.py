'''age = int(input('Введите возраст: '))
if age >= 18:
    print('Продажа алоголя разрешена.')
else:
    print('Продажа алкоголя запрещена.')


gender = input('Введите пол (М/Ж): ')
greeting = 'Привет сестренка!' if gender.upper() == 'Ж' else 'Привет братишка!'
print(greeting)


list1 = list(map(float, input('Введите два числа через пробел: ').split()))
if list1[0] > list1[1]:
    print(list1[0])
else:
    print(list1[1])


# Задание 5.2.
c = input('Введите слово: ').upper()
if c[::-1] == c:
    print('Palindrome')
else:
    print('Not a Palindrome')

# Задание 5.3.
list2 = list(map(int, input('Введите два числа через пробел: ').split()))
if list2[0] % list2[1] ==0:
    print(list2[0] // list2[1])
else:
    print(f'{list2[0]} на {list2[1]} нацело не делится')

# Задание 5.4.
a, b, c = map(int, input('Введите три числа через пробел: ').split())
if (a**2 + b**2) != c**2:
    print('No')
else:
    print('Yes')

# Задание 5.5.
num = int(input('Введите пятизначное число: ')[-1])
print('Yes') if num == 7 else print('No')

# Задание 5.6.
word = input('Введите слово: ').lower()
print('Yes') if 't' in word and 'h' in word and 'o' in word else print('No')

# Задание 5.7.
list3 = (input('Введите список городов через пробел: ')).split()
city = 'Москва'
if city in list3:
    list3.remove(city)
print(list3)

# Задание 5.8.
a, b, c, d = map(int, input('Введите четыре целых числа через пробел: ').split())
if a > c and b > d or a > d and b > c:
    print('Yes')
else:
    print('No')

# Задание 5.9.
num1 = list(map(int, input('Введите шестизначное число: ')))
if sum(num1[:3]) == sum(num1[3:]):
    print('Yes')
else:
    print('No')

# Задание 5.10.
time = float(input('Введите время в минутах: '))
x = time % 5
if x <= 3:
    print('green')
else:
    print('red')

# Задание 5.11.
num2 = int(input('Введите целое число: '))
if num2 == 1:
    print('1. Введение в Python')
elif num2 == 2:
    print('2. Строки и списки')
elif num2 == 3:
    print('3. Условные операторы')
elif num2 == 4:
    print('4. Циклы')
elif num2 == 5:
    print('5. Словари, кортежи и множества')
elif num2 == 6:
    print('6. Выход')

# Задание 5.12.
a, b, c = map(int, input('Введите три числа через пробел: ').split())
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)

# Задание 5.13.
mass = float(input('Введите вес: '))
if mass <= 60:
    print('1')
elif mass > 60 and mass <= 64:
    print('2')
elif mass > 64 and mass <= 69:
    print('3')
elif mass > 69:
    print('4')

# Задание 5.14.
day = int(input('Введите порядковый номер дня недели: '))
if day == 1:
    print('Понедельник')
elif day == 2:
    print('Вторник')
elif day == 3:
    print('Среда')
elif day == 4:
    print('Четверг')
elif day == 5:
    print('Пятница')
elif day == 6:
    print('Суббота')
elif day == 7:
    print('Воскресенье')

# Задание 5.15.
m = int(input('Введите порядковый номер месяца: '))
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print('31')
elif m == 4 or m == 6 or m == 9 or m == 11:
    print('30')
elif m == 2:
    print('28')

# Задание 5.16.
d, m = map(int, input('Введите число и порядковый номер месяца(через пробел): ').split())
m2 = m - 1
if d != 1 and d != 28 and d != 30 and d != 31:
    print(f'{d-1}.{m} {d+1}.{m}')
elif d == 1 and (m2 == 1 or m2 == 3 or m2 == 5 or m2 == 7 or m2 == 8 or m2 == 10 or m2 == 12):
    print(f'31.{m2} {d+1}.{m}')
elif d == 1 and (m2 == 4 or m2 == 6 or m2 == 9 or m2 == 11):
    print(f'30.{m2} {d+1}.{m}')
elif d == 1 and m2 == 2:
    print(f'28.{m2} {d+1}.{m}')
elif d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
    print(f'{d-1}.{m} 1.{m+1}')
elif d == 30 and (m == 4 or m == 6 or m == 9 or m == 11):
    print(f'{d-1}.{m} 1.{m+1}')
elif d == 28 and m == 2:
    print(f'{d-1}.{m} 1.{m+1}')

# Задание 5.17.
k = int(input('Введите число 1 <= k <= 365: '))
day = k%7
if day == 1:
    print('Понедельник')
elif day == 2:
    print('Вторник')
elif day == 3:
    print('Среда')
elif day == 4:
    print('Четверг')
elif day == 5:
    print('Пятница')
elif day == 6:
    print('Суббота')
elif day == 0:
    print('Воскресенье')

# Задание 5.18.
n1 = float(input('Введите первое число: '))
n2 = float(input('Введите второе число: '))
if n1 > n2:
    print(n1)
else:
    print(n2)

# Задание 5.19.
n3 = int(input('Введите первое число: '))
if n3%5 == 0:
    print(f'{n3} a multiple of 5')
else:
    print(f'{n3} not a multiple of 5')

# Задание 5.20.
keyword = input('Введите слово: ').lower()
if keyword == keyword[::-1]:
    print('Palindrome')
else:
    print('Not a Palindrome')
'''