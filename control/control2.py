# https://docs.google.com/forms/d/e/1FAIpQLSc8O2WF4M4ziAPnWG6dDPqvZ79e0Z23FrGfTCqwKWbhs5SSBA/viewform?usp=sf_link

"""1) Напишите класс с описанием параллелепипеда
-принимает в себя ширину и длинну основания, а так же высоту
-реализуйте методы для расчета его объема, площади основания и площади боковой стороны
-добавьте статический метод info, который бы выводил перечень методов
"""
'''
class Parallelepiped:
    def __init__(self, w, l, h):
        self.w = w
        self.l = l
        self.h = h
    def volume(self):
        return int(self.w) * int(self.l) * int(self.h)
    def s_osn(self):
        return int(self.w) * int(self.l)
    def s_storony(self):
        return int(self.l) * int(self.h)
    @staticmethod
    def info():
        return dir(Parallelepiped)


p1 = Parallelepiped('3', '3', '4')
print(p1.volume())
print(p1.s_osn())
print(p1.s_storony())
print(p1.info())'''

"""2)Напишите класс ListWorker
-принимает в себя неограниченное количество неименованных аргументов и работает с ними как со списком
-Реализуйте методы, которые возвращают
    -только числа
    -только строки
    -все кроме чисел и строк"""
class ListWorker:
    def __init__(self, *args):
        self.args = args
        print(args)
    def number(self):
        list1 = []
        for i in (self.args):
            print(type(i))
            #if isinstance(i, str):
            #    list1.append(i)
        print(list1)

l1 = ListWorker('3', '3', '4', 'aaa', 'bbb', '5', ':')
print(l1.number())



"""Есть папка которая содержит 100 файлов со случайными цифрами, но в одной из них есть пароль password
Проверьте все файлы, и найдите пароль. В итоге покажите в консоли номер файла с паролем и содержимое этого файла"""

'''import os

os.chdir('data')
pas = 'password'
for i in os.listdir():
    with open(i) as f:
        l1 = f.read().split(' ')
        if l1.count(pas):
            print(i)
            f.seek(0)
            print(f.read())'''

"""Напишите программу которая бы открывала файл и выводила его содержимое. Если попытаться открыть несуществующий файл
то вместо этого она его создаст и запишет туда слово 'Пусто'"""

'''import os

filename = input('Введите название файла:')
try:
    f2 = open(filename, mode='r', encoding='cp1251')
    print(f2.read())
except FileNotFoundError:
    f2 = open(filename, mode='w')
    f2.write(f'Пусто\n')
f2.close()
'''
