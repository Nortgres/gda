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
'''
class Person:
    name = 'Юрий Тверской'
    job = 'Писатель'
    city = 'Иваново'


person = Person()
if hasattr(person.__dict__, 'job'):
    print(True)
else:
    print(False)
'''
'''
Задание 1.9. Объявите класс с именем MediaPlayer с двумя методами:
open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со
значением аргумента file в объекте класса MediaPlayer)
play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение
<название медиа-файла>")
Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод
open() с аргументом "filemedia1" для объекта media1 и "filemedia2" для объекта media2.
После этого вызовите через объекты метод play().
Пример ввода:
Пример вывода:
Воспроизведение filemedia1
Воспроизведение filemedia2
'''
'''
class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print("Воспроизведение", self.filename)

media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()
'''
'''
Задание 1.10. Объявите класс с именем Graph и методами:
set_data(data) - передача набора данных data для последующего отображения (data - список
числовых данных);
draw() - отображение данных (в том же порядке, что и в списке data)
и атрибутом: LIMIT_Y = [0, 10]
Метод set_data() должен формировать локальное свойство data объекта класса Graph.
Атрибут data должен ссылаться на переданный в метод список. Метод draw() должен
выводить на экран список в виде строки из чисел, разделенных пробелами и
принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).
Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и передайте
список, сформированный из чисел, введенных через пробел.
Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с
соответствующим набором чисел, записанных через пробел.
Пример ввода:
10 -5 100 20 0 80 45 2 5 7
Пример вывода:
10 0 2 5 7
'''
'''
class Graph:

    def set_data(self, data):
        self.data = data

    def draw(self):
        LIMIT_Y = [0, 10]
        nums = filter(lambda x: LIMIT_Y[0] <= x <= LIMIT_Y[1], self.data)
        print(*nums)


graph_1 = Graph()
graph_1.set_data(map(int, (input("Введите числа: ").split())))
graph_1.draw()
'''
'''
Задание 1.11. Объявите класс с именем Translator (для перевода с английского на русский)
со следующими методами:
add(self, eng, rus) - для добавления новой связки английского и русского слова (если
английское слово уже существует, то новое русское слово добавляется как синоним для
перевода, например, go - идти, ходить, ехать); если связка eng-rus уже существует, то
второй раз ее добавлять не нужно, например: add('go', 'идти'), add('go', 'идти');
remove(self, eng) - для удаления связки по указанному английскому слову;
translate(self, eng) - для перевода с английского на русский (метод должен возвращать
список из русских слов, соответствующих переводу английского слова, даже если в списке
всего одно слово).
Все добавления и удаления связок должны выполняться внутри каждого конкретного
объекта класса Translator, т.е. связки хранить локально внутри экземпляров классов
класса Translator.
Создайте экземпляр tr класса Translator и вызовите метод add для связок, введите
несколько связок по шаблону из примера ввода (пока не встретится ноль), после него
вводится слово, которое нужно перевести.
Затем методом remove() удалите связку для одного английского слова.
С помощью метода translate() переведите слово, введенное после нуля.
Результат выведите на экран в виде строки из всех русских слов, связанных с этим словом.
Пример ввода:
tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко
0
go
Пример вывода:
идти ехать ходить
'''
'''
class Translator:
    def __init__(self):
        self.mydict = {}
    def add(self, eng, rus):
        if eng in self.mydict:
            self.mydict[eng].append(rus)
        else:
            self.mydict[eng] = [rus]
    def remove(self, eng):
        if eng in self.mydict:
            del self.mydict[eng]
    def translate(self, eng):
        if eng in self.mydict:
            return self.mydict[eng]
        else:
            return []
tr = Translator()
while True:
    w = input("Введите слово - перевод: ")
    if w != '0':
        x, y = w.split(' - ')
        tr.add(x, y)
    else:
        break
tr.remove(input("Введите слово для удаления: "))
print(*tr.translate(input("Введите слово: ")))
'''
'''
Задание 1.12. Объявите класс Money так, чтобы объекты этого класса можно было
создавать следующим образом:
my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться в
локальном свойстве (атрибуте) money каждого экземпляра класса.
'''
'''
class Money:
    def __init__(self, money):
        self.money = money

my_money = Money(100)
your_money = Money(1000)
'''
'''
Задание 1.13. Объявите класс Point так, чтобы объекты этого класса можно было создавать
командами:
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y),
а третий необязательный аргумент - цвет точки (локальное свойство color). Если цвет не
указывается, то он по умолчанию принимает значение black.
Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с
увеличением на два для каждой новой точки. Каждый объект следует поместить в
список points (по порядку). Для второго объекта в списке points укажите цвет 'yellow'.
'''
'''
class Point:

    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color

points = []
x, y = 1, 1
for i in range(1000):
    color = 'yellow' if i == 1 else None
    p = Point(x, y, color)
    points.append(p)
    x += 2
    y += 2
#print(points[999].y)
'''
'''
Задание 1.14. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть
возможность создавать объекты каждого класса следующими командами:
g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего
левого углов (произвольные числа). В каждом объекте координаты должны сохраняться в
локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и
(c, d) соответственно.
Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается
случайно (или Line, или Rect, или Ellipse). Координаты также генерируются случайным
образом (числовые значения). Все объекты сохраните в списке elements.
В списке elements обнулите координаты объектов только для класса Line.
'''
'''
import random
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = []
cl_list = ['Line', 'Rect', 'Ellipse']

for i in range(217):
    cl = random.choice([Line, Rect, Ellipse])
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = random.randint(1, 1000)
    d = random.randint(1, 1000)
    res = cl(a, b, c, d)
    elements.append(res)
for i in elements:
    if isinstance(i, Line):
        i.sp = (0, 0)
        i.ep = (0, 0)
'''
'''
Задание 1.15. Объявите класс TriangleChecker, объекты которого можно было бы создавать
командой: tr = TriangleChecker(a, b, c) Здесь a, b, c - длины сторон треугольника.
В классе TriangleChecker объявите метод is_triangle(), возвращающий следующие коды:
1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или
равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.
Проверку параметров a, b, c проводить именно в таком порядке.
Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами,
командой: a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a,
b, c. Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который
она вернет).
Пример ввода:
3 4 5
Пример вывода:
3
'''
'''
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        try:
            a, b, c = map(float, (self.a, self.b, self.c))
        except:
            return 1

        if a <= 0 or b <= 0 or c <= 0:
            return 1

        if (a + b) <= c or (a + c) <= b or (b + c) <= a:
            return 2
        else:
            return 3

a, b, c = (input("Введите длины сторон треугольника: ")).split()
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
'''
'''
Задание 1.16. Объявите класс AbstractClass, объекты которого нельзя было бы создавать.
При выполнении команды:
obj = AbstractClass()
переменная obj должна ссылаться на строку с содержимым:
"Ошибка: нельзя создавать объекты абстрактного класса"
Создайте объект данного класса и выведете его значение на экран.
Пример ввода:
Пример вывода:
Ошибка: нельзя создавать объекты абстрактного класса
'''
'''
class AbstractClass:
    def __init__(self):
        print("Ошибка: нельзя создавать объекты абстрактного класса")
        pass
obj=AbstractClass()
'''
'''
Задание 1.17. Объявите класс SingletonFive, с помощью которого можно было бы создавать
объекты командой: a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name
созданного объекта.
Этот класс должен формировать только первые пять объектов. Остальные (шестой,
седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.
Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента
программы: objs = [SingletonFive(str(n)) for n in range(10)]
Выведите созданные объекты с 4 по 7 на экран, каждый объект с новой строки.
Пример ввода:
Пример вывода:
<__main__.SingletonFive object at 0x00000193E243EB00>
<__main__.SingletonFive object at 0x00000193E243EAA0>
<__main__.SingletonFive object at 0x00000193E243EAA0>
<__main__.SingletonFive object at 0x00000193E243EAA0>
'''
'''
class SingletonFive:
    count = 0
    n = None
    def __new__(cls, name):
        if cls.count < 5:
            n = super().__new__(cls)
            cls.count += 1
            cls.n = n
            return n
        else:
            return cls.n

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]
for obj in objs[3:7]:
    print(obj)
'''
'''
Задание 1.18. В программе объявлена переменная TYPE_OS и два следующих класса:
TYPE_OS = 1 # 1 - Windows; 2 - Linux
class DialogWindows:
name_class = "DialogWindows"
class DialogLinux:
name_class = "DialogLinux"
Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и
объекты класса DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS
может меняться в последующих строчках программы. Имейте это в виду, при объявлении класса
Dialog. Создайте по одному объекту каждого типа и выведите их на экран.
Пример ввода:
Пример вывода:
<__main__.DialogWindows object at 0x000001F75843D0C0>
<__main__.DialogLinux object at 0x000001F7588AEBC0>
'''
'''
TYPE_OS = 1 # 1 - Windows; 2 - Linux
class DialogWindows:
    name_class = "DialogWindows"
class DialogLinux:
    name_class = "DialogLinux"
class Dialog:
    def __init__(self, name):
        self.name = name
        if TYPE_OS == 1:
            self.dialog = DialogWindows()
        else:
            self.dialog = DialogLinux()
dlg1 = Dialog("test1")
print(dlg1.dialog)
TYPE_OS = 2
dlg2 = Dialog("test2")
print(dlg2.dialog)
'''
'''
Задание 1.19. Объявите класс Point для представления точек на плоскости. Создавать
объекты этого класса предполагается командой: pt = Point(x, y)
Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом объекте
этого класса создаются локальные свойства x, y, хранящик конкретные координаты точки.
Необходимо в классе Point реализовать метод clone(self), который бы создавал новый
объект класса Point как копию текущего объекта с локальными атрибутами x, y и
соответствующими значениями.
Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов
метода clone. Выведите объекты и их атрибуты на экран.
Пример ввода:
Пример вывода:
<__main__.Point object at 0x0000024B1598D630> {'x': 5, 'y': 10}
<__main__.Point object at 0x0000024B15DFEA40> {'x': 5, 'y': 10}
'''
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def clone(self):
        return Point(self.x, self.y)
