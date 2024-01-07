'''
Задание 2.1. Объявите в программе базовый класс Animal (животное), объекты которого можно
создать командой: an = Animal(name, old), где name - название животного (строка); old - возраст животного
(целое число). Такие же локальные атрибуты (name и old) должны создаваться в объектах класса.
Далее, объявите дочерний класс (от базового Animal) с именем Cat (кошки), объекты которого создаются
командой: cat = Cat(name, old, color, weight), где name, old - те же самые параметры, что и в базовом
классе; color - цвет кошки (строка); weight - вес кошки (любое положительное число).
В объектах класса Cat должны автоматически формироваться локальные атрибуты: name, old, color,
weight. Формирование атрибутов name, old должен выполнять инициализатор базового класса.
По аналогии объявите еще один дочерний класс Dog (собака), объекты которого создаются командой:
dog = Dog(name, old, breed, size), здесь name, old - те же самые параметры, что и в базовом классе; breed
- порода собаки (строка); size - кортеж в формате (height, length) высота и длина - числа.
В объектах класса Dog по аналогии должны формироваться локальные атрибуты: name, old, breed, size.
За формирование атрибутов name, old отвечает инициализатор базового класса.
Наконец, в классах Cat и Dog объявите метод: get_info() - для получения информации о животном.
Этот метод должен возвращать строку в формате: "name: old, <остальные параметры через запятую>"
Пример входных данных: cat = Cat('кот', 4, 'black', 2.25); print(cat.get_info())
Пример вывода: кот: 4, black, 2.25
'''
'''
class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight
    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'
class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size[0]}, {self.size[1]}"
cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())
dog = Dog('собака', 5, 'дворняга', (50, 100))
print(dog.get_info())
'''
'''
Задание 2.2. Разработайте программу для интернет-магазина, в котором могут быть как реальные
(физические) товары, так и электронные. Для этих двух групп, очевидно, нужен разный набор атрибутов:
- для реальных физических товаров: id, name, price, weight, dims
где id - идентификатор товара (целое число); name - наименование товара (строка); price - цена товара
(вещественное число); weight - вес товара (вещественное число); dims = (lenght, width, depth) - длина,
ширина, глубина - габариты товара (вещественные числа);
- для электронных товаров: id, name, price, memory, frm
где id - идентификатор товара (целое число); name - наименование товара (строка); price - цена товара
(вещественное число); memory - занимаемый размер (в байтах - целое число); frm - формат данных
(строка: pdf, docx и т.п.)
Так как все товары могут идти вперемешку, то мы хотим, чтобы в каждом объекте (для товара)
присутствовали все атрибуты: id, name, price, weight, dims, memory, frm с начальными значениями None. А
уже, затем, нужным из них будут присвоены конкретные данные.
Для реализации этой логики объявите в программе базовый класс с именем Thing (вещь, предмет),
объекты которого могут создаваться командой:
th = Thing(name, price)
А атрибут id должен формироваться автоматически и быть уникальным для каждого товара (например,
можно для каждого нового объекта увеличивать на единицу).
В объектах класса Thing должен формироваться полный набор локальных атрибутов (id, name, price,
weight, dims, memory, frm) со значением None, кроме атрибутов: id, name, price.
 Далее, нужно объявить два дочерних класса:
Table - для столов; ElBook - для электронных книг.
Объекты этих классов должны создаваться командами:
table = Table(name, price, weight, dims)
book = ElBook(name, price, memory, frm)
Причем, атрибуты name, price (а также id) следует инициализировать в базовом классе, т.к. они общие для
всех товаров. Остальные атрибуты должны либо принимать значение None, если не используются, либо
инициализироваться конкретными значениями уже в дочерних классах.
Наконец, в базовом классе Thing объявите метод:
get_data() - для получения кортежа в формате (id, name, price, weight, dims, memory, frm)
Пример входных данных:
table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
Пример вывода:
0 Круглый 1024 812.55 (700, 750, 700) None None
1 Python ООП 2000 None None 2048 pdf
'''
'''
class Thing:
    id = 0

    def __init__(self, name, price):
        super().__init__()
        self.id = Thing.id
        Thing.id += 1
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None
    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)

class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims
class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
'''
'''Задание 2.3. Создается проект, в котором предполагается использовать списки из целых чисел. Для
этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три
метода: __init__(), __setitem__() и append(), так, чтобы список ListInteger содержал только целые
числа. При попытке присвоить любой другой тип данных, генерировать исключение командой:
raise TypeError('можно передавать только целочисленные значения')
Пример входных данных 1:
s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
Пример вывода 1:
[1, 10, 3, 11]
Пример входных данных 2:
s[0] = 10.5
Пример вывода 2:
TypeError: можно передавать только целочисленные значения
'''
class ListInteger(list):
    def __init__(self, x):
        self.__check_values(x)
        super().__init__(x)
    @classmethod
    def __check_values(cls, x):
        for i in x:
            if type(i) != int:
                raise TypeError('можно передавать только целочисленные значения')
    def __setitem__(self, index, x):
        if type(x) == int:
            self.x = x
            super().__setitem__(index, x)
        else:
            raise TypeError('можно передавать только целочисленные значения')
    def append(self, x):
        if type(x) == int:
            self.x = x
            super().append(x)
        else:
            raise TypeError('можно передавать только целочисленные значения')

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
#s[0] = 10.5