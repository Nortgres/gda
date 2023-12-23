'''
Задание 1.1. Объявите класс с именем DataBase, который бы хранил в себе следующую
информацию:
pk: 1
title: "Классы и объекты"
author: "Том Круз"
views: 153
comments: 15
Имена переменных (атрибутов класса) используйте такие же (pk, title, author, views и
comments) с соответствующими значениями.
'''
'''

class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Том Круз"
    views = 153
    comments = 15

'''
# print(DataBase.__dict__)
'''
Задание 1.2. Объявите класс с именем Goods и пропишите в нем следующие атрибуты
(переменные):
title: "Мороженое"
weight: 154
tp: "Еда"
price: 1024
Затем, после объявления класса, измените его атрибут price на значение 2048 и добавьте
еще один атрибут:
inflation: 100
'''
'''

class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100
#print(Goods.__dict__)
'''
'''
Задание 1.3. Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в
этот класс атрибуты:
model: "Тойота"
color: "Белый"
number: "Е777КХ37"
Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
'''
'''
class Car:
    pass


setattr(Car, "model", "Тойота")
setattr(Car, "color", "Белый")
setattr(Car, "number", "Е777КХ37")
print(Car.__dict__["color"])
'''
'''
Задание 1.4. Объявите класс с именем Notes и определите в нем следующие атрибуты:
uid: 100837
title: "Ave Maria"
author: "И.С. Бах"
pages: 5
Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута
author.
'''
'''

class Notes:
    uid = 100837
    title = "Ave Maria"
    author = "И.С. Бах"
    pages = 5


print(getattr(Notes, "author"))
'''
'''
Задание 1.5. Объявите класс с именем Dictionary и определите в нем следующие атрибуты:
rus: "Питон"
eng: "Python"
Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута
rus_word. Если такого атрибута в классе нет, то функция getattr() должна возвращать булево
значение False.
Пример ввода:
Пример вывода:
False
'''
'''
class Dictionary:
    rus = "Питон"
    eng = "Python"    
print(getattr(Dictionary, "rus_word", False))
'''
'''
Задание 1.6. Объявите класс с именем TravelBlog и объявите в нем атрибут:
total_blogs: 0
Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных
свойства:
name: 'Франция'
days: 6
Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два
локальных свойства:
name: 'Италия'
days: 5
Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.
Выведите на экран значение атрибута total_blogs класса TravelBlog и экземпляра tb2.
Пример ввода:
Пример вывода:
2
'''
'''

class TravelBlog:
    total_blogs = 0

    def __init__(self, name, days):
        self.name = name
        self.days = days
        TravelBlog.total_blogs += 1


tb1 = TravelBlog('Франция', 6)
tb2 = TravelBlog('Италия', 5)

print(TravelBlog.total_blogs)
print(tb2.total_blogs)
'''
'''
Задание 1.7. Объявите класс с именем Figure и двумя атрибутами:
type_fig: 'ellipse'
color: 'red'
Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные
атрибуты:
start_pt: (10, 5)
end_pt: (100, 20)
color: 'blue'
Удалите из экземпляра класса свойство color и выведите на экран список всех локальных
свойств (без значений) объекта fig1 в одну строчку через пробел, а затем цвет fig1.
Пример ввода:
Пример вывода:
start_pt end_pt red
'''
'''
class Figure:
    type_fig = 'ellipse'
    color = 'red'

    def __init__(self, start_pt, end_pt, color):
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.color = color

fig1 = Figure((10, 5), (100, 20), 'blue')
del fig1.color
print(*fig1.__dict__.keys())
print(fig1.color)
'''
'''
Задание 1.8. Объявите класс с именем Person и атрибутами:
name: 'Юрий Тверской'
job: 'Писатель'
city: 'Иваново'
Создайте экземпляр этого класса и проверьте, существует ли у него локальное свойство с
именем job. Выведите True, если оно присутствует в объекте и False - если отсутствует.
Пример ввода:
Пример вывода:
False
'''


class Person:
    name = 'Юрий Тверской'
    job = 'Писатель'
    city = 'Иваново'


person = Person()
if hasattr(person, 'job'):
    print(True)
else:
    print(False)
