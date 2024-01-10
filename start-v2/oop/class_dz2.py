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
        super().__init__(name, price)    id = 0

    def __init__(self, name, price):
        self.id = Thing.id
        Thing.id += 1
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
'''
# Задание 2.3.
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
'''
'''
Задание 2.4. Известно, что с объектами класса tuple можно складывать только такие же объекты:
t1 = (1, 2, 3)
t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)
Если же мы попытаемся прибавить любой другой итерируемый объект, например, список:
t2 = t1 + [4, 5], то возникнет ошибка. Предлагается поправить этот функционал и создать свой
собственный класс Tuple, унаследованный от базового класса tuple и поддерживающий оператор «+»:
t1 = Tuple(iter_obj)
t2 = t1 + iter_obj # создается новый объект класса Tuple с новым (соединенным) набором данных
где iter_obj - любой итерируемый объект (список, словарь, строка, множество, кортеж и т.п.)
Пример входных данных:
t = Tuple([1, 2, 3])
t = t + "Python"
print(t)
t = t + {5, 8}
print(t)
Пример вывода:
(1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
(1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n', 8, 5)
'''
'''
class Tuple(tuple):
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))

t = Tuple([1, 2, 3])
t = t + "Python"
print(t)
t = t + {5, 8}
print(t)
'''
'''
Задание 2.5. Объявите класс SoftList, который наследуется от стандартного класса list. В
классе SoftList следует объявить необходимый магический метод так, чтобы при обращении
к несуществующему элементу (по индексу) возвращалось значение False (а не исключение
Out of Range).
Пример входных данных:
sl = SoftList("python")
print(sl[0])
print(sl[-1])
print(sl[6])
print(sl[-7])
Пример вывода:
p n
False
False
'''
'''
Задание 2.5. Объявите класс SoftList, который наследуется от стандартного класса list. В
классе SoftList следует объявить необходимый магический метод так, чтобы при обращении
к несуществующему элементу (по индексу) возвращалось значение False (а не исключение
Out of Range).
Пример входных данных:
sl = SoftList("python")
print(sl[0])
print(sl[-1])
print(sl[6])
print(sl[-7])
Пример вывода:
p n
False
False
'''
'''
# Задание 2.5.
class SoftList(list):

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except:
            return False

sl = SoftList("python")
print(sl[0])
print(sl[-1])
print(sl[6])
print(sl[-7])
'''
'''
Задание 2.6. Объявите в программе базовый класс с именем Book, объекты которого создаются
командой: book = Book(title, author, pages, year), где title - заголовок книги (строка); author - автор
книги (строка); pages - число страниц (целое число); year - год издания (целое число). В каждом объекте
класса Book должны формироваться соответствующие локальные атрибуты: title, author, pages, year.
Объявите дочерний класс DigitBook от класса Book, объекты которого создаются командой:
db = DigitBook(title, author, pages, year, size, frm), где дополнительные параметры size -
размер книги в байтах (целое число); frm - формат книги (строка: 'pdf', 'doc', 'fb2', 'txt'). В каждом объекте
класса DigitBook должны формироваться соответствующие локальные атрибуты: title, author, pages, year,
size, frm. Инициализация локальных атрибутов title, author, pages, year должна выполняться в базовом
классе Book, а параметры size, frm инициализируются
в дочернем классе DigitBook.
Пример входных данных:
book1 = Book('Евгений Онегин', 'Пушкин', 650, 1830)
book2 = DigitBook('Борис Годунов ', 'Пушкин', 777, 1825, 1024, 'fb2')
data = lambda obj: [print(f'{key:6} --> {value}') for key, valuein obj.__dict__.items()]
data(book1)
print('*' * 25)
data(book2)
Пример вывода:
title --> Евгений Онегин
author --> Пушкин
pages --> 650
year --> 1830
*************************
title --> Борис Годунов
author --> Пушкин
pages --> 777
year --> 1825
size --> 1024
frm --> fb2
'''
'''
class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm

book1 = Book('Евгений Онегин', 'Пушкин', 650, 1830)
book2 = DigitBook('Борис Годунов ', 'Пушкин', 777, 1825, 1024, 'fb2')
data = lambda obj: [print(f'{key:6} --> {value}') for key, value in obj.__dict__.items()]
data(book1)
print('*' * 25)
data(book2)
'''
'''
Задание 2.7. Вам поручено организовать представление объектов для продажи в риэлтерских
агентствах. Для этого в программе нужно объявить базовый класс SellItem, объекты которого создаются
командой: item = SellItem(name, price)
где name - название объекта продажи (строка); price - цена продажи (число: целое или вещественное).
Каждые конкретные типы объектов описываются следующими классами, унаследованные от базового
SellItem:
House - дома;
Flat - квартиры;
Land - земельные участки.
Объекты этих классов создаются командами:
house = House(name, price, material, square)
flat = Flat(name, price, size, rooms)
land = Land(name, price, square)
В каждом объекте этих классов должны формироваться соответствующие локальные атрибуты: name,
price и т.д. Формирование атрибутов name и price должно выполняться в инициализаторе базового класса.
Далее, объявить еще один класс с именем Agency, объекты которого создаются командой:
ag = Agency(name)
где name - название агентства (строка).
В классе Agency объявить следующие методы:
add_object(obj) - добавление нового объекта недвижимости для продажи (один из объектов классов:
House, Flat, Land);
remove_object(obj) - удаление объекта obj из списка объектов для продажи;
get_objects() - возвращает список из всех объектов для продажи.
Пример входных данных:
ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000,
material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
print(obj.name)
Пример вывода:
квартира, 3к
квартира, 2к
квартира, 1к
дом, крипичный
участок под застройкуЗадания к разделу 2.
'''
'''
class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square
class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms
class Land(SellItem):
    def __init__(self, name, price, squar):
        super().__init__(name, price)
        self.squar = squar
class Agency:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        if isinstance(obj, SellItem):
            self.objects.append(obj)
        else:
            raise TypeError("неправильный тип объекта")
    def remove_object(self, name):
        for i in self.objects:
            if i.name == name:
                self.objects.remove(i)
                return
        raise ValueError("нет объекта с таким именем")
    def get_objects(self):
        return self.objects

ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))

for obj in ag.get_objects():
    print(obj.name)
print(ag.objects[2].name)
ag.remove_object("квартира, 1к")
print(ag.objects[2].name)
### не указано по какому признаку идёт удаление объекта.
'''
'''
Задание 2.8. Объявите класс с именем Food (еда), объекты которого создаются командой:
food = Food(name, weight, calories), где name - название продукта (строка); weight - вес продукта (любое
положительное число); calories - калорийная ценность продукта (целое положительное число).
Объявите следующие дочерние классы с именами: BreadFood - хлеб; SoupFood - суп; FishFood - рыба.
Объекты этих классов должны создаваться командами:
bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба, False - для остальных
sf = SoupFood(name, weight, calories, dietary) # dietary - True для диетического супа, False - для других
ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь, сардина и т.д.)
В каждом объекте этих дочерних классов должны формироваться соответствующие локальные атрибуты:
BreadFood: _name, _weight, _calories, _white
SoupFood: _name, _weight, _calories, _dietary
FishFood: _name, _weight, _calories, _fish
Пример входных данных:
bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")
for obj in (bf, sf, ff):
print(obj.get_data())
Пример вывода:
Бородинский хлеб
Черепаший суп
Консерва рыбная
'''
'''
class Food:
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories
    def get_data(self):
        return self._name

class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white

    def get_data(self):
        return self._name


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary
    def get_data(self):
        return self._name


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish
    def get_data(self):
        return self._name

bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")
for obj in (bf, sf, ff):
    print(obj.get_data())
'''
'''
Задание 2.9. Необходимо объявить базовый класс ShopInterface с абстрактным методом: get_id(self)
В самом методе должно генерироваться исключение командой:
raise NotImplementedError('в классе не переопределен метод get_id')
Инициализатор в классе ShopInterface прописывать не нужно. Далее объявите дочерний класс ShopItem
(от базового класса ShopInterface), объекты которого создаются командой:
item = ShopItem(name, weight, price), где name - название товара (строка); weight - вес товара (любое
положительное число); price - цена товара (любое положительное число).
В каждом объекте класса ShopItem должны формироваться локальные атрибуты с именами _name,
_weight, _price и соответствующими значениями. Также в объектах класса ShopItem должен
автоматически формироваться локальный приватный атрибут __id с уникальным (для каждого товара)
целым значением. В классе ShopItem необходимо переопределить метод get_id() базового класса так,
чтобы он (метод) возвращал значение атрибута __id.
Пример входных данных:
item1 = ShopItem("майка", 200, 1200)
item2 = ShopItem("толстовка", 500, 1900)
print(item1.get_id())
print(item2.get_id())
Пример вывода:
1 2
'''
'''
class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')
class ShopItem(ShopInterface):
    id = 1
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = ShopItem.id
        ShopItem.id += 1
    def get_id(self):
        return self.__id

item1 = ShopItem("майка", 200, 1200)
item2 = ShopItem("толстовка", 500, 1900)
print(item1.get_id())
print(item2.get_id())
'''
'''
Задание 2.10. С помощью множественного наследования удобно описывать принадлежность объектов
к нескольким разным группам. Определите в программе классы в соответствии с их иерархией,
представленной на рисунке:
Каждый объект этих классов должен создаваться однотипной командой вида: obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения
value:
- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.
Если проверка не проходит, то генерируется исключение командой:
raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:
PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.
Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с
произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.
Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:
lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.
Выведите элементы из списка lst_float на экран.
Пример входных данных:
digits = [PrimeNumber(17), PrimeNumber(7), PrimeNumber(229),
FloatPositive(.258), FloatPositive(.432), FloatPositive(1.0),
FloatPositive(999999.9), FloatPositive(8333333333.2)]
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
for obj in lst_float:
print(obj.value)
Пример вывода:
0.258
0.432
1.0
999999.9
8333333333.2
'''
'''
class Digit:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value
class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value
class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

class Positive(Digit):
    def __init__(self, value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value
class Negative(Digit):
    def __init__(self, value):
        if not (isinstance(value, (int, float)) and value < 0):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value
class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        for i in range(2, value):
            if value % i == 0:
                raise TypeError('значение не соответствует типу объекта')
        self.value = value
class FloatPositive(Float, Positive):
    pass

digits = [PrimeNumber(17), PrimeNumber(7), PrimeNumber(229),
FloatPositive(.258), FloatPositive(.432), FloatPositive(1.0),
FloatPositive(999999.9), FloatPositive(8333333333.2)]
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
for obj in lst_float:
    print(obj.value)
for obj in lst_positive:
    print(obj.value)
'''