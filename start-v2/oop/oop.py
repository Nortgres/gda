class Point:   # Имена классов с заглавной буквы
    '''Класс для представления координат точек на плоскости'''
    color = 'black'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)
    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        #print("вызов метода set_coords" + str(self))

    def get_coords(self):
        return (self.x, self.y)

    def __del__(self):
        print("Удаление экземлпяра: " + str(self))
'''
Point.color = 'red'

#print(Point.circle)
#print(Point.__dict__)
a = Point()
b = Point()
#print(type(a))

Point.circle = 1
print(a.circle)
print(a.__dict__)
a.color = 'green'
print(a.color)
print(b.color)
print(a.__dict__)
Point.type_pt = 'disc'
setattr(Point, 'prop', 1)
setattr(Point, 'type_pt', 'square')
print(Point.circle)
getattr(Point, 'a', False)  # проверка атрибута на наличие
del Point.prop
hasattr(Point, 'prop') # возвращает True если найден и удалён
delattr(Point, 'type_pt')
a.x = 1
a.y = 2
b.x = 10
b.y = 20
print(Point.__doc__)
'''
###  Point.set_coords()
pt = Point(1, 2)
print(pt)
#print(pt.__dict__)
#pt.set_coords()
#Point.set_coords(pt)

#pt.set_coords(1, 2)
#print(pt.__dict__)

#pt2 = Point()
#print(pt2.__dict__)
#pt2.set_coords(10, 20)
#print(pt2.__dict__)
#print(pt.get_coords())

# __init__(self) - инициализатор объекта класса
# __del__(self) - финализатор объекта класса
#pt = Point(10)
#pt = Point(10, 20)
