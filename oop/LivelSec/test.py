'''Объявите класс с именем Goods и пропишите в нем следующие атрибуты объекта
(переменные):
title: "Мороженое"
weight: 154
tp: "Еда"
price: 1024
Затем, после создания объекта, удвойте его атрибут price заменив на значение 2048 и добавьте
еще один атрибут класса:
inflation: 100'''


class Goods:
    def __init__(self, title, weight, tp, price):
        self.title = title
        self.weight = weight
        self.tp = tp
        self.price = price * 2
        Goods.inflation = 100

    def tovar_info(self):
        print(f'{self.title} {self.weight} {self.tp} {self.price}')


tov = Goods("Мороженое", 154, "Еда", 1024)

tov.tovar_info()
print(tov.price)
print(Goods.inflation)
