import random


class Geom:
    name = 'Geom'
    #def __str__(self):
    #    print('test')
    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        #self.draw()  но нет в базовом классе
    #def draw(self):
    #    print("Рисование примитива")
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть переопределен метод get_pr()")

class Line(Geom):
    name = 'Line'

    def draw(self):
        print("Рисование линии")

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill=None):
        #Geom.__init__(self, x1, y1, x2, y2) # рабочий, но костыль
        super().__init__(x1, y1, x2, y2)  # обращение к базовому классу - делегирование (лучше первой строкой всегда)
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")

#g = Geom()
#print(g.name)

#l = Line(0, 0, 10, 20)
#r = Rect(1, 2, 3, 4, "red")
#print(r.__dict__)
#r = Rect()
#l.set_coords(1, 1, 2, 2)
#r.set_coords(1, 1, 2, 2)
#print(l.name)
#print(r.name)
#g = Geom()
#l.draw()
#r.draw()
#g.draw()
#print(Geom.__class__)
#print(g)
#print(l.__class__())
#print(issubclass(Line, Geom))
#print(issubclass(Geom, Line))
# print(issubclass(l, Geom)) с подклассами не работает
#print(isinstance(l, Geom))
#print(isinstance(l, Line))
#print(isinstance(l, object))
#print(issubclass(int, object))
#print(issubclass(list, object))
#print(issubclass(bool, int))

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))
v = Vector([1, 2, 3])
#print(v)

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_pr(self):
        return 2*(self.w+self.h)
class Square(Geom):
    def __init__(self, a):
        self.a = a
    def get_pr(self):
        return 4*self.a

class Trianle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    #def get_pr(self):
    #    return self.a + self.b + self.c

r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
#print(r1.get_rect_pr(), r2.get_rect_pr())

s1 = Square(10)
s2 = Square(20)
#print(s1.get_sq_pr(), s2.get_sq_pr())

t1 = Trianle(1,2,3)
t2 = Trianle(4,5, 6)

#geom = [r1, r2, s1, s2, t1, t2]
geom = [Rectangle(1,2), Rectangle(3,4), Square(10), Square(20),
        Trianle(1,2,3), Trianle(4,5,6)]

#for g in geom:
#    print(g.get_pr())
    #if isinstance(g, Rectangle):
    #    print(g.get_rect_pr())
    #else:
    #    print(g.get_sq_pr())

#class A (base1, base2, ..., baseN): # множественное наследование

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.nane = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.nane}, {self.weight}, {self.price}")

class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID +=1
        self.id = self.ID

    def save_shell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")

class NoteBook(Goods, MixinLog):
    pass



n = NoteBook("Aser", 1.5, 30000)
n.print_info()
n.save_shell_log()
print(NoteBook.__mro__) # распечатать цепочку наследования