pt = Point(5, 10)
pt2 = pt.clone()
print(pt, pt.__dict__)
print(pt2, pt2.__dict__)
'''
'''
Задание 1.20. В программе предполагается реализовать парсер (обработчик) строки с данными string в
определенный выходной формат. Для этого объявлен следующий класс:
class Loader:
@staticmethod
def parse_format(string, factory):
seq = factory.build_sequence()
for sub in string.split(","):
item = factory.build_number(sub)
seq.append(item)
return seq
И предполагается его использовать следующим образом: res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
На выходе (в переменной res) ожидается получать список из набора целых чисел. Для реализации этой идеи
необходимо вначале программы прописать класс Factory с двумя статическими методами:
build_sequence() - для создания пустого списка (метод возвращает пустой список);
build_number(string) - для преобразования строки (string) в целое число (метод возвращает полученное
целочисленное значение).
Объявите класс с именем Factory, чтобы получать на выходе искомый результат. Создайте и выведите объект res.
Пример ввода:
Пример вывода:
[1, 2, 3, -5, 10]
'''
'''
class Factory:
    @staticmethod
    def build_sequence():
        return []
    @staticmethod
    def build_number(string):
        return int(string)
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq

res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)
'''
'''
Задание 1.21. Объявите класс с именем Clock и определите в нем следующие переменные и методы:
- приватная локальная переменная time для хранения текущего времени, целое число (своя для
каждого объекта класса Clock с начальным значением 0);
- публичный метод set_time(tm) для установки текущего времени (присваивает значение tm
приватному локальному свойству time, если метод check_time(tm) возвратил True);
- публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
- приватный метод класса check_time(tm) для проверки корректности времени в переменной tm
(возвращает True, если значение корректно и False - в противном случае).
Проверка корректности выполняется по критерию: tm должна быть целым числом, больше или равна
нулю и меньше 100 000.
Объекты класса Clock предполагается использовать командой: clock = Clock(время)
Создайте объекты clock и clock2 класса Clock и установите время, равным 4530 и 145300 соответственно.
Выведите значение времени обоих объектов на экран.
Пример ввода:
Пример вывода:
4530
0
'''
class Clock:
    def __init__(self, time=0):
        self.__time = 0
    def set_time(self, tm):
        if self.__private_check_time(tm):
            self.__time = tm
    def get_time(self):
        return self.__time
    def __private_check_time(self, tm):
        try:
            return 0 <= int(tm) < 100_000
        except:
            return False


clock = Clock()
clock.set_time(4530)
print(clock.get_time())

clock2 = Clock()
clock2.set_time(145300)
print(clock2.get_time())