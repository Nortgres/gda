# Задание 10.1
'''
Задание 10.1. Объявите функцию, которая вычисляет площадь прямоугольника по двум
параметрам: width и height - ширина и высота прямоугольника. И возвращает результат
(сама ничего на экран не выводит). Создайте декоратор для этой функции, который
отображает результат на экране в виде строки (без кавычек):
"Площадь прямоугольника: <значение>"
Пример ввода:
8 11
Пример вывода:
Площадь прямоугольника: 88
'''
'''

def show_area(func):
    def wrapper(*args, **kwargs):
        print(f"Площадь прямоугольника: {func(*args, **kwargs)}")
        return func(*args, **kwargs)

    return wrapper


@show_area
def rectangle_area(width, height):
    return width * height


a, b = map(int, (input("Введите стороны прямоугольника: ").split()))
rectangle_area(a, b)
'''

# Задание 10.2
'''
Задание 10.2. На вход программы поступает строка из целых чисел, записанных через
пробел. Напишите функцию, которая преобразовывает эту строку в список из целых чисел и
возвращает его. Создайте декоратор для этой функции, который сортирует список чисел по
возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
Вызовите декорированную функцию и отобразите полученный отсортированный список lst
командой: print(*lst)
Пример ввода:
8 11 -5 4 3 10
Пример вывода:
-5 3 4 8 10 11
'''

'''
def list_sorted(func):
    def wrapper(*args):
        l1 = func(*args)
        l1.sort()
        return l1

    return wrapper


@list_sorted
def list_num(n):
    return list(map(int, n.split()))


num = input("Введите числа через пробел: ")
lst = list_num(num)
print(*lst)
'''
# Задание 10.3
'''
Задание 10.3. Вводятся две строки из слов (слова записаны через пробел). Объявите
функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти
списки. Создайте декоратор для этой функции, который из двух списков формирует
словарь, в котором ключами являются слова из первого списка, а значениями -
соответствующие элементы из второго списка. Полученный словарь должен возвращаться
при вызове декоратора. Примените декоратор к первой функции и вызовите ее для
введенных строк. Результат (словарь d) отобразите на экране командой:
print(*sorted(d.items()))
Пример ввода:
house river tree car
дом река дерево машина
Пример вывода:
('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
'''
'''
str1 = input('Введите строку №1: ')
str2 = input('Введите строку №2: ')

def dict_decor(func):
    def wrapper(*args, **kwargs):
        d1 = {}
        lst1, lst2 = func(*args, **kwargs)
        for i, j in zip(lst1, lst2):
            d1[i] = j
        return d1

    return wrapper


@dict_decor
def str_lst(a, b):
    l1 = list(a.split())
    l2 = list(b.split())
    return l1, l2

d = str_lst(str1, str2)

print(*sorted(d.items()))
'''
# Задание 10.4
'''
Задание 10.4. Вводится строка текста. Объявите функцию, которая принимает введенную
строку в виде параметра, не делает с ней никаких преобразований и возвращает ее в
исходном виде (сама функция ничего на экран не выводит). Создайте три декоратора для
этой функции, которые оборачивают введенный текст в теги: <b>, <i> и <u> (каждый
декоратор оборачивает только в один тег). Примените декораторы к функции (получатся
вложенные декораторы) и вызовите ее для введенной строки.
Пример ввода:
Miracle Garden
Пример вывода:
<b><i><u>Miracle Garden</u></i></b>
'''
text1 = input("Введите текст: ")


def orig_text(text):
    return text


def dec_b(func):
    def wrapper(text):
        result = func(text)
        return f"<b>{result}</b>"

    return wrapper


def dec_i(func):
    def wrapper(text):
        result = func(text)
        return f"<i>{result}</i>"

    return wrapper


def dec_u(func):
    def wrapper(text):
        result = func(text)
        return f"<u>{result}</u>"

    return wrapper


@dec_b
@dec_i
@dec_u
def dec_text(text):
    return orig_text(text)


print(dec_text(text1))
