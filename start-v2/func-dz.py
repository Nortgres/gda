# Задание 9.1
'''
def f1():
    print('It`s my first function')
f1()
'''
# Задание 9.2
'''
def f2():
    name = input('Введите Имя и Фамилию: ')
    print(f'Уважаемый, {name}! Вы верно выполнили задание!')
f2()
'''
# Задание 9.3
'''
def f3(massa):
    print(f'Предмет имеет вес: {massa} кг.')
x = float(input('Введите вес: '))
f3(x)
'''
# Задание 9.4
'''
def f4(l1):
    a = min(l1)
    b = max(l1)
    c = sum(l1)
    print(f'Min = {a}, max = {b} sum = {c}')

l1 = list(map(int, (input('Введите числа: ').split())))
f4(l1)
'''
# Задание 9.5
'''
def f5(width, height):
    print(f'Периметр прямоугольника, равен', (width + height) * 2)


a, b = map(int, (input('Введите длины сторон: ').split()))
f5(a, b)
'''

# Задание 9.6
'''
def f6(email):
    text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_@.'
    l1 = []
    if '.' in email and '@' in email:
        for i in email:
            if i not in text:
                l1.append(1)
            else:
                l1.append(0)
        print('No' if sum(l1) > 0 else 'Yes')
    else:
        print('No')


email = input('Введите email: ')
f6(email)
'''
# Задание 9.7
'''
def f7(num):
    return print(num**2)
num = float(input('Введиете число: '))
f7(num)
'''
# Задание 9.8
'''
def triangle(num1):
    if num1[0] > num1[1] + num1[2]:
        return False
    elif num1[1] > num1[0] + num1[2]:
        return False
    elif num1[2] > num1[0] + num1[1]:
        return False
    else:
        return True


num1 = list(map(int, (input('Введите стороны треугольника: ')).split()))
print(triangle(num1))
'''
# Задание 9.9
'''
def check_text(a):
    if len(a) < 3:
        return False
    return True
print(check_text(input('Введите текст: ')))
'''
# Задание 9.10
'''
def reverse_text(t):
    return t[::-1]
print(reverse_text(input('Введите текст: ')))
'''
# Задание 9.11
'''
def num_sum(num1):
    s = 0
    for i in num1:
        s += i
    return s
num1 = list(map(int, (input('Введите числа: ')).split()))
print(num_sum(num1))
'''
# Задание 9.12
'''
def num_multiply(num1):
    s = 1
    for i in num1:
        s *= i
    return s
num1 = list(map(int, (input('Введите числа: ')).split()))
print(num_multiply(num1))
'''
# Задание 9.13
'''
def num_even():
    while True:
        n = int(input('Введите число: '))
        if n != 0:
            if n % 2 == 0:
                print(n)
        else:
            break
num_even()
'''


# Задание 9.14
'''
def num_odd(n):
    return n % 2 != 0

num1 = list(map(int, (input('Введите числа: ')).split()))
lst = [x for x in num1 if num_odd(x)]
print(*lst)
'''
# Задание 9.15
'''
def city_len(c):
    return len(c) >= 6

city = list((input('Введите города: ')).split())
lst = [x for x in city if city_len(x)]
print(*lst)
'''
# Задание 9.16
'''
def num1(a, b):
    return a*b

lst = list(map(int, (input('Введите числа: ')).split()))
print(num1(max(lst), min(lst)))
'''
# Задание 9.17
'''
def num_max(lst1):
    if num1(lst1[0], lst1[1]) and num1(lst1[0], lst1[2]):
        return lst1[0]
    if num1(lst1[1], lst1[0]) and num1(lst1[1], lst1[2]):
        return lst1[1]
    if num1(lst1[2], lst1[0]) and num1(lst1[2], lst1[0]):
        return lst1[2]
def num1(a, b):
    return a > b

lst1 = list(map(int, (input('Введите числа: ')).split()))
print(num_max(lst1))
'''
# Задание 9.18
'''
def num_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
num = int(input('Введите число: '))
print(num_prime(num))
'''
# Задание 9.19
'''
def num_unq(lst1):
    for i in range(len(lst1)):
        if lst1[i-1] == lst1[i]:
            i += 1
        else:
            lst2.append(lst1[i])
            i += 1


lst2 = []
lst1 = list(map(int, (input('Введите числа: ')).split()))
num_unq(lst1)
print(lst2)
'''
# Задание 9.20
text = input('Введите текст: ')
def text_sort(text):
    words = text.split('-')
    words.sort()
    return '-'.join(words)
print(text_sort(text))