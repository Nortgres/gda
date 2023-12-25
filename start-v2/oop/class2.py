class DataBase:
    __instance = None
    def __new__(cls, *arg, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port
    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")
    def close(self):
        print("закрытие соединения с БД")
    def read(self):
        return "данные из БД"
    def write(self, data):
        print(f"запись в БД{data}")
    def __del__(self):
        DataBase.__instance = None

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2), id(db) == id(db2))

class Point:
    MIN_COORD = 0
    MAX_COORD = 100
    color = 'black'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)
    def __init__(self, x, y):
        self.x = self.y = 0
        if Point.validate(x) and Point.validate(y):
        #print("вызов __init__ для " + str(self))
            self.x = x
            self.y = y
            print(self.norm2(self.x, self.y))

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        #print("вызов метода set_coords" + str(self))

    def get_coords(self):
        return (self.x, self.y)

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    @staticmethod
    def norm2(x, y):
        return x*x + y*y
    def __del__(self):
        print("Удаление экземлпяра: " + str(self))
res = Point.validate(5)
print(res)
res2 = Point.norm2(3, 4)
print(res2)

class Point2:
    def __int__(self, x=0, y=0):
        #self.x = x
        self.__x = self.__y = 0
        if self.__ceck_value(x) and self.__ceck_value(y):
            self.__x = x
            self.__y = y
    def set_coord(self, x, y):
        if self.__ceck_value(x) and self.__ceck_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")
    def get_coord(self):
        return self.__x, self.__y
    @classmethod
    def __ceck_value (cls, x):
        return type(x) in (int, float)

pt3 = Point2()
pt3.set_coord(1,2)
print(pt3.get_coord())
print(dir(pt3))
print(pt3._Point2__x, pt3._Point2__y)
#pt3.x = 200
#pt3.y = "ten"